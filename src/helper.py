from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os 


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    document = loader.load()

    return document



def text_split(extracted_data):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    chunks = splitter.split_documents(extracted_data)

    return chunks


embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")