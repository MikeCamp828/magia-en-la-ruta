import Hero from "../components/Hero";

function Home({ navegar }) {
  return (
    <main>
      <Hero navegar={navegar} />

      <section className="features-section">
        <h2>¿Qué hace Magia en la Ruta?</h2>

        <div className="features-grid">
          <article className="feature-card">
            <span>🗺️</span>
            <h3>Explora destinos</h3>
            <p>
              Consulta pueblos mágicos, ciudades culturales y lugares naturales
              dentro de México.
            </p>
          </article>

          <article className="feature-card">
            <span>✨</span>
            <h3>Recomienda lugares</h3>
            <p>
              El sistema selecciona destinos con base en tus intereses,
              presupuesto y distancia máxima.
            </p>
          </article>

          <article className="feature-card">
            <span>🧬</span>
            <h3>Optimiza rutas</h3>
            <p>
              Usa un algoritmo genético para ordenar los destinos y generar una
              ruta más conveniente.
            </p>
          </article>

          <article className="feature-card">
            <span>💸</span>
            <h3>Estima costos</h3>
            <p>
              Calcula un costo aproximado del viaje considerando distancia,
              gasolina, destinos y tipo de ruta.
            </p>
          </article>
        </div>
      </section>
    </main>
  );
}

export default Home;