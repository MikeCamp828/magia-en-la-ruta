import { useState } from "react";

function PreferenceForm({ onSubmit, cargando }) {
  const [formulario, setFormulario] = useState({
    origen: "Ciudad de México",
    latitud_origen: 19.432608,
    longitud_origen: -99.133209,
    presupuesto: 2500,
    distancia_maxima_km: 300,
    cantidad_destinos: 3,
    tipo_ruta: "libre",
    intereses: ["naturaleza", "cultura", "gastronomia"]
  });

  const interesesDisponibles = [
    "naturaleza",
    "cultura",
    "gastronomia",
    "aventura",
    "historia",
    "fotografia",
    "descanso",
    "artesanias"
  ];

  const manejarCambio = (evento) => {
    const { name, value } = evento.target;

    setFormulario({
      ...formulario,
      [name]:
        name === "presupuesto" ||
        name === "distancia_maxima_km" ||
        name === "cantidad_destinos"
          ? Number(value)
          : value
    });
  };

  const manejarInteres = (interes) => {
    const yaExiste = formulario.intereses.includes(interes);

    const nuevosIntereses = yaExiste
      ? formulario.intereses.filter((item) => item !== interes)
      : [...formulario.intereses, interes];

    setFormulario({
      ...formulario,
      intereses: nuevosIntereses
    });
  };

  const enviarFormulario = (evento) => {
    evento.preventDefault();
    onSubmit(formulario);
  };

  return (
    <form className="preference-form" onSubmit={enviarFormulario}>
      <h2>Planea tu ruta</h2>

      <div className="form-grid">
        <div className="form-group">
          <label>Origen</label>
          <input
            type="text"
            name="origen"
            value={formulario.origen}
            onChange={manejarCambio}
          />
        </div>

        <div className="form-group">
          <label>Presupuesto aproximado</label>
          <input
            type="number"
            name="presupuesto"
            value={formulario.presupuesto}
            onChange={manejarCambio}
          />
        </div>

        <div className="form-group">
          <label>Distancia máxima en km</label>
          <input
            type="number"
            name="distancia_maxima_km"
            value={formulario.distancia_maxima_km}
            onChange={manejarCambio}
          />
        </div>

        <div className="form-group">
          <label>Cantidad de destinos</label>
          <input
            type="number"
            name="cantidad_destinos"
            min="1"
            max="8"
            value={formulario.cantidad_destinos}
            onChange={manejarCambio}
          />
        </div>

        <div className="form-group">
          <label>Tipo de ruta</label>
          <select
            name="tipo_ruta"
            value={formulario.tipo_ruta}
            onChange={manejarCambio}
          >
            <option value="libre">Ruta libre</option>
            <option value="peaje">Ruta de peaje</option>
          </select>
        </div>

        <div className="form-group">
          <label>Intereses</label>

          <div className="checkbox-grid">
            {interesesDisponibles.map((interes) => (
              <label className="checkbox-item" key={interes}>
                <input
                  type="checkbox"
                  checked={formulario.intereses.includes(interes)}
                  onChange={() => manejarInteres(interes)}
                />
                {interes}
              </label>
            ))}
          </div>
        </div>
      </div>

      <div className="form-actions">
        <button className="btn-primary" type="submit" disabled={cargando}>
          {cargando ? "Generando ruta..." : "Generar ruta mágica"}
        </button>
      </div>
    </form>
  );
}

export default PreferenceForm;