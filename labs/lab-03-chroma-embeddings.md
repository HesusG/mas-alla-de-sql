# Lab 3: ChromaDB y Embeddings

**Duracion**: ~30 minutos
**Objetivo**: Entender embeddings y busqueda semantica con ChromaDB.

## Prerequisitos

```bash
pip install chromadb
```

## Paso 1: Tu primera coleccion

Crea un archivo `lab3.py`:

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("lab3")

# Agregar documentos sobre tecnología
collection.add(
    documents=[
        "Python es un lenguaje de programacion muy popular para ciencia de datos",
        "SQL permite consultar bases de datos relacionales de forma eficiente",
        "Los dashboards de Tableau ayudan a visualizar metricas de negocio",
        "Machine learning permite a las computadoras aprender de los datos",
        "Excel sigue siendo la herramienta mas usada para analisis basico",
        "Power BI es la herramienta de Microsoft para inteligencia de negocios",
        "Las redes neuronales son la base del deep learning moderno",
        "R es un lenguaje estadistico popular en la academia",
    ],
    ids=[f"doc{i}" for i in range(8)],
)

print(f"Coleccion creada con {collection.count()} documentos")
```

## Paso 2: Busqueda semantica

Agrega al final de tu archivo:

```python
# Busqueda por significado
queries = [
    "herramientas para hacer graficas de datos",
    "inteligencia artificial",
    "lenguajes de programacion para analistas",
]

for q in queries:
    results = collection.query(query_texts=[q], n_results=3)
    print(f"\nBusqueda: '{q}'")
    for doc, dist in zip(results["documents"][0], results["distances"][0]):
        print(f"  [{dist:.4f}] {doc}")
```

Ejecuta: `python lab3.py`

**Pregunta**: ¿Los resultados tienen sentido? ¿Alguno te sorprendio?

## Paso 3: Experimenta con queries

Prueba estas busquedas y anota que encuentras:

1. `"como analizar informacion empresarial"` — ¿Encuentra BI tools?
2. `"aprendizaje automatico"` — ¿Encuentra machine learning? (es sinonimo en espanol)
3. `"Microsoft Office"` — ¿Encuentra Excel y Power BI?

## Paso 4: Metadata y filtros

```python
# Crear nueva coleccion con metadata
tools = client.create_collection("tools")

tools.add(
    documents=[
        "Python es versatil para datos y web",
        "SQL es esencial para bases de datos",
        "Tableau crea visualizaciones interactivas",
        "Power BI se integra con Microsoft 365",
    ],
    metadatas=[
        {"tipo": "lenguaje", "dificultad": "media"},
        {"tipo": "lenguaje", "dificultad": "baja"},
        {"tipo": "visualizacion", "dificultad": "media"},
        {"tipo": "visualizacion", "dificultad": "baja"},
    ],
    ids=["py", "sql", "tab", "pbi"],
)

# Buscar SOLO herramientas de visualizacion
results = tools.query(
    query_texts=["graficas de datos"],
    n_results=2,
    where={"tipo": "visualizacion"},
)
print("\nSolo visualizacion:", results["documents"][0])
```

## Retos

1. Agrega 5 documentos sobre tu tema favorito (deportes, musica, etc.) y busca por significado
2. Intenta buscar en ingles documentos en espanol — ¿funciona?
3. Crea una coleccion con metadata `{"nivel": "junior"}` y `{"nivel": "senior"}` y filtra

## Hints

- ChromaDB usa `all-MiniLM-L6-v2` por defecto para generar embeddings
- Las distancias mas cercanas a 0 son mas similares
- `where` filters usan operadores: `$eq`, `$ne`, `$gt`, `$lt`, `$in`
