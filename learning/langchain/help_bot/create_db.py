import fitz  # PyMuPDF for PDF processing
import chromadb
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF and Extract Text
pdf_path = r"Pdf_path"
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

# Initialize ChromaDB and Store Documents
def create_chroma_db(help_doc_path, db_path="./chroma_db"):
    help_text = extract_text_from_pdf(help_doc_path)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    doc_chunks = text_splitter.split_text(help_text)
    
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_or_create_collection(name="help_docs")
    
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    for i, chunk in enumerate(doc_chunks):
        embedding = embedding_model.encode(chunk).tolist()
        collection.add(ids=[str(i)], embeddings=[embedding], documents=[chunk])
    
    print("ChromaDB created and populated successfully.")

if __name__ == "__main__":
    create_chroma_db(r"YOUR_PDF_PATH")
