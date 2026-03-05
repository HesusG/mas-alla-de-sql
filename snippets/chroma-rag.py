import chromadb
from together import Together

# 1. Base de conocimiento en ChromaDB
client = chromadb.Client()
kb = client.create_collection("knowledge_base")

kb.add(
    documents=[
        "Elasticsearch usa BM25 para rankear resultados por relevancia",
        "ChromaDB almacena vectores y permite búsqueda semántica",
        "RAG combina retrieval con generación para respuestas precisas",
        "Los embeddings representan texto como vectores numéricos",
        "SQL es ideal para datos estructurados con esquema fijo",
    ],
    ids=[f"doc{i}" for i in range(5)],
)

# 2. Retrieval: buscar contexto relevante
question = "¿Cómo funciona la búsqueda semántica?"
context = kb.query(query_texts=[question], n_results=2)

# 3. Generation: LLM responde usando el contexto
llm = Together()
response = llm.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": f"Responde usando SOLO este contexto:\n{context['documents'][0]}"},
        {"role": "user", "content": question},
    ],
)

print(f"Pregunta: {question}")
print(f"Respuesta: {response.choices[0].message.content}")
