import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// DON'T EDIT ABOVE

import React from "react";
import { Routes, Route } from "react-router-dom";

import { AuthProvider, AuthenticatedRoute } from "./auth/authentication";

import Home from "./pages/Home";
import Profile from "./pages/Profile";

import Recommendation from "./pages/Recommendation";
import RecommendedArtitems from "./pages/RecommendedPages/RecommendedArtitems";
import RecommendedExhibitions from "./pages/RecommendedPages/RecommendedExhibitions";
import RecommendedUsers from "./pages/RecommendedPages/RecommendedUsers";
import ArtItem from "./pages/ArtItem";
import Settings from "./pages/Settings";

import { Recogito } from "@recogito/recogito-js";
import "@recogito/recogito-js/dist/recogito.min.css";

function App() {
  const r = new Recogito({
    content: document.getElementById("root"),
    widgets: ["COMMENT"],
  });

  return (
    <AuthProvider>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route
          path="/discover"
          element={
            <AuthenticatedRoute>
              <Recommendation />
            </AuthenticatedRoute>
          }
        />
        <Route
          path="/discover-artitems"
          element={
            <AuthenticatedRoute>
              <RecommendedArtitems />
            </AuthenticatedRoute>
          }
        />
        <Route
          path="/discover-exhibitions"
          element={
            <AuthenticatedRoute>
              <RecommendedExhibitions />
            </AuthenticatedRoute>
          }
        />
        <Route
          path="/discover-users"
          element={
            <AuthenticatedRoute>
              <RecommendedUsers />
            </AuthenticatedRoute>
          }
        />

        <Route
          path="/my-profile"
          element={
            <AuthenticatedRoute>
              <Profile />
            </AuthenticatedRoute>
          }
        />
        <Route path="/artitems/:artitem_id" element={<ArtItem />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
