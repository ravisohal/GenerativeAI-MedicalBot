from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask
app = Flask(__name__)

# Set environment variables
load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

#print(PINECONE_API_KEY)
#print(OPENAI_API_KEY)   

# Load the embeddings
logging.info("Downloading the embeddings...")
embeddings = download_hugging_face_embeddings()
logging.info("Embeddings downloaded successfully!") 

# Initialize Pinecone
logging.info("Creating a Pinecone index...")
docsearch = PineconeVectorStore.from_existing_index(
    index_name="medicalbot",
    embedding=embeddings
)
logging.info("Pinecone index created successfully!")    

# Initialize the retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

# Initialize OpenAI
logging.info("Creating an OpenAI instance...")
llm = OpenAI(temperature=0.4, max_tokens=500)
logging.info("OpenAI instance created successfully!")

# Create the prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Create the chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
# Create the RAG chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route('/')
def index():
    logging.info("Rendering the chat interface...")
    return render_template('chat.html')
    logging.info("Chat interface rendered successfully!")

@app.route('/ask', methods=['GET', 'POST'])   
def ask():
    logging.info("Received a request...")   
    msg = request.form['msg']
    print(msg)
    response = rag_chain.invoke({"input": msg})
    print("Response: ", response["answer"])
    logging.info("Response: %s", response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    logging.info("Starting the server...")
    app.run(host="0.0.0.0", port=8080, debug=True)
    logging.info("Server stopped successfully!")