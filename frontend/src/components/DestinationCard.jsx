function DestinationCard({ destino, onVerDetalle }) {
  return (
    <article className="destination-card">
      <div
        className="destination-image"
        style={{
          backgroundImage: `url(${
            destino.imagen_url ||
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
          })`
        }}
      />

      <div className="destination-content">
        <h3>{destino.nombre}</h3>

        <div className="destination-meta">
          <span>{destino.estado}</span>
          <span>{destino.tipo}</span>
        </div>

        <p>{destino.descripcion}</p>

        <div className="destination-footer">
          <strong>${Number(destino.costo_estimado).toFixed(0)} MXN</strong>
          <span>{Number(destino.tiempo_visita_horas).toFixed(1)} h visita</span>
        </div>

        <button
          className="btn-secondary destination-button"
          onClick={() => onVerDetalle(destino)}
        >
          Ver opiniones
        </button>
      </div>
    </article>
  );
}

export default DestinationCard;