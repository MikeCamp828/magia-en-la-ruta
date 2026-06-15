import { useEffect, useState } from "react";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Destinos from "./pages/Destinos";
import PlanearRuta from "./pages/PlanearRuta";
import ResultadoRuta from "./pages/ResultadoRuta";
import Login from "./pages/Login";

function App() {
  const [paginaActual, setPaginaActual] = useState("home");
  const [rutaGenerada, setRutaGenerada] = useState(null);
  const [usuario, setUsuario] = useState(null);

  useEffect(() => {
    const usuarioGuardado = localStorage.getItem("magia_usuario");

    if (usuarioGuardado) {
      setUsuario(JSON.parse(usuarioGuardado));
    }
  }, []);

  const navegar = (pagina) => {
    setPaginaActual(pagina);
  };

  const manejarRutaGenerada = (ruta) => {
    setRutaGenerada(ruta);
    setPaginaActual("resultado");
  };

  const manejarLogin = (usuarioAutenticado) => {
    setUsuario(usuarioAutenticado);
  };

  const cerrarSesion = () => {
    localStorage.removeItem("magia_token");
    localStorage.removeItem("magia_usuario");
    setUsuario(null);
    setPaginaActual("home");
  };

  return (
    <>
      <Navbar
        navegar={navegar}
        paginaActual={paginaActual}
        usuario={usuario}
        onLogout={cerrarSesion}
      />

      {paginaActual === "home" && <Home navegar={navegar} />}

      {paginaActual === "destinos" && <Destinos />}

      {paginaActual === "planear" && (
        <PlanearRuta onRutaGenerada={manejarRutaGenerada} />
      )}

      {paginaActual === "resultado" && (
        <ResultadoRuta rutaGenerada={rutaGenerada} navegar={navegar} />
      )}

      {paginaActual === "login" && (
        <Login onLogin={manejarLogin} navegar={navegar} />
      )}
    </>
  );
}

export default App;