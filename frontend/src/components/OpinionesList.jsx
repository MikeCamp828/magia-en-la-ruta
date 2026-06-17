function OpinionesList({ opiniones, resumen, cargando }) {
  const renderEstrellas = (calificacion) => {
    return "★".repeat(calificacion) + "☆".repeat(5 - calificacion);
  };

  if (cargando) {
    return <div className="loading">Cargando opiniones...</div>;
  }

  return (
    <section className="opiniones-section">
      <div className="opiniones-header">
        <div>
          <h2>Opiniones de viajeros</h2>
          <p>
            {resumen.total_opiniones} opiniones · Promedio{" "}
            {resumen.promedio_calificacion}/5
          </p>
        </div>

        <div className="rating-big">
          ⭐ {resumen.promedio_calificacion}
        </div>
      </div>

      {opiniones.length === 0 ? (
        <div className="empty-message">
          Todavía no hay opiniones para este destino. Sé el primero en dejar una reseña.
        </div>
      ) : (
        <div className="opiniones-list">
          {opiniones.map((opinion) => (
            <article className="opinion-card" key={opinion.id_opinion}>
              <div className="opinion-top">
                <div>
                  <h3>{opinion.nombre_usuario}</h3>
                  <span className="opinion-date">
                    {new Date(opinion.fecha_creacion).toLocaleDateString()}
                  </span>
                </div>

                <div className="stars">
                  {renderEstrellas(opinion.calificacion)}
                </div>
              </div>

              <p>{opinion.comentario}</p>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

export default OpinionesList;