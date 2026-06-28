# 🎥 YouTube RAG Assistant

An AI-powered YouTube chatbot that lets users ask questions about any YouTube video using **Retrieval-Augmented Generation (RAG)**.

The application extracts the video's transcript, converts it into semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant context for each question, and generates accurate responses using a Large Language Model.

---

## 🚀 Features

* 🎥 Chat with any YouTube video
* 🌍 Multi-language transcript support

  * English
  * Hindi
  * Spanish
  * French
  * German
  * Japanese
  * Korean
  * Portuguese
  * Italian
  * Russian
* 🧠 Retrieval-Augmented Generation (RAG)
* 📚 FAISS Vector Database
* 🔍 Semantic Search using Hugging Face Embeddings
* 🤖 AI-powered question answering
* 💬 Interactive Streamlit chat interface
* 📊 Video statistics dashboard
* 🖼️ Displays video thumbnail and title

---

## 🏗️ Project Architecture

```
User
   │
   ▼
YouTube URL
   │
   ▼
Transcript Extraction
   │
   ▼
Text Chunking
   │
   ▼
Hugging Face Embeddings
   │
   ▼
FAISS Vector Store
   │
   ▼
Retriever
   │
   ▼
Prompt Template
   │
   ▼
LLM (Qwen via Hugging Face)
   │
   ▼
Answer
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / LLM

* LangChain
* Hugging Face Endpoint
* Qwen 2.5 Instruct

### Embeddings

* Hugging Face Sentence Transformers

### Vector Database

* FAISS

### Transcript

* youtube-transcript-api

---

## 📁 Project Structure

```
youtube-rag-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── rag/
│   ├── chain.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── prompt.py
│   ├── retriever.py
│   ├── splitter.py
│   └── vector_store.py
│
├── utils/
│   ├── transcript.py
│   ├── video_info.py
│   └── youtube.py
│
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/youtube-rag-assistant.git

cd youtube-rag-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
HUGGINGFACEHUB_API_TOKEN=YOUR_API_KEY
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Launch the application.
2. Paste a YouTube video URL.
3. Select the transcript language.
4. Click **Process Video**.
5. Wait for the knowledge base to be created.
6. Start asking questions about the video.

---



## 📌 Example Questions

* Summarize this video.
* What are the key takeaways?
* Explain the main concept.
* What examples are discussed?
* What are the limitations mentioned?
* Who is the speaker talking about?

---

## 🔮 Future Improvements

* Conversation memory
* Follow-up questions
* Timestamp-based citations
* Source chunk references
* PDF conversation export
* Multiple LLM support
* Persistent vector database
* Dark mode enhancements

---

## 📚 Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Embedding Models
* Vector Databases
* Prompt Engineering
* LangChain LCEL
* Large Language Models
* Streamlit Application Development

---

## 👨‍💻 Author

**Sankalp Tewari**

If you found this project helpful, consider giving it a ⭐ on GitHub.
