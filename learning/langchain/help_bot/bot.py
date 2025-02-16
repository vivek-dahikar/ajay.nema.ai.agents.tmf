import chromadb
from sentence_transformers import SentenceTransformer
from langchain_google_genai import ChatGoogleGenerativeAI
import sys

ROLE = "I am HelpBoat,the official help desk assistant for xyz. My purpose is to assist users with any queries related to xyz."

# Load ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="help_docs")

# Load Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Define Retrieval Function
def retrieve_relevant_docs(query, top_k=3):
    query_embedding = embedding_model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)
    return results["documents"][0] if "documents" in results else []

# LLM for Answer Generation using Gemini API
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key="")  # Replace with your Gemini API Key

def generate_response(query):
    retrieved_docs = retrieve_relevant_docs(query)
    context = "\n".join(retrieved_docs)
    prompt = f"{ROLE}\n\nUse the following context to answer the question. If the context is insufficient, rely on general knowledge and conversational intelligence to provide a helpful response.:\n{context}\nQuestion: {query}\nAnswer:"
    response = llm.invoke(prompt)
    return response.content  # Use .content to extract the text response

# Real-time Q&A Loop
if __name__ == "__main__":
    print("Boat is ready! Type your questions below. Type 'exit' to quit.")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            sys.exit()
        response = generate_response(user_query)
        print("Boat:", response)
