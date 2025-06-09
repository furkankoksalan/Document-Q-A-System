import streamlit as st
import os
import tempfile
from typing import List, Dict, Any
import pickle
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI, OpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.schema import Document

st.set_page_config(
    page_title="Document Q&A System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #2E86AB;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: bold;
}
.chat-message {
    padding: 1rem;
    border-radius: 0.8rem;
    margin-bottom: 1rem;
    border-left: 4px solid #2E86AB;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.user-message {
    background-color: #F8F9FA;
    border-left-color: #28A745;
    color: #212529;
}
.bot-message {
    background-color: #E3F2FD;
    border-left-color: #2E86AB;
    color: #1A1A1A;
}
.stSelectbox > div > div > div {
    background-color: white;
    color: #212529;
}
.success-box {
    background-color: #D4EDDA;
    color: #155724;
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #28A745;
}
.warning-box {
    background-color: #FFF3CD;
    color: #856404;
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #FFC107;
}
</style>
""", unsafe_allow_html=True)


class DocumentQASystem:
    def __init__(self):
        self.vectorstore = None
        self.qa_chain = None
        self.memory = None

    def load_documents(self, uploaded_files: List) -> List[Document]:
        documents = []

        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            try:
                if uploaded_file.name.endswith('.pdf'):
                    loader = PyPDFLoader(tmp_file_path)
                elif uploaded_file.name.endswith('.txt'):
                    loader = TextLoader(tmp_file_path, encoding='utf-8')
                else:
                    st.warning(f"Unsupported file format: {uploaded_file.name}")
                    continue

                file_documents = loader.load()

                for doc in file_documents:
                    doc.metadata['source_file'] = uploaded_file.name
                    doc.metadata['upload_time'] = datetime.now().isoformat()

                documents.extend(file_documents)

            except Exception as e:
                st.error(f"Error loading file: {uploaded_file.name} - {str(e)}")
            finally:
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)

        return documents

    def split_documents(self, documents: List[Document], chunk_size: int, chunk_overlap: int) -> List[Document]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        split_docs = text_splitter.split_documents(documents)
        return split_docs

    def create_vectorstore(self, documents: List[Document], embedding_type: str, vectorstore_type: str):
        if embedding_type == "OpenAI":
            embeddings = OpenAIEmbeddings()
        else:
            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

        if vectorstore_type == "FAISS":
            self.vectorstore = FAISS.from_documents(documents, embeddings)
        else:
            self.vectorstore = Chroma.from_documents(documents, embeddings)

    def setup_qa_chain(self, model_name: str, temperature: float, memory_type: str):
        if model_name.startswith("gpt-3.5") or model_name.startswith("gpt-4"):
            llm = ChatOpenAI(
                model_name=model_name,
                temperature=temperature,
                streaming=True
            )
        else:
            llm = OpenAI(
                model_name=model_name,
                temperature=temperature,
                streaming=True
            )

        if memory_type == "Buffer":
            self.memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True,
                output_key="answer"
            )
        else:
            self.memory = ConversationSummaryBufferMemory(
                llm=llm,
                memory_key="chat_history",
                return_messages=True,
                output_key="answer",
                max_token_limit=1000
            )

        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 4}),
            memory=self.memory,
            return_source_documents=True,
            verbose=True
        )

    def ask_question(self, question: str, callback_handler) -> Dict[str, Any]:
        if not self.qa_chain:
            return {"error": "QA system not initialized"}

        try:
            result = self.qa_chain(
                {"question": question},
                callbacks=[callback_handler]
            )
            return result
        except Exception as e:
            return {"error": f"Error asking question: {str(e)}"}


def save_chat_history(history: List[Dict], filename: str = None):
    try:
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chat_history_{timestamp}.pkl"

        with open(filename, 'wb') as f:
            pickle.dump(history, f)
        return True, filename
    except Exception as e:
        st.error(f"Error saving chat history: {str(e)}")
        return False, None


def start_new_chat():
    if st.session_state.chat_history:
        success, filename = save_chat_history(st.session_state.chat_history)
        if success:
            st.success(f"Previous chat saved: {filename}")

    st.session_state.chat_history = []

    if st.session_state.qa_system.memory:
        st.session_state.qa_system.memory.clear()

    st.success("New chat started!")
    return True


def load_chat_history(filename: str = "chat_history.pkl") -> List[Dict]:
    try:
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading chat history: {str(e)}")
    return []


def get_saved_chat_files() -> List[str]:
    try:
        files = [f for f in os.listdir('.') if f.startswith('chat_history_') and f.endswith('.pkl')]
        return sorted(files, reverse=True)
    except:
        return []


def main():
    st.markdown('<h1 class="main-header">Document Q&A System</h1>', unsafe_allow_html=True)

    if 'qa_system' not in st.session_state:
        st.session_state.qa_system = DocumentQASystem()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = load_chat_history()
    if 'documents_processed' not in st.session_state:
        st.session_state.documents_processed = False

    with st.sidebar:
        st.header("API Settings")

        env_api_key = os.getenv("OPENAI_API_KEY")

        if env_api_key:
            st.markdown('<div class="success-box">OpenAI API Key loaded</div>', unsafe_allow_html=True)
            os.environ["OPENAI_API_KEY"] = env_api_key
            api_key_available = True
        else:
            st.markdown('<div class="warning-box">API key not found in .env file</div>', unsafe_allow_html=True)

            openai_api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                help="Required for OpenAI models"
            )

            if openai_api_key:
                os.environ["OPENAI_API_KEY"] = openai_api_key
                api_key_available = True
                st.success("API Key configured")
            else:
                api_key_available = False

        st.divider()

        st.subheader("Upload Files")
        uploaded_files = st.file_uploader(
            "Select PDF or TXT files",
            type=['pdf', 'txt'],
            accept_multiple_files=True
        )

        st.subheader("Settings")

        model_options = [
            "gpt-4o-mini",
            "gpt-3.5-turbo",
            "gpt-4"
        ]
        selected_model = st.selectbox("AI Model", model_options)

        embedding_options = ["OpenAI", "HuggingFace (Free)"]
        embedding_type = st.selectbox("Embedding", embedding_options)
        embedding_type = embedding_type.split(" ")[0]

        vectorstore_options = ["FAISS", "Chroma"]
        vectorstore_type = st.selectbox("Vector Database", vectorstore_options)

        if uploaded_files:
            st.write("")
            if st.button("Process Documents", type="primary", use_container_width=True):
                if not api_key_available and embedding_type == "OpenAI":
                    st.error("OpenAI API key required!")
                else:
                    with st.spinner("Processing documents..."):
                        chunk_size = 1000
                        chunk_overlap = 200
                        temperature = 0.7
                        memory_type = "Buffer"

                        documents = st.session_state.qa_system.load_documents(uploaded_files)

                        if documents:
                            split_docs = st.session_state.qa_system.split_documents(
                                documents, chunk_size, chunk_overlap
                            )

                            st.session_state.qa_system.create_vectorstore(
                                split_docs, embedding_type, vectorstore_type
                            )

                            st.session_state.qa_system.setup_qa_chain(
                                selected_model, temperature, memory_type
                            )

                            st.session_state.documents_processed = True
                            st.balloons()
                            st.success(f"{len(documents)} documents processed!")
                        else:
                            st.error("No documents could be loaded!")
        else:
            st.info("Please upload files first")

        st.divider()

        st.subheader("Chat Management")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("New Chat", type="primary"):
                start_new_chat()
                st.rerun()

        with col2:
            if st.button("Clear"):
                st.session_state.chat_history = []
                if st.session_state.qa_system.memory:
                    st.session_state.qa_system.memory.clear()
                st.success("Cleared!")
                st.rerun()

        saved_files = get_saved_chat_files()
        if saved_files:
            st.write("**Saved Chats:**")

            if 'selected_chat_file' not in st.session_state:
                st.session_state.selected_chat_file = ""

            selected_file = st.selectbox(
                "Select chat:",
                [""] + saved_files[:5],
                format_func=lambda x: "Select..." if x == "" else x.replace('chat_history_', '').replace('.pkl', ''),
                key="chat_selector"
            )

            if selected_file and selected_file != st.session_state.selected_chat_file:
                st.session_state.selected_chat_file = selected_file

                if st.session_state.chat_history:
                    save_chat_history(st.session_state.chat_history)

                loaded_history = load_chat_history(selected_file)
                st.session_state.chat_history = loaded_history

                if st.session_state.qa_system.memory:
                    st.session_state.qa_system.memory.clear()

                st.success("Chat loaded!")
                st.rerun()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Chat")

        chat_container = st.container()
        with chat_container:
            for i, chat in enumerate(st.session_state.chat_history):
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You:</strong> {chat['question']}
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="chat-message bot-message">
                    <strong>Assistant:</strong> {chat['answer']}
                </div>
                """, unsafe_allow_html=True)

                if 'sources' in chat and chat['sources']:
                    with st.expander(f"Sources ({len(chat['sources'])})"):
                        for j, source in enumerate(chat['sources']):
                            st.text(f"Source {j + 1}: {source}")

        if st.session_state.documents_processed:
            with st.form("question_form", clear_on_submit=True):
                question = st.text_area(
                    "Ask your question:",
                    height=100,
                    placeholder="Ask questions about your documents..."
                )
                submitted = st.form_submit_button("Send", type="primary")

                if submitted and question.strip():
                    with st.spinner("Generating answer..."):
                        callback_handler = StreamlitCallbackHandler(st.container())

                        result = st.session_state.qa_system.ask_question(
                            question, callback_handler
                        )

                        if "error" in result:
                            st.error(result["error"])
                        else:
                            chat_entry = {
                                "question": question,
                                "answer": result.get("answer", "No answer received"),
                                "sources": [doc.page_content[:200] + "..."
                                            for doc in result.get("source_documents", [])],
                                "timestamp": datetime.now().isoformat()
                            }

                            st.session_state.chat_history.append(chat_entry)
                            st.rerun()
        else:
            st.info("Please upload and process documents first to start asking questions.")

    with col2:
        st.subheader("Status")

        if st.session_state.documents_processed:
            st.markdown('<div class="success-box">System Ready</div>', unsafe_allow_html=True)
            st.metric("Chat Count", len(st.session_state.chat_history))
        else:
            st.markdown('<div class="warning-box">Upload Documents</div>', unsafe_allow_html=True)

        st.subheader("How to Use")
        st.markdown("""
        **1.** Configure your API key  
        **2.** Upload PDF/TXT files  
        **3.** Click "Process Documents"  
        **4.** Ask your questions!
        """)

        st.subheader("Features")
        st.markdown("""
        - PDF/TXT support
        - GPT-4o Mini / GPT-4
        - Chat memory  
        - Multiple chats
        - Auto-save
        """)


if __name__ == "__main__":
    main()