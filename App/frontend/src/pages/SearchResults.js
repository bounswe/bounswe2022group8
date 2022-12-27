import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { HOST } from "../constants/host";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import "./styles/Recommendation.css";

function SearchResults(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  var host = HOST;
  const { tag_id } = useParams();
  const navigate = useNavigate();

  const [artItemInfos, setArtItemInfos] = useState([]);
  const [artItemPaths, setArtItemPaths] = useState([]);
  const [tagName, setTagName] = useState([]);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommendation-grid">
          <h1 className="page-header">Search results for {tagName} tag</h1>
          <div className="art-gallery">
            {artItemInfos.map((val, index) => {
              return (
                <div
                  key={val.id}
                  className="recommendation-card"
                  onClick={() => goToArtItem(val.id)}
                >
                  <img
                    className="art-related"
                    src={artItemPaths[index]}
                    alt={val.description}
                  />
                  <div class="artitem-context">
                    <h4>{val.title}</h4>
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

export default SearchResults;
