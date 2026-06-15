-- ============================================================
-- MAGIA EN LA RUTA
-- Valores iniciales para estimar costos
-- ============================================================

INSERT INTO costos_referencia
(concepto, valor, unidad, descripcion)
VALUES
(
    'precio_gasolina_regular',
    24.50,
    'MXN por litro',
    'Precio promedio usado para estimar gasto de gasolina en el MVP.'
),
(
    'rendimiento_auto_promedio',
    13.00,
    'km por litro',
    'Rendimiento promedio estimado para automóvil compacto.'
),
(
    'costo_caseta_por_km_estimado',
    1.80,
    'MXN por km',
    'Valor aproximado para estimar casetas cuando el usuario elige ruta de peaje.'
),
(
    'factor_tiempo_ruta_libre',
    1.25,
    'multiplicador',
    'La ruta libre suele tardar más, por eso se multiplica el tiempo base.'
),
(
    'factor_tiempo_ruta_peaje',
    1.00,
    'multiplicador',
    'La ruta de peaje se toma como tiempo base estimado.'
),
(
    'velocidad_promedio_carretera',
    80.00,
    'km/h',
    'Velocidad promedio usada para estimar tiempo de traslado.'
),
(
    'gasto_alimentos_promedio',
    180.00,
    'MXN por persona',
    'Gasto promedio de alimentos por destino visitado.'
),
(
    'gasto_extra_promedio',
    120.00,
    'MXN por destino',
    'Gasto extra aproximado para entradas, estacionamiento o compras menores.'
)
ON CONFLICT(concepto) DO NOTHING;