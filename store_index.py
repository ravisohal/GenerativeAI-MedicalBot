from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set environment variables
load_dotenv()
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

# Load the data, split the text, and download the embeddings
logging.info("Loading the data, splitting the text, and downloading the embeddings...")
extracted_data=load_pdf_file(data='data/')
logging.info("Data loaded successfully!")
text_chunks=text_split(extracted_data)
logging.info("Text split successfully!")
embeddings = download_hugging_face_embeddings()
logging.info("Embeddings downloaded successfully!")

# Initialize Pinecone and create an index
logging.info("Creating a Pinecone index...")    
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalbot"

pc.create_index(
    name=index_name,
    dimension=384, 
    metric="cosine", 
    spec=ServerlessSpec(
        cloud="aws", 
        region="us-east-1"
    ) 
) 
logging.info("Pinecone index created successfully!")

# Embed each chunk and upsert the embeddings into your Pinecone index.
logging.info("Upserting the embeddings into the Pinecone index...")
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)
logging.info("Embeddings upserted successfully!")
logging.info("Indexing complete!")