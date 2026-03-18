# MicroPréstamos MX — RAG Demo (Hugging Face Spaces)

Guía completa para construir un demo de **Retrieval-Augmented Generation** con datos realistas de una fintech mexicana de micro-créditos. Diseñado como herramienta didáctica para estudiantes de Inteligencia de Negocios (BI) del ITESM.

---

## Qué es este proyecto

Un chatbot RAG que permite a un analista de BI hacer preguntas en lenguaje natural sobre datos **no estructurados** de MicroPréstamos MX: transcripciones de llamadas, emails de quejas, conversaciones de chatbot, posts en redes sociales y documentos internos.

**¿Por qué importa?** El 80% de los datos empresariales son no estructurados. SQL no puede buscar por significado — solo por palabras exactas. Este demo muestra cómo ChromaDB + un LLM resuelven ese problema.

### Stack técnico

| Componente | Tecnología |
|------------|-----------|
| Base de datos vectorial | ChromaDB (in-memory) |
| Embeddings | sentence-transformers (default de ChromaDB) |
| LLM | Llama-3.3-70B-Instruct-Turbo vía together.ai |
| UI | Gradio |
| Generación de datos | faker + together.ai |
| Deploy | Hugging Face Spaces |

---

## Arquitectura

```
┌──────────────────────────────────────────────────────┐
│                    Gradio UI                         │
│  ┌────────────────────────────────────────────────┐  │
│  │  "¿Cuáles son las quejas más frecuentes       │  │
│  │   de clientes en mora?"                        │  │
│  └──────────────────┬─────────────────────────────┘  │
│                     │                                │
│         ┌───────────▼───────────┐                    │
│         │  1. Embed query       │                    │
│         │  (sentence-transform) │                    │
│         └───────────┬───────────┘                    │
│                     │                                │
│         ┌───────────▼───────────┐    ┌────────────┐  │
│         │  2. Retrieve top-5    │◄───│  ChromaDB  │  │
│         │  (cosine similarity)  │    │  200+ docs │  │
│         └───────────┬───────────┘    └────────────┘  │
│                     │                                │
│         ┌───────────▼───────────┐                    │
│         │  3. Generate response │                    │
│         │  (Llama-3.3-70B)      │                    │
│         └───────────┬───────────┘                    │
│                     │                                │
│         ┌───────────▼───────────┐                    │
│         │  Respuesta con citas  │                    │
│         │  de fuente y canal    │                    │
│         └───────────────────────┘                    │
└──────────────────────────────────────────────────────┘
```

---

## Paso 1: Generar los datos

El lab original del workshop tiene 25 documentos hardcodeados. Para un demo creíble necesitamos **200+** documentos que simulen la operación real de una fintech mexicana.

### Datos estructurados (CSV)

Dos archivos CSV que representan la base de datos relacional de la empresa:

**`data/clientes.csv`** — 150 clientes ficticios

| Campo | Tipo | Ejemplo |
|-------|------|---------|
| `id` | int | 1 |
| `nombre` | str | "María González López" |
| `edad` | int | 28 |
| `estado` | str | "Nuevo León" |
| `ingreso_mensual` | float | 12500.00 |
| `score_crediticio` | int | 650 |
| `fecha_registro` | date | "2024-03-15" |

**`data/prestamos.csv`** — 300 préstamos

| Campo | Tipo | Ejemplo |
|-------|------|---------|
| `id` | int | 1 |
| `cliente_id` | int | 42 |
| `monto` | float | 5000.00 |
| `tasa_mensual` | float | 0.025 |
| `plazo_dias` | int | 90 |
| `estatus` | str | "activo" |
| `fecha_desembolso` | date | "2024-06-01" |

Valores de `estatus`: `activo`, `liquidado`, `moroso`, `reestructurado`.

### Datos no estructurados (documentos para ChromaDB)

Estos son los documentos que ChromaDB indexará. Provienen de 6 canales distintos:

| Canal | Clave | Volumen | Descripción |
|-------|-------|---------|-------------|
| Chatbot de la app | `chatbot` | ~40 | Consultas de clientes: solicitudes de préstamo, dudas sobre pagos, problemas con la app |
| Quejas por email | `quejas_email` | ~35 | Quejas formales: cobros indebidos, hostigamiento, amenazas de ir a CONDUSEF |
| Notas de cobranza | `cobranza` | ~30 | Notas internas de agentes: resultados de llamadas, promesas de pago, escalamientos |
| Llamadas transcritas | `llamadas` | ~30 | Transcripciones de llamadas: reestructuraciones, planes de pago, aclaraciones |
| Redes sociales | `redes_sociales` | ~35 | Posts de Twitter/Facebook: elogios, quejas públicas, preguntas |
| Documentos internos | `interno` | ~15 | Políticas de cobranza, procesos de originación, reportes de riesgo, memos de cumplimiento |

**Total: ~185-200 documentos**

### Metadata por documento

Cada documento lleva metadata que permite filtros en ChromaDB:

```json
{
  "id": "chatbot_023",
  "text": "Hola, quiero saber si puedo pedir un préstamo de 5000 pesos...",
  "metadata": {
    "fuente": "chatbot",
    "cliente_id": 42,
    "fecha": "2024-07-15",
    "sentimiento": "neutro"
  }
}
```

Valores de `sentimiento`: `positivo`, `negativo`, `neutro`.

### Script de generación: `generate_data.py`

El script genera todos los datos en dos fases: datos estructurados con `faker` + `random`, y documentos no estructurados con un LLM.

```python
"""
generate_data.py — Genera datos realistas para MicroPréstamos MX RAG demo.

Uso:
    pip install faker together
    export TOGETHER_API_KEY="tu-api-key"
    python generate_data.py

Output:
    data/clientes.csv
    data/prestamos.csv
    data/documents.json
"""

import csv
import json
import os
import random
from datetime import datetime, timedelta

from faker import Faker
from together import Together

fake = Faker("es_MX")
random.seed(42)
Faker.seed(42)

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Constantes del negocio ───

ESTADOS = [
    "Nuevo León", "Jalisco", "Ciudad de México", "Estado de México",
    "Puebla", "Guanajuato", "Veracruz", "Chihuahua", "Sonora",
    "Querétaro", "Yucatán", "Sinaloa", "Tamaulipas", "Michoacán",
    "Oaxaca", "Aguascalientes", "San Luis Potosí", "Baja California",
]

ESTATUS_PRESTAMO = ["activo", "liquidado", "moroso", "reestructurado"]
ESTATUS_WEIGHTS = [0.35, 0.30, 0.25, 0.10]

# ─── Fase 1: Datos estructurados ───

def generate_clientes(n=150):
    clientes = []
    for i in range(1, n + 1):
        clientes.append({
            "id": i,
            "nombre": fake.name(),
            "edad": random.randint(21, 58),
            "estado": random.choice(ESTADOS),
            "ingreso_mensual": round(random.uniform(6000, 45000), 2),
            "score_crediticio": random.randint(400, 800),
            "fecha_registro": fake.date_between(
                start_date="-2y", end_date="today"
            ).isoformat(),
        })
    return clientes


def generate_prestamos(clientes, avg_per_client=2):
    prestamos = []
    prestamo_id = 1
    for cliente in clientes:
        n_prestamos = random.choices([1, 2, 3, 4], weights=[30, 40, 20, 10])[0]
        for _ in range(n_prestamos):
            monto = round(random.choice([1000, 2000, 3000, 5000, 8000, 10000, 15000]), 2)
            prestamos.append({
                "id": prestamo_id,
                "cliente_id": cliente["id"],
                "monto": monto,
                "tasa_mensual": round(random.uniform(0.015, 0.045), 3),
                "plazo_dias": random.choice([30, 60, 90, 120, 180]),
                "estatus": random.choices(ESTATUS_PRESTAMO, weights=ESTATUS_WEIGHTS)[0],
                "fecha_desembolso": fake.date_between(
                    start_date="-18m", end_date="today"
                ).isoformat(),
            })
            prestamo_id += 1
    return prestamos


def save_csv(data, filename, fieldnames):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"  ✅ {path} — {len(data)} registros")


# ─── Fase 2: Datos no estructurados (LLM) ───

# Prompts de generación por canal. Cada prompt pide un batch de documentos
# con instrucciones de estilo, registro y contenido específico.

CHANNEL_PROMPTS = {
    "chatbot": {
        "count": 40,
        "batch_size": 10,
        "system": (
            "Eres un generador de datos sintéticos para una fintech mexicana de micro-créditos "
            "llamada MicroPréstamos MX. Genera conversaciones de chatbot de la app móvil."
        ),
        "user_template": (
            "Genera {n} mensajes de clientes al chatbot de MicroPréstamos MX. "
            "Cada mensaje debe ser un JSON con campos 'text' y 'sentimiento' (positivo/negativo/neutro).\n\n"
            "Reglas:\n"
            "- Lenguaje informal, como chat (abreviaciones, sin acentos a veces)\n"
            "- Temas: solicitudes de préstamo, dudas sobre pagos, problemas con la app, "
            "consultas de saldo, aumento de línea de crédito, fechas de pago\n"
            "- Incluir montos en pesos mexicanos ($1,000 - $15,000)\n"
            "- Algunos mensajes con urgencia (emergencias médicas, renta, colegiatura)\n"
            "- Mezclar mensajes cortos (1 línea) y medianos (2-3 líneas)\n"
            "- Mencionar métodos de pago mexicanos: OXXO, 7-Eleven, SPEI, transferencia\n\n"
            "Responde SOLO con un JSON array. Sin explicaciones."
        ),
    },
    "quejas_email": {
        "count": 35,
        "batch_size": 10,
        "system": (
            "Eres un generador de datos sintéticos para una fintech mexicana. "
            "Genera emails de queja de clientes."
        ),
        "user_template": (
            "Genera {n} emails de queja de clientes de MicroPréstamos MX. "
            "Cada email debe ser un JSON con campos 'text' y 'sentimiento'.\n\n"
            "Reglas:\n"
            "- Formato de email: empezar con 'Asunto:' seguido del cuerpo\n"
            "- Registro formal a semi-formal\n"
            "- Temas: cobros indebidos, hostigamiento de cobranza, errores en Buró de Crédito, "
            "tasas diferentes a las pactadas, no poder acceder a la app, "
            "comisiones no informadas, filtración de datos personales\n"
            "- ~30% deben mencionar CONDUSEF, demanda o acciones legales\n"
            "- ~20% deben mencionar Buró de Crédito\n"
            "- Incluir términos financieros mexicanos: CAT, comisión por apertura, "
            "cargo moratorio, interés ordinario\n"
            "- Longitud: 3-6 oraciones por email\n"
            "- Sentimiento mayormente negativo\n\n"
            "Responde SOLO con un JSON array. Sin explicaciones."
        ),
    },
    "cobranza": {
        "count": 30,
        "batch_size": 10,
        "system": (
            "Eres un generador de datos sintéticos para una fintech mexicana. "
            "Genera notas internas del departamento de cobranza."
        ),
        "user_template": (
            "Genera {n} notas internas de agentes de cobranza de MicroPréstamos MX. "
            "Cada nota debe ser un JSON con campos 'text' y 'sentimiento' (neutro en su mayoría).\n\n"
            "Reglas:\n"
            "- Formato de nota interna: breve, factual, con jerga de cobranza\n"
            "- Temas: resultado de llamadas (contactado/no contactado/buzón), "
            "promesas de pago con fecha, escalamientos a jurídico, convenios de pago, "
            "referencias personales contactadas, visitas domiciliarias programadas\n"
            "- Incluir montos, fechas y plazos específicos\n"
            "- Algunos con banderas rojas: cliente agresivo, amenaza legal, "
            "teléfono desconectado, dirección incorrecta\n"
            "- Longitud: 2-4 oraciones\n"
            "- Usar formato 'Folio #XXXX:' al inicio\n\n"
            "Responde SOLO con un JSON array. Sin explicaciones."
        ),
    },
    "llamadas": {
        "count": 30,
        "batch_size": 10,
        "system": (
            "Eres un generador de datos sintéticos para una fintech mexicana. "
            "Genera transcripciones resumidas de llamadas del call center."
        ),
        "user_template": (
            "Genera {n} resúmenes de transcripciones de llamadas al call center de MicroPréstamos MX. "
            "Cada resumen debe ser un JSON con campos 'text' y 'sentimiento'.\n\n"
            "Reglas:\n"
            "- Formato: 'Transcript llamada #XXXX:' seguido del resumen\n"
            "- Temas: solicitudes de reestructuración, aclaraciones de pagos, "
            "planes de pago, estados de cuenta, quejas sobre agentes de cobranza, "
            "cancelación de préstamos, liquidaciones anticipadas\n"
            "- Incluir emociones del cliente (molesto, preocupado, tranquilo, llorando)\n"
            "- Algunos mencionan pérdida de empleo, enfermedad, divorcio como causa de mora\n"
            "- Incluir acciones del agente (ofreció reestructura, escaló a supervisor, etc.)\n"
            "- Longitud: 3-5 oraciones\n"
            "- Mezcla de sentimientos\n\n"
            "Responde SOLO con un JSON array. Sin explicaciones."
        ),
    },
    "redes_sociales": {
        "count": 35,
        "batch_size": 10,
        "system": (
            "Eres un generador de datos sintéticos para una fintech mexicana. "
            "Genera posts de redes sociales (Twitter/X y Facebook)."
        ),
        "user_template": (
            "Genera {n} posts de redes sociales sobre MicroPréstamos MX. "
            "Cada post debe ser un JSON con campos 'text' y 'sentimiento'.\n\n"
            "Reglas:\n"
            "- Mezcla de Twitter/X (cortos, con hashtags y @) y Facebook (más largos)\n"
            "- ~40% positivos (recomiendan, agradecen, servicio rápido)\n"
            "- ~45% negativos (quejas públicas, amenazas, malas experiencias)\n"
            "- ~15% neutros (preguntas, consultas)\n"
            "- Lenguaje coloquial mexicano: 'neta', 'chido', 'lana', 'jalar', 'nada que ver'\n"
            "- Incluir emojis donde sea natural (👍 😤 🙌 ⚠️ 💸)\n"
            "- Algunos tagueando @MicroPrestamosMX o @ABORADADN o @ABORADPRO\n"
            "- Hashtags: #fintech #microprestamos #fraude #buenservicio #mexico\n"
            "- Longitud: 1-3 oraciones\n\n"
            "Responde SOLO con un JSON array. Sin explicaciones."
        ),
    },
    "interno": {
        "count": 15,
        "batch_size": 5,
        "system": (
            "Eres un generador de datos sintéticos para una fintech mexicana. "
            "Genera documentos internos corporativos."
        ),
        "user_template": (
            "Genera {n} documentos internos de MicroPréstamos MX. "
            "Cada documento debe ser un JSON con campos 'text' y 'sentimiento' (neutro).\n\n"
            "Tipos de documentos:\n"
            "- Políticas de cobranza (límite de llamadas, horarios, prohibiciones)\n"
            "- Procesos de originación (requisitos, validaciones, tiempos de respuesta)\n"
            "- Reportes mensuales de riesgo (cartera vencida, factores de mora, tendencias)\n"
            "- Memos de cumplimiento regulatorio (CONDUSEF, CNBV, protección de datos)\n"
            "- Guías de capacitación para agentes (tono, frases prohibidas, escalamiento)\n"
            "- Comunicados internos (cambios de política, nuevos productos, alertas)\n\n"
            "Reglas:\n"
            "- Registro formal corporativo\n"
            "- Incluir números, porcentajes y fechas específicas\n"
            "- Mencionar reguladores mexicanos: CONDUSEF, CNBV, Profeco, Ley Fintech\n"
            "- Longitud: 2-4 párrafos por documento\n"
            "- Sentimiento neutro (son documentos oficiales)\n\n"
            "Responde SOLO con un JSON array. Sin explicaciones."
        ),
    },
}


def generate_documents_for_channel(client, channel, config, clientes):
    """Genera documentos para un canal usando el LLM en batches."""
    all_docs = []
    remaining = config["count"]
    batch_num = 0

    while remaining > 0:
        n = min(config["batch_size"], remaining)
        print(f"    Generando batch {batch_num + 1} ({n} docs)...")

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": config["system"]},
                {"role": "user", "content": config["user_template"].format(n=n)},
            ],
            max_tokens=4096,
            temperature=0.8,
        )

        raw = response.choices[0].message.content
        # Extraer JSON del response (puede venir envuelto en ```json ... ```)
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1]  # quitar primera línea
            raw = raw.rsplit("```", 1)[0]  # quitar última línea

        try:
            docs = json.loads(raw)
        except json.JSONDecodeError:
            print(f"    ⚠️ Error parseando JSON, reintentando batch...")
            continue

        for doc in docs:
            cliente = random.choice(clientes)
            fecha = fake.date_between(start_date="-12m", end_date="today").isoformat()
            all_docs.append({
                "id": f"{channel}_{len(all_docs):03d}",
                "text": doc["text"],
                "metadata": {
                    "fuente": channel,
                    "cliente_id": cliente["id"],
                    "fecha": fecha,
                    "sentimiento": doc.get("sentimiento", "neutro"),
                },
            })

        remaining -= n
        batch_num += 1

    return all_docs


def generate_all_documents(clientes):
    """Genera todos los documentos no estructurados."""
    client = Together(api_key=TOGETHER_API_KEY)
    all_documents = []

    for channel, config in CHANNEL_PROMPTS.items():
        print(f"\n  📝 Canal: {channel} ({config['count']} docs)")
        docs = generate_documents_for_channel(client, channel, config, clientes)
        all_documents.extend(docs)
        print(f"    ✅ {len(docs)} documentos generados")

    return all_documents


# ─── Main ───

if __name__ == "__main__":
    print("🏦 Generando datos para MicroPréstamos MX\n")

    # Fase 1: Estructurados
    print("📊 Fase 1: Datos estructurados")
    clientes = generate_clientes(150)
    prestamos = generate_prestamos(clientes)

    save_csv(clientes, "clientes.csv", list(clientes[0].keys()))
    save_csv(prestamos, "prestamos.csv", list(prestamos[0].keys()))

    # Fase 2: No estructurados
    print("\n📝 Fase 2: Datos no estructurados (LLM)")
    if not TOGETHER_API_KEY:
        print("  ⚠️ TOGETHER_API_KEY no encontrada.")
        print("  Exporta tu API key: export TOGETHER_API_KEY='tu-key'")
        print("  Obtén una gratis en: https://api.together.xyz")
    else:
        documents = generate_all_documents(clientes)
        doc_path = os.path.join(OUTPUT_DIR, "documents.json")
        with open(doc_path, "w", encoding="utf-8") as f:
            json.dump(documents, f, ensure_ascii=False, indent=2)
        print(f"\n  ✅ {doc_path} — {len(documents)} documentos")

    print("\n🎉 Generación completa")
```

### Cómo ejecutar el script de generación

```bash
# 1. Instalar dependencias
pip install faker together

# 2. Configurar API key (gratis en https://api.together.xyz)
export TOGETHER_API_KEY="tu-api-key-aqui"

# 3. Ejecutar
python generate_data.py
```

El script es **reproducible** — usa `random.seed(42)` y `Faker.seed(42)` para que los datos estructurados sean idénticos en cada ejecución. Los documentos generados por LLM variarán, pero la estructura y metadata serán consistentes.

### Técnicas de realismo

Para que los documentos sean creíbles en un contexto de BI, el script aplica:

| Técnica | Canal | Ejemplo |
|---------|-------|---------|
| Registro formal | `quejas_email`, `interno` | "Estimado, por medio de la presente..." |
| Registro coloquial | `chatbot`, `redes_sociales` | "Oye necesito lana urgente" |
| Jerga financiera MX | todos | CONDUSEF, Buró de Crédito, CAT, comisión, cargo moratorio |
| Slang mexicano | `redes_sociales`, `chatbot` | "neta", "chido", "jalar", "lana" |
| Longitud variable | por canal | Redes sociales: 1-3 oraciones; internos: 2-4 párrafos |
| Casos edge | `quejas_email`, `cobranza` | Números de cuenta erróneos, cobros duplicados, errores de sistema |

---

## Paso 2: El pipeline RAG

### Cómo funciona ChromaDB en este demo

ChromaDB almacena cada documento como un **vector de embedding** (representación numérica del significado). Cuando un usuario hace una pregunta:

1. La pregunta se convierte en embedding con el mismo modelo (sentence-transformers)
2. ChromaDB busca los 5 documentos más cercanos por **similitud coseno**
3. Esos documentos se pasan como contexto al LLM

```
"¿Hay clientes que mencionan CONDUSEF?"
         │
         ▼
    [0.23, -0.41, 0.87, ...]   ← embedding de la pregunta
         │
         ▼  similitud coseno
    doc_037: "Si no corrigen voy a ir a CONDUSEF"        (dist: 0.18)
    doc_042: "Esto lo voy a reportar a CONDUSEF y CNBV"  (dist: 0.22)
    doc_015: "Me dijeron que demandara en CONDUSEF"       (dist: 0.25)
    doc_089: "Le informé que puede acudir a CONDUSEF"     (dist: 0.31)
    doc_103: "Amenaza con acción legal ante regulador"    (dist: 0.34)
```

La búsqueda semántica encuentra el documento `doc_103` aunque **no contiene la palabra "CONDUSEF"** — entiende que "acción legal ante regulador" tiene el mismo significado.

### Cómo funciona la generación con LLM

El LLM (Llama-3.3-70B) recibe:

1. Un **system prompt** que define su rol como analista de BI
2. Los **5 documentos** recuperados como contexto
3. La **pregunta** del usuario

El system prompt le indica que **solo use la información del contexto** y cite las fuentes — esto evita alucinaciones.

### app.py — Código completo

```python
"""
MicroPréstamos MX — RAG Demo
Chatbot para análisis de datos no estructurados de una fintech mexicana.
Deploy: Hugging Face Spaces (Gradio SDK)
"""

import json
import os

import chromadb
import gradio as gr
from together import Together

# ─── 1. Cargar documentos en ChromaDB ───

def load_knowledge_base():
    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="microprestamos_mx",
        metadata={"hnsw:space": "cosine"},
    )

    if collection.count() > 0:
        return collection

    with open(os.path.join(os.path.dirname(__file__), "data", "documents.json")) as f:
        documents = json.load(f)

    texts = []
    metadatas = []
    ids = []

    for doc in documents:
        texts.append(doc["text"])
        metadatas.append(doc["metadata"])
        ids.append(doc["id"])

    collection.add(documents=texts, metadatas=metadatas, ids=ids)
    print(f"Loaded {len(texts)} documents into ChromaDB")
    return collection


# ─── 2. RAG: Retrieve + Generate ───

llm = Together()
collection = load_knowledge_base()

SYSTEM_PROMPT = """Eres un analista de Business Intelligence en MicroPréstamos MX, una fintech mexicana de micro-créditos.

Tu rol es responder preguntas del equipo directivo usando SOLO la información de los documentos proporcionados como contexto.

Reglas:
- Responde SIEMPRE en español
- Cita la fuente de cada dato: [chatbot], [quejas_email], [cobranza], [llamadas], [redes_sociales], [interno]
- Si cruzas información de múltiples canales, menciónalo explícitamente
- Si no tienes información suficiente en el contexto, dilo honestamente
- Sé conciso pero completo — piensa como analista, no como chatbot
- Cuando identifiques patrones o tendencias, destácalos
- Si detectas riesgos regulatorios (CONDUSEF, CNBV), márcalos como ⚠️"""


def query_rag(question: str, history: list) -> str:
    # Retrieve
    results = collection.query(query_texts=[question], n_results=5)
    context_parts = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        source = meta.get("fuente", "desconocido")
        fecha = meta.get("fecha", "")
        context_parts.append(f"[{source}] ({fecha}) {doc}")
    context = "\n\n---\n\n".join(context_parts)

    # Build messages
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({
        "role": "user",
        "content": (
            f"Contexto (documentos internos de MicroPréstamos MX):\n{context}\n\n"
            f"Pregunta del equipo: {question}"
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


# ─── 3. Gradio UI ───

demo = gr.ChatInterface(
    fn=query_rag,
    title="🏦 MicroPréstamos MX — Analista BI (RAG)",
    description=(
        "Soy un analista de BI que busca en **200+ documentos no estructurados** de MicroPréstamos MX: "
        "chats, emails, llamadas, redes sociales y documentos internos.\n\n"
        "Haz preguntas como si fueras parte del equipo directivo. "
        "Mis respuestas se basan en datos reales, no en conocimiento general."
    ),
    examples=[
        # Cross-channel intelligence
        "¿Cuáles son las quejas más frecuentes de clientes en mora?",
        "¿Qué dicen los clientes en redes sociales vs lo que reportan por email?",
        # Regulatory risk
        "¿Hay clientes que mencionan CONDUSEF o demanda?",
        "¿Estamos cumpliendo con la política de máximo 2 llamadas por día?",
        # Operational insights
        "¿Qué patrones hay en los clientes que piden reestructuración?",
        "Resume las quejas sobre cobros indebidos del último mes",
        # Strategic
        "¿Cuáles son los principales motivos de deserción de clientes?",
        "¿Qué fortalezas mencionan los clientes satisfechos?",
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()
```

---

## Paso 3: La interfaz Gradio

### Queries sugeridas y por qué son didácticas

Las queries de ejemplo están diseñadas con principios de **andragogía** (aprendizaje de adultos): parten de problemas reales que un profesional de BI encontraría en su trabajo.

#### Categoría 1: Inteligencia cross-channel

> "¿Cuáles son las quejas más frecuentes de clientes en mora?"

**Por qué es didáctica**: Demuestra que RAG cruza automáticamente chatbot + emails + llamadas + redes sociales para encontrar patrones. Con SQL necesitarías saber de antemano qué palabras buscar en cada tabla.

> "¿Qué dicen los clientes en redes sociales vs lo que reportan por email?"

**Por qué es didáctica**: Muestra que un mismo cliente puede expresar frustración diferente según el canal. El tono en Twitter es agresivo y público; el email es formal y detallado. RAG captura ambos registros.

#### Categoría 2: Riesgo regulatorio

> "¿Hay clientes que mencionan CONDUSEF o demanda?"

**Por qué es didáctica**: En fintech mexicana, detectar amenazas de CONDUSEF es crítico. RAG encuentra no solo menciones literales sino también frases como "voy a reportarlos" o "esto es ilegal" — algo que `LIKE '%CONDUSEF%'` nunca haría.

> "¿Estamos cumpliendo con la política de máximo 2 llamadas por día?"

**Por qué es didáctica**: Cruza documentos internos (la política) con notas de cobranza y quejas de clientes (la realidad). Muestra cómo RAG puede auditar el cumplimiento operativo.

#### Categoría 3: Insights operativos

> "¿Qué patrones hay en los clientes que piden reestructuración?"

**Por qué es didáctica**: Conecta con el trabajo real de un analista de BI — descubrir patrones para modelos predictivos. RAG extrae de transcripciones de llamadas las causas comunes: desempleo, enfermedad, sobreendeudamiento.

> "Resume las quejas sobre cobros indebidos del último mes"

**Por qué es didáctica**: Un gerente de operaciones haría exactamente esta pregunta. Demuestra el valor de tener un asistente que sintetiza decenas de quejas en un resumen ejecutivo.

#### Categoría 4: Preguntas estratégicas

> "¿Cuáles son los principales motivos de deserción de clientes?"

**Por qué es didáctica**: Pregunta de nivel C-suite. RAG encuentra señales de deserción dispersas en múltiples canales que ningún dashboard tradicional capturaría.

> "¿Qué fortalezas mencionan los clientes satisfechos?"

**Por qué es didáctica**: Balancea el sesgo negativo de las quejas. RAG filtra opiniones positivas para identificar ventajas competitivas — información valiosa para marketing y retención.

---

## Paso 4: Deploy en Hugging Face Spaces

### Estructura del repositorio en HF Spaces

```
microprestamos-rag/
├── app.py                    # Gradio app (entry point para HF Spaces)
├── generate_data.py          # Script de generación (no se ejecuta en Spaces)
├── requirements.txt          # Dependencias de Python
├── data/
│   ├── clientes.csv          # Datos estructurados (generados)
│   ├── prestamos.csv         # Datos estructurados (generados)
│   └── documents.json        # Documentos para ChromaDB (generados)
├── instructions.md           # Este archivo
└── README.md                 # Card de HF Spaces (metadata)
```

### requirements.txt

```
chromadb>=0.4.0
together>=1.0.0
gradio>=4.0.0
faker>=20.0.0
```

### README.md (HF Spaces card)

```yaml
---
title: MicroPréstamos MX — RAG Demo
emoji: 🏦
colorFrom: teal
colorTo: purple
sdk: gradio
sdk_version: "4.44.1"
app_file: app.py
pinned: false
license: mit
---
```

### Pasos para deploy

```bash
# 1. Crear el Space en Hugging Face
#    Ve a huggingface.co/new-space
#    - SDK: Gradio
#    - Visibility: Public

# 2. Clonar el repo del Space
git clone https://huggingface.co/spaces/TU_USUARIO/microprestamos-rag
cd microprestamos-rag

# 3. Copiar los archivos
#    Copia app.py, requirements.txt, data/ y generate_data.py

# 4. Configurar el secret de together.ai
#    En Settings del Space → Repository secrets:
#    TOGETHER_API_KEY = tu-api-key

# 5. Push
git add -A
git commit -m "Initial RAG demo"
git push
```

El Space se construye automáticamente. En ~2 minutos estará live.

### Variable de entorno

El único secret necesario es `TOGETHER_API_KEY`. Se configura en la UI de HF Spaces (Settings → Repository secrets), no en el código.

---

## Contexto pedagógico (andragogía)

### ¿Por qué este demo funciona para enseñar BI?

Este demo está diseñado siguiendo los principios de **andragogía** (aprendizaje de adultos profesionales) de Knowles:

| Principio | Cómo se aplica |
|-----------|---------------|
| **Orientación a problemas** | El escenario es un problema real de negocio: "tenemos datos dispersos en 6 canales y no podemos analizarlos con SQL" |
| **Relevancia inmediata** | Los estudiantes de BI ven exactamente el tipo de análisis que harían en su trabajo: quejas, riesgo regulatorio, tendencias de deserción |
| **Experiencia previa** | Se parte de lo que ya saben (SQL, dashboards, pandas) y se muestra dónde esas herramientas se quedan cortas |
| **Autonomía** | Las queries de ejemplo son punto de partida — los estudiantes pueden hacer sus propias preguntas y explorar |
| **Motivación interna** | El demo resuelve una frustración real: "¿cómo analizo datos de texto sin leer 200 documentos uno por uno?" |

### Qué NO hacer con este demo

- **No presentarlo como reemplazo de SQL** — es complemento. Los datos estructurados (CSV) siguen siendo mejor para métricas y agregaciones.
- **No enfocarse en la infraestructura** — los estudiantes son analistas de BI, no ingenieros de MLOps. Mantener ChromaDB in-memory simplifica todo.
- **No complicar el código** — el `app.py` tiene ~80 líneas. Eso es intencional. Si un estudiante no puede leer todo el código en 5 minutos, es demasiado complejo.

### Conexión con el workshop

Este demo extiende el lab del notebook (`labs/lab-chroma-rag.ipynb`) que tiene 25 documentos hardcodeados. La progresión es:

1. **Notebook** (lab): 25 docs, sin LLM, entienden embeddings y búsqueda semántica
2. **HF Space** (demo): 200+ docs, con LLM, ven el sistema completo en producción
3. **Reflexión**: ¿Cómo aplicarías esto en tu empresa/proyecto?

---

## Referencia rápida

### Ejecutar localmente

```bash
# Instalar dependencias
pip install chromadb together gradio faker

# Generar datos (una sola vez)
export TOGETHER_API_KEY="tu-key"
python generate_data.py

# Iniciar la app
python app.py
# → Abre http://localhost:7860
```

### Troubleshooting

| Problema | Solución |
|----------|---------|
| `TOGETHER_API_KEY not found` | `export TOGETHER_API_KEY="tu-key"` o configurar en HF Spaces secrets |
| `documents.json not found` | Ejecutar `python generate_data.py` primero |
| ChromaDB error de memoria | Reducir `n_results` de 5 a 3 en `collection.query()` |
| LLM responde en inglés | Verificar que el system prompt dice "Responde SIEMPRE en español" |
| JSON parse error en generación | El script reintenta el batch automáticamente |
