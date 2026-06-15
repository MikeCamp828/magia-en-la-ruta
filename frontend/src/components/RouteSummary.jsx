function RouteSummary({ ruta }) {
  if (!ruta) return null;

  return (
    <section className="result-summary">
      <article className="summary-card">
        <span>Distancia total</span>
        <strong>{ruta.distancia_total_km} km</strong>
      </article>

      <article className="summary-card">
        <span>Tiempo aproximado</span>
        <strong>{ruta.tiempo_total_horas} h</strong>
      </article>

      <article className="summary-card">
        <span>Costo estimado</span>
        <strong>${ruta.costo_total_estimado} MXN</strong>
      </article>
    </section>
  );
}

export default RouteSummary;