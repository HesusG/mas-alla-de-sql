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

<div class="mt-4 text-sm opacity-50 font-mono">
github.com/HesusG/mas-alla-de-sql
</div>

---

<!-- Slide 2: About me -->

# Sobre mi

<div class="pixel-divider my-4" />

<div class="grid grid-cols-[1fr_2fr] gap-8 mt-4 items-center">
  <div class="border-2 border-black p-6 text-center bg-[#C0C0C0]">
    <div class="i-pixelarticons-user inline-block w-16 h-16 mb-4" />
    <div class="text-lg font-bold">[Tu nombre]</div>
    <div class="text-sm mt-1">[Tu rol / titulo]</div>
  </div>
  <div class="space-y-3">

<v-clicks>

  <div class="border-2 border-black bg-white p-3 text-sm flex items-center gap-2"><div class="i-pixelarticons-map-pin inline-block w-5 h-5 flex-shrink-0" /> [Ciudad, organizacion]</div>
  <div class="border-2 border-black bg-white p-3 text-sm flex items-center gap-2"><div class="i-pixelarticons-briefcase-search inline-block w-5 h-5 flex-shrink-0" /> [Experiencia relevante]</div>
  <div class="border-2 border-black bg-white p-3 text-sm flex items-center gap-2"><div class="i-pixelarticons-tool-case inline-block w-5 h-5 flex-shrink-0" /> [Stack / tecnologias]</div>
  <div class="border-2 border-black bg-white p-3 text-sm flex items-center gap-2"><div class="i-pixelarticons-bullseye-arrow inline-block w-5 h-5 flex-shrink-0" /> [Por que este tema te apasiona]</div>

</v-clicks>

  </div>
</div>

---

<!-- Slide 3: Roadmap -->

# Hoy vamos a recorrer este camino

<div class="pixel-divider my-4" />

<div class="flex items-center justify-center gap-3 mt-6">

<v-clicks>

  <div class="border-2 border-black p-4 text-center min-w-28 bg-[#C0C0C0]">
    <div class="i-pixelarticons-database inline-block w-8 h-8 mb-1" />
    <br/><strong>SQL</strong><br/>
    <span class="text-xs">Lo que conoces</span>
  </div>
  <div class="text-3xl font-bold text-black/30">→</div>
  <div class="border-2 border-black p-4 text-center min-w-28 bg-[#ff6b6b]/15">
    <div class="i-pixelarticons-warning-box inline-block w-8 h-8 mb-1" />
    <br/><strong>El problema</strong><br/>
    <span class="text-xs">Donde SQL no llega</span>
  </div>
  <div class="text-3xl font-bold text-black/30">→</div>
  <div class="border-2 border-[#ff6b6b] p-4 text-center min-w-28 bg-[#ff6b6b]/15">
    <div class="i-pixelarticons-search inline-block w-8 h-8 mb-1" />
    <br/><strong>Elasticsearch</strong><br/>
    <span class="text-xs">Busqueda de texto</span>
  </div>
  <div class="text-3xl font-bold text-black/30">→</div>
  <div class="border-2 border-[#6c5ce7] p-4 text-center min-w-28 bg-[#6c5ce7]/15">
    <div class="i-pixelarticons-ai-app-mac inline-block w-8 h-8 mb-1" />
    <br/><strong>ChromaDB</strong><br/>
    <span class="text-xs">Busqueda por significado</span>
  </div>

</v-clicks>

</div>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 mt-6 text-center text-lg">
Al terminar, van a tener un <strong>superpoder</strong> que la mayoria de profesionales con experiencia no tienen.
</div>

</v-click>

---

<!-- Slide 4: Cold Open - Setup -->

# Empecemos con un reto

<div class="grid grid-cols-[2fr_1fr] gap-6 mt-4">
  <div>

Imaginen que trabajan en el area de **servicio al cliente** de una tienda online.

Su jefe les dice:

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-5 mt-4 text-center text-lg">
<em>"Necesito un reporte de todas las reseñas donde los clientes estan <strong>frustrados</strong>.<br/> Tenemos 10,000 reseñas en la base de datos. Para ayer."</em>
</div>

</v-click>

<v-click>

<div class="mt-4 text-center text-lg">
¿Como lo harian con las herramientas que conocen?
</div>

</v-click>

  </div>
  <div class="flex items-center">
    <img src="/images/slides/slide_04_reto.png" class="w-full border-2 border-black shadow-[2px_2px_0px_#000]" />
  </div>
</div>

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

<div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4 mt-4">
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
  <div class="border-2 border-black bg-white p-3"><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" />Hay que <strong>adivinar</strong> todas las palabras posibles — ¿cuantas formas hay de expresar frustracion?</div>
  <div class="border-2 border-black bg-white p-3"><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /><strong>No entiende contexto</strong>: "no estoy molesto" apareceria como resultado positivo</div>
  <div class="border-2 border-black bg-white p-3"><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" />Es <strong>lento</strong>: cada <code>LIKE</code> con <code>%</code> escanea toda la tabla, fila por fila</div>
  <div class="border-2 border-black bg-white p-3"><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /><strong>Sin ranking</strong>: no sabes cual resena es "mas frustrada" que otra</div>
</div>

</v-clicks>

---

<!-- Slide 7: The reveal - WHY ES returns more -->

# Ahora miren esto

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="space-y-4">
    <h3 class="text-coral">SQL</h3>
    <div class="border-2 border-black bg-white p-4">

```sql
SELECT * FROM resenas
WHERE texto LIKE '%frustrado%';
```

<div class="mt-2 text-[#ff6b6b] font-bold">→ 23 resultados. Sin ranking.</div>
    </div>
  </div>
  <div class="space-y-4">
    <h3 class="text-sky">Elasticsearch</h3>
    <div class="border-2 border-black bg-white p-4">

```json
GET resenas/_search
{ "query": { "match": {
    "texto": "frustrado"
}}}
```

<div class="mt-2 text-[#2DD4BF] font-bold">→ 147 resultados. Rankeados por relevancia.</div>
    </div>
  </div>
</div>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 mt-4 text-sm">
<strong>¿Por que 147 vs 23?</strong> Elasticsearch <em>tokeniza</em> el texto: separa "frustrado" en su raiz y busca variaciones. Ademas, su <strong>indice invertido</strong> ya mapeó cada palabra a los documentos donde aparece — no escanea fila por fila como <code>LIKE</code>. SQL busca la cadena exacta; ES entiende la estructura del idioma.
</div>

</v-click>

<v-click>

<div class="text-center mt-3 text-sm">
Al final de esta sesion, van a saber como hacer esto. Y mucho mas.
</div>

</v-click>

---
layout: neo-section
---

<!-- Slide 8: Section - Unstructured data -->

<h1 class="text-white text-6xl font-bold">El mundo real no cabe en tablas</h1>

<p class="text-[#2DD4BF] mt-6 text-xl font-mono">// entendiendo por que SQL no es suficiente</p>

---

<!-- Slide 9: Audience interaction -->

# Antes de seguir... un sondeo rapido

<div class="mt-8 space-y-6">

<v-clicks>

<div class="border-2 border-black p-5 text-lg">
<div class="i-pixelarticons-human-handsup inline-block w-5 h-5 align-middle mr-1" /><strong>Levanten la mano si...</strong> han usado SQL en algun proyecto o clase
</div>

<div class="border-2 border-black p-5 text-lg">
<div class="i-pixelarticons-human-handsup inline-block w-5 h-5 align-middle mr-1" /><strong>Levanten la mano si...</strong> alguna vez intentaron buscar texto libre en una base de datos y les frustro el resultado
</div>

<div class="border-2 border-black p-5 text-lg">
<div class="i-pixelarticons-human-handsup inline-block w-5 h-5 align-middle mr-1" /><strong>Levanten la mano si...</strong> han usado un buscador inteligente (Google, Spotify, Netflix) y se preguntaron "¿como sabe lo que quiero?"
</div>

</v-clicks>

</div>

<v-click>

<div class="mt-6 text-center text-lg">
Perfecto. Hoy vamos a entender como funcionan esos buscadores <strong>por dentro</strong>.
</div>

</v-click>

---

<!-- Slide 10: What is unstructured data -->

# ¿Que son los datos no estructurados?

<div class="pixel-divider my-3" />

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <h3 class="mb-3 text-[#2DD4BF]"><div class="i-pixelarticons-check inline-block w-5 h-5 align-middle mr-1" /> Datos estructurados (SQL)</h3>
    <div class="border-2 border-black bg-white p-3 text-sm">
      <table class="w-full text-xs mac-table">
        <tr><th class="text-left p-1 font-bold">id</th><th class="text-left p-1 font-bold">nombre</th><th class="text-left p-1 font-bold">precio</th><th class="text-left p-1 font-bold">stock</th></tr>
        <tr><td class="p-1">1</td><td class="p-1">Laptop</td><td class="p-1">15000</td><td class="p-1">42</td></tr>
        <tr><td class="p-1">2</td><td class="p-1">Mouse</td><td class="p-1">350</td><td class="p-1">200</td></tr>
      </table>
      <p class="mt-2 font-bold">Filas, columnas, tipos definidos. Perfecto para SQL.</p>
    </div>
  </div>
  <div>
    <h3 class="mb-3 text-[#ff6b6b]"><div class="i-pixelarticons-warning-box inline-block w-5 h-5 align-middle mr-1" /> Datos no estructurados</h3>
    <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-3 text-sm space-y-2">
      <div><div class="i-pixelarticons-mail inline-block w-4 h-4 align-middle mr-1" /><em>"Hola, llevo 2 semanas sin recibir mi pedido..."</em></div>
      <div><div class="i-pixelarticons-file-text inline-block w-4 h-4 align-middle mr-1" />Contrato de 45 paginas en PDF</div>
      <div><div class="i-pixelarticons-chat inline-block w-4 h-4 align-middle mr-1" />Conversaciones de chat con soporte</div>
      <div><div class="i-pixelarticons-device-tablet inline-block w-4 h-4 align-middle mr-1" />Posts de redes sociales</div>
      <div><div class="i-pixelarticons-note inline-block w-4 h-4 align-middle mr-1" />Notas de reuniones, minutas</div>
    </div>
  </div>
</div>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 mt-4 text-center">
<strong>Mas del 80% de los datos en las empresas son no estructurados.</strong>
No caben en una tabla de SQL.
</div>

</v-click>

<RefFootnote :sources="['McKinsey & Company. (2024). The state of AI in 2024. McKinsey Global Institute.']" />

---

<!-- Slide 11: What is normalization - for dummies -->

# ¿Que es normalizacion? (Normalization)

<div class="mt-4 text-sm">

Antes de entender el problema, veamos como SQL <strong>organiza</strong> los datos. Normalizacion = separar la informacion en tablas relacionadas para evitar repeticion.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <h4 class="mb-2 text-[#ff6b6b]">Antes: una tabla desordenada</h4>
    <div class="border-2 border-black p-3 text-xs font-mono bg-white">
      <table class="w-full mac-table">
        <tr><th class="p-1">pedido</th><th class="p-1">cliente</th><th class="p-1">email</th><th class="p-1">producto</th><th class="p-1">precio</th></tr>
        <tr><td class="p-1">001</td><td class="p-1">Ana</td><td class="p-1">ana@mail</td><td class="p-1">Laptop</td><td class="p-1">15000</td></tr>
        <tr><td class="p-1">002</td><td class="p-1">Ana</td><td class="p-1">ana@mail</td><td class="p-1">Mouse</td><td class="p-1">350</td></tr>
        <tr><td class="p-1">003</td><td class="p-1">Luis</td><td class="p-1">luis@mail</td><td class="p-1">Laptop</td><td class="p-1">15000</td></tr>
      </table>
      <p class="mt-1 text-[#ff6b6b]">↑ "Ana" y "Laptop" repetidos</p>
    </div>
  </div>
  <div>
    <h4 class="mb-2 text-[#2DD4BF]">Despues: 3 tablas limpias</h4>
    <div class="border-2 border-black p-3 text-xs font-mono bg-white space-y-2">
      <div><strong>clientes</strong>: id, nombre, email</div>
      <div><strong>productos</strong>: id, nombre, precio</div>
      <div><strong>pedidos</strong>: id, cliente_id, producto_id</div>
      <p class="mt-1 text-[#2DD4BF]">↑ Sin repeticion, conectados por IDs</p>
    </div>
  </div>
</div>

<v-click>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
Esto es lo que SQL hace mejor que nadie: datos <strong>estructurados, limpios y sin duplicados</strong>.
</div>

</v-click>

<RefFootnote :sources="['Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), 377-387.']" />

---

<!-- Slide 12: Downsides of normalization -->

# Las desventajas de normalizar

<div class="grid grid-cols-[2fr_1fr] gap-6 mt-4">
  <div>
    <div class="text-sm">Normalizar es excelente para datos estructurados. Pero tiene un costo:</div>

<v-clicks>

<div class="space-y-3 mt-3">
  <div class="border-2 border-black bg-white p-3 text-sm">
    <strong>JOINs son lentos a escala</strong> — Para reconstruir la informacion original necesitas cruzar 3, 4, 5 tablas. Con millones de filas, esto se vuelve costoso.
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <strong>Esquema rigido</strong> — Cada columna tiene un tipo definido. ¿Quieres agregar un campo nuevo? ALTER TABLE. ¿Un documento que no tiene ese campo? NULL.
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <strong>No puedes buscar "a traves" de los datos</strong> — Si la informacion esta repartida en 5 tablas, buscar texto libre requiere JOINs + LIKE en cada tabla. Impracticable.
  </div>
</div>

</v-clicks>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-3 mt-3 text-center text-sm">
Normalizacion funciona perfecto para datos estructurados. Pero... <strong>¿que pasa con texto libre, emails, PDFs, chats?</strong>
</div>

</v-click>

  </div>
  <div class="flex items-center">
    <img src="/images/slides/slide_12_normalizar.png" class="w-full border-2 border-black shadow-[2px_2px_0px_#000]" />
  </div>
</div>

---

<!-- Slide 13: SQL is powerful - Codd + ACID -->

# SQL es poderoso — para lo que fue diseñado

<div class="grid grid-cols-[1fr_2fr] gap-6 mt-4">
  <div class="border-2 border-black p-4 text-center">
    <div class="w-32 h-32 mx-auto border-2 border-black flex items-center justify-center bg-gray-100"><div class="i-pixelarticons-user inline-block w-16 h-16" /></div>
    <div class="text-sm font-bold mt-2">Edgar F. Codd</div>
    <div class="text-xs">IBM, 1970</div>
    <div class="text-xs mt-1">Inventor del modelo relacional</div>
  </div>
  <div>
    <h3 class="mb-3">Transacciones ACID</h3>
    <div class="grid grid-cols-2 gap-2">
      <div class="border-2 border-black p-2 text-sm"><strong class="text-[#ff6b6b]">A</strong>tomicidad — Todo o nada</div>
      <div class="border-2 border-black p-2 text-sm"><strong class="text-[#ff6b6b]">C</strong>onsistencia — Reglas siempre se cumplen</div>
      <div class="border-2 border-black p-2 text-sm"><strong class="text-[#ff6b6b]">I</strong>solamiento — Transacciones no se estorban</div>
      <div class="border-2 border-black p-2 text-sm"><strong class="text-[#ff6b6b]">D</strong>urabilidad — Lo guardado no se pierde</div>
    </div>
    <div class="text-sm mt-3">
    Si transfieres $1,000 de una cuenta a otra, SQL garantiza que el dinero no desaparezca en el camino. Esto es <strong>fundamental</strong> para bancos, inventarios y cualquier sistema critico.
    </div>
  </div>
</div>

<RefFootnote :sources="['Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), 377-387.']" />

---

<!-- Slide 14: What SQL can't do - Text -->

# Pero SQL no fue diseñado para buscar texto

<div class="mt-4">

Intenta responder estas preguntas con SQL:

</div>

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="border-2 border-black bg-white p-3">
    <strong>1.</strong> "Encuentra reseñas de clientes <strong>insatisfechos</strong>" → ¿Con que palabra buscas? Hay cientos de formas de expresar insatisfaccion.
  </div>
  <div class="border-2 border-black bg-white p-3">
    <strong>2.</strong> "Busca productos similares a <strong>tenis para correr</strong>" → <code>LIKE '%tenis%'</code> no encuentra "zapatillas deportivas" ni "running shoes".
  </div>
  <div class="border-2 border-black bg-white p-3">
    <strong>3.</strong> "¿Cuales son las quejas <strong>mas urgentes</strong>?" → SQL no puede rankear por "urgencia" — devuelve todo o nada.
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-3">
    <strong>4.</strong> "El cliente escribio <strong>'teniz'</strong> en vez de 'tenis'" → <code>LIKE '%teniz%'</code> no encuentra nada. Un simple error tipografico y perdiste resultados.
  </div>
</div>

</v-clicks>

---

<!-- Slide 15: Relevance explained -->

# ¿Que es "relevancia"? (Relevance)

<div class="mt-4 text-sm">

Piensa en como buscas en Google: escribes <strong>"receta pastel de chocolate"</strong> y obtienes resultados ordenados del mas util al menos. Eso es relevancia.

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <h4 class="text-[#ff6b6b] mb-2">SQL: Binario (si/no)</h4>
    <div class="border-2 border-black p-3 text-sm space-y-2">
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> "Pastel de chocolate con crema"</div>
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> "El chocolate del pastel se quemo"</div>
      <div><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /> "Torta de cacao con ganache"</div>
      <div class="text-xs text-gray-500 mt-2">No distingue cual es mejor. Todas las que contienen "pastel" + "chocolate" son iguales.</div>
    </div>
  </div>
  <div>
    <h4 class="text-[#2DD4BF] mb-2">Elasticsearch: Ranking por score</h4>
    <div class="border-2 border-black p-3 text-sm space-y-2">
      <div><span class="font-mono text-[#2DD4BF]">_score: 15.7</span> "Receta de pastel de chocolate"</div>
      <div><span class="font-mono text-[#2DD4BF]">_score: 8.2</span> "Torta de cacao con ganache"</div>
      <div><span class="font-mono text-[#2DD4BF]">_score: 3.1</span> "El chocolate se uso en el pastel"</div>
      <div class="text-xs text-gray-500 mt-2">Cada resultado tiene un puntaje. Los mas relevantes primero.</div>
    </div>
  </div>
</div>

<v-click>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
<strong>La diferencia entre una lista y un ranking.</strong> En BI, no solo importa encontrar datos — importa saber cuales son los <em>mas importantes</em>.
</div>

</v-click>

---

<!-- Slide 16: The frustration expanded -->

# El costo real de estas limitaciones

<div class="grid grid-cols-[1fr_2fr] gap-6 mt-4">
  <div class="flex items-center">
    <img src="/images/slides/slide_16_costo.png" class="w-full border-2 border-black shadow-[2px_2px_0px_#000]" />
  </div>
  <div>
    <div class="text-sm">Volvamos a nuestro reto de las reseñas. Con SQL encontramos 23 resultados. ¿Que paso con los otros 124?</div>

<v-clicks>

<div class="space-y-2 mt-3">
  <div class="border-2 border-black bg-white p-2 text-sm">
    <strong>"El producto llego roto y nadie me ayudo"</strong> — cliente claramente frustrado, pero no usa esa palabra
  </div>
  <div class="border-2 border-black bg-white p-2 text-sm">
    <strong>"3 llamadas al soporte y sigo sin solucion"</strong> — frustracion implicita en el contexto
  </div>
  <div class="border-2 border-black bg-white p-2 text-sm">
    <strong>"Esperaba mucho mas por este precio"</strong> — decepcion, un sinonimo de frustracion
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-2 text-sm">
    <strong>"Mi experiencia fue desastrosa desde el primer dia"</strong> — intensidad alta, pero SQL la ignora por completo
  </div>
</div>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-3 mt-3 text-center text-sm">
<strong>Cada resena que SQL no encuentra es un cliente que podrias perder.</strong>
En BI, los datos que no ves son los mas peligrosos.
</div>

</v-clicks>

  </div>
</div>

---

<!-- Slide 17: Modern data needs -->

# Las empresas de hoy necesitan mas

<div class="pixel-divider my-3" />

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="border-2 border-black bg-white p-4">
    <h3 class="text-[#ff6b6b]"><div class="i-pixelarticons-search inline-block w-5 h-5 align-middle mr-1" /> Busqueda inteligente</h3>
    <p class="text-sm mt-1">Los usuarios esperan busquedas tipo Google: rapidas, tolerantes a errores, con resultados rankeados.</p>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <h3 class="text-[#ff6b6b]"><div class="i-pixelarticons-chart inline-block w-5 h-5 align-middle mr-1" /> Analisis de texto a escala</h3>
    <p class="text-sm mt-1">Miles de tickets, reseñas, contratos. No puedes leerlos uno por uno — necesitas que la maquina entienda el contenido.</p>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <h3 class="text-[#2DD4BF]"><div class="i-pixelarticons-zap inline-block w-5 h-5 align-middle mr-1" /> Tiempo real</h3>
    <p class="text-sm mt-1">Monitoreo de logs, alertas, dashboards que se actualizan al segundo. SQL batch no alcanza.</p>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <h3 class="text-[#6c5ce7]"><div class="i-pixelarticons-ai-app-mac inline-block w-5 h-5 align-middle mr-1" /> IA sobre tus datos</h3>
    <p class="text-sm mt-1">Chatbots que responden preguntas usando la informacion de tu empresa, no alucinaciones.</p>
  </div>
</div>

</v-clicks>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-3 mt-4 text-center text-lg">
Para estas necesidades, existen herramientas especializadas. <strong>Hoy vamos a conocer dos.</strong>
</div>

</v-click>

---

<!-- Slide 18: Database types intro -->

# No solo existen las bases de datos relacionales

<div class="mt-4 text-sm mb-4">

SQL (bases de datos relacionales) es solo <strong>uno</strong> de varios tipos de bases de datos. Cada tipo resuelve un problema distinto:

</div>

<div class="grid grid-cols-3 gap-3">
  <div class="border-2 border-black bg-[#2DD4BF]/15 p-3 text-center text-sm">
    <strong>Relacional (SQL)</strong>
    <p class="text-xs mt-1">Tablas con filas y columnas. Para transacciones y datos estructurados.</p>
    <p class="text-xs italic">MySQL, PostgreSQL, SQL Server</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <strong>Documento</strong>
    <p class="text-xs mt-1">Almacena documentos JSON flexibles. Sin esquema fijo.</p>
    <p class="text-xs italic">MongoDB, CouchDB</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <strong>Clave-Valor</strong>
    <p class="text-xs mt-1">Como un diccionario gigante. Ultrarapido para lecturas simples.</p>
    <p class="text-xs italic">Redis, DynamoDB</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <strong>Grafo</strong>
    <p class="text-xs mt-1">Datos como redes: nodos y conexiones. Para relaciones complejas.</p>
    <p class="text-xs italic">Neo4j, Amazon Neptune</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-3 text-center text-sm">
    <strong>Motor de busqueda</strong>
    <p class="text-xs mt-1">Busqueda de texto rapida, con ranking y tolerancia a errores.</p>
    <p class="text-xs italic">Elasticsearch, Apache Solr</p>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-3 text-center text-sm">
    <strong>Vectorial</strong>
    <p class="text-xs mt-1">Busca por significado usando matematicas. Base de la IA moderna.</p>
    <p class="text-xs italic">ChromaDB, Pinecone</p>
  </div>
</div>

<RefFootnote :sources="['DB-Engines. (2026). DB-Engines ranking. https://db-engines.com/en/ranking']" />

---

<!-- Slide 19: What we'll cover today -->

# Hoy nos enfocamos en dos

<div class="pixel-divider my-3" />

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-6 text-center">
    <div class="i-pixelarticons-search inline-block w-10 h-10 mb-2" />
    <h2 class="text-[#ff6b6b]">Elasticsearch</h2>
    <div class="pixel-divider my-3" />
    <p class="text-sm">Busqueda de texto completo (full-text search). Rapido, con ranking, tolerante a errores.</p>
    <p class="text-sm mt-2 font-bold">Resuelve: el problema de buscar en texto no estructurado.</p>
  </div>
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-6 text-center">
    <div class="i-pixelarticons-ai-app-mac inline-block w-10 h-10 mb-2" />
    <h2 class="text-[#6c5ce7]">ChromaDB</h2>
    <div class="pixel-divider my-3" />
    <p class="text-sm">Busqueda semantica con vectores (embeddings). Entiende significado, no solo palabras.</p>
    <p class="text-sm mt-2 font-bold">Resuelve: buscar por conceptos e ideas, no solo texto exacto.</p>
  </div>
</div>

---
layout: neo-section
---

<!-- Slide 20: ES Section Divider -->

<div class="relative">
  <img src="/images/logos/elasticsearch.png" class="w-28 h-28 mx-auto -mt-24 relative z-20 drop-shadow-[3px_3px_0px_rgba(0,0,0,0.5)]" />
</div>

<h1 class="text-white text-6xl font-bold">Elasticsearch</h1>

<p class="text-[#2DD4BF] mt-6 text-xl font-mono">// busqueda de texto a la velocidad de Google</p>

<div class="mt-6">
  <TimerBadge time="60 min" />
</div>

---

<!-- Slide 21: What is ES -->

# ¿Que es Elasticsearch?

<div class="pixel-divider my-3" />

<div class="grid grid-cols-[2fr_1fr] gap-6 mt-4">
  <div class="space-y-3">
    <div class="border-2 border-black bg-white p-3">
      <strong>Motor de busqueda y analitica</strong> de codigo abierto (open source), creado en 2010 por Shay Banon.
    </div>
    <div class="border-2 border-black bg-white p-3">
      Nacio como un proyecto para que su esposa pudiera buscar recetas de cocina. Hoy lo usan Netflix, Wikipedia, Uber y miles de empresas.
    </div>
    <div class="border-2 border-black bg-white p-3">
      <strong>Elasticsearch ≠ base de datos relacional</strong>. Es un complemento especializado en busqueda de texto y analitica en tiempo real.
    </div>
  </div>
  <div class="space-y-3">
    <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
      <strong>Creado</strong><br/>2010
    </div>
    <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
      <strong>Licencia</strong><br/>Open source (SSPL)
    </div>
    <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
      <strong>Costo</strong><br/>Gratis local. Cloud desde $0 (trial)
    </div>
  </div>
</div>

<RefFootnote :sources="['Elastic NV. (2024). Elasticsearch reference (v8.x). https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html']" />

---

<!-- Slide 22: ES & OpenSearch -->

# Elasticsearch y OpenSearch

<div class="mt-6">

<div class="border-2 border-black bg-white p-4">

En 2021, **Amazon creo OpenSearch**: un fork (copia independiente) de Elasticsearch, porque no estaba de acuerdo con el cambio de licencia de Elastic.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4">
    <h3>Elasticsearch (Elastic NV)</h3>
    <p class="text-sm mt-1">Version original. La empresa Elastic la mantiene. Elastic Cloud es su servicio en la nube.</p>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-4">
    <h3>OpenSearch (AWS)</h3>
    <p class="text-sm mt-1">Fork mantenido por Amazon. Incluido en AWS. Misma API base, desarrollo independiente.</p>
  </div>
</div>

<div class="mt-4 text-center text-sm">

Para nuestro workshop usaremos <strong>Elastic Cloud</strong> (la version oficial), pero lo que aprendan aplica a ambos.

</div>

</div>

---

<!-- Slide 23: Who uses ES -->

# ¿Quien usa Elasticsearch en el mundo real?

<div class="pixel-divider my-3" />

<div class="grid grid-cols-2 gap-4 mt-3">
  <div class="border-2 border-[#ff6b6b] bg-white p-4">
    <h3 class="text-[#ff6b6b]">Netflix</h3>
    <p class="text-sm">Busqueda de contenido, monitoreo de servidores y analisis de errores en tiempo real para 200M+ suscriptores.</p>
    <p class="text-xs mt-1 text-gray-400 font-mono">elastic.co/customers/netflix</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-white p-4">
    <h3 class="text-[#ff6b6b]">Wikipedia</h3>
    <p class="text-sm">Potencia la busqueda en 300+ idiomas. Cada vez que buscas un articulo, Elasticsearch responde.</p>
    <p class="text-xs mt-1 text-gray-400 font-mono">mediawiki.org/wiki/Wikimedia_Search_Platform</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-white p-4">
    <h3 class="text-[#ff6b6b]">Uber</h3>
    <p class="text-sm">Monitoreo en tiempo real de millones de viajes. Detecta anomalias y problemas al instante.</p>
    <p class="text-xs mt-1 text-gray-400 font-mono">elastic.co/customers/uber</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-white p-4">
    <h3 class="text-[#ff6b6b]">GitHub</h3>
    <p class="text-sm">Cuando buscas codigo en GitHub, Elasticsearch busca en miles de millones de lineas de codigo.</p>
    <p class="text-xs mt-1 text-gray-400 font-mono">github.blog/engineering</p>
  </div>
</div>

<RefFootnote :sources="['Elastic. (2023). Customer stories. https://www.elastic.co/customers']" />

---

<!-- Slide 24: SQL vs ES terminology -->

# Si hablas SQL, ya casi hablas Elasticsearch

<div class="pixel-divider my-3" />

<div class="mt-2 text-sm mb-4">Los conceptos son similares, solo cambian los nombres:</div>

<div class="border-2 border-black bg-white p-0 overflow-hidden">

| SQL | Elasticsearch | Explicacion |
|-----|--------------|-------------|
| Base de datos (Database) | Indice (Index) | El contenedor de tus datos |
| Tabla (Table) | Tipo de mapeo (Mapping) | La estructura/esquema |
| Fila (Row) | Documento (Document) | Un registro individual, en JSON |
| Columna (Column) | Campo (Field) | Una propiedad del documento |
| `SELECT ... WHERE` | `GET index/_search { "query": ... }` | Buscar datos |

</div>

<v-click>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
<strong>La gran diferencia</strong>: en SQL escribes texto plano. En Elasticsearch escribes JSON. Pero la logica es la misma.
</div>

</v-click>

---

<!-- Slide 25: Inverted index - book analogy -->

# ¿Como busca tan rapido? El indice invertido

<div class="mt-2 text-sm">

Piensa en el <strong>indice al final de un libro de texto</strong>:

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <h4 class="mb-2"><div class="i-pixelarticons-book-open inline-block w-5 h-5 align-middle mr-1" /> Indice de un libro</h4>
    <div class="border-2 border-black bg-white p-3 text-sm font-mono">
      Elasticsearch ... pag. 12, 45, 89<br/>
      Indice invertido ... pag. 23, 45<br/>
      Tokenizacion ... pag. 34, 67<br/>
      BM25 ... pag. 56
    </div>
    <p class="text-xs mt-2">No lees todo el libro — vas directo a las paginas que necesitas.</p>
  </div>
  <div>
    <h4 class="mb-2"><div class="i-pixelarticons-server inline-block w-5 h-5 align-middle mr-1" /> Indice invertido de ES</h4>
    <div class="border-2 border-black bg-[#282A36] p-3 text-sm font-mono text-[#2DD4BF]">
      "comida" → Doc 1, 2, 3<br/>
      "mexicana" → Doc 1<br/>
      "deliciosa" → Doc 1<br/>
      "rapida" → Doc 2<br/>
      "italiana" → Doc 3
    </div>
    <p class="text-xs mt-2">Buscar "comida" → consulta el indice → resultado instantaneo.</p>
  </div>
</div>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-3 mt-4 text-center text-sm">
<strong>SQL lee documento por documento</strong> (como leer el libro entero). <strong>ES consulta su indice</strong> (como ir al indice del libro). Por eso ES es ordenes de magnitud mas rapido para busqueda de texto.
</div>

</v-click>

<RefFootnote :sources="['Gormley, C. & Tong, Z. (2015). Elasticsearch: The Definitive Guide. OReilly Media.']" />

---

<!-- Slide 26: How inverted index is built -->

# Asi se construye el indice invertido

<div class="mt-4">

<v-clicks>

<div class="grid grid-cols-3 gap-4">
  <div class="border-2 border-black p-3 text-sm">
    <h4 class="text-[#2DD4BF]">1. Documentos originales</h4>
    <p class="text-xs mt-1 font-mono">Doc 1: "La comida mexicana es deliciosa"</p>
    <p class="text-xs font-mono">Doc 2: "Comida rapida y economica"</p>
    <p class="text-xs font-mono">Doc 3: "Recetas de comida italiana"</p>
  </div>
  <div class="border-2 border-[#ff6b6b] p-3 text-sm">
    <h4 class="text-[#ff6b6b]">2. Tokenizar + normalizar</h4>
    <p class="text-xs mt-1">Separa en palabras, quita acentos, minusculas:</p>
    <p class="text-xs font-mono mt-1">"la" → eliminada (stop word)</p>
    <p class="text-xs font-mono">"comida" → "comida"</p>
    <p class="text-xs font-mono">"mexicana" → "mexican"</p>
    <p class="text-xs font-mono">"deliciosa" → "delic"</p>
  </div>
  <div class="border-2 border-[#2DD4BF] p-3 text-sm">
    <h4 class="text-[#2DD4BF]">3. Indice invertido</h4>
    <div class="text-xs mt-1 font-mono">
      comida → [1, 2, 3]<br/>
      mexican → [1]<br/>
      delic → [1]<br/>
      rapid → [2]<br/>
      econom → [2]<br/>
      italian → [3]
    </div>
  </div>
</div>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
Buscar "comida mexicana" → mapa dice Doc 1 tiene ambas → <strong>resultado en milisegundos</strong>. SQL leeria los 3 documentos completos caracter por caracter.
</div>

</v-clicks>

</div>

---

<!-- Slide 27: Ranking - BM25 -->

# Elasticsearch no solo encuentra — RANKEA

<div class="pixel-divider my-3" />

<div class="mt-2 text-sm">

Cuando buscas "comida mexicana" y hay 500 resultados, ¿cual te muestro primero? Elasticsearch usa un algoritmo llamado <strong>BM25</strong> que asigna un puntaje (_score) a cada resultado:

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <div class="text-2xl font-bold text-[#ff6b6b]">Frecuencia</div>
    <p class="text-xs mt-1">¿Cuantas veces aparece la palabra en el documento? Mas veces → mas relevante.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <div class="text-2xl font-bold text-[#ff6b6b]">Rareza</div>
    <p class="text-xs mt-1">Una palabra rara vale mas. "Elasticsearch" es mas informativa que "el" o "de".</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <div class="text-2xl font-bold text-[#ff6b6b]">Longitud</div>
    <p class="text-xs mt-1">Documentos cortos donde aparece la palabra son mas relevantes que documentos largos.</p>
  </div>
</div>

<div class="border-2 border-black bg-[#282A36] text-[#2DD4BF] p-3 mt-4 text-sm font-mono">
  "hits": [<br/>
  &nbsp;&nbsp;{ "_score": 15.7, "_source": { "texto": "Comida mexicana autentica..." } },<br/>
  &nbsp;&nbsp;{ "_score": 8.2, "_source": { "texto": "Recetas de comida del mundo..." } },<br/>
  &nbsp;&nbsp;{ "_score": 3.1, "_source": { "texto": "La comida en general..." } }<br/>
  ]
</div>

</v-clicks>

<RefFootnote :sources="['Elastic NV. (2024). Similarity module. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html']" />

---

<!-- Slide 28: Clusters concept -->

# Clusters: muchos servidores, un solo sistema

<div class="mt-4 text-sm">

Un <strong>cluster</strong> no es exclusivo de Elasticsearch — es un concepto general en computacion: multiples computadoras trabajando juntas como si fueran una sola.

</div>

<v-click>

<div class="flex flex-col items-center mt-4 gap-3">
  <div class="border-2 border-black bg-[#2DD4BF]/15 p-3 text-center font-bold">
    Cluster (grupo de servidores)
  </div>
  <div class="text-xl">↓</div>
  <div class="flex gap-4">
    <div class="border-2 border-black p-3 text-center text-sm">Nodo 1<br/><span class="text-xs font-mono">Servidor A</span></div>
    <div class="border-2 border-black p-3 text-center text-sm">Nodo 2<br/><span class="text-xs font-mono">Servidor B</span></div>
    <div class="border-2 border-black p-3 text-center text-sm">Nodo 3<br/><span class="text-xs font-mono">Servidor C</span></div>
  </div>
</div>

</v-click>

<v-click>

<div class="border-2 border-black bg-white p-3 mt-4 text-sm">

**¿Por que importa?** Netflix tiene millones de documentos. Un solo servidor no alcanza. Con clusters, distribuyes los datos en pedazos (shards) y si un servidor falla, otro tiene una copia (replica). Elastic Cloud maneja todo esto automaticamente — tu solo usas la interfaz.

</div>

</v-click>

---
layout: neo-demo
---

<!-- Slide 29: Lab - Elastic Cloud Setup -->

::title::

<h2 class="text-[#2DD4BF] font-mono">$ lab: Registrarnos en Elastic Cloud</h2>

::default::

<div class="text-[#F8F8F2]">

### Vamos a hacerlo juntos:

1. Abrir **elastic.co/cloud** → "Start free trial"
2. Registrarse con email y password
3. **Create deployment** → Seleccionar region
4. Esperar ~2 minutos → **Guardar** las credenciales
5. Abrir **Kibana** desde el panel

<div class="mt-4 border-2 border-black p-3 text-sm">

**Importante**: Guarden el password del usuario `elastic` que se genera automaticamente. Lo necesitan para todo lo demas.

</div>

<div class="mt-2 border-2 border-black p-3 text-sm">

**Trial gratuito**: 14 dias, sin tarjeta de credito. Suficiente para este workshop y los labs.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 30: Lab - Load sample data -->

::title::

<h2 class="text-[#2DD4BF] font-mono">$ lab: Cargar datos de muestra</h2>

::default::

<div class="text-[#F8F8F2]">

### En Kibana:

1. **Home** → "Try sample data"
2. Clic en **"Add data"** en **"Sample eCommerce orders"**
3. Listo: **10,000+ ordenes** de una tienda online

**Incluye**: productos, categorias, precios, clientes, fechas, ubicaciones

### Explorar el dashboard:

4. Clic en **"View data"** → **"Dashboard"**
5. Observen: mapas, graficas de ventas, top productos...

<div class="mt-3 border-2 border-black p-3 text-sm">

Todo esto se construyo <strong>sin codigo</strong>. Kibana + Elasticsearch generan dashboards interactivos listos para BI.

</div>

</div>

---
layout: neo-demo
---

<!-- Slide 31: Lab - Dev Tools -->

::title::

<h2 class="text-[#2DD4BF] font-mono">$ lab: Dev Tools — tu consola de Elasticsearch</h2>

::default::

<div class="text-[#F8F8F2]">

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

<!-- Slide 32: Things SQL can't do - live -->

# Cosas que SQL no puede hacer — y ES si

<div class="mt-4 text-sm">

Ahora que tenemos datos, veamos lo que hace a Elasticsearch especial:

</div>

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="border-2 border-black bg-white p-3">
    <strong>1. Busqueda con errores tipograficos (fuzziness)</strong> — buscar "shoees" y encontrar "shoes"
  </div>
  <div class="border-2 border-black bg-white p-3">
    <strong>2. Ranking por relevancia</strong> — ¿que producto es MAS relevante para "comfortable running shoes"?
  </div>
  <div class="border-2 border-black bg-white p-3">
    <strong>3. Resaltado (highlighting)</strong> — mostrar DONDE en el texto se encontro la coincidencia
  </div>
  <div class="border-2 border-black bg-white p-3">
    <strong>4. Busqueda en multiples campos</strong> — buscar en nombre, descripcion y categoria al mismo tiempo
  </div>
  <div class="border-2 border-black bg-white p-3">
    <strong>5. Combinaciones complejas</strong> — "DEBE contener esto, NO debe contener aquello, BONUS si tiene esto otro"
  </div>
</div>

</v-clicks>

---
layout: neo-demo
---

<!-- Slide 33: Fuzziness demo -->

::title::

<h2 class="text-[#2DD4BF] font-mono">$ demo: Escribiste mal? No importa</h2>

::default::

<div class="text-[#F8F8F2]">

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
  <div class="border-2 border-[#ff6b6b]/50 p-3">
    <strong>SQL</strong>: <code>LIKE '%shoees%'</code> → <strong>0 resultados</strong>
  </div>
  <div class="border-2 border-[#2DD4BF]/50 p-3">
    <strong>ES</strong>: "shoees" → corrige a "shoes" → <strong>resultados encontrados</strong>
  </div>
</div>

**fuzziness: AUTO** = tolera 1-2 errores dependiendo de la longitud de la palabra. Es como el autocompletado de tu celular.

</div>

---
layout: neo-two-cols
---

<!-- Slide 34: SQL vs ES side by side -->

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

<!-- Slide 35: NLP parenthesis - intro -->

# ¿Como "entiende" texto Elasticsearch?

<div class="mt-4 text-sm">

Elasticsearch usa tecnicas de <strong>NLP</strong> (Procesamiento de Lenguaje Natural / Natural Language Processing) internamente:

</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4>Tokenizacion</h4>
    <p class="text-xs mt-1">"La comida es deliciosa" → ["la", "comida", "es", "deliciosa"]. Separa texto en palabras individuales.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4>Normalizacion</h4>
    <p class="text-xs mt-1">"Deliciosa" → "deliciosa". Convierte a minusculas, quita acentos para uniformar.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4>Stemming (raices)</h4>
    <p class="text-xs mt-1">"corriendo", "corrio", "correr" → todos se reducen a "corr". Asi "correr" encuentra "corriendo".</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4>Stop words</h4>
    <p class="text-xs mt-1">Ignora palabras sin significado propio: "el", "la", "de", "un". Se enfoca en palabras que importan.</p>
  </div>
</div>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
Todo esto pasa <strong>automaticamente</strong>. Tu solo escribes la busqueda y Elasticsearch aplica estos pasos.
</div>

---

<!-- Slide 36: NLP history → embeddings → LLMs -->

# De NLP a LLMs: una breve historia

<div class="mt-4 text-sm">

Las tecnicas que usa Elasticsearch son el <strong>primer nivel</strong> de NLP. Pero hay mucho mas:

</div>

<v-clicks>

<div class="flex items-center gap-3 mt-6">
  <div class="border-2 border-black p-3 text-center text-sm flex-1">
    <div class="font-bold text-[#ff6b6b]">1960s-90s</div>
    <strong>Reglas</strong>
    <p class="text-xs mt-1">Diccionarios, gramatica manual. Fragil y limitado.</p>
  </div>
  <div class="text-xl">→</div>
  <div class="border-2 border-black p-3 text-center text-sm flex-1">
    <div class="font-bold text-[#ff6b6b]">2000s</div>
    <strong>Estadistico</strong>
    <p class="text-xs mt-1">Probabilidades de palabras. Mejor, pero sin "entender".</p>
  </div>
  <div class="text-xl">→</div>
  <div class="border-2 border-[#2DD4BF] p-3 text-center text-sm flex-1">
    <div class="font-bold text-[#2DD4BF]">2013</div>
    <strong>Word2Vec</strong>
    <p class="text-xs mt-1">Palabras como vectores. Primer "significado" numerico.</p>
  </div>
  <div class="text-xl">→</div>
  <div class="border-2 border-[#6c5ce7] p-3 text-center text-sm flex-1">
    <div class="font-bold text-[#6c5ce7]">2017+</div>
    <strong>Transformers</strong>
    <p class="text-xs mt-1">Atencion. GPT, BERT, Claude. La revolucion actual.</p>
  </div>
</div>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 mt-6 text-center">
<strong>Los embeddings (Word2Vec → Transformers) son la base de todo.</strong><br/>
ChromaDB usa exactamente esta tecnologia. Lo que alimenta a ChatGPT, tu lo puedes usar en tu base de datos.
</div>

</v-clicks>

<RefFootnote :sources="['Vaswani, A., et al. (2017). Attention is all you need. NeurIPS, 30.']" />

---

<!-- Slide 37: ES capabilities panorama -->

# Panorama rapido: ¿que mas puede hacer ES?

<div class="pixel-divider my-3" />

<div class="grid grid-cols-3 gap-3 mt-3">
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4 class="text-[#ff6b6b]">Agregaciones</h4>
    <p class="text-xs">Como GROUP BY pero mas poderoso. Conteos, promedios, percentiles — todo en una query.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4 class="text-[#ff6b6b]">Histogramas</h4>
    <p class="text-xs">Agrupar datos por rangos automaticamente: ventas por precio, pedidos por hora.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4 class="text-[#ff6b6b]">Buckets</h4>
    <p class="text-xs">Agrupar documentos en "cubetas" por cualquier campo: pais, categoria, fecha.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4 class="text-[#ff6b6b]">Highlighting</h4>
    <p class="text-xs">Resalta exactamente donde en el texto se encontro tu busqueda.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4 class="text-[#ff6b6b]">Sugerencias</h4>
    <p class="text-xs">Auto-completar y "quiso decir..." como los buscadores web.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <h4 class="text-[#ff6b6b]">Geo-busquedas</h4>
    <p class="text-xs">Buscar por ubicacion: "restaurantes a 5km de aqui".</p>
  </div>
</div>

<div class="text-center mt-4 text-sm">
Todo esto lo pueden explorar en los labs despues del workshop.
</div>

---

<!-- Slide 38: When NOT to use ES -->

# Cuando NO usar Elasticsearch

<div class="pixel-divider my-3" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4 text-center">
    <div class="i-pixelarticons-close-box inline-block w-8 h-8 mb-2 text-[#ff6b6b]" />
    <strong>Transacciones</strong>
    <p class="text-sm mt-1">No es ACID. Nunca para transferencias bancarias o inventario critico.</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4 text-center">
    <div class="i-pixelarticons-close-box inline-block w-8 h-8 mb-2 text-[#ff6b6b]" />
    <strong>Base de datos principal</strong>
    <p class="text-sm mt-1">Usalo como complemento de PostgreSQL/MySQL, nunca como reemplazo.</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4 text-center">
    <div class="i-pixelarticons-close-box inline-block w-8 h-8 mb-2 text-[#ff6b6b]" />
    <strong>JOINs complejos</strong>
    <p class="text-sm mt-1">ES no normaliza datos como SQL. Sus documentos son "aplanados" — cada uno es independiente.</p>
  </div>
</div>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 mt-6 text-center">
<strong>Elasticsearch es un complemento, no un reemplazo de SQL.</strong>
<br/>En las empresas, se usan juntos: SQL para la operacion, ES para la busqueda y analitica.
</div>

</v-click>

---

<!-- Slide 39: ES References -->

# Referencias — Seccion Elasticsearch

<div class="text-xs mt-4 space-y-2 font-mono">

- Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM, 13*(6), 377-387. https://doi.org/10.1145/362384.362685

- Elastic NV. (2024). *Elasticsearch reference* (v8.x). https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

- Elastic NV. (2024). *Similarity module*. https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html

- Gormley, C., & Tong, Z. (2015). *Elasticsearch: The Definitive Guide*. O'Reilly Media.

- DB-Engines. (2026). *DB-Engines ranking*. https://db-engines.com/en/ranking

- Elastic. (2023). *Customer stories*. https://www.elastic.co/customers

- McKinsey & Company. (2024). *The state of AI in 2024*. McKinsey Global Institute.

- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS, 30*.

</div>

---
layout: neo-section
---

<!-- Slide 40: Pause -->

<h1 class="text-white text-5xl font-bold">Pausa: 5 minutos</h1>

<div class="i-pixelarticons-coffee inline-block w-16 h-16 mt-6 text-[#2DD4BF]" />

<p class="text-[#2DD4BF] mt-6 text-xl font-mono">// estiren las piernas. tomen agua.</p>

<div class="mt-6 border-2 border-[#2DD4BF]/30 p-4 max-w-md mx-auto">
<p class="text-white text-lg text-center">Lo que sigue es la parte que les va a volar la cabeza.</p>
</div>

---
layout: neo-section
---

<!-- Slide 41: ChromaDB Section Divider -->

<div class="relative">
  <img src="/images/logos/chroma.png" class="w-28 h-28 mx-auto -mt-24 relative z-20 drop-shadow-[3px_3px_0px_rgba(0,0,0,0.5)]" />
</div>

<h1 class="text-white text-6xl font-bold">ChromaDB</h1>

<p class="text-[#2DD4BF] mt-6 text-xl font-mono">// busqueda por significado, no por palabras</p>

<div class="mt-6">
  <TimerBadge time="30 min" />
</div>

---

<!-- Slide 42: The problem ES doesn't solve -->

# El problema que ni Elasticsearch resuelve

<div class="grid grid-cols-[2fr_1fr] gap-6 mt-4">
  <div>

Elasticsearch es genial para buscar <strong>palabras</strong>. Pero... ¿que pasa cuando la respuesta no comparte palabras con la pregunta?

<v-clicks>

<div class="space-y-3 mt-4">
  <div class="border-2 border-black bg-white p-3 text-sm">
    <strong>Busqueda:</strong> "peliculas que me hagan sentir nostalgico"
    <div class="mt-2 grid grid-cols-2 gap-2">
      <div class="text-xs"><span class="text-[#ff6b6b] font-bold">SQL</span>: <div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle" /> "nostalgico" no aparece en las sinopsis</div>
      <div class="text-xs"><span class="text-[#2DD4BF] font-bold">Elasticsearch</span>: <div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle" /> busca la palabra "nostalgia" pero "Roma" evoca nostalgia sin decirlo</div>
    </div>
  </div>
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-4 text-center">
    <strong>Necesitamos algo que entienda el SIGNIFICADO detras de las palabras.</strong>
    <br/>Necesitamos que la maquina "lea entre lineas".
  </div>
</div>

</v-clicks>

  </div>
  <div class="flex items-center">
    <img src="/images/slides/slide_42_semantica.png" class="w-full border-2 border-black shadow-[2px_2px_0px_#000]" />
  </div>
</div>

---

<!-- Slide 43: Why embeddings matter -->

# Los embeddings estan en todas partes

<div class="pixel-divider my-3" />

<div class="mt-2 text-sm">

Los <strong>embeddings</strong> (representaciones vectoriales) son la tecnologia detras de:

</div>

<v-clicks>

<div class="grid grid-cols-2 gap-4 mt-3">
  <div class="border-2 border-[#6c5ce7] bg-white p-4">
    <h3 class="text-[#6c5ce7]"><div class="i-pixelarticons-ai-app-mac inline-block w-5 h-5 align-middle mr-1" /> ChatGPT, Claude, Gemini</h3>
    <p class="text-sm mt-1">Todos los modelos de IA modernos usan embeddings para entender lenguaje.</p>
  </div>
  <div class="border-2 border-[#6c5ce7] bg-white p-4">
    <h3 class="text-[#6c5ce7]"><div class="i-pixelarticons-play inline-block w-5 h-5 align-middle mr-1" /> Recomendaciones</h3>
    <p class="text-sm mt-1">"Si te gusto esta pelicula, te gustara esta otra" — Netflix, Spotify, Amazon.</p>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-white p-4">
    <h3 class="text-[#2DD4BF]"><div class="i-pixelarticons-text-search inline-block w-5 h-5 align-middle mr-1" /> Busqueda semantica</h3>
    <p class="text-sm mt-1">Google entiende que "como curar dolor de cabeza" y "remedios para cefalea" son la misma pregunta.</p>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-white p-4">
    <h3 class="text-[#2DD4BF]"><div class="i-pixelarticons-book inline-block w-5 h-5 align-middle mr-1" /> RAG (IA + tus datos)</h3>
    <p class="text-sm mt-1">Chatbots que responden usando la informacion de tu empresa, no inventando cosas.</p>
  </div>
</div>

</v-clicks>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-3 mt-4 text-center text-sm">
Entender embeddings es <strong>entender como funciona la IA moderna</strong>. Es la habilidad mas relevante que van a aprender hoy.
</div>

</v-click>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 44: Physical analogy -->

# Imagina un cuarto lleno de peliculas

<div class="grid grid-cols-[1fr_2fr] gap-6 mt-4">
  <div class="flex items-center">
    <img src="/images/slides/slide_44_peliculas.png" class="w-full border-2 border-black shadow-[2px_2px_0px_#000]" />
  </div>
  <div>

**Ejercicio mental**: Te doy 100 peliculas escritas en tarjetas. Tienes una mesa grande. ¿Como las organizarias para que peliculas **similares** queden **cerca** entre si?

<v-clicks>

<div class="grid grid-cols-4 gap-2 mt-3">
  <div class="border-2 border-black bg-[#2DD4BF]/15 p-2 text-center text-xs">
    <strong>Esquina 1</strong><br/>Comedias familiares
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-2 text-center text-xs">
    <strong>Esquina 2</strong><br/>Thrillers oscuros
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-2 text-center text-xs">
    <strong>Esquina 3</strong><br/>Dramas sociales
  </div>
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-2 text-center text-xs">
    <strong>Esquina 4</strong><br/>Ciencia ficcion
  </div>
</div>

<div class="border-2 border-black bg-white p-3 mt-3 text-center text-sm">

Tu cerebro acaba de hacer lo que hace un **embedding**: tomo cada pelicula, "entendio" de que trata, y le asigno una **posicion en el espacio** segun su significado.

Ahora imagina que la mesa es un plano con coordenadas (x, y). Cada pelicula tiene una posicion numerica. **Eso es un vector.**

</div>

</v-clicks>

  </div>
</div>

---

<!-- Slide 45: From analogy to math -->

# De la mesa a los numeros

<div class="grid grid-cols-2 gap-6 mt-6">
  <div>
    <h3>Texto → Vector (embedding)</h3>
    <div class="text-sm space-y-2 mt-3">
      <div class="border-2 border-black bg-[#282A36] text-[#2DD4BF] p-2 font-mono text-xs">"perro" → [0.2, 0.8, 0.1, ...]</div>
      <div class="border-2 border-black bg-[#282A36] text-[#2DD4BF] p-2 font-mono text-xs">"cachorro" → [0.21, 0.79, 0.12, ...]</div>
      <div class="border-2 border-black bg-[#282A36] text-[#2DD4BF] p-2 font-mono text-xs">"automovil" → [0.9, 0.1, 0.7, ...]</div>
    </div>
    <p class="text-sm mt-3">"perro" y "cachorro" tienen numeros <strong>muy parecidos</strong> → estan <strong>cerca</strong> en el espacio. "automovil" tiene numeros muy diferentes → esta <strong>lejos</strong>.</p>
  </div>
  <div class="flex items-center justify-center">
    <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-6 text-center">
      <div class="text-lg font-bold mb-3">Espacio de significado</div>
      <div class="text-sm text-left font-mono">
        <strong>[A]</strong> perro<br/>
        &nbsp;&nbsp;&nbsp;↕ <em>cerca</em><br/>
        <strong>[B]</strong> cachorro<br/>
        <br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↕ <em>lejos</em><br/>
        <br/>
        <strong>[C]</strong> automovil
      </div>
    </div>
  </div>
</div>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 46: The classic analogy -->

# El ejemplo clasico que demuestra que funciona

<div class="grid grid-cols-[2fr_1fr] gap-6 mt-4">
  <div>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-6 text-center text-2xl font-mono">
<strong>"rey" - "hombre" + "mujer" ≈ "reina"</strong>
</div>

<div class="mt-4 text-center text-sm">

Si restas las coordenadas de "hombre" a "rey" y sumas las de "mujer", llegas a un punto en el espacio que esta muy cerca de "reina". Los embeddings capturan **relaciones y analogias** — no solo similitud de palabras.

</div>

<v-click>

<div class="grid grid-cols-2 gap-3 mt-4">
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <h4>¿Quien calcula los embeddings?</h4>
    <p class="text-xs mt-1">Modelos de IA entrenados con miles de millones de textos. ChromaDB usa uno por defecto — tu no tienes que hacer nada.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center text-sm">
    <h4>¿Que es la "distancia"?</h4>
    <p class="text-xs mt-1">Se mide el angulo entre dos vectores (similitud coseno). Angulo chico = similares. ChromaDB calcula esto automaticamente.</p>
  </div>
</div>

</v-click>

  </div>
  <div class="flex items-center">
    <img src="/images/slides/slide_46_rey_reina.png" class="w-full border-2 border-black shadow-[2px_2px_0px_#000]" />
  </div>
</div>

<RefFootnote :sources="['Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. arXiv:1301.3781.']" />

---

<!-- Slide 47: What is a vector DB -->

# ¿Que es una base de datos vectorial?

<div class="mt-4 text-sm">

Si los embeddings son las "coordenadas de significado" de un texto, necesitamos un lugar para <strong>guardarlos</strong> y <strong>buscar en ellos</strong> eficientemente. Eso es una base de datos vectorial.

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-4 text-center">
    <div class="i-pixelarticons-database inline-block w-8 h-8 mb-2" />
    <strong>Guarda vectores</strong>
    <p class="text-xs mt-1">Los numeros que representan el significado de cada documento.</p>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-4 text-center">
    <div class="i-pixelarticons-search inline-block w-8 h-8 mb-2" />
    <strong>Busca por cercania</strong>
    <p class="text-xs mt-1">"Dame los 5 documentos cuyo significado sea mas cercano a esta pregunta."</p>
  </div>
  <div class="border-2 border-black bg-[#2DD4BF]/15 p-4 text-center">
    <div class="i-pixelarticons-file-text inline-block w-8 h-8 mb-2" />
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

<!-- Slide 48: ChromaDB intro -->

# ChromaDB: busqueda semantica en 5 lineas de Python

<div class="pixel-divider my-3" />

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="space-y-3">
    <div class="border-2 border-black bg-white p-3 text-sm">
      <strong>Open source</strong> — codigo abierto, licencia Apache 2.0. Gratis.
    </div>
    <div class="border-2 border-black bg-white p-3 text-sm">
      <strong>Python-first</strong> — <code>pip install chromadb</code> y listo.
    </div>
    <div class="border-2 border-black bg-white p-3 text-sm">
      <strong>Auto-embed</strong> — genera los vectores automaticamente, sin configuracion.
    </div>
    <div class="border-2 border-black bg-white p-3 text-sm">
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

<!-- Slide 49: Predict then reveal -->

# Predice: ¿que resultados devolvera?

<div class="mt-2 text-sm">Coleccion con 5 documentos: comida mexicana, IA en negocios, Python para datos, burritos deliciosos, machine learning.</div>

<v-clicks>

<div class="space-y-4 mt-4">
  <div class="border-2 border-black bg-white p-4">
    <strong>Query 1:</strong> "tacos"
    <div class="text-sm text-[#ff6b6b] font-bold mt-1">→ "comida mexicana" y "burritos" — palabras diferentes, mismo concepto</div>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <strong>Query 2:</strong> "inteligencia artificial"
    <div class="text-sm text-[#2DD4BF] font-bold mt-1">→ "IA en negocios" y "machine learning" — entiende sinonimos y conceptos relacionados</div>
  </div>
  <div class="border-2 border-black bg-[#2DD4BF]/15 p-4">
    <strong>Query 3:</strong> "analisis de informacion"
    <div class="text-sm text-[#6c5ce7] font-bold mt-1">→ "Python para datos" — la conexion es conceptual, no hay palabras en comun</div>
  </div>
</div>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
<strong>Los embeddings entienden CONCEPTOS, no solo palabras.</strong> Esa es la diferencia entre busqueda de texto (Elasticsearch) y busqueda semantica (ChromaDB).
</div>

</v-clicks>

---

<!-- Slide 50: RAG intro -->

# RAG: IA que responde desde TUS datos

<div class="mt-4 text-sm">

El gran problema de ChatGPT: a veces **inventa** respuestas (alucina). ¿La solucion? Darle tus datos como contexto antes de responder. Eso es **RAG** (Retrieval-Augmented Generation):

</div>

<v-click>

<div class="flex items-center justify-center gap-2 mt-6">
  <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
    <div class="i-pixelarticons-chat inline-block w-6 h-6" />
    <strong>Pregunta</strong>
  </div>
  <div class="text-2xl font-bold">→</div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-3 text-center text-sm">
    <div class="i-pixelarticons-search inline-block w-6 h-6" />
    <strong>ChromaDB busca</strong>
    <p class="text-xs">contexto relevante</p>
  </div>
  <div class="text-2xl font-bold">→</div>
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-3 text-center text-sm">
    <div class="i-pixelarticons-ai-app-mac inline-block w-6 h-6" />
    <strong>LLM genera</strong>
    <p class="text-xs">respuesta con contexto</p>
  </div>
  <div class="text-2xl font-bold">→</div>
  <div class="border-2 border-black bg-[#2DD4BF]/25 p-3 text-center text-sm">
    <div class="i-pixelarticons-check inline-block w-6 h-6 text-[#2DD4BF]" />
    <strong>Respuesta</strong>
    <p class="text-xs">fundamentada</p>
  </div>
</div>

</v-click>

<v-click>

<div class="border-2 border-black bg-white p-4 mt-4 text-center">
<strong>La IA no hallucina porque responde desde TUS datos</strong>, no desde su entrenamiento general. Es como darle un libro de texto al estudiante antes del examen.
</div>

</v-click>

<RefFootnote :sources="['Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS, 33, 9459-9474.']" />

---
layout: neo-demo
---

<!-- Slide 51: Career Coach RAG Demo -->

::title::

<h2 class="text-[#2DD4BF] font-mono">$ demo: Tu coach de carrera con IA</h2>

::default::

<div class="text-[#F8F8F2]">

### AI Career Coach para estudiantes de BI

Un chatbot que responde preguntas sobre carreras en datos usando **40+ ofertas de trabajo reales** de empresas en Mexico.

**Stack**: ChromaDB (busqueda) + together.ai (LLM) + Gradio (interfaz)

### Prueben estas preguntas:

- *"¿Que habilidades necesito para Data Analyst en consulting?"*
- *"¿Que empresas en Monterrey buscan egresados de BI?"*
- *"Se Python, SQL y Tableau — ¿para que puestos califico?"*
- *"¿Que tecnologias deberia aprender este semestre?"*

<div class="mt-2 border-2 border-black p-2 text-sm">
Cada respuesta muestra las <strong>fuentes</strong>: las ofertas de trabajo reales en las que se basa. Eso es RAG en accion.
</div>

</div>

---

<!-- Slide 52: Chroma References -->

# Referencias — Seccion ChromaDB y RAG

<div class="text-xs mt-4 space-y-2 font-mono">

- Chroma. (2024). *Chroma documentation*. https://docs.trychroma.com/

- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS, 33*, 9459-9474. https://arxiv.org/abs/2005.11401

- Mikolov, T., et al. (2013). Efficient estimation of word representations in vector space. *arXiv:1301.3781*. https://arxiv.org/abs/1301.3781

- Pan, J. W., et al. (2024). A survey on vector database. *arXiv:2310.11703*. https://arxiv.org/abs/2310.11703

- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS, 30*. https://arxiv.org/abs/1706.03762

</div>

---
layout: neo-section
---

<!-- Slide 53: Closing section -->

<h1 class="text-[#2DD4BF] text-4xl font-bold">La herramienta correcta para la pregunta correcta</h1>

<p class="text-[#2DD4BF] mt-6 font-mono">// decision framework</p>

<div class="mt-6">
  <TimerBadge time="15 min" />
</div>

---

<!-- Slide 54: Decision flowchart -->

# ¿Que herramienta uso?

<div class="pixel-divider my-3" />

<div class="mt-4">

<div class="flex flex-col items-center gap-3">
  <div class="border-2 border-black bg-[#282A36] text-white p-3 text-center font-bold text-lg">
    ¿Que tipo de datos tienes?
  </div>
  <div class="flex gap-12 mt-2">
    <div class="flex flex-col items-center gap-2">
      <div class="text-sm font-bold">↓ Estructurados</div>
      <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
        ¿Necesitas transacciones?
      </div>
      <div class="text-sm font-bold">↓ Si</div>
      <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/25 p-3 text-center font-bold text-sm">
        SQL <div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle" />
      </div>
    </div>
    <div class="flex flex-col items-center gap-2">
      <div class="text-sm font-bold">↓ Texto libre</div>
      <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
        ¿Busqueda por palabras?
      </div>
      <div class="text-sm font-bold">↓ Si</div>
      <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/25 p-3 text-center font-bold text-sm">
        Elasticsearch <div class="i-pixelarticons-check inline-block w-4 h-4 text-[#ff6b6b] align-middle" />
      </div>
    </div>
    <div class="flex flex-col items-center gap-2">
      <div class="text-sm font-bold">↓ Significado/conceptos</div>
      <div class="border-2 border-black bg-[#C0C0C0] p-3 text-center text-sm">
        ¿Busqueda semantica / IA?
      </div>
      <div class="text-sm font-bold">↓ Si</div>
      <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/25 p-3 text-center font-bold text-sm">
        Vector DB <div class="i-pixelarticons-check inline-block w-4 h-4 text-[#6c5ce7] align-middle" />
      </div>
    </div>
  </div>
</div>

</div>

<v-click>

<div class="border-2 border-black bg-white p-3 mt-4 text-center text-sm">
<strong>En la practica, las empresas usan los tres juntos.</strong> SQL para la operacion, ES para busqueda, Vector DB para IA.
</div>

</v-click>

---

<!-- Slide 55: Comparison table -->

# SQL vs Elasticsearch vs ChromaDB

<div class="pixel-divider my-3" />

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

---

<!-- Slide 56: Your new superpower -->

# Tu nuevo superpoder empieza ahora

<div class="pixel-divider my-3" />

<div class="mt-4">

<div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/20 p-6">

### Ofertas de empleo reales que ya piden estas habilidades:

<!-- TODO: Reemplazar con vacantes reales verificadas -->
- *"Data Engineer — **Elasticsearch**, Kafka, Python"*
- *"BI Developer — SQL, **vector databases**, LLM integration"*
- *"AI Engineer — **RAG pipelines**, ChromaDB/Pinecone"*
- *"Data Scientist — NLP, **embeddings**, search systems"*

</div>

<div class="border-2 border-black bg-[#282A36] text-white p-4 mt-4 text-center text-lg">
<strong>Ahora saben que es esto. La mayoria de profesionales con experiencia no.</strong>
</div>

</div>

---

<!-- Slide 57: Keep practicing -->

# Sigue practicando

<div class="pixel-divider my-3" />

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="border-2 border-black bg-white p-4">
    <h3>Labs en este repo</h3>
    <ul class="text-sm mt-2 space-y-1">
      <li>Lab 1: Elasticsearch Basics (~30 min)</li>
      <li>Lab 2: ES Search avanzado (~45 min)</li>
      <li>Lab 3: ChromaDB y embeddings (~30 min)</li>
      <li>Lab 4: Construye un mini RAG (~45 min)</li>
    </ul>
  </div>
  <div class="border-2 border-black bg-white p-4">
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

<!-- Slide 58: All references -->

# Referencias completas

<div class="text-xs mt-2 space-y-1 font-mono">

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
- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS, 30*.

</div>

<div class="mt-2 text-center text-xs font-mono">
Lista completa con hyperlinks: <code>references/apa7.md</code> en el repositorio
</div>

---
layout: neo-cover
---

<!-- Slide 59: Closing -->

# Gracias!

<div class="pixel-divider my-4" />

<div class="text-lg mb-4 font-mono">#MasAlladeSQL</div>

<div class="text-sm">
Comparte lo que construiste hoy
</div>

<div class="flex gap-4 justify-center items-center mt-6">
  <span class="neo-tag bg-coral text-white">github.com/HesusG/mas-alla-de-sql</span>
</div>
