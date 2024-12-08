# 🏥 End-to-End Medical Chatbot  

### 🌟 Introduction  
This **healthcare chatbot** provides reliable information on diseases and treatments, including recommended medicines and precautions.  
It aims to simplify healthcare access by enabling users to directly ask questions without searching through numerous articles and websites.  

---

### 📚 Data Acquisition  
- **Type**: Retrieval-Augmented Generative (RAG) AI Project.  
- **Source**: Gale Medicine Encyclopedia.  
  - Over **1000 pages** covering major and minor diseases and their treatments.  

---

### 🔧 Data Preprocessing  
- **Tool**: LangChain's `DirectoryLoader` for document loading.  
- **Splitter**: `RecursiveCharacterTextSplitter` with:  
  - **Chunk Size**: 1000 tokens.  
  - **Chunk Overlap**: 100 tokens to preserve semantic context.  

---

### 🔢 Vectorization  
- Converts text into machine-readable **vector form**.  
- **Embedding Model**:  
  - `GoogleGenerativeAIEmbeddings` with `models/embedding-001`.  
  - Generates **768-dimensional embeddings**.  

---

### 💾 Storing Embeddings in Pinecone Database  
- **Database**: Pinecone (cloud-based vector storage platform).  
- **Process**:  
  1. Generate API Key via Pinecone account.  
  2. Create an index to store vectors.  
  3. Store embeddings using `langchain.vectorstores.Pinecone` API.  

---

### 🔍 Document Retrieval  
- **Similarity Metric**: Cosine similarity.  
- Retrieves documents relevant to user queries from the vector database.  

---

### 🤖 Chatbot Development  
- **Tools**: LangChain.  
- **Components**:  
  - `ChatGoogleGenerativeAI` (LLM).  
  - `ChatPromptTemplate` for task instructions.  
  - `create_retrieval_chain` and `create_stuff_documents_chain` for:  
    - Integrating LLM, prompt, and retriever.  
    - Generating **structured responses** to user queries using the **Gemini-1.5-Pro model**.  

---

### 🌐 Frontend and Backend  
- **Backend**: Flask-based API.  
- **Frontend**: HTML/CSS for a user-friendly interface.  

---

### 🚀 Deployment  
- **Containerization**: Docker for creating a deployable image.  
- **CI/CD Pipeline**:  
  - **Tool**: GitHub Actions.  
  - Ensures seamless updates to the database without interrupting user services.  

---

### 📜 License  
This project is licensed under the **MIT License**.  

---

## 🛠️ How to Run  

### Prerequisites  
1. Python 3.x  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
3.Clone the repository:
 ```bash
 Copy code:
  git clone https://github.com/yourusername/medical-chatbot.git
  cd medical-chatbot
 Run the Flask API:
 Copy code:
  python app.py
