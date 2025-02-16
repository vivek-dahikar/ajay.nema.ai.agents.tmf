How to Set Up & Use Boat
Step 1: Clone the GitHub Repository.

Step 2: Install Dependencies
    pip install -r requirements.txt

Step 3: Create the Vector Database, Add your PDF file path in the code.
        Run the following command to generate the vector database:

    python create_db.py


Step 3: Run the Bot


    python bot.py







Overview:- 


Step 1: Define the Project Goal
 We aimed to build a help bot that can answer user queries using a help document (PDF).
 It should use free and open-source LLMs (due to system limitations).
 The bot should retrieve relevant context from the document before generating responses (RAG pipeline).

Step 2: Extract Text from the Help Document (PDF)
 We used Python to read and extract text from the PDF.
 The extracted text serves as the knowledge base for the bot.

Step 3: Generate Embeddings for Text Retrieval
 Since LLMs can't search large documents directly, we converted the extracted text into embeddings (vector representations).
 We used chromaDB (a free and fast vector database) to store and retrieve relevant text based on user queries.

Step 4: Set Up the Language Model (LLM) for Responses
    Due to system limitations, we used a small and free open-source LLM.
    The model takes the retrieved context and user query as input to generate answers.

Step 5: Build the Query Pipeline (RAG - Retrieval-Augmented Generation)
    When a user asks a question:
    Convert the query into an embedding.
    Retrieve the most relevant text chunks from chromaDB.
    Pass this retrieved text and the user query to the LLM.
    Generate the final answer.

Step 6: Improve the Prompt for Better Answers
    We modified the prompt to allow the bot to:
    Answer using the help document first.
    If the document lacks info, use general intelligence to respond.
    This made the bot more conversational (e.g., responding naturally to "thank you").

Step 7: Testing the Prototype & Recording a Demo
    We tested different queries to ensure the bot retrieves and answers correctly.
    The current version works well but has limited help document data.

