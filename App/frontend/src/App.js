import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// DON'T EDIT ABOVE

import React from "react";
import { Routes, Route } from "react-router-dom";
import Homepage from "./pages/Homepage";
import { AuthProvider } from "./auth/authentication";

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<Homepage />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
