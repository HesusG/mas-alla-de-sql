---
theme: default
title: "Mas alla de SQL"
info: "Busquedas inteligentes con Elasticsearch y ChromaDB"
author: ""
keywords: elasticsearch,chromadb,vector-databases,rag,workshop
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
colorSchema: light
fonts:
  sans: Inter
  serif: Space Grotesk
  mono: JetBrains Mono
layout: neo-cover
---

<!-- Slide 1: Cover -->
<style>
.slidev-layout { --slidev-code-font-size: 0.85em; }
</style>

# Mas alla de SQL

## Busquedas inteligentes con Elasticsearch y ChromaDB

<div class="pixel-divider my-6" />

<div class="flex gap-4 justify-center items-center mt-4">
  <span class="neo-tag bg-coral text-white">ITESM</span>
  <span class="neo-tag bg-sky text-white">Inteligencia de Negocios</span>
  <span class="neo-tag bg-grape text-white">2 horas</span>
</div>

<div class="mt-4 text-sm opacity-70">
github.com/HesusG/mas-alla-de-sql
</div>

---
layout: center
class: bg-cream
---

<!-- Slide 2: Cold Open - La busqueda imposible -->

# La busqueda imposible

<div class="neo-card bg-white max-w-2xl mx-auto">

**Dataset**: 10,000 reseñas de clientes de una tienda online

**Reto**: *"Encuentra reseñas donde los clientes estan frustrados... sin usar la palabra 'frustrado'"*

</div>

<v-clicks>

<div class="mt-6 grid grid-cols-2 gap-4 max-w-2xl mx-auto">
<div class="neo-card bg-coral text-white p-4">

**SQL** `LIKE '%frustrado%'`
→ **0 resultados** ❌

</div>
<div class="neo-card bg-sky text-white p-4">

**Elasticsearch** `match: "frustrado"`
→ **147 resultados** ✅
con sinónimos, contexto y ranking

</div>
</div>

</v-clicks>

<v-click>

<div class="text-center mt-6 text-xl font-bold font-heading">
Al final de hoy, sabran como.
</div>

</v-click>

---
layout: neo-section
class: bg-grape
---

<!-- Slide 3: Section - El mundo real -->

<h1 class="text-white text-4xl">El mundo real no cabe en tablas</h1>

<div class="mt-6">
  <span class="neo-tag bg-banana text-ink">80%+ de los datos empresariales son no estructurados</span>
</div>

<p class="text-white/80 mt-4 text-lg">Emails, PDFs, reseñas, tickets de soporte, posts en redes sociales...</p>

<RefFootnote :sources="['McKinsey & Company. (2024). The state of AI in 2024.']" />

---
layout: neo-two-cols
---

<!-- Slide 4: SQL fue diseñado para otro mundo -->

::title::

# SQL fue diseñado para otro mundo

::left::

### Lo que SQL hace bien ✅

- Datos **estructurados** con esquema fijo
- Transacciones **ACID**
- JOINs entre tablas
- Consultas exactas (`WHERE x = 5`)
- 50+ años de madurez

::right::

### Lo que SQL NO puede ❌

- Busqueda **fuzzy** (con errores)
- **Ranking** por relevancia
- Entender **sinónimos**
- Buscar por **significado**
- Escalar a **millones** de docs/seg

```sql
-- El techo de SQL para texto:
SELECT * FROM docs
WHERE text LIKE '%frustrad%'
-- 0 resultados. Fin.
```

---

<!-- Slide 5: Universo de bases de datos -->

# Asi se ve el universo de bases de datos

<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="neo-card bg-banana p-3 text-center text-sm">
    <div class="text-2xl mb-1">🏛️</div>
    <strong>Relacional</strong><br/>Oracle, PostgreSQL, MySQL
  </div>
  <div class="neo-card bg-coral p-3 text-center text-sm text-white">
    <div class="text-2xl mb-1">📄</div>
    <strong>Documento</strong><br/>MongoDB, CouchDB
  </div>
  <div class="neo-card bg-sky p-3 text-center text-sm text-white">
    <div class="text-2xl mb-1">🔑</div>
    <strong>Clave-Valor</strong><br/>Redis, DynamoDB
  </div>
  <div class="neo-card bg-grape p-3 text-center text-sm text-white">
    <div class="text-2xl mb-1">🕸️</div>
    <strong>Grafo</strong><br/>Neo4j, Neptune
  </div>
  <div class="neo-card bg-coral p-3 text-center text-sm text-white">
    <div class="text-2xl mb-1">🔍</div>
    <strong>Busqueda</strong><br/>Elasticsearch, Solr
  </div>
  <div class="neo-card bg-sky p-3 text-center text-sm text-white">
    <div class="text-2xl mb-1">🧠</div>
    <strong>Vectorial</strong><br/>ChromaDB, Pinecone
  </div>
</div>

<div class="mt-4 text-sm text-center">
DB-Engines (2026): Elasticsearch es el motor de busqueda #1 del mundo
</div>

<RefFootnote :sources="['DB-Engines. (2026). DB-Engines ranking. https://db-engines.com/en/ranking']" />

---

<!-- Slide 6: Empresas que rompieron los limites -->

# Empresas que rompieron los limites de SQL

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Netflix</h3>
    <p class="text-sm">Multiples clusters de Elasticsearch para busqueda de contenido, monitoreo y analytics en tiempo real.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Amazon</h3>
    <p class="text-sm">Creo OpenSearch (fork de ES) para manejar busqueda en su marketplace con millones de productos.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Wikipedia</h3>
    <p class="text-sm">Elasticsearch potencia la busqueda en 300+ idiomas con millones de articulos.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Walmart</h3>
    <p class="text-sm">Analytics en tiempo real sobre inventario y ventas en 10,000+ tiendas.</p>
  </div>
</div>

<RefFootnote :sources="['Elastic. (2023). Customer stories. https://www.elastic.co/customers', 'Logz.io. (2023). 15 tech companies using ELK Stack.']" />

---
layout: center
class: bg-cream
---

<!-- Slide 7: Roadmap -->

# Hoy vamos de aqui... a aqui

<div class="flex items-center justify-center gap-2 mt-8">
  <div class="neo-card bg-banana p-4 text-center">
    <div class="text-3xl">🏛️</div>
    <strong>SQL</strong><br/>
    <span class="text-sm">Lo que sabes</span>
  </div>
  <div class="text-3xl">→</div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-3xl">🔍</div>
    <strong>Elasticsearch</strong><br/>
    <span class="text-sm">Busqueda full-text</span>
  </div>
  <div class="text-3xl">→</div>
  <div class="neo-card bg-sky text-white p-4 text-center">
    <div class="text-3xl">🧠</div>
    <strong>ChromaDB</strong><br/>
    <span class="text-sm">Busqueda semantica</span>
  </div>
  <div class="text-3xl">→</div>
  <div class="neo-card bg-grape text-white p-4 text-center">
    <div class="text-3xl">⚡</div>
    <strong>Tu superpoder</strong><br/>
    <span class="text-sm">RAG + IA</span>
  </div>
</div>

---
layout: neo-section
class: bg-coral
---

<!-- Slide 8: ES Section -->

<h1 class="text-white text-4xl">Google para tus datos de negocio</h1>

<p class="text-white/90 text-xl mt-4">Elasticsearch: open-source, distribuido, rapidisimo</p>

<div class="mt-6">
  <TimerBadge time="60 min" />
</div>

---
layout: neo-two-cols
---

<!-- Slide 9: SQL vs ES terminology -->

::title::

# Hablas SQL? Ya casi hablas Elasticsearch

::left::

### SQL

| Concepto | |
|---|---|
| **Database** | Contenedor |
| **Table** | Esquema fijo |
| **Row** | Un registro |
| **Column** | Un campo |
| **SQL Query** | `SELECT...WHERE` |

::right::

### Elasticsearch

| Concepto | |
|---|---|
| **Index** | Contenedor |
| **Mapping** | Esquema flexible |
| **Document** | JSON completo |
| **Field** | Un campo |
| **JSON Query** | `{"query":{...}}` |

---

<!-- Slide 10: Inverted Index -->

# El truco: el indice invertido

<div class="mt-4">

Imagina el **indice de un libro**, pero al reves:

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="neo-card bg-banana p-4">
    <h4>1. Documento</h4>
    <p class="text-sm">"La comida mexicana es deliciosa"</p>
  </div>
  <div class="neo-card bg-coral text-white p-4">
    <h4>2. Tokenizar</h4>
    <p class="text-sm">["comida", "mexicana", "deliciosa"]</p>
  </div>
  <div class="neo-card bg-sky text-white p-4">
    <h4>3. Indice Invertido</h4>
    <p class="text-sm">
      comida → doc1, doc3<br/>
      mexicana → doc1, doc5<br/>
      deliciosa → doc1, doc2
    </p>
  </div>
</div>

</v-clicks>

<v-click>

<div class="mt-4 text-center neo-card bg-cream p-3">
SQL escanea TODA la tabla. ES va directo al termino. <strong>Como buscar "Python" en un libro: vas al indice, no lees todo.</strong>
</div>

</v-click>

<RefFootnote :sources="['Gormley, C. & Tong, Z. (2015). Elasticsearch: The Definitive Guide. O\'Reilly Media.']" />

---

<!-- Slide 11: BM25 Scoring -->

# No solo encuentra, RANKEA

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">SQL WHERE</h3>
    <p>Devuelve <strong>0 o 1</strong></p>
    <p class="text-sm">¿Cumple la condicion? Si/No.</p>
    <p class="text-sm">Sin orden de relevancia.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-sky">ES BM25</h3>
    <p>Devuelve un <strong>_score</strong></p>
    <p class="text-sm">¿Que tan relevante es? 0.0 a ∞</p>
    <p class="text-sm">Considera: frecuencia del termino, rareza del termino, longitud del documento.</p>
  </div>
</div>

<v-click>

<div class="mt-4 neo-card bg-cream p-3 text-center">
<strong>BM25</strong> es la evolucion de TF-IDF. Es el algoritmo por defecto en ES desde la version 5.0 (2016).
<br/><span class="text-sm">Imagina Google sin ranking: solo una lista aleatoria de paginas que contienen tu palabra.</span>
</div>

</v-click>

<RefFootnote :sources="['Elastic NV. (2024). Similarity module. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html']" />

---

<!-- Slide 12: Architecture -->

# Un ejercito de servidores trabajando juntos

<div class="flex flex-col items-center mt-6 gap-4">
  <div class="neo-card bg-banana p-3 text-center font-bold text-lg">
    Cluster (tu despliegue)
  </div>
  <div class="text-2xl">↓</div>
  <div class="flex gap-4">
    <div class="neo-card bg-coral text-white p-3 text-center">Nodo 1</div>
    <div class="neo-card bg-coral text-white p-3 text-center">Nodo 2</div>
    <div class="neo-card bg-coral text-white p-3 text-center">Nodo 3</div>
  </div>
  <div class="text-2xl">↓</div>
  <div class="flex gap-2 flex-wrap justify-center">
    <div class="neo-tag bg-sky text-white">Shard P0</div>
    <div class="neo-tag bg-sky text-white">Shard P1</div>
    <div class="neo-tag bg-grape text-white">Replica R0</div>
    <div class="neo-tag bg-grape text-white">Replica R1</div>
  </div>
</div>

<div class="mt-4 text-center text-sm">
<strong>Shards</strong> = pedazos de tu indice distribuidos entre nodos.
<strong>Replicas</strong> = copias de seguridad en otros nodos.
</div>

---

<!-- Slide 13: Elastic Stack -->

# Elasticsearch, Kibana, Logstash, Beats

<div class="flex items-center justify-center gap-2 mt-8">
  <div class="neo-card bg-white p-3 text-center text-sm">
    <strong>Beats</strong><br/>Recolecta
  </div>
  <div class="text-xl">→</div>
  <div class="neo-card bg-white p-3 text-center text-sm">
    <strong>Logstash</strong><br/>Transforma
  </div>
  <div class="text-xl">→</div>
  <div class="neo-card bg-coral text-white p-3 text-center text-sm">
    <strong>Elasticsearch</strong><br/>Almacena + Busca
  </div>
  <div class="text-xl">→</div>
  <div class="neo-card bg-sky text-white p-3 text-center text-sm">
    <strong>Kibana</strong><br/>Visualiza
  </div>
</div>

<div class="mt-8 neo-card bg-banana p-3 text-center">
<strong>Hoy nos enfocamos en Elasticsearch + Kibana</strong>
<br/>Los otros son opcionales y los veran en los labs.
</div>

---
layout: neo-demo
---

<!-- Slide 14: Elastic Cloud Setup -->

::title::

<h2 class="text-banana">Elastic Cloud: tu laboratorio en 2 minutos</h2>

::default::

<div class="text-white/90">

### Pasos:

1. Ir a **elastic.co/cloud** → "Start free trial"
2. Crear cuenta (email + password)
3. **Create deployment** → Seleccionar region mas cercana
4. Esperar ~2 minutos → Copiar credenciales
5. Abrir **Kibana** desde el panel

<div class="mt-4 neo-card bg-white/10 p-3 text-sm">

**Tip**: Guarden el password de `elastic` que genera automaticamente. Lo necesitaran despues.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 15: Sample Data -->

::title::

<h2 class="text-banana">Datos listos para explorar</h2>

::default::

<div class="text-white/90">

### En Kibana:

1. **Home** → "Try sample data"
2. Clic en **"Add data"** en "Sample eCommerce orders"
3. Listo: **10,000+ ordenes** de una tienda online

<div class="mt-4">

**Incluye**: productos, categorias, precios, clientes, fechas, ubicaciones

</div>

<div class="mt-4 neo-card bg-white/10 p-3 text-sm">

**¿Por que eCommerce?** Porque es el escenario mas cercano a BI: ventas, clientes, productos, revenue.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 16: Dev Tools -->

::title::

<h2 class="text-banana">Dev Tools: tu nueva terminal favorita</h2>

::default::

<div class="text-white/90">

### Abrir Dev Tools:

Kibana → Menu lateral → **Management** → **Dev Tools**

- **Izquierda**: escribes tu request (como SQL Workbench)
- **Derecha**: ves la respuesta JSON
- **Ctrl+Enter**: ejecutar
- **Autocompletado** integrado

<div class="mt-4 neo-card bg-white/10 p-3">

```
GET _cluster/health
```
Si ves `"status": "green"` → todo funciona.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 17: eCommerce match query -->

::title::

<h2 class="text-banana">Misma pregunta, resultados rankeados</h2>

::default::

<div class="text-white/90">

```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "products.product_name": "shoes"
    }
  },
  "size": 3
}
```

<div class="mt-3">

**Observa**: cada resultado tiene un `_score` — eso es **BM25 en accion**.

**SQL equivalente**: `SELECT * FROM orders WHERE product_name LIKE '%shoes%'`
→ Sin score. Sin ranking. Sin magia.

</div>

</div>

<RefFootnote :sources="['Elastic NV. (2024). Elasticsearch reference (v8.x).']" />

---
layout: neo-two-cols
---

<!-- Slide 18: SQL vs ES query -->

::title::

# SELECT...WHERE vs match query

::left::

### SQL

```sql
SELECT *
FROM orders
WHERE product_name
  LIKE '%shoes%'
ORDER BY price DESC
LIMIT 5;
```

- Coincidencia **exacta**
- Sin ranking
- Full table scan

::right::

### Elasticsearch

```json
GET ecommerce/_search
{
  "query": {
    "match": {
      "product_name": "shoes"
    }
  },
  "size": 5
}
```

- Tokeniza y analiza
- **Rankea** por relevancia
- Indice invertido (rapido)

---
layout: neo-demo
---

<!-- Slide 19: Bool query -->

::title::

<h2 class="text-banana">Filtra como un pro</h2>

::default::

<div class="text-white/90">

```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "products.product_name": "shoes" } }
      ],
      "filter": [
        { "range": { "taxful_total_price": { "gte": 50, "lte": 200 } } }
      ],
      "should": [
        { "match": { "products.category": "Women's Clothing" } }
      ]
    }
  }
}
```

**must** = DEBE cumplirse | **filter** = filtro sin score | **should** = bonus

</div>

---
layout: neo-two-cols
---

<!-- Slide 20: GROUP BY vs aggregations -->

::title::

# GROUP BY vs aggregations

::left::

### SQL

```sql
SELECT category,
       COUNT(*) as total,
       AVG(price) as avg_price
FROM orders
GROUP BY category
ORDER BY total DESC;
```

::right::

### Elasticsearch

```json
GET ecommerce/_search
{
  "size": 0,
  "aggs": {
    "por_categoria": {
      "terms": {
        "field": "category.keyword"
      },
      "aggs": {
        "precio_promedio": {
          "avg": { "field": "price" }
        }
      }
    }
  }
}
```

---
layout: neo-demo
---

<!-- Slide 21: Aggregations live -->

::title::

<h2 class="text-banana">Dashboards en segundos</h2>

::default::

<div class="text-white/90">

```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "por_categoria": {
      "terms": { "field": "products.category.keyword", "size": 10 },
      "aggs": {
        "revenue_promedio": {
          "avg": { "field": "taxful_total_price" }
        }
      }
    }
  }
}
```

<div class="mt-3">

**Esto es lo que alimenta dashboards en Kibana.** Cada panel es una agregacion.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 22: Create peliculas index -->

::title::

<h2 class="text-banana">Crea tu propio indice: peliculas mexicanas</h2>

::default::

<div class="text-white/90">

```json
PUT peliculas
{
  "settings": {
    "analysis": {
      "analyzer": {
        "spanish_custom": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "spanish_stop", "spanish_stemmer"]
        }
      },
      "filter": {
        "spanish_stop": { "type": "stop", "stopwords": "_spanish_" },
        "spanish_stemmer": { "type": "stemmer", "language": "spanish" }
      }
    }
  },
  "mappings": { ... }
}
```

**Analizador en español**: quita stop words ("el", "la", "de") y aplica stemming ("corriendo" → "corr")

</div>

---
layout: neo-demo
---

<!-- Slide 23: Bulk insert -->

::title::

<h2 class="text-banana">10 peliculas en un segundo</h2>

::default::

<div class="text-white/90">

```json
POST peliculas/_bulk
{"index":{}}
{"titulo":"Roma","sinopsis":"Historia de una trabajadora domestica...","director":"Alfonso Cuarón","genero":"Drama","anio":2018,"rating":8.7,"pais":"Mexico"}
{"index":{}}
{"titulo":"Nosotros los nobles","sinopsis":"Un padre millonario finge la bancarrota...","genero":"Comedia","anio":2013,"rating":7.1,"pais":"Mexico"}
...
```

<div class="mt-3">

Ahora busquemos: **"comedia familiar"**

```json
GET peliculas/_search
{ "query": { "match": { "sinopsis": "comedia familiar" } } }
```

Observa los `_score` — ¿Cual pelicula es mas relevante?

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 24: Fuzzy search -->

::title::

<h2 class="text-banana">Escribiste mal? No importa</h2>

::default::

<div class="text-white/90">

```json
GET peliculas/_search
{
  "query": {
    "match": {
      "sinopsis": {
        "query": "peliula familar mexicana",
        "fuzziness": "AUTO"
      }
    }
  }
}
```

<div class="mt-3 grid grid-cols-2 gap-4">
  <div class="neo-card bg-coral/20 p-3">
    <strong>SQL:</strong> <code>LIKE '%peliula%'</code> → <strong>0 resultados</strong>
  </div>
  <div class="neo-card bg-sky/20 p-3">
    <strong>ES:</strong> "peliula" → "pelicula" → <strong>resultados encontrados!</strong>
  </div>
</div>

**fuzziness: AUTO** = tolerancia basada en longitud de palabra

</div>

---
layout: neo-demo
---

<!-- Slide 25: Highlighting -->

::title::

<h2 class="text-banana">Resalta lo que importa</h2>

::default::

<div class="text-white/90">

```json
GET peliculas/_search
{
  "query": {
    "multi_match": {
      "query": "viaje descubrimiento sociedad",
      "fields": ["titulo", "sinopsis"]
    }
  },
  "highlight": {
    "fields": {
      "titulo": {},
      "sinopsis": { "fragment_size": 150 }
    }
  }
}
```

<div class="mt-3">

En el resultado veras: `"...emprenden un <em>viaje</em> por carretera...descubriendo la <em>sociedad</em>..."`

Como Google resaltando tus terminos de busqueda.

</div>

</div>

---

<!-- Slide 26: When NOT to use ES -->

# Cuando NO usar Elasticsearch

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl mb-2">🚫</div>
    <strong>Transacciones</strong>
    <p class="text-sm mt-1">No es ACID. No hagas transferencias bancarias con ES.</p>
  </div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl mb-2">🚫</div>
    <strong>Base de datos primaria</strong>
    <p class="text-sm mt-1">Usalo como complemento, no como reemplazo de PostgreSQL/MySQL.</p>
  </div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl mb-2">🚫</div>
    <strong>JOINs complejos</strong>
    <p class="text-sm mt-1">ES es un motor de busqueda. Para relaciones complejas, SQL sigue siendo rey.</p>
  </div>
</div>

<div class="mt-6 neo-card bg-cream p-4 text-center">
<strong>Elasticsearch es un complemento, no un reemplazo de SQL.</strong>
<br/>La herramienta correcta para el trabajo correcto.
</div>

---

<!-- Slide 27: ES References -->

# Referencias — Seccion Elasticsearch

<div class="text-sm mt-4 space-y-3">

- Gormley, C., & Tong, Z. (2015). *Elasticsearch: The Definitive Guide*. O'Reilly Media. https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html

- Elastic NV. (2024). *Elasticsearch reference* (v8.x). https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

- Elastic NV. (2024). *Similarity module*. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html

- DB-Engines. (2026). *DB-Engines ranking*. https://db-engines.com/en/ranking

- Elastic. (2023). *Customer stories*. https://www.elastic.co/customers

- Logz.io. (2023). *15 tech companies that chose the ELK Stack*. https://logz.io/blog/15-tech-companies-chose-elk-stack/

</div>

---
layout: center
class: bg-cream
---

<!-- Slide 28: Pause -->

# Pausa: 3 minutos

<div class="text-6xl mt-4">☕</div>

<div class="mt-4 text-xl">
Tomen agua. Lo que sigue les va a volar la cabeza.
</div>

---
layout: neo-section
class: bg-sky
---

<!-- Slide 29: ChromaDB Section -->

<h1 class="text-white text-4xl">Y si tu base de datos entendiera significado?</h1>

<p class="text-white/90 text-xl mt-4">ChromaDB: busqueda semantica con vectores</p>

<div class="mt-6">
  <TimerBadge time="30 min" />
</div>

---

<!-- Slide 30: The problem ES doesn't solve -->

# El problema que ni Elasticsearch resuelve

<div class="mt-6 space-y-4">

<v-clicks>

<div class="neo-card bg-white p-4">
<strong>Busqueda:</strong> "peliculas que me hagan sentir nostalgico"
<br/><span class="text-coral font-bold">SQL LIKE</span>: ❌ la palabra "nostalgico" no aparece en ninguna sinopsis
</div>

<div class="neo-card bg-white p-4">
<strong>Busqueda:</strong> "peliculas que me hagan sentir nostalgico"
<br/><span class="text-sky font-bold">Elasticsearch</span>: ❌ puede buscar "nostalgia" (stemming) pero no entiende que "Roma" evoca nostalgia sin decirlo
</div>

<div class="neo-card bg-grape text-white p-4">
<strong>Necesitamos algo que entienda SIGNIFICADO</strong>, no solo palabras.
<br/>Necesitamos... <strong>embeddings</strong>.
</div>

</v-clicks>

</div>

---

<!-- Slide 31: Physical analogy -->

# Imagina un cuarto lleno de peliculas

<div class="mt-4">

**Ejercicio mental**: Te doy 100 peliculas en tarjetas. ¿Como las organizarias en una mesa para que peliculas similares queden cerca?

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="neo-card bg-banana p-3 text-center text-sm">
    <strong>Esquina 1</strong><br/>Comedias familiares
  </div>
  <div class="neo-card bg-coral text-white p-3 text-center text-sm">
    <strong>Esquina 2</strong><br/>Thrillers oscuros
  </div>
  <div class="neo-card bg-sky text-white p-3 text-center text-sm">
    <strong>Esquina 3</strong><br/>Dramas sociales
  </div>
</div>

<div class="mt-4 neo-card bg-cream p-3 text-center">
<strong>Eso es EXACTAMENTE lo que hacen los embeddings.</strong>
<br/>Convierten texto en coordenadas. Textos similares → coordenadas cercanas.
</div>

</v-clicks>

---

<!-- Slide 32: Embeddings -->

# Asi leen las maquinas entre lineas

<div class="grid grid-cols-2 gap-6 mt-6">
  <div>
    <h3>Texto → Vector</h3>
    <div class="text-sm space-y-2 mt-2">
      <div class="neo-card bg-white p-2">"perro" → [0.2, 0.8, 0.1, ...]</div>
      <div class="neo-card bg-white p-2">"cachorro" → [0.21, 0.79, 0.12, ...]</div>
      <div class="neo-card bg-white p-2">"automovil" → [0.9, 0.1, 0.7, ...]</div>
    </div>
    <p class="text-sm mt-2">"perro" y "cachorro" tienen vectores <strong>cercanos</strong>.<br/>"automovil" esta <strong>lejos</strong>.</p>
  </div>
  <div class="flex items-center justify-center">
    <div class="neo-card bg-grape text-white p-6 text-center">
      <div class="text-lg font-bold mb-2">Espacio vectorial</div>
      <div class="text-sm">
        🐕 perro ← cerca → cachorro 🐶<br/><br/>
        🚗 automovil ← lejos → perro 🐕
      </div>
    </div>
  </div>
</div>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 33: Cosine similarity -->

# Distancia = Similitud

<div class="mt-6">

<div class="neo-card bg-banana p-4 text-center text-lg">
La famosa analogia: <strong>"rey" - "hombre" + "mujer" ≈ "reina"</strong>
</div>

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="neo-card bg-white p-4">
    <h3>Similitud coseno</h3>
    <p class="text-sm">Mide el angulo entre dos vectores. Angulo pequeño = similares. No necesitan saber la matematica — solo la intuicion.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>En la practica</h3>
    <p class="text-sm">ChromaDB calcula esto automaticamente. Tu solo dices: "busca documentos similares a esta pregunta."</p>
  </div>
</div>

</div>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 34: Vector DBs -->

# Bases de datos que entienden significado

<div class="mt-4">

**¿Que almacena una base de datos vectorial?**

</div>

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="neo-card bg-grape text-white p-4 text-center">
    <div class="text-2xl mb-2">📐</div>
    <strong>Vectores</strong>
    <p class="text-sm">Representaciones numericas del significado</p>
  </div>
  <div class="neo-card bg-sky text-white p-4 text-center">
    <div class="text-2xl mb-2">🏷️</div>
    <strong>Metadata</strong>
    <p class="text-sm">Filtros: categoria, fecha, autor</p>
  </div>
  <div class="neo-card bg-banana p-4 text-center">
    <div class="text-2xl mb-2">📄</div>
    <strong>Documentos</strong>
    <p class="text-sm">El texto original para devolver</p>
  </div>
</div>

<div class="mt-4 text-sm">

**El mercado**: ChromaDB, Pinecone, Weaviate, Qdrant, Milvus, pgvector (PostgreSQL)

</div>

---

<!-- Slide 35: ChromaDB intro -->

# ChromaDB: la mas simple del mercado

<div class="grid grid-cols-4 gap-3 mt-6">
  <div class="neo-card bg-white p-3 text-center">
    <div class="text-2xl font-bold text-sky">Open Source</div>
    <p class="text-sm">Apache 2.0</p>
  </div>
  <div class="neo-card bg-white p-3 text-center">
    <div class="text-2xl font-bold text-sky">Python-first</div>
    <p class="text-sm">pip install chromadb</p>
  </div>
  <div class="neo-card bg-white p-3 text-center">
    <div class="text-2xl font-bold text-sky">Auto-embed</div>
    <p class="text-sm">Genera vectores por ti</p>
  </div>
  <div class="neo-card bg-white p-3 text-center">
    <div class="text-2xl font-bold text-sky">RAG-ready</div>
    <p class="text-sm">Funcional en &lt;30 lineas</p>
  </div>
</div>

<div class="mt-6 neo-card bg-cream p-4 text-center">
<strong>¿Por que ChromaDB?</strong> Porque su API es tan simple que pueden tener un RAG funcional en menos de 30 lineas de Python.
</div>

<RefFootnote :sources="['Chroma. (2024). Chroma documentation. https://docs.trychroma.com/']" />

---
layout: neo-demo
---

<!-- Slide 36: ChromaDB in 5 lines -->

::title::

<h2 class="text-banana">ChromaDB en 5 lineas de Python</h2>

::default::

<div class="text-white/90">

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("demo")

collection.add(
    documents=["Me encanta la comida mexicana",
               "Python es ideal para datos",
               "Los tacos son deliciosos"],
    ids=["doc1", "doc2", "doc3"]
)

results = collection.query(
    query_texts=["gastronomía latinoamericana"],
    n_results=2
)
# Encuentra "comida mexicana" y "tacos" — sin mencionar esas palabras!
```

</div>

---

<!-- Slide 37: Predict then reveal -->

# Predice: que resultados devolvera esto?

<div class="mt-4 text-sm">Coleccion con 5 documentos sobre: comida mexicana, IA, Python, burritos, machine learning</div>

<v-clicks>

<div class="mt-4 space-y-3">
  <div class="neo-card bg-white p-3">
    <strong>Query 1:</strong> "tacos" → <span class="text-coral font-bold">Facil: "comida mexicana" y "burritos"</span> (palabras relacionadas)
  </div>
  <div class="neo-card bg-white p-3">
    <strong>Query 2:</strong> "estoy contento" → <span class="text-sky font-bold">Hmm: ¿encuentra "me encanta"?</span> (sinonimos emocionales)
  </div>
  <div class="neo-card bg-banana p-3">
    <strong>Query 3:</strong> "transporte economico" → <span class="text-grape font-bold">Sorpresa: ¿que encuentra?</span> (conexion conceptual, no palabras)
  </div>
</div>

<div class="mt-4 neo-card bg-cream p-3 text-center">
<strong>Los embeddings entienden CONCEPTOS, no solo palabras.</strong>
<br/>Esto es busqueda semantica.
</div>

</v-clicks>

---

<!-- Slide 38: RAG diagram -->

# Ensenando a la IA con TUS datos

<div class="flex items-center justify-center gap-2 mt-8">
  <div class="neo-card bg-banana p-4 text-center">
    <div class="text-2xl">❓</div>
    <strong>Pregunta</strong>
    <p class="text-xs">del usuario</p>
  </div>
  <div class="text-2xl">→</div>
  <div class="neo-card bg-sky text-white p-4 text-center">
    <div class="text-2xl">🔍</div>
    <strong>ChromaDB</strong>
    <p class="text-xs">busca contexto relevante</p>
  </div>
  <div class="text-2xl">→</div>
  <div class="neo-card bg-grape text-white p-4 text-center">
    <div class="text-2xl">🧠</div>
    <strong>LLM</strong>
    <p class="text-xs">genera respuesta con contexto</p>
  </div>
  <div class="text-2xl">→</div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl">✅</div>
    <strong>Respuesta</strong>
    <p class="text-xs">fundamentada en datos</p>
  </div>
</div>

<div class="mt-6 neo-card bg-cream p-4 text-center">
<strong>RAG = Retrieval-Augmented Generation</strong>
<br/>La IA no hallucina porque responde desde TUS datos, no desde su entrenamiento.
</div>

<RefFootnote :sources="['Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS, 33, 9459-9474.']" />

---
layout: neo-demo
---

<!-- Slide 39: Career Coach RAG Demo -->

::title::

<h2 class="text-banana">DEMO: Tu coach de carrera con IA</h2>

::default::

<div class="text-white/90">

### AI Career Coach para estudiantes de BI

- **100+ ofertas de trabajo** reales: Data Analyst, BI Developer, Data Scientist
- Empresas: Deloitte, Amazon, Mercado Libre, FEMSA, Banorte...
- Stack: **ChromaDB** (retrieval) + **together.ai** (LLM) + **Gradio** (UI)

### Preguntas que pueden hacer:

- *"¿Que habilidades necesito para Data Analyst en consulting?"*
- *"¿Que empresas en Monterrey buscan egresados de BI?"*
- *"Se Python, SQL y Tableau — ¿para que puestos califico?"*
- *"¿Cual es la diferencia entre lo que pide Amazon y Deloitte?"*

<div class="mt-2 neo-card bg-white/10 p-2 text-sm">

Cada respuesta muestra las **fuentes**: las ofertas de trabajo reales en las que se basa.

</div>

</div>

---

<!-- Slide 40: The stack behind the magic -->

# El stack detras de la magia

<div class="grid grid-cols-3 gap-4 mt-8">
  <div class="neo-card bg-sky text-white p-4 text-center">
    <div class="text-3xl mb-2">🔍</div>
    <strong>ChromaDB</strong>
    <p class="text-sm mt-2">Almacena las ofertas de trabajo como vectores. Busca las mas relevantes a tu pregunta.</p>
  </div>
  <div class="neo-card bg-grape text-white p-4 text-center">
    <div class="text-3xl mb-2">🧠</div>
    <strong>together.ai</strong>
    <p class="text-sm mt-2">Llama 3.3 70B genera respuestas naturales usando el contexto recuperado.</p>
  </div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-3xl mb-2">💬</div>
    <strong>Gradio</strong>
    <p class="text-sm mt-2">Interfaz de chat en 3 lineas de codigo. Se abre en el navegador.</p>
  </div>
</div>

<div class="mt-6 text-center text-sm">
Esto es lo que hacen internamente las grandes consultoras para busqueda interna de conocimiento.
</div>

---

<!-- Slide 41: ChromaDB References -->

# Referencias — Seccion ChromaDB y RAG

<div class="text-sm mt-4 space-y-3">

- Chroma. (2024). *Chroma documentation*. https://docs.trychroma.com/

- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS, 33*, 9459-9474.

- Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. *arXiv:1301.3781*.

- Pan, J. W., et al. (2024). A survey on vector database. *arXiv:2310.11703*.

</div>

---
layout: neo-section
class: bg-ink
---

<!-- Slide 42: Section 4 -->

<h1 class="text-banana text-4xl">La herramienta correcta para la pregunta correcta</h1>

<div class="mt-6">
  <TimerBadge time="15 min" />
</div>

---

<!-- Slide 43: Comparison table -->

# SQL vs Elasticsearch vs ChromaDB

<ComparisonTable
  :headers="['', 'SQL', 'Elasticsearch', 'ChromaDB']"
  :rows="[
    ['Modelo de datos', 'Tablas + filas', 'Documentos JSON', 'Vectores + docs'],
    ['Tipo de query', 'Exacto (WHERE)', 'Full-text (match)', 'Semantico (similitud)'],
    ['Ranking', 'No', 'BM25 score', 'Distancia coseno'],
    ['Mejor para', 'Transacciones, JOINs', 'Busqueda de texto', 'Significado, RAG'],
    ['Fuzzy/Typos', 'No', 'Si (fuzziness)', 'Implicito'],
    ['Curva aprendizaje', 'Media', 'Media-Alta', 'Baja'],
  ]"
/>

---
layout: neo-two-cols
---

<!-- Slide 44: Decision tree -->

::title::

# El arbol de decision

::left::

### ¿Que herramienta uso?

```
¿Datos estructurados?
  → SI → ¿Necesitas JOINs/ACID?
          → SI → SQL ✅
          → NO → ¿Necesitas busqueda?
                  → Elasticsearch
  → NO → ¿Busqueda por texto?
          → SI → Elasticsearch ✅
          → NO → ¿Busqueda por significado?
                  → SI → Vector DB ✅
```

::right::

### En la practica...

Se usan **juntos**:

- **SQL** para la operacion del negocio
- **ES** para busqueda y analytics
- **Vector DB** para IA y RAG

<div class="neo-card bg-banana p-3 mt-4 text-sm">
<strong>Ejemplo real</strong>: Una tienda online usa PostgreSQL para pedidos, Elasticsearch para busqueda de productos, y ChromaDB para recomendaciones con IA.
</div>

---

<!-- Slide 45: Fronteras se difuminan -->

# Las fronteras se difuminan

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="neo-card bg-white p-4 text-center">
    <h3 class="text-coral">SQL Server 2025</h3>
    <p class="text-sm">Microsoft agrego busqueda vectorial nativa a SQL Server.</p>
  </div>
  <div class="neo-card bg-white p-4 text-center">
    <h3 class="text-sky">Elasticsearch 8.x</h3>
    <p class="text-sm">Agrego vector search (kNN) ademas de full-text.</p>
  </div>
  <div class="neo-card bg-white p-4 text-center">
    <h3 class="text-grape">pgvector</h3>
    <p class="text-sm">Extension de PostgreSQL para vectores. SQL + semantica.</p>
  </div>
</div>

<div class="mt-6 neo-card bg-cream p-4 text-center">
<strong>El futuro es hibrido.</strong> Las herramientas convergen. Saber los fundamentos de cada una es tu ventaja.
</div>

<RefFootnote :sources="['Gartner. (2024). Hype Cycle for Data Management.']" />

---

<!-- Slide 46: Your new superpower -->

# Tu nuevo superpoder empieza ahora

<div class="mt-6">

<div class="neo-card bg-banana p-6">

### Ofertas de empleo reales que piden estas habilidades:

- *"Data Engineer — **Elasticsearch**, Kafka, Python"* — Amazon
- *"BI Developer — SQL, **vector databases**, LLM integration"* — Deloitte
- *"ML Engineer — **RAG pipelines**, ChromaDB/Pinecone"* — Mercado Libre

</div>

<div class="mt-4 text-center text-lg">
<strong>Ahora saben que es esto. La mayoria de profesionales con 5 años de experiencia no.</strong>
</div>

</div>

---

<!-- Slide 47: Keep practicing -->

# Sigue practicando

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="neo-card bg-white p-4">
    <h3>Labs en este repo</h3>
    <ul class="text-sm mt-2">
      <li>Lab 1: ES Basics (~30 min)</li>
      <li>Lab 2: ES Search avanzado (~45 min)</li>
      <li>Lab 3: ChromaDB embeddings (~30 min)</li>
      <li>Lab 4: Mini RAG app (~45 min)</li>
    </ul>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>Recursos</h3>
    <ul class="text-sm mt-2">
      <li>Elastic Cloud: 14 dias gratis</li>
      <li>ChromaDB: docs.trychroma.com</li>
      <li>together.ai: $5 USD gratis</li>
      <li>Kaggle: datasets para practicar</li>
    </ul>
  </div>
</div>

---

<!-- Slide 48: References -->

# Referencias completas

<div class="text-xs mt-4 space-y-2">

- Chroma. (2024). *Chroma documentation*. https://docs.trychroma.com/
- DB-Engines. (2026). *DB-Engines ranking*. https://db-engines.com/en/ranking
- Elastic NV. (2024). *Elasticsearch reference* (v8.x). https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
- Elastic NV. (2024). *Similarity module*. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html
- Gartner. (2024). *Hype Cycle for Data Management*. Gartner, Inc.
- Gormley, C., & Tong, Z. (2015). *Elasticsearch: The Definitive Guide*. O'Reilly Media.
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS, 33*, 9459-9474.
- McKinsey & Company. (2024). *The state of AI in 2024*. McKinsey Global Institute.
- Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. *arXiv:1301.3781*.
- Pan, J. W., et al. (2024). A survey on vector database. *arXiv:2310.11703*.

</div>

<div class="mt-2 text-center text-sm">

Lista completa con hyperlinks: <code>references/apa7.md</code> en el repositorio

</div>

---
layout: neo-cover
---

<!-- Slide 49: Closing -->

# Gracias!

<div class="pixel-divider my-4" />

<div class="text-lg mb-4">#MasAlladeSQL</div>

<div class="text-sm">
Comparte lo que construiste hoy
</div>

<div class="flex gap-4 justify-center items-center mt-6">
  <span class="neo-tag bg-coral text-white">github.com/HesusG/mas-alla-de-sql</span>
</div>
