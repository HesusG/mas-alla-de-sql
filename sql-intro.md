---
theme: default
title: "Introduccion a SQL"
info: "Lo esencial antes del taller"
author: ""
keywords: sql,databases,intro,workshop,pre-work
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

# Introduccion a SQL

## Lo esencial antes del taller

<div class="pixel-divider my-6" />

<div class="flex gap-4 justify-center items-center mt-4">
  <span class="neo-tag bg-coral text-white">ITESM</span>
  <span class="neo-tag bg-sky text-white">Pre-work</span>
  <span class="neo-tag bg-grape text-white">~15 min</span>
</div>

<div class="mt-4 text-sm opacity-50 font-mono">
github.com/HesusG/mas-alla-de-sql
</div>

---

<!-- Slide 2: What is a database -->

# ¿Que es una base de datos?

<div class="pixel-divider my-4" />

<div class="grid grid-cols-[1fr_2fr] gap-6 mt-4">
  <div class="border-2 border-black bg-[#2DD4BF]/15 p-6 text-center">
    <div class="i-pixelarticons-database inline-block w-12 h-12 mb-2" />
    <div class="text-lg font-bold">Excel con superpoderes</div>
  </div>
  <div>

Una base de datos es un sistema para **almacenar, organizar y consultar** informacion de forma eficiente.

<v-clicks>
<div class="space-y-3 mt-4">
  <div class="border-2 border-black bg-white p-3 text-sm">
    <div class="i-pixelarticons-list-box inline-block w-5 h-5 align-middle mr-1" /> Organiza datos en <strong>tablas</strong> (como hojas de calculo)
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <div class="i-pixelarticons-users inline-block w-5 h-5 align-middle mr-1" /> Permite que <strong>muchas personas</strong> accedan al mismo tiempo
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <div class="i-pixelarticons-speed-fast inline-block w-5 h-5 align-middle mr-1" /> Maneja <strong>millones de filas</strong> sin sudar
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <div class="i-pixelarticons-lock inline-block w-5 h-5 align-middle mr-1" /> Protege tus datos con <strong>permisos y respaldos</strong>
  </div>
</div>
</v-clicks>

  </div>
</div>

---

<!-- Slide 3: CSV vs Excel vs DB -->

# CSV, Excel y bases de datos

<div class="pixel-divider my-4" />

<div class="grid grid-cols-3 gap-4 mt-6">
<v-clicks>
  <div class="border-2 border-black bg-[#C0C0C0] p-4 text-center">
    <div class="i-pixelarticons-file-text inline-block w-8 h-8 mb-2" />
    <h3>CSV</h3>
    <div class="pixel-divider my-2" />
    <div class="text-sm text-left space-y-1 mt-2">
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Texto plano, simple</div>
      <div><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /> Sin tipos de datos</div>
      <div><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /> Sin relaciones</div>
      <div><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /> Un usuario a la vez</div>
    </div>
  </div>
  <div class="border-2 border-black bg-[#C0C0C0] p-4 text-center">
    <div class="i-pixelarticons-chart inline-block w-8 h-8 mb-2" />
    <h3>Excel</h3>
    <div class="pixel-divider my-2" />
    <div class="text-sm text-left space-y-1 mt-2">
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Visual, formulas</div>
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Bueno hasta ~100K filas</div>
      <div><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /> Se pone lento con muchos datos</div>
      <div><div class="i-pixelarticons-close-box inline-block w-4 h-4 text-[#ff6b6b] align-middle mr-1" /> Dificil compartir</div>
    </div>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-4 text-center">
    <div class="i-pixelarticons-database inline-block w-8 h-8 mb-2" />
    <h3>Base de datos</h3>
    <div class="pixel-divider my-2" />
    <div class="text-sm text-left space-y-1 mt-2">
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Estructurada y tipada</div>
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Millones de filas</div>
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Multi-usuario</div>
      <div><div class="i-pixelarticons-check inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" /> Relaciones entre tablas</div>
    </div>
  </div>
</v-clicks>
</div>

---

<!-- Slide 4: Most popular databases -->

# ¿Cuales son las mas populares?

<div class="pixel-divider my-4" />

<div class="grid grid-cols-5 gap-3 mt-6">
<v-clicks>
  <div class="border-2 border-black bg-white p-3 text-center">
    <div class="text-2xl mb-1">🐬</div>
    <strong class="text-sm">MySQL</strong>
    <p class="text-xs mt-1">La mas popular del mundo. Gratis.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center">
    <div class="text-2xl mb-1">🐘</div>
    <strong class="text-sm">PostgreSQL</strong>
    <p class="text-xs mt-1">La favorita de los desarrolladores.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center">
    <div class="text-2xl mb-1">🏢</div>
    <strong class="text-sm">SQL Server</strong>
    <p class="text-xs mt-1">Microsoft. Comun en empresas grandes.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center">
    <div class="text-2xl mb-1">🏛️</div>
    <strong class="text-sm">Oracle</strong>
    <p class="text-xs mt-1">Bancos, gobiernos, corporativos.</p>
  </div>
  <div class="border-2 border-black bg-white p-3 text-center">
    <div class="text-2xl mb-1">📱</div>
    <strong class="text-sm">SQLite</strong>
    <p class="text-xs mt-1">Dentro de tu celular y apps.</p>
  </div>
</v-clicks>
</div>

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 mt-6 text-center">
<strong>SQL es el lenguaje. Estas son los motores.</strong> Es como hablar español — puedes hablarlo en Mexico, España o Argentina. Mismo idioma, diferente "motor".
</div>

</v-click>

<RefFootnote :sources="['DB-Engines. (2026). DB-Engines ranking. https://db-engines.com/en/ranking']" />

---

<!-- Slide 5: Why SQL -->

# ¿Por que TODO el mundo usa SQL?

<div class="pixel-divider my-4" />

<div class="grid grid-cols-2 gap-4 mt-6">
<v-clicks>
  <div class="border-2 border-black bg-white p-4 text-center">
    <div class="i-pixelarticons-globe inline-block w-8 h-8 mb-2 text-[#2DD4BF]" />
    <h3 class="text-[#2DD4BF]">Universal</h3>
    <p class="text-sm mt-1">Funciona en MySQL, PostgreSQL, SQL Server, Oracle... Aprendes una vez, lo usas en todos.</p>
  </div>
  <div class="border-2 border-black bg-white p-4 text-center">
    <div class="i-pixelarticons-clock inline-block w-8 h-8 mb-2 text-[#2DD4BF]" />
    <h3 class="text-[#2DD4BF]">50+ años de historia</h3>
    <p class="text-sm mt-1">Creado en los 70s, sigue siendo el estandar. Ninguna tecnologia ha logrado reemplazarlo.</p>
  </div>
  <div class="border-2 border-black bg-white p-4 text-center">
    <div class="i-pixelarticons-shield inline-block w-8 h-8 mb-2 text-[#2DD4BF]" />
    <h3 class="text-[#2DD4BF]">Estandar ISO</h3>
    <p class="text-sm mt-1">Es un estandar internacional. No depende de una empresa — es de todos.</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4 text-center">
    <div class="i-pixelarticons-briefcase-search inline-block w-8 h-8 mb-2 text-[#ff6b6b]" />
    <h3 class="text-[#ff6b6b]">Requerido en TODOS los trabajos de datos</h3>
    <p class="text-sm mt-1">No hay puesto de datos que no pida SQL. Es el idioma minimo.</p>
  </div>
</v-clicks>
</div>

<RefFootnote :sources="['Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), 377-387.']" />

---

<!-- Slide 6: SQL in careers -->

# ¿Vas a usar SQL en tu carrera?

<div class="pixel-divider my-4" />

<div class="grid grid-cols-2 gap-4 mt-4">
<v-clicks>
  <div class="border-2 border-black bg-white p-4">
    <h3><div class="i-pixelarticons-chart inline-block w-5 h-5 align-middle mr-1" /> Data Analyst</h3>
    <p class="text-sm mt-1">Consultas diarias, reportes, dashboards. <strong class="text-[#2DD4BF]">SQL</strong> es tu herramienta #1.</p>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <h3><div class="i-pixelarticons-tool-case inline-block w-5 h-5 align-middle mr-1" /> Data Engineer</h3>
    <p class="text-sm mt-1">Diseñar pipelines y bases de datos. <strong class="text-[#2DD4BF]">SQL</strong> avanzado + Python.</p>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <h3><div class="i-pixelarticons-ai-app-mac inline-block w-5 h-5 align-middle mr-1" /> Data Scientist</h3>
    <p class="text-sm mt-1">Extraer datos para modelos de ML. <strong class="text-[#2DD4BF]">SQL</strong> + Python + estadistica.</p>
  </div>
  <div class="border-2 border-black bg-white p-4">
    <h3><div class="i-pixelarticons-briefcase-search inline-block w-5 h-5 align-middle mr-1" /> BI Developer</h3>
    <p class="text-sm mt-1">Conectar datos a Tableau, Power BI. <strong class="text-[#2DD4BF]">SQL</strong> para alimentar todo.</p>
  </div>
</v-clicks>
</div>

<v-click>

<div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-4 mt-4 text-center text-lg">
<strong>SQL aparece en el 90%+ de las ofertas de empleo en datos.</strong> No es opcional.
</div>

</v-click>

---

<!-- Slide 7: Anatomy of a table -->

# Anatomia de una tabla

<div class="pixel-divider my-4" />

<div class="border-2 border-black bg-white p-0 overflow-hidden mt-6">
  <table class="w-full mac-table">
    <tr>
      <th class="text-left p-2 font-bold text-sm">id</th>
      <th class="text-left p-2 font-bold text-sm">nombre</th>
      <th class="text-left p-2 font-bold text-sm">precio</th>
      <th class="text-left p-2 font-bold text-sm">categoria</th>
    </tr>
    <tr>
      <td class="p-2 text-sm">1</td>
      <td class="p-2 text-sm">Laptop HP</td>
      <td class="p-2 text-sm">15000</td>
      <td class="p-2 text-sm">Electronica</td>
    </tr>
    <tr>
      <td class="p-2 text-sm">2</td>
      <td class="p-2 text-sm">Mouse Logitech</td>
      <td class="p-2 text-sm">350</td>
      <td class="p-2 text-sm">Accesorios</td>
    </tr>
    <tr>
      <td class="p-2 text-sm">3</td>
      <td class="p-2 text-sm">Monitor Samsung</td>
      <td class="p-2 text-sm">5200</td>
      <td class="p-2 text-sm">Electronica</td>
    </tr>
    <tr>
      <td class="p-2 text-sm">4</td>
      <td class="p-2 text-sm">Teclado mecanico</td>
      <td class="p-2 text-sm">1200</td>
      <td class="p-2 text-sm">Accesorios</td>
    </tr>
  </table>
</div>

<div class="grid grid-cols-3 gap-4 mt-4">
<v-clicks>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-3 text-center">
    <strong>Tabla</strong>
    <p class="text-xs mt-1">El contenedor: "productos"</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-3 text-center">
    <strong>Fila (Row)</strong>
    <p class="text-xs mt-1">Un registro: un producto</p>
  </div>
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/15 p-3 text-center">
    <strong>Columna (Column)</strong>
    <p class="text-xs mt-1">Una propiedad: nombre, precio...</p>
  </div>
</v-clicks>
</div>

---

<!-- Slide 8: SELECT -->

# Tu primera consulta: SELECT

<div class="pixel-divider my-4" />

<div class="grid grid-cols-[1fr_1fr] gap-6 mt-4">
  <div>

<v-click>

```sql
SELECT nombre, precio FROM productos;
```

</v-click>

<v-click>

<div class="border-2 border-black bg-white p-0 overflow-hidden mt-4">
  <table class="w-full mac-table">
    <tr>
      <th class="text-left p-2 font-bold text-sm">nombre</th>
      <th class="text-left p-2 font-bold text-sm">precio</th>
    </tr>
    <tr><td class="p-2 text-sm">Laptop HP</td><td class="p-2 text-sm">15000</td></tr>
    <tr><td class="p-2 text-sm">Mouse Logitech</td><td class="p-2 text-sm">350</td></tr>
    <tr><td class="p-2 text-sm">Monitor Samsung</td><td class="p-2 text-sm">5200</td></tr>
    <tr><td class="p-2 text-sm">Teclado mecanico</td><td class="p-2 text-sm">1200</td></tr>
  </table>
</div>

</v-click>

  </div>
  <div>

<v-clicks>
<div class="space-y-3">
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-3 text-sm">
    <strong>SELECT</strong> = ¿que columnas quiero ver?
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-3 text-sm">
    <strong>FROM</strong> = ¿de que tabla?
  </div>
  <div class="border-2 border-black bg-[#282A36] text-[#2DD4BF] p-3 text-sm font-mono">
    SELECT * FROM productos;<br/>
    <span class="text-white/50">-- * = todas las columnas</span>
  </div>
</div>
</v-clicks>

  </div>
</div>

---

<!-- Slide 9: WHERE -->

# Filtrando datos: WHERE

<div class="pixel-divider my-4" />

<div class="grid grid-cols-[1fr_1fr] gap-6 mt-4">
  <div>

<v-click>

```sql
SELECT * FROM productos
WHERE precio > 500;
```

</v-click>

<v-click>

<div class="border-2 border-black bg-white p-0 overflow-hidden mt-4">
  <table class="w-full mac-table">
    <tr>
      <th class="text-left p-2 font-bold text-sm">id</th>
      <th class="text-left p-2 font-bold text-sm">nombre</th>
      <th class="text-left p-2 font-bold text-sm">precio</th>
      <th class="text-left p-2 font-bold text-sm">categoria</th>
    </tr>
    <tr><td class="p-2 text-sm">1</td><td class="p-2 text-sm">Laptop HP</td><td class="p-2 text-sm">15000</td><td class="p-2 text-sm">Electronica</td></tr>
    <tr><td class="p-2 text-sm">3</td><td class="p-2 text-sm">Monitor Samsung</td><td class="p-2 text-sm">5200</td><td class="p-2 text-sm">Electronica</td></tr>
    <tr><td class="p-2 text-sm">4</td><td class="p-2 text-sm">Teclado mecanico</td><td class="p-2 text-sm">1200</td><td class="p-2 text-sm">Accesorios</td></tr>
  </table>
</div>

</v-click>

  </div>
  <div>

<v-clicks>
<div class="space-y-3">
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/15 p-3 text-sm">
    <strong>WHERE</strong> = el filtro. Solo muestra filas que cumplan la condicion.
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    <strong>Operadores</strong>: <code>=</code>, <code>></code>, <code><</code>, <code>>=</code>, <code><=</code>, <code>!=</code>
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm">
    El Mouse (precio 350) <strong>no aparece</strong> porque no cumple <code>precio > 500</code>.
  </div>
</div>
</v-clicks>

  </div>
</div>

---

<!-- Slide 10: SELECT + WHERE combined -->

# Combinando: SELECT + WHERE

<div class="pixel-divider my-4" />

<v-click>

```sql
SELECT nombre, precio
FROM productos
WHERE categoria = 'Electronica'
  AND precio > 1000
ORDER BY precio DESC;
```

</v-click>

<v-click>

<div class="border-2 border-black bg-white p-0 overflow-hidden mt-4 max-w-md">
  <table class="w-full mac-table">
    <tr>
      <th class="text-left p-2 font-bold text-sm">nombre</th>
      <th class="text-left p-2 font-bold text-sm">precio</th>
    </tr>
    <tr><td class="p-2 text-sm">Laptop HP</td><td class="p-2 text-sm">15000</td></tr>
    <tr><td class="p-2 text-sm">Monitor Samsung</td><td class="p-2 text-sm">5200</td></tr>
  </table>
</div>

</v-click>

<v-click>

<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="border-2 border-black bg-white p-3 text-sm text-center">
    <strong>AND</strong><br/>Ambas condiciones deben cumplirse
  </div>
  <div class="border-2 border-black bg-white p-3 text-sm text-center">
    <strong>OR</strong><br/>Al menos una condicion
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/15 p-3 text-sm text-center">
    <strong>ORDER BY</strong><br/>Ordena resultados (ASC/DESC)
  </div>
</div>

</v-click>

---

<!-- Slide 11: Summary -->

# Lo que necesitas recordar

<div class="pixel-divider my-4" />

<div class="grid grid-cols-2 gap-4 mt-6">
<v-clicks>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/10 p-5">
    <h3 class="text-[#2DD4BF]"><div class="i-pixelarticons-database inline-block w-5 h-5 align-middle mr-1" /> Base de datos = Excel con superpoderes</h3>
    <p class="text-sm mt-2">Mas rapida, mas segura, mas escalable. Maneja millones de registros sin problema.</p>
  </div>
  <div class="border-2 border-[#2DD4BF] bg-[#2DD4BF]/10 p-5">
    <h3 class="text-[#2DD4BF]"><div class="i-pixelarticons-globe inline-block w-5 h-5 align-middle mr-1" /> SQL = lenguaje universal</h3>
    <p class="text-sm mt-2">50+ años, estandar ISO, funciona en todos los motores. Aprendes una vez, lo usas siempre.</p>
  </div>
  <div class="border-2 border-[#ff6b6b] bg-[#ff6b6b]/10 p-5">
    <h3 class="text-[#ff6b6b]"><div class="i-pixelarticons-code inline-block w-5 h-5 align-middle mr-1" /> SELECT / FROM / WHERE</h3>
    <p class="text-sm mt-2">Con estas tres palabras puedes hacer el 80% de las consultas de datos. Es tu base.</p>
  </div>
  <div class="border-2 border-[#6c5ce7] bg-[#6c5ce7]/10 p-5">
    <h3 class="text-[#6c5ce7]"><div class="i-pixelarticons-briefcase-search inline-block w-5 h-5 align-middle mr-1" /> VAS a usar SQL</h3>
    <p class="text-sm mt-2">No importa si vas a Data Analysis, Engineering, Science o BI. SQL es el minimo requerido.</p>
  </div>
</v-clicks>
</div>

---
layout: neo-cover
---

<!-- Slide 12: Ready for workshop -->

# Listo para el taller

## Con esto tienes todo. En el taller vamos MAS ALLA.

<div class="pixel-divider my-6" />

<v-click>

<div class="border-2 border-black bg-[#2DD4BF]/15 p-4 text-center text-lg">
Vamos a explorar <strong>Elasticsearch</strong> y <strong>ChromaDB</strong> — herramientas que complementan SQL para busqueda inteligente e IA.
</div>

</v-click>

<div class="mt-6 text-sm opacity-50 font-mono">
github.com/HesusG/mas-alla-de-sql
</div>
