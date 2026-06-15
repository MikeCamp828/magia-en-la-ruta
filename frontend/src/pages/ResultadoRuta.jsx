import RouteMap from "../components/RouteMap";
import RouteSummary from "../components/RouteSummary";

function ResultadoRuta({ rutaGenerada, navegar }) {
  if (!rutaGenerada) {
    return (
      <main className="result-page">
        <section className="page-header">
          <h1>No hay ruta generada</h1>
          <p>Primero genera una ruta desde la sección de planeación.</p>
          <button className="btn-primary" onClick={() => navegar("planear")}>
            Ir a planear ruta
          </button>
        </section>
      </main>
    );
  }

  return (
    <main className="result-page">
      <section className="page-header">
        <h1>Tu ruta mágica</h1>
        <p>{rutaGenerada.mensaje}</p>
      </section>

      <RouteSummary ruta={rutaGenerada} />

      <RouteMap ruta={rutaGenerada} />

      <section className="route-list">
        {rutaGenerada.destinos.map((destino) => (
          <article className="route-stop" key={destino.id_destino}>
            <div className="route-number">{destino.orden_visita}</div>

            <div>
              <h3>
                {destino.nombre}, {destino.estado}
              </h3>
              <p>{destino.descripcion}</p>

              <div className="destination-meta">
                <span>{destino.tipo}</span>
                <span>${Number(destino.costo_estimado).toFixed(0)} MXN</span>
                <span>{Number(destino.tiempo_visita_horas).toFixed(1)} h</span>
              </div>
            </div>
          </article>
        ))}
      </section>

      <div className="form-actions">
        <button className="btn-secondary" onClick={() => navegar("planear")}>
          Generar otra ruta
        </button>
      </div>
    </main>
  );
}

export default ResultadoRuta;