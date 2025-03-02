# Generative AI Projects: Medical Chatbot using RAG for learning purpose

## How to Run?

### Steps:

# Medical Chatbot Project

This project is a learning exercise to build a medical chatbot using AI. It lets you ask medical questions and get answers.

## How to Get Started

Here's how to run the chatbot on your computer:

### 1. Get the Project

First, download the project files from this website:

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)  # Replace with your repository URL
cd YOUR_REPO_NAME
```

### 2. Set Up the Environment

We need to create a special space for the project to run. Follow these steps:

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 3. Install the Necessary Tools

Now, install the tools the project needs:

```bash
pip install -r requirements.txt
```

### 4. Add Your Secret Keys

The chatbot needs access to some online services. You'll need to create a file with your secret keys:

* Create a file named `.env` in the same folder as the project files.
* Open the `.env` file and add these lines, replacing the "x"s with your actual keys:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 5. Prepare the Data

The chatbot needs to learn about medical information. Run this command:

```bash
python store_index.py
```

### 6. Start the Chatbot

Finally, start the chatbot with this command:

```bash
python app.py
```

### 7. Use the Chatbot

Open your web browser and go to `http://localhost:5000`. You can now ask medical questions.

## What We Used

* **Python:** The main programming language.
* **LangChain:** A tool to help build AI applications.
* **Flask:** A tool to create the website for the chatbot.
* **GPT (OpenAI):** The AI that generates the answers.
* **Pinecone:** A place to store the medical information.

## Important Notes

* Make sure you have your Pinecone and OpenAI keys ready.
* Preparing the data might take some time.
* This chatbot is for learning purposes only. Always ask a real doctor for medical advice.
* Replace `YOUR_USERNAME/YOUR_REPO_NAME` with your actual repository path.
```

Credits: 
Bappy Ahmed for guidance by youtube video