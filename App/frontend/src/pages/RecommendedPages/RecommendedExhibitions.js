import React from "react";
import Layout from "../../layout/Layout";

import { SampleExhibitions } from "../data/SampleExhibitions";
import "../styles/RecommendedExhibitions.css";

function RecommendedExhibitions(props) {
  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommended-exhibitions">
          <div className="gallery">
            {SampleExhibitions.map((val, key) => {
              return (
                <div key={key} className="exhibition">
                  <img src={val.src} alt="" />
                  <div class="context">
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
