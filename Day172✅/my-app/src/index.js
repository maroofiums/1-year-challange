import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";

import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";

// register the plugin globally
gsap.registerPlugin(useGSAP);

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
  