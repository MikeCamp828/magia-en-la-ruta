import React from "react";
import ReactDOM from "react-dom/client";

import "leaflet/dist/leaflet.css";
import "./styles/global.css";
import "./styles/home.css";
import "./styles/cards.css";
import "./styles/route.css";

import App from "./App.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);