import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { Link } from "react-router-dom";
import { HOST } from "../constants/host";
import Layout from "../layout/Layout";

import "./styles/Recommendation.css";
import * as dotenv from "dotenv";
import { SampleExhibitions } from "./data/SampleExhibitions";

function Recommendation(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  var host = HOST;
  const { token } = useAuth();
  const navigate = useNavigate();

  const [artItemInfos, setArtItemInfos] = useState([]);
  const [artItemPaths, setArtItemPaths] = useState([]);
  const [exhibitionPaths, setExhibitionPaths] = useState([]);
  const [exhibitionInfos, setExhibitionInfos] = useState([]);
  const [allUsers, setAllUsers] = useState([]);
  const [allUsersPhotos, setAllUsersPhotos] = useState([]);
  const [myID, setMyID] = useState(null);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  useEffect(() => {
    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/recommendations/artitems/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        //console.log(response);
        setArtItemInfos(response.artitems);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var art_item_paths = [];

        for (let i = 0; i < response.artitems.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.artitems[i].artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);

          art_item_paths.push(artitem_url);
        }

        setArtItemPaths(art_item_paths);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

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
        var exhibition_paths = [];

        for (let i = 0; i < response.exhibitions.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.exhibitions[i].artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);

          exhibition_paths.push(artitem_url);
        }

        setExhibitionPaths(exhibition_paths);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

  // GET CURRENTLY LOGGED IN USERS' ID
  // IN REAL SHOULD NOT RECOMMEND HERSELF
  // SHOULD NOT GET HER ID
  useEffect(() => {
    fetch(`${host}/api/v1/users/profile/me/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        setMyID(response.id);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

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

  useEffect(() => {
    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/recommendations/users/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        //console.log(response);
        setAllUsers(response.users);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var profile_photos = [];

        for (let i = 0; i < response.users.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.users[i].profile_path,
          };

          var profile_path = s3.getSignedUrl("getObject", params);

          profile_photos.push(profile_path);
        }

        setAllUsersPhotos(profile_photos);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

  return (
    <Layout>
      <div class="recommendation-container">
        <div class="recommendation-grid">
          <h1>Discover Art Items</h1>

          <div className="see-more">
            <Link to="/discover-artitems" onClick={scrollToTop}>
              SEE MORE
            </Link>
          </div>

          <div class="list">
            {artItemInfos.slice(0, 5).map((val, index) => {
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

        <div class="recommendation-grid">
          <h1>Discover Exhibitions</h1>

          <div className="see-more">
            <Link to="/discover-exhibitions" onClick={scrollToTop}>
              SEE MORE
            </Link>
          </div>

          {exhibitionInfos.length!==0 ? (
            <div class="list">
              {exhibitionInfos.slice(0, 5).map((val, index) => {
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
          ) : (
            <div class="list">
              {SampleExhibitions.map((val, key) => {
                return (
                  <div key={key} className="recommendation-card">
                    <img className="art-related" src={val.src} alt="" />
                    <div class="artitem-context">
                      <h4>{val.name}</h4>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        <div class="recommendation-grid">
          <h1>Users you may want to follow...</h1>

          <div className="see-more">
            <Link to="/discover-users" onClick={scrollToTop}>
              SEE MORE
            </Link>
          </div>

          <div class="list">
            {allUsers.slice(0, 5).map((val, index) => {
              return (
                <div
                  key={val.id}
                  className="recommendation-card"
                  onClick={() => goToProfile(val.id)}
                >
                  <img
                    className="profile-photo"
                    src={allUsersPhotos[index]}
                    alt=""
                  />
                  <div class="profile-context">
                    <h4>{val.username}</h4>
                    <p>{val.name}</p>
                    <p>{val.location}</p>
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

export default Recommendation;
