import chromadb

# 1. Crear cliente (en memoria, sin servidor)
client = chromadb.Client()

# 2. Crear colección (como una "tabla" pero para vectores)
collection = client.create_collection("mi_primera_coleccion")

# 3. Agregar documentos (ChromaDB genera los embeddings automáticamente)
collection.add(
    documents=[
        "Me encanta la comida mexicana, especialmente los tacos",
        "La inteligencia artificial está transformando los negocios",
        "Python es el mejor lenguaje para análisis de datos",
        "Los burritos y las enchiladas son deliciosos",
        "Machine learning permite predecir tendencias del mercado",
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
)

# 4. Buscar por SIGNIFICADO (no por palabras exactas)
results = collection.query(
    query_texts=["gastronomía latinoamericana"],  # No dice "tacos" ni "mexicana"
    n_results=2,
)

print("Búsqueda: 'gastronomía latinoamericana'")
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"  [{dist:.4f}] {doc}")
