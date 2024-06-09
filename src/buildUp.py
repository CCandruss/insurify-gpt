import setUp
import bs4
from pathlib import Path
import os
from pymongo import MongoClient

from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch

client = OpenAI(organization='org-GPDJJQ8LUt6Px5RrkzmU6onv')

# Only keep post title, headers, and content from the full HTML.
# bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
file_path = (
    "/Users/caleb/Documents/2018-IRC.pdf"
)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

ATLAS_CONNECTION_STRING = os.getenv('ATLAS_CONNECTION_STRING')
if not ATLAS_CONNECTION_STRING:
    raise ValueError("The ATLAS_CONNECTION_STRING environment variable is not set.")

cluster = MongoClient(ATLAS_CONNECTION_STRING)

DB_NAME = "Insurify-Vec-Store"
COLLECTION_NAME = "Xactify"

MONGODB_COLLECTION = cluster[DB_NAME][COLLECTION_NAME]

loader = PyPDFLoader(file_path)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

docs = text_splitter.split_documents(data)



vector_search = MongoDBAtlasVectorSearch.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(),
    collection=MONGODB_COLLECTION,
    index_name="default"  # Use a predefined index name
)
# vector_search = MongoDBAtlasVectorSearch.from_documents(
#     documents=docs,
#     embedding=OpenAIEmbeddings(),
#     collection=MONGODB_COLLECTION,
#     index_name="default"  # Use a predefined index name
# )
