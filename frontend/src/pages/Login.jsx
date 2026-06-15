import { useState } from "react";

import apiClient from "../api/apiClient";

function Login({ onLogin, navegar }) {
  const [modo, setModo] = useState("login");
  const [formulario, setFormulario] = useState({
    nombre: "",
    correo: "",
    password: ""
  });

  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState("");

  const esRegistro = modo === "registro";

  const manejarCambio = (evento) => {
    const { name, value } = evento.target;

    setFormulario({
      ...formulario,
      [name]: value
    });
  };

  const enviarFormulario = async (evento) => {
    evento.preventDefault();

    try {
      setCargando(true);
      setError("");

      const endpoint = esRegistro
        ? "/api/auth/registro"
        : "/api/auth/login";

      const payload = esRegistro
        ? {
            nombre: formulario.nombre,
            correo: formulario.correo,
            password: formulario.password
          }
        : {
            correo: formulario.correo,
            password: formulario.password
          };

      const respuesta = await apiClient.post(endpoint, payload);

      localStorage.setItem("magia_token", respuesta.data.access_token);
      localStorage.setItem(
        "magia_usuario",
        JSON.stringify(respuesta.data.usuario)
      );

      onLogin(respuesta.data.usuario);
      navegar("home");
    } catch (err) {
      console.error(err);

      const detalle =
        err.response?.data?.detail ||
        "No se pudo iniciar sesión. Revisa tus datos.";

      setError(detalle);
    } finally {
      setCargando(false);
    }
  };

  return (
    <main className="login-page">
      <section className="login-card">
        <div className="login-info">
          <span className="login-icon">✨</span>
          <h1>{esRegistro ? "Crea tu cuenta" : "Bienvenido de vuelta"}</h1>
          <p>
            Guarda tus rutas, comparte opiniones y construye tu propia bitácora
            de viajes mágicos por México.
          </p>
        </div>

        <form className="login-form" onSubmit={enviarFormulario}>
          {esRegistro && (
            <div className="form-group">
              <label>Nombre</label>
              <input
                type="text"
                name="nombre"
                value={formulario.nombre}
                onChange={manejarCambio}
                placeholder="Tu nombre"
                required
              />
            </div>
          )}

          <div className="form-group">
            <label>Correo</label>
            <input
              type="email"
              name="correo"
              value={formulario.correo}
              onChange={manejarCambio}
              placeholder="correo@ejemplo.com"
              required
            />
          </div>

          <div className="form-group">
            <label>Contraseña</label>
            <input
              type="password"
              name="password"
              value={formulario.password}
              onChange={manejarCambio}
              placeholder="Mínimo 6 caracteres"
              required
              minLength={6}
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <button className="btn-primary login-button" type="submit">
            {cargando
              ? "Procesando..."
              : esRegistro
                ? "Registrarme"
                : "Iniciar sesión"}
          </button>

          <button
            type="button"
            className="auth-switch"
            onClick={() => {
              setError("");
              setModo(esRegistro ? "login" : "registro");
            }}
          >
            {esRegistro
              ? "Ya tengo cuenta, iniciar sesión"
              : "No tengo cuenta, registrarme"}
          </button>
        </form>
      </section>
    </main>
  );
}

export default Login;