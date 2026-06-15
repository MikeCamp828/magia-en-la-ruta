# Magia en la Ruta

**Magia en la Ruta** es un sistema web para la planeación de viajes turísticos dentro de México.  
El proyecto permite explorar destinos, recibir recomendaciones personalizadas, generar rutas optimizadas y visualizar estimaciones de distancia, tiempo y costo.

## Objetivo del MVP

Construir una primera versión funcional donde el usuario pueda:

- Consultar destinos turísticos.
- Filtrar destinos por estado, tipo e intereses.
- Ingresar preferencias de viaje.
- Recibir una ruta recomendada.
- Visualizar distancia, tiempo y costo estimado.
- Guardar rutas generadas.

## Tecnologías utilizadas

### Frontend
- React
- Vite
- CSS
- Leaflet para mapas

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Base de datos
- PostgreSQL

### Algoritmo
- Python
- Algoritmo genético para optimización de rutas
- Cálculo de distancia aproximada con fórmula Haversine

## Estructura del proyecto

```txt
magia-en-la-ruta/
│
├── database/
├── backend/
├── optimizer/
└── frontend/