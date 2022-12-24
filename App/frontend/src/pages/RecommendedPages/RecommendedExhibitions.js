import React from "react";
import Layout from "../../layout/Layout";

import { SampleExhibitions } from "../data/SampleExhibitions";

import "../styles/Recommendation.css";

function RecommendedExhibitions(props) {
  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommendation-grid">
          <h1 className="page-header">Discover Exhibitions</h1>
          <div className="list">
            {SampleExhibitions.map((val, key) => {
              return (
                <div key={key} className="recommendation-card">
                  <img className="art-related" src={val.src} alt="" />
                  <div class="artitem-context">
                    <h4>{val.name}</h4>
                    <p>{val.owner}</p>
                    <p>{val.date}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default RecommendedExhibitions;
