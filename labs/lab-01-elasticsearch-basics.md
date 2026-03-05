# Lab 1: Elasticsearch Basics

**Duracion**: ~30 minutos
**Objetivo**: Configurar Elastic Cloud, cargar datos de muestra y ejecutar tus primeras queries.

## Paso 1: Crear tu cuenta en Elastic Cloud

1. Ve a [elastic.co/cloud](https://www.elastic.co/cloud)
2. Clic en "Start free trial"
3. Registrate con tu email
4. Crea un deployment (region: cualquiera cercana)
5. **GUARDA** el password del usuario `elastic`

## Paso 2: Cargar datos de muestra

1. En Kibana, ve a **Home**
2. Clic en "Try sample data"
3. Agrega **"Sample eCommerce orders"**

## Paso 3: Abrir Dev Tools

1. Menu lateral → **Management** → **Dev Tools**
2. Verifica tu cluster:

```json
GET _cluster/health
```

Deberias ver `"status": "green"` o `"yellow"`.

## Paso 4: Tu primera busqueda

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

**Observa**: Cada resultado tiene un campo `_score`. Eso es el ranking de relevancia.

## Paso 5: Filtrar con bool query

```json
GET kibana_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "products.product_name": "boots" } }
      ],
      "filter": [
        { "range": { "taxful_total_price": { "gte": 50, "lte": 150 } } }
      ]
    }
  },
  "size": 5
}
```

## Paso 6: Tu primera agregacion

```json
GET kibana_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "por_categoria": {
      "terms": {
        "field": "products.category.keyword",
        "size": 5
      }
    }
  }
}
```

## Retos

1. Busca productos que contengan "jacket" Y cuesten mas de $100
2. Encuentra los 3 clientes con mayor gasto total (tip: usa `sum` aggregation)
3. Calcula el precio promedio por dia de la semana (tip: usa `day_of_week`)

## Hints

- `terms` aggregation = GROUP BY en SQL
- `sum`, `avg`, `max`, `min` = funciones de agregacion como en SQL
- `"size": 0` = solo quiero agregaciones, no documentos individuales
