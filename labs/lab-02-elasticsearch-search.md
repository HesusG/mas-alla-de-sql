# Lab 2: Elasticsearch Search Avanzado

**Duracion**: ~45 minutos
**Objetivo**: Crear tu propio indice, insertar datos y usar fuzzy search, highlighting y multi-match.

**Prerequisito**: Lab 1 completado.

## Paso 1: Crear el indice de peliculas

Copia y pega en Dev Tools:

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
  "mappings": {
    "properties": {
      "titulo":   { "type": "text", "analyzer": "spanish_custom" },
      "sinopsis": { "type": "text", "analyzer": "spanish_custom" },
      "director": { "type": "keyword" },
      "genero":   { "type": "keyword" },
      "anio":     { "type": "integer" },
      "rating":   { "type": "float" },
      "pais":     { "type": "keyword" }
    }
  }
}
```

## Paso 2: Insertar peliculas

```json
POST peliculas/_bulk
{"index":{}}
{"titulo":"Roma","sinopsis":"Historia de una trabajadora domestica en la Ciudad de Mexico durante los anos 70.","director":"Alfonso Cuaron","genero":"Drama","anio":2018,"rating":8.7,"pais":"Mexico"}
{"index":{}}
{"titulo":"Nosotros los nobles","sinopsis":"Un padre millonario finge la bancarrota para ensenar a sus hijos el valor del trabajo.","director":"Gaz Alazraki","genero":"Comedia","anio":2013,"rating":7.1,"pais":"Mexico"}
{"index":{}}
{"titulo":"El laberinto del fauno","sinopsis":"Una nina descubre un mundo fantastico durante la Espana franquista.","director":"Guillermo del Toro","genero":"Fantasia","anio":2006,"rating":8.2,"pais":"Mexico"}
{"index":{}}
{"titulo":"Amores perros","sinopsis":"Tres historias sobre amor y violencia conectadas por un accidente en Ciudad de Mexico.","director":"Alejandro Gonzalez Inarritu","genero":"Drama","anio":2000,"rating":8.1,"pais":"Mexico"}
{"index":{}}
{"titulo":"Relatos salvajes","sinopsis":"Seis cortometrajes sobre personas llevadas al limite por la venganza.","director":"Damian Szifron","genero":"Comedia negra","anio":2014,"rating":8.1,"pais":"Argentina"}
```

## Paso 3: Match query

```json
GET peliculas/_search
{
  "query": {
    "match": { "sinopsis": "familia Mexico" }
  }
}
```

**Pregunta**: ¿Cuantos resultados obtienes? ¿Cual tiene el _score mas alto y por que?

## Paso 4: Fuzzy search

```json
GET peliculas/_search
{
  "query": {
    "match": {
      "sinopsis": {
        "query": "peliula familar",
        "fuzziness": "AUTO"
      }
    }
  }
}
```

**Observa**: Aunque escribiste con errores, ES encuentra resultados.

## Paso 5: Multi-match con boost

```json
GET peliculas/_search
{
  "query": {
    "multi_match": {
      "query": "historia Mexico",
      "fields": ["titulo^3", "sinopsis"],
      "type": "best_fields"
    }
  }
}
```

## Paso 6: Highlighting

```json
GET peliculas/_search
{
  "query": {
    "multi_match": {
      "query": "violencia sociedad",
      "fields": ["titulo", "sinopsis"]
    }
  },
  "highlight": {
    "fields": {
      "sinopsis": { "fragment_size": 200 }
    }
  }
}
```

## Retos

1. Agrega 5 peliculas mas de tu eleccion (pueden ser de cualquier pais)
2. Crea una query que combine: match en sinopsis + filter por anio >= 2010 + should por rating >= 8.0
3. Haz una agregacion que muestre el rating promedio por pais
4. Intenta buscar con 3 errores tipograficos diferentes — ¿ES siempre los encuentra?

## Hints

- `_bulk` API necesita un newline al final del ultimo documento
- `keyword` fields son para filtros exactos, `text` fields para busqueda full-text
- `boost` con `^` multiplica la importancia de un campo en el score
