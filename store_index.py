from src.helper import load_pdf_file,text_split,embedding_model
from langchain.vectorstores import Pinecone
from pinecone.grpc import PineconeGRPC
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os


load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

extracted_data = load_pdf_file(data="Data/")
text_chunks = text_split(extracted_data)


pc = PineconeGRPC(api_key=PINECONE_API_KEY)

index_name = "medicalbot"

pc.create_index(
    name=index_name,
    dimension=768,
    metric='cosine',
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

docsearch = Pinecone.from_documents(
    documents=text_chunks,
    embedding=embedding_model,
    index_name = index_name
)