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
    fetch(`${host}/api/v1/artitems/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        //console.log(response);
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
    fetch(`${host}/api/v1/users/profile/users/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        //console.log(response);
        setAllUsers(response);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var profile_photos = [];

        for (let i = 0; i < response.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response[i].profile_path,
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
      <main>
        <div class="recommendation-container">
          <div class="recommended-artitems">
            <h1>
              Discover Art Items <Link to="/discover-artitems">SEE MORE</Link>
            </h1>

            <div class="list">
              {artItemInfos.slice(0, 5).map((val, index) => {
                return (
                  <div
                    key={val.id}
                    className="artitem"
                    onClick={() => goToArtItem(val.id)}
                  >
                    <img src={artItemPaths[index]} alt={val.description} />
                    <div class="context">
                      <h4>{val.title}</h4>
                      <p>{val.description}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div class="recommended-exhibitions">
            <h1>
              Discover Exhibitions{" "}
              <Link to="/discover-exhibitions">SEE MORE</Link>
            </h1>
            <div class="list">
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

          <div class="recommended-users">
            <h1>
              Users you may want to follow...{" "}
              <Link to="/discover-users">SEE MORE</Link>
            </h1>
            <div class="list">
              {allUsers.slice(0, 5).map((val, index) => {
                return (
                  <div
                    key={val.id}
                    className="user"
                    onClick={() => goToProfile(val.id)}
                  >
                    <img src={allUsersPhotos[index]} alt="" />
                    <div class="context">
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
      </main>
    </Layout>
  );
}

export default Recommendation;
