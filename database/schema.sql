-- ============================================================
-- MAGIA EN LA RUTA
-- Esquema principal de base de datos
-- ============================================================

DROP TABLE IF EXISTS ruta_destinos CASCADE;
DROP TABLE IF EXISTS rutas CASCADE;
DROP TABLE IF EXISTS preferencias CASCADE;
DROP TABLE IF EXISTS costos_referencia CASCADE;
DROP TABLE IF EXISTS destinos CASCADE;
DROP TABLE IF EXISTS usuarios CASCADE;

-- ============================================================
-- Tabla: usuarios
-- Guarda los usuarios registrados en el sistema.
-- En el MVP el login puede ser opcional, pero la tabla queda lista.
-- ============================================================

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- Tabla: destinos
-- Guarda pueblos mágicos, ciudades turísticas y sitios culturales.
-- ============================================================

CREATE TABLE destinos (
    id_destino SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    tipo VARCHAR(80) NOT NULL,
    descripcion TEXT NOT NULL,
    latitud DECIMAL(10, 7) NOT NULL,
    longitud DECIMAL(10, 7) NOT NULL,
    costo_estimado DECIMAL(10, 2) DEFAULT 0,
    tiempo_visita_horas DECIMAL(5, 2) DEFAULT 2,
    intereses TEXT NOT NULL,
    imagen_url TEXT,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(nombre, estado)
);

-- ============================================================
-- Tabla: preferencias
-- Guarda las preferencias de viaje indicadas por el usuario.
-- ============================================================

CREATE TABLE preferencias (
    id_preferencia SERIAL PRIMARY KEY,
    id_usuario INTEGER REFERENCES usuarios(id_usuario) ON DELETE SET NULL,
    origen VARCHAR(150) NOT NULL,
    latitud_origen DECIMAL(10, 7),
    longitud_origen DECIMAL(10, 7),
    presupuesto DECIMAL(10, 2),
    distancia_maxima_km DECIMAL(10, 2),
    cantidad_destinos INTEGER DEFAULT 3,
    tipo_ruta VARCHAR(30) DEFAULT 'libre',
    intereses TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- Tabla: rutas
-- Guarda las rutas generadas por el sistema.
-- ============================================================

CREATE TABLE rutas (
    id_ruta SERIAL PRIMARY KEY,
    id_usuario INTEGER REFERENCES usuarios(id_usuario) ON DELETE SET NULL,
    id_preferencia INTEGER REFERENCES preferencias(id_preferencia) ON DELETE SET NULL,
    nombre_ruta VARCHAR(150) DEFAULT 'Ruta mágica',
    origen VARCHAR(150) NOT NULL,
    distancia_total_km DECIMAL(10, 2) DEFAULT 0,
    tiempo_total_horas DECIMAL(10, 2) DEFAULT 0,
    costo_total DECIMAL(10, 2) DEFAULT 0,
    tipo_ruta VARCHAR(30) DEFAULT 'libre',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- Tabla: ruta_destinos
-- Relaciona una ruta con los destinos en orden de visita.
-- ============================================================

CREATE TABLE ruta_destinos (
    id_ruta_destino SERIAL PRIMARY KEY,
    id_ruta INTEGER REFERENCES rutas(id_ruta) ON DELETE CASCADE,
    id_destino INTEGER REFERENCES destinos(id_destino) ON DELETE CASCADE,
    orden_visita INTEGER NOT NULL,
    distancia_desde_anterior_km DECIMAL(10, 2) DEFAULT 0,
    tiempo_desde_anterior_horas DECIMAL(10, 2) DEFAULT 0,
    costo_tramo DECIMAL(10, 2) DEFAULT 0
);

-- ============================================================
-- Tabla: costos_referencia
-- Guarda valores de referencia para estimar costos del viaje.
-- ============================================================

CREATE TABLE costos_referencia (
    id_costo SERIAL PRIMARY KEY,
    concepto VARCHAR(100) UNIQUE NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    unidad VARCHAR(50) NOT NULL,
    descripcion TEXT
);

-- ============================================================
-- Índices para mejorar búsquedas
-- ============================================================

CREATE INDEX idx_destinos_estado ON destinos(estado);
CREATE INDEX idx_destinos_tipo ON destinos(tipo);
CREATE INDEX idx_destinos_intereses ON destinos(intereses);
CREATE INDEX idx_rutas_usuario ON rutas(id_usuario);