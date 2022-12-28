import React, { useState, useEffect } from "react";
import Layout from "../../layout/Layout";
import { useNavigate } from "react-router-dom";
import { HOST } from "../../constants/host";
import * as dotenv from "dotenv";
import { useAuth } from "../../auth/authentication";

import "../styles/Recommendation.css";

function RecommendedExhibitions(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  const navigate = useNavigate();
  const { token } = useAuth();
  var host = HOST;

  const [exhibitionInfos, setExhibitionInfos] = useState([]);
  const [exhibitionPaths, setExhibitionPaths] = useState([]);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  useEffect(() => {
    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/recommendations/exhibitions/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        //console.log(response);
        setExhibitionInfos(response.exhibitions);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var exhibition_posters = [];

        for (let i = 0; i < response.exhibitions.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.exhibitions[i].poster.artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);

          exhibition_posters.push(artitem_url);
        }

        setExhibitionPaths(exhibition_posters);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

  function goToExhibition(id) {
    navigate(`/exhibitions/online/${id}`);
    scrollToTop();
  }

  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommendation-grid">
          <h1 className="page-header">Discover Exhibitions</h1>
          <div className="art-gallery">
            {exhibitionInfos.map((val, index) => {
              return (
                <div
                  key={val.id}
                  className="recommendation-card"
                  onClick={() => goToExhibition(val.id)}
                >
                  <img
                    className="art-related"
                    src={exhibitionPaths[index]}
                    alt={val.description}
                  />
                  <div class="artitem-context">
                    <h4>{val.title}</h4>
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
