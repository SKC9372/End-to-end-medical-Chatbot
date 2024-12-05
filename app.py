from flask import Flask,render_template,jsonify,request
from src.helper import embedding_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain,RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.vectorstores import Pinecone
from src.prompt import system_prompt
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


app = Flask(__name__)

index_name = 'medicalbot'

docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embedding_model
)

retriever = docsearch.as_retriever(similarity = 'cosine',search_kwargs = {"k":5})

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro',max_tokens=500,temperature=0.3)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]

)


question_answer_chain = create_stuff_documents_chain(llm,prompt=prompt)

rag_chain = create_retrieval_chain(
    retriever,question_answer_chain,
)

@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/get',methods = ['GET','POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({"input":msg})
    print("Response: ",response['answer'])
    return str(response['answer'])


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)


