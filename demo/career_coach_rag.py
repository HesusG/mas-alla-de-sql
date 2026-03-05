"""
AI Career Coach for BI Students
RAG demo: ChromaDB + together.ai + Gradio
"""

import json
import os

import chromadb
import gradio as gr
from dotenv import load_dotenv
from together import Together

load_dotenv()

# --- 1. Load job postings into ChromaDB ---

def load_knowledge_base():
    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="bi_job_postings",
        metadata={"hnsw:space": "cosine"},
    )

    if collection.count() > 0:
        return collection

    with open(os.path.join(os.path.dirname(__file__), "data", "bi_job_postings.json")) as f:
        postings = json.load(f)

    documents = []
    metadatas = []
    ids = []

    for i, posting in enumerate(postings):
        doc = (
            f"Puesto: {posting['title']}\n"
            f"Empresa: {posting['company']}\n"
            f"Ubicacion: {posting['location']}\n"
            f"Salario: {posting['salary_range']}\n"
            f"Experiencia: {posting['experience']}\n"
            f"Habilidades: {', '.join(posting['skills'])}\n"
            f"Descripcion: {posting['description']}"
        )
        documents.append(doc)
        metadatas.append({
            "company": posting["company"],
            "location": posting["location"],
            "experience": posting["experience"],
        })
        ids.append(f"job_{i}")

    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print(f"Loaded {len(documents)} job postings into ChromaDB")
    return collection


# --- 2. RAG: Retrieve + Generate ---

llm = Together()
collection = load_knowledge_base()

SYSTEM_PROMPT = """Eres un coach de carrera especializado en estudiantes de Inteligencia de Negocios (BI) en Mexico.
Responde SIEMPRE en espanol.
Usa SOLO la informacion de las ofertas de trabajo proporcionadas como contexto.
Si no tienes informacion suficiente, dilo honestamente.
Se motivador pero realista. Da consejos accionables.
Al final de tu respuesta, lista las ofertas de trabajo que usaste como fuente."""


def query_career_coach(question: str, history: list) -> str:
    # Retrieve relevant job postings
    results = collection.query(query_texts=[question], n_results=5)
    context = "\n\n---\n\n".join(results["documents"][0])

    # Build messages
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({
        "role": "user",
        "content": (
            f"Contexto (ofertas de trabajo reales):\n{context}\n\n"
            f"Pregunta del estudiante: {question}"
        ),
    })

    # Generate
    response = llm.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
    )

    return response.choices[0].message.content


# --- 3. Gradio UI ---

demo = gr.ChatInterface(
    fn=query_career_coach,
    title="AI Career Coach para BI",
    description=(
        "Preguntame sobre carreras en datos, habilidades que necesitas, "
        "empresas que contratan en Mexico, o que tecnologias aprender. "
        "Mis respuestas se basan en 40+ ofertas de trabajo reales."
    ),
    examples=[
        "Que habilidades necesito para un puesto de Data Analyst en consulting?",
        "Que empresas en Monterrey buscan egresados de BI?",
        "Se Python, SQL y Tableau - para que puestos califico?",
        "Cual es la diferencia entre lo que pide Amazon y Deloitte?",
        "Que tecnologias deberia aprender este semestre?",
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()
