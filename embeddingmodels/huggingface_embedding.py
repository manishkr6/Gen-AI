from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello this is Manish Kumar",
    "I am form Gangtok Sikkim"
    "You are going to learn Gen AI",
]

vector = embedding.embed_query(texts)

print(vector)