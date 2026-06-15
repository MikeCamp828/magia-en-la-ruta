import { useState } from "react";

import apiClient from "../api/apiClient";
import PreferenceForm from "../components/PreferenceForm";
import LoadingMagic from "../components/LoadingMagic";

function PlanearRuta({ onRutaGenerada }) {
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState("");

  const generarRuta = async (datosFormulario) => {
    try {
      setCargando(true);
      setError("");

      const respuesta = await apiClient.post(
        "/api/rutas/generar",
        datosFormulario
      );

      onRutaGenerada(respuesta.data);
    } catch (err) {
      console.error(err);
      setError("No se pudo generar la ruta. Revisa que el backend esté encendido.");
    } finally {
      setCargando(false);
    }
  };

  return (
    <main className="plan-page">
      <section className="page-header">
        <h1>Planea una ruta turística</h1>
        <p>
          Ingresa tus preferencias y el sistema generará una ruta recomendada
          usando el algoritmo de optimización.
        </p>
      </section>

      <section className="plan-layout">
        <PreferenceForm onSubmit={generarRuta} cargando={cargando} />

        <div className="route-preview-card">
          <div>
            <h2>Tu viaje empieza aquí</h2>
            <p>
              Selecciona intereses, presupuesto, tipo de ruta y cantidad de
              destinos. Magia en la Ruta buscará una combinación conveniente
              para tu recorrido.
            </p>

            {cargando && <LoadingMagic />}

            {error && <div className="error-message">{error}</div>}
          </div>
        </div>
      </section>
    </main>
  );
}

export default PlanearRuta;