-- El problema: buscar texto en SQL
-- "Encuentra reseñas donde los clientes estan frustrados"

-- Intento 1: LIKE - Solo encuentra coincidencias exactas
SELECT * FROM resenas
WHERE texto LIKE '%frustrado%';
-- ❌ No encuentra: "decepcionado", "molesto", "terrible experiencia"

-- Intento 2: Multiples LIKE - Frágil y lento
SELECT * FROM resenas
WHERE texto LIKE '%frustrado%'
   OR texto LIKE '%decepcionado%'
   OR texto LIKE '%molesto%'
   OR texto LIKE '%enojado%';
-- ❌ Hay que adivinar TODAS las palabras posibles

-- Intento 3: CONTAINS (SQL Server) o MATCH (MySQL)
SELECT * FROM resenas
WHERE CONTAINS(texto, '"frustrado" OR "decepcionado"');
-- ❌ Mejor, pero NO rankea por relevancia
-- ❌ No entiende sinónimos ni contexto
-- ❌ Configuración compleja (full-text indexes)

-- El resultado: SQL devuelve 0 o 1. Sin ranking.
-- No entiende que "pésimo servicio" = frustración.
