# Document Q&A System

A comprehensive document question-answering system built with Streamlit and LangChain for analyzing PDF and TXT files using advanced language models.

## Overview

This project enables users to upload documents and ask questions about their content using state-of-the-art GPT models. It combines document processing, vector databases, and conversational AI to provide intelligent document analysis capabilities.

The system automatically processes documents, creates searchable embeddings, and maintains conversation context to deliver accurate answers with source references.

## Features

- **Multi-format support**: Process PDF and TXT documents
- **Advanced AI models**: Choose from GPT-4o Mini, GPT-3.5 Turbo, and GPT-4
- **Flexible embeddings**: Select between OpenAI and HuggingFace embeddings
- **Vector databases**: FAISS and Chroma integration for efficient search
- **Conversation memory**: Maintains context across multiple questions
- **Chat management**: Create, save, and load conversation histories
- **Source attribution**: Shows which document sections were used for answers
- **Real-time streaming**: Get responses as they're generated
- **Responsive UI**: Clean, modern web interface

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd document-qa-system
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
echo "OPENAI_API_KEY=your-openai-api-key-here" > .env
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser to `http://localhost:8501`

3. Configure your preferences:
   - Select AI model (GPT-4o Mini recommended)
   - Choose embedding type (OpenAI for quality, HuggingFace for free)
   - Pick vector database (FAISS for speed, Chroma for features)

4. Upload PDF or TXT documents

5. Click "Process Documents" and wait for completion

6. Start asking questions about your documents!

## Configuration Options

### AI Models
- **GPT-4o Mini**: Most cost-effective with excellent performance
- **GPT-3.5 Turbo**: Fast and affordable for general use  
- **GPT-4**: Highest quality for complex queries

### Embeddings
- **OpenAI**: Higher quality embeddings (requires API credits)
- **HuggingFace**: Free alternative using sentence-transformers

### Vector Databases
- **FAISS**: Facebook's fast similarity search library
- **Chroma**: Modern vector database with advanced features

## Project Structure

```
document-qa-system/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies  
├── .env.example          # Environment variables template
├── README.md             # Project documentation
└── chat_history_*.pkl    # Auto-generated conversation files
```

## Requirements

- Python >= 3.8
- OpenAI API Key
- Internet connection

## Dependencies

```
streamlit>=1.28.0
langchain>=0.1.0
langchain-community>=0.0.10
langchain-openai>=0.0.5
openai>=1.0.0
faiss-cpu>=1.7.4
chromadb>=0.4.0
pypdf>=3.17.0
sentence-transformers>=2.2.2
tiktoken>=0.5.0
python-dotenv>=1.0.0
```

## Chat Management

- **New Chat**: Automatically saves current conversation when starting new one
- **Auto-save**: Conversations saved with timestamp filenames
- **Load Chats**: Select from dropdown to instantly load previous conversations
- **Clear**: Remove current conversation from memory

## Performance Tips

### Cost Optimization
- Model: GPT-4o Mini
- Embedding: HuggingFace (free)
- Database: FAISS

### Quality Optimization  
- Model: GPT-4
- Embedding: OpenAI
- Database: Chroma

### Speed Optimization
- Model: GPT-3.5 Turbo
- Embedding: HuggingFace  
- Database: FAISS

## Troubleshooting

### Common Issues

**Import Errors:**
```bash
pip install --upgrade langchain langchain-community langchain-openai
```

**API Key Issues:**
- Verify OpenAI API key is valid and has credits
- Check .env file formatting

**Memory Issues:**
- Use smaller documents or reduce chunk sizes
- Close other applications to free memory

**Performance Issues:**
- FAISS generally faster than Chroma for large documents
- HuggingFace embeddings process locally (slower but free)

## Security

Create a `.gitignore` file to protect sensitive data:
```
.env
*.pkl
__pycache__/
.streamlit/
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request



