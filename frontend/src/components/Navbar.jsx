function Navbar({ navegar, paginaActual, usuario, onLogout }) {
  return (
    <nav className="navbar">
      <div className="navbar-logo" onClick={() => navegar("home")}>
        <span className="logo-icon">✨</span>
        <span>Magia en la Ruta</span>
      </div>

      <div className="navbar-links">
        <button
          className={paginaActual === "home" ? "nav-active" : ""}
          onClick={() => navegar("home")}
        >
          Inicio
        </button>

        <button
          className={paginaActual === "destinos" ? "nav-active" : ""}
          onClick={() => navegar("destinos")}
        >
          Destinos
        </button>

        <button
          className={paginaActual === "planear" ? "nav-active" : ""}
          onClick={() => navegar("planear")}
        >
          Planear ruta
        </button>

        {usuario ? (
          <>
            <span className="user-pill">Hola, {usuario.nombre}</span>

            <button onClick={onLogout}>
              Salir
            </button>
          </>
        ) : (
          <button
            className={paginaActual === "login" ? "nav-active" : ""}
            onClick={() => navegar("login")}
          >
            Login
          </button>
        )}
      </div>
    </nav>
  );
}

export default Navbar;