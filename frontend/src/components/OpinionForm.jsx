import { useState } from "react";

function OpinionForm({ destino, usuario, onPublicar, navegar, cargando }) {
  const [calificacion, setCalificacion] = useState(5);
  const [comentario, setComentario] = useState("");

  const enviarOpinion = (evento) => {
    evento.preventDefault();

    onPublicar({
      id_destino: destino.id_destino,
      calificacion,
      comentario
    });

    setComentario("");
    setCalificacion(5);
  };

  if (!usuario) {
    return (
      <section className="opinion-form-card">
        <h2>Comparte tu experiencia</h2>
        <p>
          Inicia sesión para publicar una opinión sobre {destino.nombre}.
        </p>

        <button className="btn-primary" onClick={() => navegar("login")}>
          Iniciar sesión
        </button>
      </section>
    );
  }

  return (
    <section className="opinion-form-card">
      <h2>Comparte tu experiencia</h2>
      <p>
        Cuéntale a otros viajeros qué tal estuvo tu visita a {destino.nombre}.
      </p>

      <form onSubmit={enviarOpinion}>
        <div className="form-group">
          <label>Calificación</label>
          <select
            value={calificacion}
            onChange={(e) => setCalificacion(Number(e.target.value))}
          >
            <option value={5}>⭐⭐⭐⭐⭐ Excelente</option>
            <option value={4}>⭐⭐⭐⭐ Muy bueno</option>
            <option value={3}>⭐⭐⭐ Bueno</option>
            <option value={2}>⭐⭐ Regular</option>
            <option value={1}>⭐ Malo</option>
          </select>
        </div>

        <div className="form-group">
          <label>Comentario</label>
          <textarea
            value={comentario}
            onChange={(e) => setComentario(e.target.value)}
            placeholder="Escribe tu opinión..."
            minLength={3}
            maxLength={1000}
            required
          />
        </div>

        <button className="btn-primary" type="submit" disabled={cargando}>
          {cargando ? "Publicando..." : "Publicar opinión"}
        </button>
      </form>
    </section>
  );
}

export default OpinionForm;