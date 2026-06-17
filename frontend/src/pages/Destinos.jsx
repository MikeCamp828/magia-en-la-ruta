import { useEffect, useState } from "react";

import apiClient from "../api/apiClient";
import DestinationCard from "../components/DestinationCard";

function Destinos({ onVerDetalle }) {
  const [destinos, setDestinos] = useState([]);
  const [busqueda, setBusqueda] = useState("");
  const [estado, setEstado] = useState("");
  const [interes, setInteres] = useState("");
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState("");

  const cargarDestinos = async () => {
    try {
      setCargando(true);
      setError("");

      const respuesta = await apiClient.get("/api/destinos/", {
        params: {
          q: busqueda || undefined,
          estado: estado || undefined,
          interes: interes || undefined
        }
      });

      setDestinos(respuesta.data);
    } catch (err) {
      console.error(err);
      setError("No se pudieron cargar los destinos. Revisa que el backend esté encendido.");
    } finally {
      setCargando(false);
    }
  };

  useEffect(() => {
    cargarDestinos();
  }, []);

  const manejarFiltro = (evento) => {
    evento.preventDefault();
    cargarDestinos();
  };

  return (
    <main className="destinos-page">
      <section className="page-header">
        <h1>Destinos mágicos</h1>
        <p>
          Explora destinos turísticos registrados en la base de datos y consulta
          las opiniones de otros viajeros.
        </p>
      </section>

      <form className="filters-card" onSubmit={manejarFiltro}>
        <input
          type="text"
          placeholder="Buscar destino..."
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value)}
        />

        <input
          type="text"
          placeholder="Estado..."
          value={estado}
          onChange={(e) => setEstado(e.target.value)}
        />

        <select value={interes} onChange={(e) => setInteres(e.target.value)}>
          <option value="">Todos los intereses</option>
          <option value="naturaleza">Naturaleza</option>
          <option value="cultura">Cultura</option>
          <option value="gastronomia">Gastronomía</option>
          <option value="aventura">Aventura</option>
          <option value="historia">Historia</option>
          <option value="fotografia">Fotografía</option>
        </select>

        <button className="btn-primary" type="submit">
          Filtrar
        </button>
      </form>

      {cargando && <div className="loading">Cargando destinos...</div>}

      {error && <div className="error-message">{error}</div>}

      {!cargando && !error && destinos.length === 0 && (
        <div className="empty-message">No se encontraron destinos.</div>
      )}

      <section className="destinos-grid">
        {destinos.map((destino) => (
          <DestinationCard
            key={destino.id_destino}
            destino={destino}
            onVerDetalle={onVerDetalle}
          />
        ))}
      </section>
    </main>
  );
}

export default Destinos;