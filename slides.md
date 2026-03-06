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

<!-- Slide 2: About me -->

# Sobre mi

<div class="grid grid-cols-[1fr_2fr] gap-8 mt-8 items-center">
  <div class="neo-card bg-banana p-6 text-center">
    <div class="text-6xl mb-4">👨‍💻</div>
    <div class="text-lg font-bold">[Tu nombre]</div>
    <div class="text-sm mt-1">[Tu rol / titulo]</div>
  </div>
  <div class="space-y-3">
    <div class="neo-card bg-white p-3 text-sm">📍 [Ciudad, organizacion]</div>
    <div class="neo-card bg-white p-3 text-sm">💼 [Experiencia relevante]</div>
    <div class="neo-card bg-white p-3 text-sm">🔧 [Stack / tecnologias]</div>
    <div class="neo-card bg-white p-3 text-sm">🎯 [Por que este tema te apasiona]</div>
  </div>
</div>

---

<!-- Slide 3: Roadmap - moved to beginning -->

# Hoy vamos a recorrer este camino

<div class="flex items-center justify-center gap-3 mt-10">
  <div class="neo-card bg-banana p-4 text-center min-w-28">
    <div class="text-3xl mb-1">🏛️</div>
    <strong>SQL</strong><br/>
    <span class="text-xs">Lo que conoces</span>
  </div>
  <div class="text-3xl font-bold text-[#2D3436]">→</div>
  <div class="neo-card bg-coral text-white p-4 text-center min-w-28">
    <div class="text-3xl mb-1">🤔</div>
    <strong>El problema</strong><br/>
    <span class="text-xs">Donde SQL no llega</span>
  </div>
  <div class="text-3xl font-bold text-[#2D3436]">→</div>
  <div class="neo-card bg-sky text-white p-4 text-center min-w-28">
    <div class="text-3xl mb-1">🔍</div>
    <strong>Elasticsearch</strong><br/>
    <span class="text-xs">Busqueda de texto</span>
  </div>
  <div class="text-3xl font-bold text-[#2D3436]">→</div>
  <div class="neo-card bg-grape text-white p-4 text-center min-w-28">
    <div class="text-3xl mb-1">🧠</div>
    <strong>ChromaDB</strong><br/>
    <span class="text-xs">Busqueda por significado</span>
  </div>
</div>

<div class="mt-8 text-center text-lg">
Al terminar, van a tener un <strong>superpoder</strong> que la mayoria de profesionales con experiencia no tienen.
</div>

---

<!-- Slide 4: Cold Open - Setup -->

# Empecemos con un reto

<div class="mt-8">

Imaginen que trabajan en el area de **servicio al cliente** de una tienda online.

Su jefe les dice:

</div>

<v-click>

<div class="neo-card bg-banana p-6 mt-6 text-center text-xl">
<em>"Necesito un reporte de todas las reseñas donde los clientes estan <strong>frustrados</strong>.<br/> Tenemos 10,000 reseñas en la base de datos. Para ayer."</em>
</div>

</v-click>

<v-click>

<div class="mt-6 text-center text-lg">
¿Como lo harian con las herramientas que conocen?
</div>

</v-click>

---

<!-- Slide 5: The SQL attempt -->

# El primer instinto: SQL

<div class="mt-6">

Lo mas logico: abrir tu herramienta de SQL y escribir algo como...

</div>

<v-click>

```sql
SELECT * FROM resenas WHERE texto LIKE '%frustrado%';
```

</v-click>

<v-click>

<div class="neo-card bg-coral text-white p-4 mt-4">
<strong>Resultado: 23 reseñas.</strong> Pero... ¿de 10,000? Algo no cuadra.
</div>

</v-click>

<v-click>

<div class="mt-4">

¿Que pasa con los clientes que escribieron...?

- *"Pesimo servicio, nunca vuelvo"* — no dice "frustrado"
- *"Me siento decepcionado con la calidad"* — tampoco
- *"Llevo 3 semanas esperando mi pedido"* — implica frustracion, pero no usa la palabra

</div>

</v-click>

---

<!-- Slide 6: Trying harder with SQL -->

# Intentemos mas duro con SQL

```sql
SELECT * FROM resenas
WHERE texto LIKE '%frustrado%'
   OR texto LIKE '%decepcionado%'
   OR texto LIKE '%molesto%'
   OR texto LIKE '%enojado%'
   OR texto LIKE '%terrible%'
   OR texto LIKE '%pesimo%'
   OR texto LIKE '%horrible%';
```

<v-clicks>

<div class="mt-4 space-y-3">
  <div class="neo-card bg-white p-3">❌ Hay que <strong>adivinar</strong> todas las palabras posibles — ¿cuantas formas hay de expresar frustracion?</div>
  <div class="neo-card bg-white p-3">❌ <strong>No entiende contexto</strong>: "no estoy molesto" apareceria como resultado positivo</div>
  <div class="neo-card bg-white p-3">❌ Es <strong>lento</strong>: cada <code>LIKE</code> con <code>%</code> escanea toda la tabla, fila por fila</div>
  <div class="neo-card bg-white p-3">❌ <strong>Sin ranking</strong>: no sabes cual resena es "mas frustrada" que otra</div>
</div>

</v-clicks>

---

<!-- Slide 7: The reveal -->

# Ahora miren esto

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="space-y-4">
    <h3 class="text-coral">SQL</h3>
    <div class="neo-card bg-white p-4">

```sql
SELECT * FROM resenas
WHERE texto LIKE '%frustrado%';
```

<div class="mt-2 text-coral font-bold">→ 23 resultados. Sin ranking.</div>
    </div>
  </div>
  <div class="space-y-4">
    <h3 class="text-sky">Elasticsearch</h3>
    <div class="neo-card bg-white p-4">

```json
GET resenas/_search
{ "query": { "match": {
    "texto": "frustrado"
}}}
```

<div class="mt-2 text-sky font-bold">→ 147 resultados. Rankeados por relevancia.</div>
    </div>
  </div>
</div>

<v-click>

<div class="neo-card bg-banana p-4 mt-6 text-center text-lg">
Al final de esta sesion, van a saber como hacer esto. Y mucho mas.
</div>

</v-click>

---
layout: neo-section
class: bg-grape
---

<!-- Slide 8: Section - Unstructured data -->

<h1 class="text-white text-4xl">El mundo real no cabe en tablas</h1>

<p class="text-white/80 mt-4 text-xl">Entendiendo por que SQL no es suficiente</p>

---

<!-- Slide 9: What is unstructured data -->

# ¿Que son los datos no estructurados?

<div class="grid grid-cols-2 gap-6 mt-6">
  <div>
    <h3 class="mb-3">Datos estructurados (SQL)</h3>
    <div class="neo-card bg-white p-3 text-sm">
      <table class="w-full text-xs">
        <tr class="border-b"><th class="text-left p-1">id</th><th class="text-left p-1">nombre</th><th class="text-left p-1">precio</th><th class="text-left p-1">stock</th></tr>
        <tr class="border-b"><td class="p-1">1</td><td class="p-1">Laptop</td><td class="p-1">15000</td><td class="p-1">42</td></tr>
        <tr><td class="p-1">2</td><td class="p-1">Mouse</td><td class="p-1">350</td><td class="p-1">200</td></tr>
      </table>
      <p class="mt-2">Filas, columnas, tipos definidos. Perfecto para SQL.</p>
    </div>
  </div>
  <div>
    <h3 class="mb-3">Datos no estructurados</h3>
    <div class="neo-card bg-coral/10 p-3 text-sm space-y-2">
      <div>📧 <em>"Hola, llevo 2 semanas sin recibir mi pedido..."</em></div>
      <div>📄 Contrato de 45 paginas en PDF</div>
      <div>💬 Conversaciones de chat con soporte</div>
      <div>📱 Posts de redes sociales</div>
      <div>📝 Notas de reuniones, minutas</div>
    </div>
  </div>
</div>

<v-click>

<div class="neo-card bg-banana p-4 mt-4 text-center">
<strong>Mas del 80% de los datos en las empresas son no estructurados.</strong>
No caben en una tabla de SQL.
</div>

</v-click>

<RefFootnote :sources="['McKinsey & Company. (2024). The state of AI in 2024. McKinsey Global Institute.']" />

---

<!-- Slide 10: What SQL does well -->

# SQL es poderoso — para lo que fue diseñado

<div class="mt-6">

SQL fue creado en los años 70 para manejar datos **estructurados** con reglas claras:

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="neo-card bg-white p-4">

### Transacciones ACID

Garantiza que tus datos sean **consistentes**. Si transfieres $1,000 de una cuenta a otra, SQL asegura que no se pierda dinero en el camino.

<div class="text-xs mt-2 text-gray-500">

ACID = Atomicidad, Consistencia, Aislamiento, Durabilidad. Concepto fundamental de bases de datos relacionales.

</div>

</div>

<div class="neo-card bg-white p-4">

### JOINs y relaciones

Conecta tablas entre si: clientes con pedidos, pedidos con productos. Modelo relacional, inventado por Edgar F. Codd (1970).

</div>

</div>

<RefFootnote :sources="['Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), 377-387.']" />

---

<!-- Slide 11: What SQL can't do - Text -->

# Pero SQL no fue diseñado para buscar texto

<div class="mt-6">

Intenta responder estas preguntas con SQL:

</div>

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="neo-card bg-white p-3">
    <strong>1.</strong> "Encuentra reseñas de clientes <strong>insatisfechos</strong>" → ¿Con que palabra buscas? Hay cientos de formas de expresar insatisfaccion.
  </div>
  <div class="neo-card bg-white p-3">
    <strong>2.</strong> "Busca productos similares a <strong>tenis para correr</strong>" → <code>LIKE '%tenis%'</code> no encuentra "zapatillas deportivas" ni "running shoes".
  </div>
  <div class="neo-card bg-white p-3">
    <strong>3.</strong> "¿Cuales son las quejas <strong>mas urgentes</strong>?" → SQL no puede rankear por "urgencia" — devuelve todo o nada.
  </div>
  <div class="neo-card bg-coral/10 p-3">
    <strong>4.</strong> "El cliente escribio <strong>'teniz'</strong> en vez de 'tenis'" → <code>LIKE '%teniz%'</code> no encuentra nada. Un simple error tipografico y perdiste resultados.
  </div>
</div>

</v-clicks>

---

<!-- Slide 12: What SQL can't do - Scale & Speed -->

# SQL tampoco fue diseñado para esto

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Velocidad en texto</h3>
    <p class="text-sm mt-2"><code>LIKE '%palabra%'</code> escanea <strong>cada fila</strong> de la tabla, caracter por caracter. Con 10 millones de documentos, esto puede tardar minutos.</p>
    <p class="text-sm mt-2">¿Se imaginan que Google tardara minutos en cada busqueda?</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Relevancia</h3>
    <p class="text-sm mt-2">SQL devuelve resultados en modo <strong>binario</strong>: cumple la condicion o no. No hay concepto de "este resultado es mejor que aquel".</p>
    <p class="text-sm mt-2">Cuando buscas en Google, los primeros resultados son los mas relevantes. SQL no puede hacer eso.</p>
  </div>
</div>

<v-click>

<div class="neo-card bg-cream p-4 mt-6 text-center">
Esto no es un defecto de SQL — <strong>fue diseñado para otro proposito</strong>. Es como usar un martillo para poner un tornillo: funciona, pero hay herramientas mejores.
</div>

</v-click>

---

<!-- Slide 13: The frustration expanded -->

# El costo real de estas limitaciones

<div class="mt-6">

Volvamos a nuestro reto de las reseñas. Con SQL encontramos 23 resultados. ¿Que paso con los otros 124?

</div>

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="neo-card bg-white p-3 text-sm">
    <strong>"El producto llego roto y nadie me ayudo"</strong> — cliente claramente frustrado, pero no usa esa palabra
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <strong>"3 llamadas al soporte y sigo sin solucion"</strong> — frustracion implicita en el contexto
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <strong>"Esperaba mucho mas por este precio"</strong> — decepcion, un sinonimo de frustracion
  </div>
  <div class="neo-card bg-coral/10 p-3 text-sm">
    <strong>"Mi experiencia fue desastrosa desde el primer dia"</strong> — intensidad alta, pero SQL la ignora por completo
  </div>
</div>

<div class="neo-card bg-banana p-4 mt-4 text-center">
<strong>Cada resena que SQL no encuentra es un cliente que podrias perder.</strong>
En BI, los datos que no ves son los mas peligrosos.
</div>

</v-clicks>

---

<!-- Slide 14: Modern data needs -->

# Las empresas de hoy necesitan mas

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="neo-card bg-white p-4">
    <h3>Busqueda inteligente</h3>
    <p class="text-sm mt-1">Los usuarios esperan busquedas tipo Google: rapidas, tolerantes a errores, con resultados rankeados.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>Analisis de texto a escala</h3>
    <p class="text-sm mt-1">Miles de tickets, reseñas, contratos. No puedes leerlos uno por uno — necesitas que la maquina entienda el contenido.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>Tiempo real</h3>
    <p class="text-sm mt-1">Monitoreo de logs, alertas, dashboards que se actualizan al segundo. SQL batch no alcanza.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>IA sobre tus datos</h3>
    <p class="text-sm mt-1">Chatbots que responden preguntas usando la informacion de tu empresa, no alucinaciones.</p>
  </div>
</div>

<v-click>

<div class="text-center mt-4 text-lg">
Para estas necesidades, existen herramientas especializadas. Hoy vamos a conocer dos.
</div>

</v-click>

---

<!-- Slide 15: Database types intro -->

# No solo existen las bases de datos relacionales

<div class="mt-4 text-sm mb-4">

SQL (bases de datos relacionales) es solo <strong>uno</strong> de varios tipos de bases de datos. Cada tipo resuelve un problema distinto:

</div>

<div class="grid grid-cols-3 gap-3">
  <div class="neo-card bg-banana p-3 text-center text-sm">
    <strong>Relacional (SQL)</strong>
    <p class="text-xs mt-1">Tablas con filas y columnas. Para transacciones y datos estructurados.</p>
    <p class="text-xs italic">MySQL, PostgreSQL, SQL Server</p>
  </div>
  <div class="neo-card bg-white p-3 text-center text-sm">
    <strong>Documento</strong>
    <p class="text-xs mt-1">Almacena documentos JSON flexibles. Sin esquema fijo.</p>
    <p class="text-xs italic">MongoDB, CouchDB</p>
  </div>
  <div class="neo-card bg-white p-3 text-center text-sm">
    <strong>Clave-Valor</strong>
    <p class="text-xs mt-1">Como un diccionario gigante. Ultrarapido para lecturas simples.</p>
    <p class="text-xs italic">Redis, DynamoDB</p>
  </div>
  <div class="neo-card bg-white p-3 text-center text-sm">
    <strong>Grafo</strong>
    <p class="text-xs mt-1">Datos como redes: nodos y conexiones. Para relaciones complejas.</p>
    <p class="text-xs italic">Neo4j, Amazon Neptune</p>
  </div>
  <div class="neo-card bg-coral text-white p-3 text-center text-sm">
    <strong>Motor de busqueda</strong>
    <p class="text-xs mt-1">Busqueda de texto rapida, con ranking y tolerancia a errores.</p>
    <p class="text-xs italic">Elasticsearch, Apache Solr</p>
  </div>
  <div class="neo-card bg-sky text-white p-3 text-center text-sm">
    <strong>Vectorial</strong>
    <p class="text-xs mt-1">Busca por significado usando matematicas. Base de la IA moderna.</p>
    <p class="text-xs italic">ChromaDB, Pinecone</p>
  </div>
</div>

<RefFootnote :sources="['DB-Engines. (2026). DB-Engines ranking. https://db-engines.com/en/ranking']" />

---

<!-- Slide 16: What we'll cover today -->

# Hoy nos enfocamos en dos

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="neo-card bg-coral text-white p-6 text-center">
    <div class="text-4xl mb-2">🔍</div>
    <h2>Elasticsearch</h2>
    <div class="pixel-divider my-3" />
    <p class="text-sm">Busqueda de texto completo (full-text search). Rapido, con ranking, tolerante a errores.</p>
    <p class="text-sm mt-2"><strong>Resuelve</strong>: el problema de buscar en texto no estructurado.</p>
  </div>
  <div class="neo-card bg-sky text-white p-6 text-center">
    <div class="text-4xl mb-2">🧠</div>
    <h2>ChromaDB</h2>
    <div class="pixel-divider my-3" />
    <p class="text-sm">Busqueda semantica con vectores (embeddings). Entiende significado, no solo palabras.</p>
    <p class="text-sm mt-2"><strong>Resuelve</strong>: buscar por conceptos e ideas, no solo texto exacto.</p>
  </div>
</div>

---
layout: neo-section
class: bg-coral
---

<!-- Slide 17: ES Section Divider -->

<div class="text-6xl mb-4">🔍</div>

<h1 class="text-white text-5xl">Elasticsearch</h1>

<div class="pixel-divider my-6" />

<p class="text-white/90 text-xl">Busqueda de texto a la velocidad de Google</p>

<div class="mt-6">
  <TimerBadge time="60 min" />
</div>

---

<!-- Slide 18: What is ES -->

# ¿Que es Elasticsearch?

<div class="grid grid-cols-[2fr_1fr] gap-6 mt-6">
  <div class="space-y-3">
    <div class="neo-card bg-white p-3">
      <strong>Motor de busqueda y analitica</strong> de codigo abierto (open source), creado en 2010 por Shay Banon.
    </div>
    <div class="neo-card bg-white p-3">
      Nacio como un proyecto para que su esposa pudiera buscar recetas de cocina. Hoy lo usan Netflix, Wikipedia, Uber y miles de empresas.
    </div>
    <div class="neo-card bg-white p-3">
      <strong>Elasticsearch ≠ base de datos relacional</strong>. Es un complemento especializado en busqueda de texto y analitica en tiempo real.
    </div>
  </div>
  <div class="space-y-3">
    <div class="neo-card bg-banana p-3 text-center text-sm">
      <strong>Creado</strong><br/>2010
    </div>
    <div class="neo-card bg-banana p-3 text-center text-sm">
      <strong>Licencia</strong><br/>Open source (SSPL / Elastic License)
    </div>
    <div class="neo-card bg-banana p-3 text-center text-sm">
      <strong>Costo</strong><br/>Gratis local. Cloud desde $0 (trial 14 dias)
    </div>
  </div>
</div>

<RefFootnote :sources="['Elastic NV. (2024). Elasticsearch reference (v8.x). https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html']" />

---

<!-- Slide 19: ES & OpenSearch -->

# Elasticsearch y OpenSearch

<div class="mt-6">

<div class="neo-card bg-white p-4">

En 2021, **Amazon creo OpenSearch**: un fork (copia independiente) de Elasticsearch, porque no estaba de acuerdo con el cambio de licencia de Elastic.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="neo-card bg-coral/10 p-4">
    <h3>Elasticsearch (Elastic NV)</h3>
    <p class="text-sm mt-1">Version original. La empresa Elastic la mantiene. Elastic Cloud es su servicio en la nube.</p>
  </div>
  <div class="neo-card bg-sky/10 p-4">
    <h3>OpenSearch (AWS)</h3>
    <p class="text-sm mt-1">Fork mantenido por Amazon. Incluido en AWS. Misma API base, desarrollo independiente.</p>
  </div>
</div>

<div class="mt-4 text-center text-sm">

Para nuestro workshop usaremos <strong>Elastic Cloud</strong> (la version oficial), pero lo que aprendan aplica a ambos.

</div>

</div>

---

<!-- Slide 20: Who uses ES - with links -->

# ¿Quien usa Elasticsearch en el mundo real?

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Netflix</h3>
    <p class="text-sm">Busqueda de contenido, monitoreo de servidores y analisis de errores en tiempo real para 200M+ suscriptores.</p>
    <p class="text-xs mt-1 text-gray-500">elastic.co/customers/netflix</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Wikipedia</h3>
    <p class="text-sm">Potencia la busqueda en 300+ idiomas. Cada vez que buscas un articulo, Elasticsearch responde.</p>
    <p class="text-xs mt-1 text-gray-500">mediawiki.org/wiki/Wikimedia_Search_Platform</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">Uber</h3>
    <p class="text-sm">Monitoreo en tiempo real de millones de viajes. Detecta anomalias y problemas al instante.</p>
    <p class="text-xs mt-1 text-gray-500">elastic.co/customers/uber</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3 class="text-coral">GitHub</h3>
    <p class="text-sm">Cuando buscas codigo en GitHub, Elasticsearch busca en miles de millones de lineas de codigo.</p>
    <p class="text-xs mt-1 text-gray-500">github.blog/engineering</p>
  </div>
</div>

<RefFootnote :sources="['Elastic. (2023). Customer stories. https://www.elastic.co/customers']" />

---

<!-- Slide 21: ES strengths overview -->

# Las fortalezas de Elasticsearch

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="neo-card bg-white p-3">
    <h4 class="text-coral">Busqueda de texto completo (Full-text search)</h4>
    <p class="text-xs mt-1">Busca en documentos de texto largo, entiende idiomas, maneja sinonimos y errores tipograficos.</p>
  </div>
  <div class="neo-card bg-white p-3">
    <h4 class="text-coral">Ranking por relevancia</h4>
    <p class="text-xs mt-1">No solo encuentra, sino que ordena resultados del mas relevante al menos. Como Google.</p>
  </div>
  <div class="neo-card bg-white p-3">
    <h4 class="text-coral">Velocidad</h4>
    <p class="text-xs mt-1">Respuestas en milisegundos, incluso con millones de documentos. Usa un "indice invertido" (lo veremos).</p>
  </div>
  <div class="neo-card bg-white p-3">
    <h4 class="text-coral">Escalabilidad (Clusters)</h4>
    <p class="text-xs mt-1">Distribuye datos en multiples servidores. Si necesitas mas capacidad, agregas mas nodos.</p>
  </div>
  <div class="neo-card bg-white p-3">
    <h4 class="text-coral">Analitica en tiempo real</h4>
    <p class="text-xs mt-1">Agregaciones, histogramas, metricas — todo actualizado al segundo. Ideal para dashboards.</p>
  </div>
  <div class="neo-card bg-white p-3">
    <h4 class="text-coral">API REST + JSON</h4>
    <p class="text-xs mt-1">Toda la interaccion es via JSON. Si sabes hacer requests HTTP, ya sabes usar Elasticsearch.</p>
  </div>
</div>

---

<!-- Slide 22: SQL vs ES terminology -->

# Si hablas SQL, ya casi hablas Elasticsearch

<div class="mt-4 text-sm mb-4">Los conceptos son similares, solo cambian los nombres:</div>

<div class="neo-card bg-white p-0 overflow-hidden">

| SQL | Elasticsearch | Explicacion |
|-----|--------------|-------------|
| Base de datos (Database) | Indice (Index) | El contenedor de tus datos |
| Tabla (Table) | Tipo de mapeo (Mapping) | La estructura/esquema |
| Fila (Row) | Documento (Document) | Un registro individual, en JSON |
| Columna (Column) | Campo (Field) | Una propiedad del documento |
| `SELECT ... WHERE` | `GET index/_search { "query": ... }` | Buscar datos |

</div>

<v-click>

<div class="neo-card bg-cream p-3 mt-4 text-center text-sm">
<strong>La gran diferencia</strong>: en SQL escribes texto plano. En Elasticsearch escribes JSON. Pero la logica es la misma.
</div>

</v-click>

---

<!-- Slide 23: How ES searches - Inverted Index -->

# ¿Como busca tan rapido? El indice invertido

<div class="mt-2 text-sm">

Piensa en el <strong>indice al final de un libro de texto</strong>. En vez de leer todo el libro para encontrar "Elasticsearch", vas al indice y ves en que paginas aparece. Elasticsearch hace exactamente eso, pero con todos tus datos:

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="neo-card bg-banana p-3 text-sm">
    <h4>1. Documentos originales</h4>
    <p class="text-xs mt-1">Doc 1: "La comida mexicana es deliciosa"</p>
    <p class="text-xs">Doc 2: "Comida rapida y economica"</p>
    <p class="text-xs">Doc 3: "Recetas de comida italiana"</p>
  </div>
  <div class="neo-card bg-coral text-white p-3 text-sm">
    <h4>2. Tokenizar</h4>
    <p class="text-xs mt-1">Separa en palabras, quita acentos, pasa a minusculas:</p>
    <p class="text-xs">"comida", "mexicana", "deliciosa", "rapida", "economica"...</p>
  </div>
  <div class="neo-card bg-sky text-white p-3 text-sm">
    <h4>3. Indice invertido</h4>
    <p class="text-xs mt-1">
      comida → Doc 1, 2, 3<br/>
      mexicana → Doc 1<br/>
      deliciosa → Doc 1<br/>
      rapida → Doc 2<br/>
      italiana → Doc 3
    </p>
  </div>
</div>

<div class="neo-card bg-cream p-3 mt-4 text-center text-sm">
Buscar "comida mexicana" → va al indice → Doc 1 tiene ambas palabras → <strong>resultado instantaneo</strong>. SQL leeria los 3 documentos completos.
</div>

</v-clicks>

<RefFootnote :sources="['Gormley, C. & Tong, Z. (2015). Elasticsearch: The Definitive Guide. OReilly Media.']" />

---

<!-- Slide 24: Ranking - BM25 -->

# Elasticsearch no solo encuentra — RANKEA

<div class="mt-4 text-sm">

Cuando buscas "comida mexicana" y hay 500 resultados, ¿cual te muestro primero? Elasticsearch usa un algoritmo llamado <strong>BM25</strong> que asigna un puntaje (score) a cada resultado:

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="neo-card bg-white p-3 text-center text-sm">
    <div class="text-2xl font-bold text-coral">Frecuencia</div>
    <p class="text-xs mt-1">¿Cuantas veces aparece la palabra en el documento? Mas veces → mas relevante.</p>
  </div>
  <div class="neo-card bg-white p-3 text-center text-sm">
    <div class="text-2xl font-bold text-coral">Rareza</div>
    <p class="text-xs mt-1">Una palabra rara vale mas. "Elasticsearch" es mas informativa que "el" o "de".</p>
  </div>
  <div class="neo-card bg-white p-3 text-center text-sm">
    <div class="text-2xl font-bold text-coral">Longitud</div>
    <p class="text-xs mt-1">Documentos cortos donde aparece la palabra son mas relevantes que documentos largos.</p>
  </div>
</div>

<div class="neo-card bg-cream p-3 mt-4 text-center text-sm">
<strong>SQL devuelve 0 o 1</strong> (cumple o no cumple). <strong>Elasticsearch devuelve un _score</strong> (0.5, 2.3, 15.7...) que te dice que tan relevante es cada resultado. Es la diferencia entre una lista y un ranking.
</div>

</v-clicks>

<RefFootnote :sources="['Elastic NV. (2024). Similarity module. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html']" />

---

<!-- Slide 25: Clusters concept -->

# Clusters: muchos servidores, un solo sistema

<div class="mt-4 text-sm">

Un <strong>cluster</strong> no es exclusivo de Elasticsearch — es un concepto general en computacion: multiples computadoras trabajando juntas como si fueran una sola.

</div>

<v-click>

<div class="flex flex-col items-center mt-4 gap-3">
  <div class="neo-card bg-banana p-3 text-center font-bold">
    Cluster (grupo de servidores)
  </div>
  <div class="text-xl">↓</div>
  <div class="flex gap-4">
    <div class="neo-card bg-coral text-white p-3 text-center text-sm">Nodo 1<br/><span class="text-xs">Servidor A</span></div>
    <div class="neo-card bg-coral text-white p-3 text-center text-sm">Nodo 2<br/><span class="text-xs">Servidor B</span></div>
    <div class="neo-card bg-coral text-white p-3 text-center text-sm">Nodo 3<br/><span class="text-xs">Servidor C</span></div>
  </div>
</div>

</v-click>

<v-click>

<div class="neo-card bg-cream p-3 mt-4 text-sm">

**¿Por que importa?** Netflix tiene millones de documentos. Un solo servidor no alcanza. Con clusters, distribuyes los datos en pedazos (shards) y si un servidor falla, otro tiene una copia (replica). Elastic Cloud maneja todo esto automaticamente — tu solo usas la interfaz.

</div>

</v-click>

---
layout: neo-demo
---

<!-- Slide 26: Lab - Elastic Cloud Setup -->

::title::

<h2 class="text-banana">Laboratorio: Registrarnos en Elastic Cloud</h2>

::default::

<div class="text-white/90">

### Vamos a hacerlo juntos:

1. Abrir **elastic.co/cloud** → "Start free trial"
2. Registrarse con email y password
3. **Create deployment** → Seleccionar region
4. Esperar ~2 minutos → **Guardar** las credenciales
5. Abrir **Kibana** desde el panel

<div class="mt-4 neo-card bg-white/10 p-3 text-sm">

**Importante**: Guarden el password del usuario `elastic` que se genera automaticamente. Lo necesitan para todo lo demas.

</div>

<div class="mt-2 neo-card bg-white/10 p-3 text-sm">

**Trial gratuito**: 14 dias, sin tarjeta de credito. Suficiente para este workshop y los labs.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 27: Lab - Load sample data -->

::title::

<h2 class="text-banana">Laboratorio: Cargar datos de muestra</h2>

::default::

<div class="text-white/90">

### En Kibana:

1. **Home** → "Try sample data"
2. Clic en **"Add data"** en **"Sample eCommerce orders"**
3. Listo: **10,000+ ordenes** de una tienda online

**Incluye**: productos, categorias, precios, clientes, fechas, ubicaciones

### Explorar el dashboard:

4. Clic en **"View data"** → **"Dashboard"**
5. Observen: mapas, graficas de ventas, top productos...

<div class="mt-3 neo-card bg-white/10 p-3 text-sm">

Todo esto se construyo <strong>sin codigo</strong>. Kibana + Elasticsearch generan dashboards interactivos listos para BI. Comparen esto con cuanto tarda hacer algo similar con SQL + Excel.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 28: Lab - Dev Tools -->

::title::

<h2 class="text-banana">Laboratorio: Dev Tools — tu consola de Elasticsearch</h2>

::default::

<div class="text-white/90">

### Abrir Dev Tools:

Kibana → Menu lateral → **Management** → **Dev Tools**

Izquierda = tu query. Derecha = la respuesta. **Ctrl+Enter** para ejecutar.

### Tu primera query:

```
GET _cluster/health
```

Si ves `"status": "green"` o `"yellow"` → **todo funciona.**

### Ahora busquemos en los datos de eCommerce:

```json
GET kibana_sample_data_ecommerce/_search
{
  "query": { "match": { "products.product_name": "shoes" } },
  "size": 3
}
```

**Observen el `_score`** en cada resultado — eso es BM25 en accion.

</div>

---

<!-- Slide 29: Things SQL can't do - live -->

# Cosas que SQL no puede hacer — y ES si

<div class="mt-4 text-sm">

Ahora que tenemos datos, veamos lo que hace a Elasticsearch especial. Estas cosas serian muy dificiles (o imposibles) con SQL:

</div>

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="neo-card bg-white p-3">
    <strong>1. Busqueda con errores tipograficos (fuzziness)</strong> — buscar "shoees" y encontrar "shoes"
  </div>
  <div class="neo-card bg-white p-3">
    <strong>2. Ranking por relevancia</strong> — ¿que producto es MAS relevante para "comfortable running shoes"?
  </div>
  <div class="neo-card bg-white p-3">
    <strong>3. Resaltado (highlighting)</strong> — mostrar DONDE en el texto se encontro la coincidencia
  </div>
  <div class="neo-card bg-white p-3">
    <strong>4. Busqueda en multiples campos</strong> — buscar en nombre, descripcion y categoria al mismo tiempo
  </div>
  <div class="neo-card bg-white p-3">
    <strong>5. Combinaciones complejas</strong> — "DEBE contener esto, NO debe contener aquello, BONUS si tiene esto otro"
  </div>
</div>

</v-clicks>

---
layout: neo-demo
---

<!-- Slide 30: Fuzziness demo -->

::title::

<h2 class="text-banana">Demo: Escribiste mal? No importa</h2>

::default::

<div class="text-white/90">

```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "products.product_name": {
        "query": "shoees",
        "fuzziness": "AUTO"
      }
    }
  },
  "size": 3
}
```

<div class="mt-3 grid grid-cols-2 gap-4">
  <div class="neo-card bg-coral/30 p-3">
    <strong>SQL</strong>: <code>LIKE '%shoees%'</code> → <strong>0 resultados</strong>
  </div>
  <div class="neo-card bg-sky/30 p-3">
    <strong>ES</strong>: "shoees" → corrige a "shoes" → <strong>resultados encontrados</strong>
  </div>
</div>

**fuzziness: AUTO** = tolera 1-2 errores dependiendo de la longitud de la palabra. Es como el autocompletado de tu celular.

</div>

---
layout: neo-two-cols
---

<!-- Slide 31: SQL vs ES side by side -->

::title::

# SQL vs ES: la misma pregunta, diferente poder

::left::

### SQL

```sql
SELECT * FROM orders
WHERE product_name LIKE '%shoes%'
  AND price BETWEEN 50 AND 200;
-- 0 o 1: cumple o no cumple
-- Sin ranking
```

::right::

### Elasticsearch

```json
GET ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": {
            "product_name": "shoes" } }
      ],
      "filter": [
        { "range": {
            "price": { "gte": 50,
                       "lte": 200 }}}
      ]
    }
  }
}
```

---

<!-- Slide 32: NLP parenthesis -->

# Mini parentesis: ¿como "entiende" texto Elasticsearch?

<div class="mt-4 text-sm">

Elasticsearch usa tecnicas de <strong>NLP</strong> (Procesamiento de Lenguaje Natural / Natural Language Processing) internamente:

</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="neo-card bg-white p-3 text-sm">
    <h4>Tokenizacion</h4>
    <p class="text-xs mt-1">"La comida es deliciosa" → ["la", "comida", "es", "deliciosa"]. Separa texto en palabras individuales.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4>Normalizacion</h4>
    <p class="text-xs mt-1">"Deliciosa" → "deliciosa". Convierte a minusculas, quita acentos para uniformar.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4>Stemming (raices)</h4>
    <p class="text-xs mt-1">"corriendo", "corrio", "correr" → todos se reducen a "corr". Asi "correr" encuentra "corriendo".</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4>Stop words</h4>
    <p class="text-xs mt-1">Ignora palabras sin significado propio: "el", "la", "de", "un". Se enfoca en palabras que importan.</p>
  </div>
</div>

<div class="neo-card bg-cream p-3 mt-4 text-center text-sm">
Todo esto pasa <strong>automaticamente</strong>. Tu solo escribes la busqueda y Elasticsearch aplica estos pasos. En SQL, tendrias que programar cada uno manualmente.
</div>

---

<!-- Slide 33: ES capabilities panorama -->

# Panorama rapido: ¿que mas puede hacer ES?

<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="neo-card bg-white p-3 text-sm">
    <h4 class="text-coral">Agregaciones</h4>
    <p class="text-xs">Como GROUP BY pero mas poderoso. Conteos, promedios, sumas, percentiles — todo en una sola query.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4 class="text-coral">Histogramas</h4>
    <p class="text-xs">Agrupar datos por rangos automaticamente: ventas por rango de precio, pedidos por hora del dia.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4 class="text-coral">Buckets</h4>
    <p class="text-xs">Agrupar documentos en "cubetas" por cualquier campo: por pais, por categoria, por fecha.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4 class="text-coral">Highlighting</h4>
    <p class="text-xs">Resalta exactamente donde en el texto se encontro tu busqueda. Como Google en negritas.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4 class="text-coral">Sugerencias</h4>
    <p class="text-xs">Auto-completar y "quiso decir..." como los buscadores web.</p>
  </div>
  <div class="neo-card bg-white p-3 text-sm">
    <h4 class="text-coral">Geo-busquedas</h4>
    <p class="text-xs">Buscar por ubicacion: "restaurantes a 5km de aqui". Integrado con mapas en Kibana.</p>
  </div>
</div>

<div class="text-center mt-4 text-sm">
Todo esto lo pueden explorar en los labs despues del workshop.
</div>

---

<!-- Slide 34: When NOT to use ES -->

# Cuando NO usar Elasticsearch

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl mb-2">🚫</div>
    <strong>Transacciones</strong>
    <p class="text-sm mt-1">No es ACID. Nunca para transferencias bancarias o inventario critico.</p>
  </div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl mb-2">🚫</div>
    <strong>Base de datos principal</strong>
    <p class="text-sm mt-1">Usalo como complemento de PostgreSQL/MySQL, nunca como reemplazo.</p>
  </div>
  <div class="neo-card bg-coral text-white p-4 text-center">
    <div class="text-2xl mb-2">🚫</div>
    <strong>JOINs complejos</strong>
    <p class="text-sm mt-1">ES no normaliza datos como SQL. Sus documentos son "aplanados" — cada uno es independiente.</p>
  </div>
</div>

<v-click>

<div class="neo-card bg-banana p-4 mt-6 text-center">
<strong>Elasticsearch es un complemento, no un reemplazo de SQL.</strong>
<br/>En las empresas, se usan juntos: SQL para la operacion, ES para la busqueda y analitica.
</div>

</v-click>

---

<!-- Slide 35: ES References -->

# Referencias — Seccion Elasticsearch

<div class="text-xs mt-4 space-y-2">

- Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM, 13*(6), 377-387. https://doi.org/10.1145/362384.362685

- Elastic NV. (2024). *Elasticsearch reference* (v8.x). https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

- Elastic NV. (2024). *Similarity module*. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html

- Gormley, C., & Tong, Z. (2015). *Elasticsearch: The Definitive Guide*. O'Reilly Media. https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html

- DB-Engines. (2026). *DB-Engines ranking*. https://db-engines.com/en/ranking

- Elastic. (2023). *Customer stories*. https://www.elastic.co/customers

- McKinsey & Company. (2024). *The state of AI in 2024*. McKinsey Global Institute.

</div>

---
layout: center
---

<!-- Slide 36: Pause -->

# Pausa: 5 minutos

<div class="text-6xl mt-6">☕</div>

<div class="mt-6 text-xl">
Estiren las piernas. Tomen agua.
</div>

<div class="mt-4 neo-card bg-banana p-4 text-center max-w-md mx-auto">
Lo que sigue es la parte que les va a volar la cabeza.
</div>

---
layout: neo-section
class: bg-sky
---

<!-- Slide 37: ChromaDB Section Divider -->

<div class="text-6xl mb-4">🧠</div>

<h1 class="text-white text-5xl">ChromaDB</h1>

<div class="pixel-divider my-6" />

<p class="text-white/90 text-xl">Busqueda por significado, no por palabras</p>

<div class="mt-6">
  <TimerBadge time="30 min" />
</div>

---

<!-- Slide 38: The problem ES doesn't solve -->

# El problema que ni Elasticsearch resuelve

<div class="mt-4">

Elasticsearch es genial para buscar <strong>palabras</strong>. Pero... ¿que pasa cuando la respuesta no comparte palabras con la pregunta?

</div>

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="neo-card bg-white p-4">
    <strong>Busqueda:</strong> "peliculas que me hagan sentir nostalgico"
    <div class="mt-2 grid grid-cols-2 gap-2">
      <div class="text-sm"><span class="text-coral font-bold">SQL</span>: ❌ "nostalgico" no aparece en las sinopsis</div>
      <div class="text-sm"><span class="text-sky font-bold">Elasticsearch</span>: ❌ busca la palabra "nostalgia" pero la pelicula "Roma" evoca nostalgia sin decirlo</div>
    </div>
  </div>
  <div class="neo-card bg-grape text-white p-4 text-center">
    <strong>Necesitamos algo que entienda el SIGNIFICADO detras de las palabras.</strong>
    <br/>Necesitamos que la maquina "lea entre lineas".
  </div>
</div>

</v-clicks>

---

<!-- Slide 39: Why embeddings matter -->

# Antes de la solucion: ¿por que importa esto?

<div class="mt-6">

Los <strong>embeddings</strong> (representaciones vectoriales) son la tecnologia detras de:

</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="neo-card bg-white p-4">
    <h3>ChatGPT, Claude, Gemini</h3>
    <p class="text-sm mt-1">Todos los modelos de IA modernos usan embeddings para entender lenguaje.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>Recomendaciones</h3>
    <p class="text-sm mt-1">"Si te gusto esta pelicula, te gustara esta otra" — Netflix, Spotify, Amazon.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>Busqueda semantica</h3>
    <p class="text-sm mt-1">Google entiende que "como curar dolor de cabeza" y "remedios para cefalea" son la misma pregunta.</p>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>RAG (IA + tus datos)</h3>
    <p class="text-sm mt-1">Chatbots que responden usando la informacion de tu empresa, no inventando cosas.</p>
  </div>
</div>

<v-click>

<div class="neo-card bg-banana p-3 mt-4 text-center text-sm">
Entender embeddings es <strong>entender como funciona la IA moderna</strong>. Es la habilidad mas relevante que van a aprender hoy.
</div>

</v-click>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 40: Physical analogy -->

# Imagina un cuarto lleno de peliculas

<div class="mt-4">

**Ejercicio mental**: Te doy 100 peliculas escritas en tarjetas. Tienes una mesa grande. ¿Como las organizarias para que peliculas **similares** queden **cerca** entre si?

</div>

<v-clicks>

<div class="grid grid-cols-4 gap-3 mt-4">
  <div class="neo-card bg-banana p-3 text-center text-sm">
    <strong>Esquina 1</strong><br/>Comedias familiares
  </div>
  <div class="neo-card bg-coral text-white p-3 text-center text-sm">
    <strong>Esquina 2</strong><br/>Thrillers oscuros
  </div>
  <div class="neo-card bg-sky text-white p-3 text-center text-sm">
    <strong>Esquina 3</strong><br/>Dramas sociales
  </div>
  <div class="neo-card bg-grape text-white p-3 text-center text-sm">
    <strong>Esquina 4</strong><br/>Ciencia ficcion
  </div>
</div>

<div class="neo-card bg-cream p-4 mt-4 text-center">

Tu cerebro acaba de hacer lo que hace un **embedding**: tomo cada pelicula, "entendio" de que trata, y le asigno una **posicion en el espacio** segun su significado.

Ahora imagina que la mesa es un plano con coordenadas (x, y). Cada pelicula tiene una posicion numerica. **Eso es un vector.**

</div>

</v-clicks>

---

<!-- Slide 41: From analogy to math -->

# De la mesa a los numeros

<div class="grid grid-cols-2 gap-6 mt-6">
  <div>
    <h3>Texto → Vector (embedding)</h3>
    <div class="text-sm space-y-2 mt-3">
      <div class="neo-card bg-white p-2">"perro" → [0.2, 0.8, 0.1, ...]</div>
      <div class="neo-card bg-white p-2">"cachorro" → [0.21, 0.79, 0.12, ...]</div>
      <div class="neo-card bg-white p-2">"automovil" → [0.9, 0.1, 0.7, ...]</div>
    </div>
    <p class="text-sm mt-3">"perro" y "cachorro" tienen numeros <strong>muy parecidos</strong> → estan <strong>cerca</strong> en el espacio. "automovil" tiene numeros muy diferentes → esta <strong>lejos</strong>.</p>
  </div>
  <div class="flex items-center justify-center">
    <div class="neo-card bg-grape text-white p-6 text-center">
      <div class="text-lg font-bold mb-3">Espacio de significado</div>
      <div class="text-sm text-left">
        🐕 perro<br/>
        &nbsp;&nbsp;&nbsp;↕ <em>cerca</em><br/>
        🐶 cachorro<br/>
        <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↕ <em>lejos</em><br/>
        <br/>
        🚗 automovil
      </div>
    </div>
  </div>
</div>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 42: The classic analogy -->

# El ejemplo clasico que demuestra que funciona

<div class="mt-8">

<div class="neo-card bg-banana p-6 text-center text-2xl">
<strong>"rey" − "hombre" + "mujer" ≈ "reina"</strong>
</div>

<div class="mt-6 text-center">

Si restas las coordenadas de "hombre" a "rey" y sumas las de "mujer", llegas a un punto en el espacio que esta muy cerca de "reina". Los embeddings capturan **relaciones y analogias** — no solo similitud de palabras.

</div>

</div>

<v-click>

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="neo-card bg-white p-4 text-center text-sm">
    <h4>¿Quien calcula los embeddings?</h4>
    <p class="text-xs mt-1">Modelos de IA entrenados con miles de millones de textos. ChromaDB usa uno por defecto — tu no tienes que hacer nada.</p>
  </div>
  <div class="neo-card bg-white p-4 text-center text-sm">
    <h4>¿Que es la "distancia"?</h4>
    <p class="text-xs mt-1">Se mide el angulo entre dos vectores (similitud coseno). Angulo chico = similares. ChromaDB calcula esto automaticamente.</p>
  </div>
</div>

</v-click>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 43: What is a vector DB -->

# ¿Que es una base de datos vectorial?

<div class="mt-4 text-sm">

Si los embeddings son las "coordenadas de significado" de un texto, necesitamos un lugar para <strong>guardarlos</strong> y <strong>buscar en ellos</strong> eficientemente. Eso es una base de datos vectorial.

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="neo-card bg-grape text-white p-4 text-center">
    <div class="text-3xl mb-2">📐</div>
    <strong>Guarda vectores</strong>
    <p class="text-xs mt-1">Los numeros que representan el significado de cada documento.</p>
  </div>
  <div class="neo-card bg-sky text-white p-4 text-center">
    <div class="text-3xl mb-2">🔍</div>
    <strong>Busca por cercania</strong>
    <p class="text-xs mt-1">"Dame los 5 documentos cuyo significado sea mas cercano a esta pregunta."</p>
  </div>
  <div class="neo-card bg-banana p-4 text-center">
    <div class="text-3xl mb-2">📄</div>
    <strong>Devuelve el texto original</strong>
    <p class="text-xs mt-1">No solo los numeros — tambien el documento de donde vino, con metadata.</p>
  </div>
</div>

<div class="mt-4 text-sm">

**El mercado**: ChromaDB, Pinecone, Weaviate, Qdrant, Milvus, pgvector (PostgreSQL). Hoy usaremos <strong>ChromaDB</strong> porque es la mas simple.

</div>

</v-clicks>

<RefFootnote :sources="['Pan, J. W., et al. (2024). A survey on vector database. arXiv:2310.11703.']" />

---

<!-- Slide 44: ChromaDB intro -->

# ChromaDB: busqueda semantica en 5 lineas de Python

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="space-y-3">
    <div class="neo-card bg-white p-3 text-sm">
      <strong>Open source</strong> — codigo abierto, licencia Apache 2.0. Gratis.
    </div>
    <div class="neo-card bg-white p-3 text-sm">
      <strong>Python-first</strong> — <code>pip install chromadb</code> y listo.
    </div>
    <div class="neo-card bg-white p-3 text-sm">
      <strong>Auto-embed</strong> — genera los vectores automaticamente, sin configuracion.
    </div>
    <div class="neo-card bg-white p-3 text-sm">
      <strong>RAG-ready</strong> — diseñado para construir apps de IA con tus datos.
    </div>
  </div>
  <div>

```python
import chromadb

client = chromadb.Client()
col = client.create_collection("demo")

col.add(
    documents=["Comida mexicana",
               "Python para datos",
               "Tacos deliciosos"],
    ids=["d1", "d2", "d3"]
)

results = col.query(
    query_texts=["gastronomia"],
    n_results=2
)
# Encuentra "Comida mexicana"
# y "Tacos deliciosos"
# sin mencionar esas palabras!
```

  </div>
</div>

<RefFootnote :sources="['Chroma. (2024). Chroma documentation. https://docs.trychroma.com/']" />

---

<!-- Slide 45: Predict then reveal -->

# Predice: ¿que resultados devolvera?

<div class="mt-2 text-sm">Coleccion con 5 documentos: comida mexicana, IA en negocios, Python para datos, burritos deliciosos, machine learning.</div>

<v-clicks>

<div class="space-y-4 mt-4">
  <div class="neo-card bg-white p-4">
    <strong>Query 1:</strong> "tacos"
    <div class="text-sm text-coral font-bold mt-1">→ "comida mexicana" y "burritos" — palabras diferentes, mismo concepto</div>
  </div>
  <div class="neo-card bg-white p-4">
    <strong>Query 2:</strong> "inteligencia artificial"
    <div class="text-sm text-sky font-bold mt-1">→ "IA en negocios" y "machine learning" — entiende sinonimos y conceptos relacionados</div>
  </div>
  <div class="neo-card bg-banana p-4">
    <strong>Query 3:</strong> "analisis de informacion"
    <div class="text-sm text-grape font-bold mt-1">→ "Python para datos" — la conexion es conceptual, no hay palabras en comun</div>
  </div>
</div>

<div class="neo-card bg-cream p-3 mt-4 text-center text-sm">
<strong>Los embeddings entienden CONCEPTOS, no solo palabras.</strong> Esa es la diferencia entre busqueda de texto (Elasticsearch) y busqueda semantica (ChromaDB).
</div>

</v-clicks>

---

<!-- Slide 46: RAG intro -->

# RAG: IA que responde desde TUS datos

<div class="mt-4 text-sm">

El gran problema de ChatGPT: a veces **inventa** respuestas (alucina). ¿La solucion? Darle tus datos como contexto antes de responder. Eso es **RAG** (Retrieval-Augmented Generation):

</div>

<v-click>

<div class="flex items-center justify-center gap-2 mt-6">
  <div class="neo-card bg-banana p-3 text-center text-sm">
    <div class="text-xl">❓</div>
    <strong>Pregunta</strong>
  </div>
  <div class="text-xl">→</div>
  <div class="neo-card bg-sky text-white p-3 text-center text-sm">
    <div class="text-xl">🔍</div>
    <strong>ChromaDB busca</strong>
    <p class="text-xs">contexto relevante</p>
  </div>
  <div class="text-xl">→</div>
  <div class="neo-card bg-grape text-white p-3 text-center text-sm">
    <div class="text-xl">🧠</div>
    <strong>LLM genera</strong>
    <p class="text-xs">respuesta con contexto</p>
  </div>
  <div class="text-xl">→</div>
  <div class="neo-card bg-coral text-white p-3 text-center text-sm">
    <div class="text-xl">✅</div>
    <strong>Respuesta</strong>
    <p class="text-xs">fundamentada</p>
  </div>
</div>

</v-click>

<v-click>

<div class="neo-card bg-cream p-4 mt-4 text-center">
<strong>La IA no hallucina porque responde desde TUS datos</strong>, no desde su entrenamiento general. Es como darle un libro de texto al estudiante antes del examen.
</div>

</v-click>

<RefFootnote :sources="['Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS, 33, 9459-9474.']" />

---
layout: neo-demo
---

<!-- Slide 47: Career Coach RAG Demo -->

::title::

<h2 class="text-banana">DEMO: Tu coach de carrera con IA</h2>

::default::

<div class="text-white/90">

### AI Career Coach para estudiantes de BI

Un chatbot que responde preguntas sobre carreras en datos usando **40+ ofertas de trabajo reales** de empresas en Mexico.

**Stack**: ChromaDB (busqueda) + together.ai (LLM) + Gradio (interfaz)

### Prueben estas preguntas:

- *"¿Que habilidades necesito para Data Analyst en consulting?"*
- *"¿Que empresas en Monterrey buscan egresados de BI?"*
- *"Se Python, SQL y Tableau — ¿para que puestos califico?"*
- *"¿Que tecnologias deberia aprender este semestre?"*

<div class="mt-2 neo-card bg-white/10 p-2 text-sm">
Cada respuesta muestra las <strong>fuentes</strong>: las ofertas de trabajo reales en las que se basa. Eso es RAG en accion.
</div>

</div>

---

<!-- Slide 48: Chroma References -->

# Referencias — Seccion ChromaDB y RAG

<div class="text-xs mt-4 space-y-2">

- Chroma. (2024). *Chroma documentation*. https://docs.trychroma.com/

- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS, 33*, 9459-9474. https://arxiv.org/abs/2005.11401

- Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. *arXiv:1301.3781*. https://arxiv.org/abs/1301.3781

- Pan, J. W., et al. (2024). A survey on vector database. *arXiv:2310.11703*. https://arxiv.org/abs/2310.11703

</div>

---
layout: neo-section
class: bg-ink
---

<!-- Slide 49: Closing section -->

<h1 class="text-banana text-4xl">La herramienta correcta para la pregunta correcta</h1>

<div class="mt-6">
  <TimerBadge time="15 min" />
</div>

---

<!-- Slide 50: Comparison table -->

# SQL vs Elasticsearch vs ChromaDB

<ComparisonTable
  :headers="['', 'SQL', 'Elasticsearch', 'ChromaDB']"
  :rows="[
    ['Modelo de datos', 'Tablas + filas', 'Documentos JSON', 'Vectores + docs'],
    ['Tipo de busqueda', 'Exacta (WHERE)', 'Texto completo (match)', 'Semantica (significado)'],
    ['Ranking', 'No (0 o 1)', 'Si (BM25 score)', 'Si (distancia coseno)'],
    ['Typos/errores', 'No tolera', 'Si (fuzziness)', 'Implicito (entiende concepto)'],
    ['Mejor para', 'Transacciones, JOINs', 'Busqueda de texto, logs', 'IA, recomendaciones, RAG'],
  ]"
/>

<v-click>

<div class="neo-card bg-cream p-4 mt-6 text-center">
<strong>No son competidores — son complementos.</strong>
En la practica, las empresas usan SQL + ES + Vector DB juntos, cada uno para lo que hace mejor.
</div>

</v-click>

---

<!-- Slide 51: Your new superpower -->

# Tu nuevo superpoder empieza ahora

<div class="mt-6">

<div class="neo-card bg-banana p-6">

### Ofertas de empleo reales que ya piden estas habilidades:

- *"Data Engineer — **Elasticsearch**, Kafka, Python"* — Amazon
- *"BI Developer — SQL, **vector databases**, LLM integration"* — Deloitte
- *"AI Engineer — **RAG pipelines**, ChromaDB/Pinecone"* — Wizeline
- *"Data Scientist — NLP, **Elasticsearch**, ChromaDB"* — HSBC Mexico

</div>

<div class="mt-4 text-center text-lg">
<strong>Ahora saben que es esto. La mayoria de profesionales con 5 años de experiencia no.</strong>
</div>

</div>

---

<!-- Slide 52: Keep practicing -->

# Sigue practicando

<div class="grid grid-cols-2 gap-4 mt-6">
  <div class="neo-card bg-white p-4">
    <h3>Labs en este repo</h3>
    <ul class="text-sm mt-2 space-y-1">
      <li>Lab 1: Elasticsearch Basics (~30 min)</li>
      <li>Lab 2: ES Search avanzado (~45 min)</li>
      <li>Lab 3: ChromaDB y embeddings (~30 min)</li>
      <li>Lab 4: Construye un mini RAG (~45 min)</li>
    </ul>
  </div>
  <div class="neo-card bg-white p-4">
    <h3>Recursos</h3>
    <ul class="text-sm mt-2 space-y-1">
      <li>Elastic Cloud: 14 dias gratis</li>
      <li>ChromaDB: docs.trychroma.com</li>
      <li>together.ai: creditos gratis</li>
      <li>Kaggle: datasets para practicar</li>
    </ul>
  </div>
</div>

---

<!-- Slide 53: All references -->

# Referencias completas

<div class="text-xs mt-2 space-y-1">

- Chroma. (2024). *Chroma documentation*. https://docs.trychroma.com/
- Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM, 13*(6), 377-387.
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

<div class="mt-2 text-center text-xs">
Lista completa con hyperlinks: <code>references/apa7.md</code> en el repositorio
</div>

---
layout: neo-cover
---

<!-- Slide 54: Closing -->

# Gracias!

<div class="pixel-divider my-4" />

<div class="text-lg mb-4">#MasAlladeSQL</div>

<div class="text-sm">
Comparte lo que construiste hoy
</div>

<div class="flex gap-4 justify-center items-center mt-6">
  <span class="neo-tag bg-coral text-white">github.com/HesusG/mas-alla-de-sql</span>
</div>
