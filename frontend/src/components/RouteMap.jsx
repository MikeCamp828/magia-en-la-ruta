import { CircleMarker, MapContainer, Polyline, Popup, TileLayer } from "react-leaflet";

function RouteMap({ ruta }) {
  if (!ruta || !ruta.destinos || ruta.destinos.length === 0) {
    return null;
  }

  const origen = [19.432608, -99.133209];

  const puntosDestino = ruta.destinos.map((destino) => [
    destino.latitud,
    destino.longitud
  ]);

  const puntosRuta = [origen, ...puntosDestino];

  return (
    <div className="route-map">
      <MapContainer
        center={origen}
        zoom={7}
        style={{ width: "100%", height: "100%" }}
      >
        <TileLayer
          attribution="&copy; OpenStreetMap"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <CircleMarker center={origen} radius={9}>
          <Popup>Origen: {ruta.origen}</Popup>
        </CircleMarker>

        {ruta.destinos.map((destino) => (
          <CircleMarker
            key={destino.id_destino}
            center={[destino.latitud, destino.longitud]}
            radius={8}
          >
            <Popup>
              {destino.orden_visita}. {destino.nombre}, {destino.estado}
            </Popup>
          </CircleMarker>
        ))}

        <Polyline positions={puntosRuta} />
      </MapContainer>
    </div>
  );
}

export default RouteMap;