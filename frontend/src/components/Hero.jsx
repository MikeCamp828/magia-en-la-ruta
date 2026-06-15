function Hero({ navegar }) {
  return (
    <section className="hero">
      <div className="hero-content">
        <p className="hero-label">Sistema inteligente de turismo</p>

        <h1>Descubre México con una ruta hecha a tu medida.</h1>

        <p className="hero-description">
          Magia en la Ruta te ayuda a encontrar destinos turísticos, recomendar
          pueblos mágicos y generar recorridos optimizados con distancia, tiempo
          y costo estimado.
        </p>

        <div className="hero-actions">
          <button className="btn-primary" onClick={() => navegar("planear")}>
            Crear mi ruta mágica
          </button>

          <button className="btn-secondary" onClick={() => navegar("destinos")}>
            Ver destinos
          </button>
        </div>
      </div>

      <div className="hero-card">
        <div className="floating-card">
          <span>📍</span>
          <div>
            <strong>Ruta sugerida</strong>
            <p>CDMX → Tepoztlán → Taxco → Malinalco</p>
          </div>
        </div>

        <div className="magic-orb">
          <span>🧭</span>
        </div>

        <div className="stats-card">
          <div>
            <strong>3</strong>
            <span>destinos</span>
          </div>

          <div>
            <strong>245 km</strong>
            <span>aprox.</span>
          </div>

          <div>
            <strong>$2,400</strong>
            <span>estimado</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;