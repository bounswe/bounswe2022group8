import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
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
  const { token } = useAuth();
  const { input } = useParams();
  const navigate = useNavigate();

  const [artItemInfos, setArtItemInfos] = useState([]);
  const [artItemPaths, setArtItemPaths] = useState([]);
  const [exhibitionInfos, setExhibitionInfos] = useState([]);
  const [exhibitionPaths, setExhibitionPaths] = useState([]);
  const [userInfos, setUserInfos] = useState([]);
  const [userPaths, setUserPaths] = useState([]);
  const [noResult, setNoResult] = useState(false);
  const [myID, setMyID] = useState(null);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  useEffect(() => {
    fetch(`${host}/api/v1/search/lexical/?search=${input}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        setArtItemInfos(response);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var art_item_paths = [];

        for (let i = 0; i < response.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response[i].artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);

          art_item_paths.push(artitem_url);
        }

        setArtItemPaths(art_item_paths);
      })
      .catch((error) => console.error("Error:", error));
  }, [host, input]);

  useEffect(() => {
    fetch(`${host}/api/v1/search/lexical/exhibitions/online/?search=${input}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        setExhibitionInfos(response);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var poster_paths = [];

        for (let i = 0; i < response.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response[i].poster.artitem_path,
          };

          var poster_url = s3.getSignedUrl("getObject", params);

          poster_paths.push(poster_url);
        }

        setExhibitionPaths(poster_paths);
      })
      .catch((error) => console.error("Error:", error));
  }, [host, input]);

  useEffect(() => {
    fetch(`${host}/api/v1/search/lexical/users/?search=${input}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        setUserInfos(response);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var user_paths = [];

        for (let i = 0; i < response.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response[i].profile_path,
          };

          var user_url = s3.getSignedUrl("getObject", params);

          user_paths.push(user_url);
        }

        setUserPaths(user_paths);
      })
      .catch((error) => console.error("Error:", error));
  }, [host, input]);

  useEffect(() => {
    var config = {};

    if (token) {
      config = {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      };
    } else {
      config = { "Content-Type": "application/json" };
    }

    fetch(`${host}/api/v1/users/profile/me/`, {
      method: "GET",
      headers: config,
    })
      .then((response) => response.json())
      .then((response) => {
        setMyID(response.id);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

  useEffect(() => {
    if (
      artItemInfos.length === 0 &&
      exhibitionInfos.length === 0 &&
      userInfos.length === 0
    ) {
      setNoResult(true);
    } else {
      setNoResult(false);
    }
  }, [artItemInfos, exhibitionInfos, userInfos]);

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
    scrollToTop();
  }

  function goToExhibition(id) {
    navigate(`/exhibitions/online/${id}`);
    scrollToTop();
  }

  function goToProfile(id) {
    if (myID === id) {
      navigate(`/my-profile`);
    } else {
      navigate(`/users/${id}`);
    }

    scrollToTop();
  }

  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommendation-grid">
          <h1 className="page-header">Search results for {input}</h1>
          <div className="art-gallery">
            {noResult ? (
              <div className="no-results-found">No results found...</div>
            ) : (
              <>
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
                {exhibitionInfos.map((val, index) => {
                  return (
                    <div
                      key={val.id}
                      className="recommendation-card-exhibition"
                      onClick={() => goToExhibition(val.id)}
                    >
                      <img
                        className="art-related"
                        src={exhibitionPaths[index]}
                        alt={val.description}
                      />
                      <div class="artitem-context">
                        <h4 style={{ color: "#f6f6f6" }}>{val.title}</h4>
                        <p style={{ color: "#222222" }}>{val.description}</p>
                      </div>
                    </div>
                  );
                })}
                {userInfos.map((val, index) => {
                  return (
                    <div
                      key={val.id}
                      className="recommendation-card-user"
                      onClick={() => goToProfile(val.id)}
                    >
                      <img
                        className="profile-photo"
                        src={userPaths[index]}
                        alt=""
                      />
                      <div class="profile-context">
                        <h4 style={{ color: "#000000" }}>{val.username}</h4>
                        {/*<p>{val.name}</p>
                    <p>{val.location}</p>*/}
                      </div>
                    </div>
                  );
                })}
              </>
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default SearchResults;
