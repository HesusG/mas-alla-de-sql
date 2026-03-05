# Mas alla de SQL

**Busquedas inteligentes con Elasticsearch y ChromaDB**

Workshop de 2 horas para estudiantes de Inteligencia de Negocios (ITESM).

## Que aprenderas

- Por que SQL no es suficiente para busquedas de texto completo y semanticas
- Elasticsearch: busqueda full-text, relevancia y agregaciones
- ChromaDB: bases de datos vectoriales y busqueda semantica
- RAG (Retrieval-Augmented Generation): IA que responde desde tus datos

## Inicio rapido

### Presentacion

```bash
npm install
npm run dev
```

Abre http://localhost:3030

### Demo RAG (AI Career Coach)

```bash
cd demo
pip install -r requirements.txt
cp .env.example .env
# Agrega tu TOGETHER_API_KEY en .env
python career_coach_rag.py
```

## Estructura

| Carpeta | Contenido |
|---------|-----------|
| `slides.md` | Presentacion principal (~50 slides) |
| `snippets/` | Codigo para Kibana Dev Tools y Python |
| `demo/` | AI Career Coach con RAG (Gradio + ChromaDB + together.ai) |
| `labs/` | Laboratorios guiados para practica individual |
| `references/` | Referencias APA 7 completas |

## Requisitos

- **Elastic Cloud**: Trial gratuito en [elastic.co/cloud](https://www.elastic.co/cloud)
- **Python 3.10+**: Para el demo de RAG
- **together.ai API key**: Para el LLM en el demo
- **Node.js 18+**: Para la presentacion Slidev

## Labs

1. [Elasticsearch Basics](labs/lab-01-elasticsearch-basics.md) - Configuracion de Elastic Cloud (~30 min)
2. [Elasticsearch Search](labs/lab-02-elasticsearch-search.md) - Queries avanzados (~45 min)
3. [ChromaDB Embeddings](labs/lab-03-chroma-embeddings.md) - Busqueda semantica (~30 min)
4. [Mini RAG](labs/lab-04-mini-rag.md) - Construye una app RAG (~45 min)

## Referencias

Todas las referencias en formato APA 7 estan en [references/apa7.md](references/apa7.md).

## Licencia

MIT
