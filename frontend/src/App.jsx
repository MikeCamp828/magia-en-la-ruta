import { useState } from "react";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Destinos from "./pages/Destinos";
import PlanearRuta from "./pages/PlanearRuta";
import ResultadoRuta from "./pages/ResultadoRuta";

function App() {
  const [paginaActual, setPaginaActual] = useState("home");
  const [rutaGenerada, setRutaGenerada] = useState(null);

  const navegar = (pagina) => {
    setPaginaActual(pagina);
  };

  const manejarRutaGenerada = (ruta) => {
    setRutaGenerada(ruta);
    setPaginaActual("resultado");
  };

  return (
    <>
      <Navbar navegar={navegar} paginaActual={paginaActual} />

      {paginaActual === "home" && <Home navegar={navegar} />}

      {paginaActual === "destinos" && <Destinos />}

      {paginaActual === "planear" && (
        <PlanearRuta onRutaGenerada={manejarRutaGenerada} />
      )}

      {paginaActual === "resultado" && (
        <ResultadoRuta rutaGenerada={rutaGenerada} navegar={navegar} />
      )}
    </>
  );
}

export default App;