import React from "react";
import Layout from "../../layout/Layout";

import { SampleArtItems } from "../data/SampleArtItems";
import "../styles/RecommendedArtitems.css";
//import "../styles/Recommendation.css";

function RecommendedArtitems(props) {
  function goToArtItem() {
    //navigate to /artitems/id
  }

  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommended-artitems">
          <div className="gallery">
            {SampleArtItems.map((val, key) => {
              return (
                <div key={key} className="artitem" onClick={() => goToArtItem()}>
                  <img src={val.src} alt="" />
                  <div class="context">
                    <h4>{val.name}</h4>
                    <p>{val.description}</p>
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

export default RecommendedArtitems;
