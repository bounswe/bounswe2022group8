import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// DON'T EDIT ABOVE

import React from "react";
import { Routes, Route } from "react-router-dom";
import { AuthProvider, AuthenticatedRoute } from "./auth/authentication";

import Home from "./pages/Home";
import Profile from "./pages/Profile";
import ArtItem from "./pages/ArtItem";
import Settings from "./pages/Settings";

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/my-profile"
          element={
            <AuthenticatedRoute>
              <Profile />
            </AuthenticatedRoute>
          }
        />
        <Route path="/artitems/:id" element={<ArtItem />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
