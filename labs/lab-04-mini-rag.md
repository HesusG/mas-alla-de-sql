# Lab 4: Mini RAG App

**Duracion**: ~45 minutos
**Objetivo**: Construir una aplicacion RAG completa con ChromaDB, together.ai y Gradio.

## Prerequisitos

```bash
pip install chromadb together gradio python-dotenv
```

Necesitas una API key de [together.ai](https://api.together.ai/) (tier gratuito disponible).

Crea un archivo `.env`:
```
TOGETHER_API_KEY=tu_api_key_aqui
```

## Paso 1: Base de conocimiento

Crea un archivo `my_rag.py`:

```python
import chromadb
from together import Together
from dotenv import load_dotenv

load_dotenv()

# Crear base de conocimiento
client = chromadb.Client()
kb = client.create_collection("mi_knowledge_base")

# Agrega tus propios documentos (cambia estos por tu tema)
kb.add(
    documents=[
        "Para ser Data Analyst necesitas SQL, Python y una herramienta de visualizacion como Tableau o Power BI",
        "Los Data Engineers construyen pipelines de datos y necesitan Python, SQL, Spark y cloud (AWS/Azure/GCP)",
        "Business Intelligence se enfoca en reportes y dashboards para la toma de decisiones",
        "Machine Learning Engineers implementan modelos en produccion usando Python, Docker y APIs",
        "Los Data Scientists combinan estadistica, programacion y conocimiento de negocio",
        "El salario promedio de un Data Analyst entry-level en Mexico es de 20,000-30,000 MXN mensuales",
        "Las habilidades mas demandadas en 2024 son: SQL, Python, Power BI, cloud computing y machine learning",
        "La diferencia entre BI y Data Science es que BI mira el pasado/presente y DS predice el futuro",
    ],
    ids=[f"doc{i}" for i in range(8)],
)

print(f"Knowledge base creada con {kb.count()} documentos")
```

## Paso 2: Funcion RAG

Agrega despues:

```python
llm = Together()

def ask_rag(question: str) -> str:
    # 1. Retrieve: buscar documentos relevantes
    results = kb.query(query_texts=[question], n_results=3)
    context = "\n".join(results["documents"][0])

    # 2. Generate: LLM responde usando el contexto
    response = llm.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente experto en carreras de datos. "
                    "Responde en espanol usando SOLO el contexto proporcionado. "
                    "Si no tienes informacion suficiente, dilo."
                ),
            },
            {
                "role": "user",
                "content": f"Contexto:\n{context}\n\nPregunta: {question}",
            },
        ],
        max_tokens=512,
        temperature=0.7,
    )

    return response.choices[0].message.content
```

## Paso 3: Probar en terminal

```python
# Prueba rapida
preguntas = [
    "Que necesito aprender para ser Data Analyst?",
    "Cual es la diferencia entre BI y Data Science?",
    "Cuanto gana un analista de datos en Mexico?",
]

for p in preguntas:
    print(f"\nPregunta: {p}")
    print(f"Respuesta: {ask_rag(p)}")
```

Ejecuta: `python my_rag.py`

## Paso 4: Agregar interfaz Gradio

Reemplaza el bloque de prueba por:

```python
import gradio as gr

def chat_fn(question, history):
    return ask_rag(question)

demo = gr.ChatInterface(
    fn=chat_fn,
    title="Mi Mini RAG",
    description="Preguntame sobre carreras en datos!",
    examples=[
        "Que necesito para ser Data Analyst?",
        "Cuanto gana un analista en Mexico?",
    ],
)

demo.launch()
```

Ejecuta y abre http://localhost:7860 en tu navegador.

## Retos

1. Cambia los documentos por informacion de tu interes (recetas, deportes, tu carrera)
2. Agrega mas documentos (15-20) y observa como mejoran las respuestas
3. Experimenta con `temperature` (0.0 = determinista, 1.0 = creativo)
4. Agrega metadata a tus documentos y usa `where` filters

## Hints

- Si el LLM "alucina" (inventa informacion), revisa que el contexto recuperado sea relevante
- Mas documentos = mejores respuestas (hasta cierto punto)
- `n_results=3` es un buen default; mas contexto no siempre es mejor
- together.ai tiene un tier gratuito con creditos suficientes para este lab
