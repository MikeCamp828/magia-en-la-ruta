import { useEffect, useState } from "react";

import apiClient from "../api/apiClient";
import OpinionesList from "../components/OpinionesList";
import OpinionForm from "../components/OpinionForm";

function DetalleDestino({ destino, usuario, navegar }) {
  const [opiniones, setOpiniones] = useState([]);
  const [resumen, setResumen] = useState({
    id_destino: destino?.id_destino || 0,
    total_opiniones: 0,
    promedio_calificacion: 0
  });

  const [cargandoOpiniones, setCargandoOpiniones] = useState(true);
  const [publicando, setPublicando] = useState(false);
  const [error, setError] = useState("");
  const [mensaje, setMensaje] = useState("");

  const cargarOpiniones = async () => {
    if (!destino) return;

    try {
      setCargandoOpiniones(true);
      setError("");

      const [respuestaOpiniones, respuestaResumen] = await Promise.all([
        apiClient.get(`/api/opiniones/destino/${destino.id_destino}`),
        apiClient.get(`/api/opiniones/destino/${destino.id_destino}/resumen`)
      ]);

      setOpiniones(respuestaOpiniones.data);
      setResumen(respuestaResumen.data);
    } catch (err) {
      console.error(err);
      setError("No se pudieron cargar las opiniones.");
    } finally {
      setCargandoOpiniones(false);
    }
  };

  useEffect(() => {
    cargarOpiniones();
  }, [destino]);

  const publicarOpinion = async (datosOpinion) => {
    try {
      setPublicando(true);
      setError("");
      setMensaje("");

      await apiClient.post("/api/opiniones/", datosOpinion);

      setMensaje("Opinión publicada correctamente.");
      await cargarOpiniones();
    } catch (err) {
      console.error(err);

      const detalle =
        err.response?.data?.detail ||
        "No se pudo publicar la opinión. Revisa tu sesión.";

      setError(detalle);
    } finally {
      setPublicando(false);
    }
  };

  if (!destino) {
    return (
      <main className="detalle-page">
        <section className="page-header">
          <h1>No hay destino seleccionado</h1>
          <p>Regresa a la sección de destinos para elegir uno.</p>

          <button className="btn-primary" onClick={() => navegar("destinos")}>
            Ir a destinos
          </button>
        </section>
      </main>
    );
  }

  return (
    <main className="detalle-page">
      <section className="detalle-hero">
        <div
          className="detalle-image"
          style={{
            backgroundImage: `url(${
              destino.imagen_url ||
              "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
            })`
          }}
        />

        <div className="detalle-info">
          <button className="back-button" onClick={() => navegar("destinos")}>
            ← Volver a destinos
          </button>

          <span className="hero-label">{destino.tipo}</span>

          <h1>{destino.nombre}</h1>

          <div className="destination-meta">
            <span>{destino.estado}</span>
            <span>${Number(destino.costo_estimado).toFixed(0)} MXN</span>
            <span>{Number(destino.tiempo_visita_horas).toFixed(1)} h visita</span>
          </div>

          <p>{destino.descripcion}</p>
        </div>
      </section>

      {mensaje && <div className="success-message">{mensaje}</div>}
      {error && <div className="error-message">{error}</div>}

      <section className="detalle-layout">
        <OpinionForm
          destino={destino}
          usuario={usuario}
          onPublicar={publicarOpinion}
          navegar={navegar}
          cargando={publicando}
        />

        <OpinionesList
          opiniones={opiniones}
          resumen={resumen}
          cargando={cargandoOpiniones}
        />
      </section>
    </main>
  );
}

export default DetalleDestino;