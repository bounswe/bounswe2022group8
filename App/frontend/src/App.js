import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// DON'T EDIT ABOVE

import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import { AuthenticatedRoute, AuthProvider } from "./auth/authentication";

import Profile from "./pages/Profile";
import Recommendation from "./pages/Recommendation";
import RecommendedArtitems from "./pages/RecommendedPages/RecommendedArtitems";
import RecommendedExhibitions from "./pages/RecommendedPages/RecommendedExhibitions";
import RecommendedUsers from "./pages/RecommendedPages/RecommendedUsers";

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/:username" element={<Profile />} />
        <Route path="/just-for-you" element={<AuthenticatedRoute><Recommendation/></AuthenticatedRoute>} />
        <Route path="/recommended-artitems" element={<AuthenticatedRoute><RecommendedArtitems /></AuthenticatedRoute>} />
        <Route path="/recommended-exhibitions" element={<AuthenticatedRoute><RecommendedExhibitions /></AuthenticatedRoute>} />
        <Route path="/recommended-users" element={<AuthenticatedRoute><RecommendedUsers/></AuthenticatedRoute>} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
