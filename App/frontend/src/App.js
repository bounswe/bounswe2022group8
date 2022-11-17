import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// DON'T EDIT ABOVE

import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import { AuthProvider } from "./auth/authentication";

import Profile from "./pages/Profile";

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/:username" element={<Profile />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
