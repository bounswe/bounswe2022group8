import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import React from "react";
import { Routes, Route } from "react-router-dom";
import Homepage from "./pages/Homepage";
// import Layout from "./layout/Layout";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Homepage />} />
    </Routes>
  );
}

export default App;
