-- ============================================================
-- MAGIA EN LA RUTA
-- Datos iniciales de destinos turísticos
-- ============================================================

INSERT INTO destinos
(nombre, estado, tipo, descripcion, latitud, longitud, costo_estimado, tiempo_visita_horas, intereses, imagen_url)
VALUES
(
    'Tepoztlán',
    'Morelos',
    'Pueblo Mágico',
    'Destino reconocido por el Cerro del Tepozteco, su ambiente místico, gastronomía tradicional y calles llenas de vida cultural.',
    18.9848,
    -99.0931,
    650.00,
    5.00,
    'naturaleza,cultura,gastronomia,aventura',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee'
),
(
    'Valle de Bravo',
    'Estado de México',
    'Pueblo Mágico',
    'Pueblo rodeado de bosque y lago, ideal para actividades al aire libre, descanso, caminatas y recorridos panorámicos.',
    19.1950,
    -100.1313,
    900.00,
    6.00,
    'naturaleza,aventura,descanso,fotografia',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee'
),
(
    'Malinalco',
    'Estado de México',
    'Pueblo Mágico',
    'Lugar histórico y cultural con zona arqueológica, arquitectura colonial, artesanías y paisajes montañosos.',
    18.9484,
    -99.4962,
    700.00,
    5.00,
    'cultura,historia,naturaleza,gastronomia',
    'https://images.unsplash.com/photo-1506744038136-46273834b3fb'
),
(
    'Taxco',
    'Guerrero',
    'Pueblo Mágico',
    'Ciudad colonial famosa por su producción de plata, calles empedradas, arquitectura virreinal y la iglesia de Santa Prisca.',
    18.5565,
    -99.6059,
    850.00,
    6.00,
    'cultura,historia,artesanias,gastronomia',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Bernal',
    'Querétaro',
    'Pueblo Mágico',
    'Destino conocido por la Peña de Bernal, uno de los monolitos más grandes del mundo, ideal para caminatas y fotografía.',
    20.7400,
    -99.9417,
    750.00,
    5.00,
    'naturaleza,aventura,cultura,fotografia',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee'
),
(
    'Tequisquiapan',
    'Querétaro',
    'Pueblo Mágico',
    'Pueblo tranquilo con rutas de vino y queso, calles coloridas, plazas tradicionales y ambiente familiar.',
    20.5225,
    -99.8917,
    800.00,
    5.00,
    'gastronomia,cultura,descanso,romantico',
    'https://images.unsplash.com/photo-1507525428034-b723cf961d3e'
),
(
    'Huasca de Ocampo',
    'Hidalgo',
    'Pueblo Mágico',
    'Primer Pueblo Mágico de México, famoso por los Prismas Basálticos, haciendas antiguas y paisajes naturales.',
    20.2036,
    -98.5761,
    700.00,
    5.00,
    'naturaleza,historia,aventura,fotografia',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee'
),
(
    'Real del Monte',
    'Hidalgo',
    'Pueblo Mágico',
    'Pueblo minero con arquitectura inglesa, clima frío, historia minera y gastronomía tradicional como los pastes.',
    20.1408,
    -98.6731,
    600.00,
    4.00,
    'historia,cultura,gastronomia,fotografia',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Cholula',
    'Puebla',
    'Pueblo Mágico',
    'Destino con gran riqueza histórica, iglesias, vida universitaria y la Gran Pirámide con vista al Popocatépetl.',
    19.0641,
    -98.3035,
    750.00,
    5.00,
    'historia,cultura,gastronomia,fotografia',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Atlixco',
    'Puebla',
    'Pueblo Mágico',
    'Pueblo famoso por su clima agradable, viveros, flores, gastronomía y vistas al volcán Popocatépetl.',
    18.9089,
    -98.4361,
    650.00,
    5.00,
    'naturaleza,gastronomia,descanso,fotografia',
    'https://images.unsplash.com/photo-1506744038136-46273834b3fb'
),
(
    'Zacatlán',
    'Puebla',
    'Pueblo Mágico',
    'Destino serrano conocido por sus manzanas, relojes monumentales, miradores de cristal y paisajes boscosos.',
    19.9333,
    -97.9611,
    850.00,
    6.00,
    'naturaleza,cultura,gastronomia,fotografia',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee'
),
(
    'Chignahuapan',
    'Puebla',
    'Pueblo Mágico',
    'Pueblo conocido por sus esferas navideñas, aguas termales, laguna y tradiciones populares.',
    19.8386,
    -98.0317,
    800.00,
    5.00,
    'cultura,artesanias,descanso,naturaleza',
    'https://images.unsplash.com/photo-1507525428034-b723cf961d3e'
),
(
    'Pátzcuaro',
    'Michoacán',
    'Pueblo Mágico',
    'Lugar emblemático por su lago, tradiciones purépechas, arquitectura colonial y celebraciones de Día de Muertos.',
    19.5159,
    -101.6092,
    950.00,
    6.00,
    'cultura,historia,gastronomia,tradiciones',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Tzintzuntzan',
    'Michoacán',
    'Pueblo Mágico',
    'Antigua capital purépecha con zona arqueológica, convento histórico y vistas al Lago de Pátzcuaro.',
    19.6283,
    -101.5789,
    700.00,
    4.00,
    'historia,cultura,tradiciones,fotografia',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'San Miguel de Allende',
    'Guanajuato',
    'Ciudad Patrimonio',
    'Ciudad reconocida internacionalmente por su arquitectura colonial, arte, cultura, gastronomía y ambiente romántico.',
    20.9144,
    -100.7452,
    1200.00,
    7.00,
    'cultura,arte,gastronomia,romantico',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Dolores Hidalgo',
    'Guanajuato',
    'Pueblo Mágico',
    'Cuna de la Independencia de México, famosa por su historia, nieves tradicionales y cerámica.',
    21.1561,
    -100.9325,
    700.00,
    5.00,
    'historia,cultura,gastronomia,artesanias',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Guanajuato',
    'Guanajuato',
    'Ciudad Patrimonio',
    'Ciudad histórica con callejones, túneles, museos, arquitectura colonial y gran vida cultural.',
    21.0190,
    -101.2574,
    1100.00,
    7.00,
    'historia,cultura,arte,gastronomia',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Tepotzotlán',
    'Estado de México',
    'Pueblo Mágico',
    'Pueblo cercano a la Ciudad de México, famoso por el Museo Nacional del Virreinato y su arquitectura colonial.',
    19.7191,
    -99.2237,
    550.00,
    4.00,
    'historia,cultura,gastronomia,familiar',
    'https://images.unsplash.com/photo-1518005020951-eccb494ad742'
),
(
    'Cuetzalan',
    'Puebla',
    'Pueblo Mágico',
    'Pueblo serrano con neblina, cascadas, grutas, tradiciones indígenas y arquitectura tradicional.',
    20.0186,
    -97.5211,
    950.00,
    7.00,
    'naturaleza,cultura,aventura,tradiciones',
    'https://images.unsplash.com/photo-1506744038136-46273834b3fb'
),
(
    'Peña de Bernal',
    'Querétaro',
    'Sitio Natural',
    'Monolito ideal para caminata, fotografía y recorridos de aventura en un entorno semidesértico.',
    20.7489,
    -99.9489,
    500.00,
    4.00,
    'naturaleza,aventura,fotografia',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee'
)
ON CONFLICT(nombre, estado) DO NOTHING;