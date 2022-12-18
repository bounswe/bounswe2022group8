import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../auth/authentication";
import Layout from "../../layout/Layout";
import { HOST } from "../../constants/host";
import * as dotenv from "dotenv";

// import "../styles/RecommendedUsers.css";
import "../styles/Recommendation.css";

function RecommendedUsers(props) {
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

  // IN REAL SHOULD NOT RECOMMEND HERSELF
  // SHOULD NOT GET HER ID
  // THIS CHECK SHOULD BE UNNECESSARY
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
      <div className="recommendation-container">
        <div class="recommendation-grid">
          <h1 className="page-header">Users you may want to follow...</h1>
          <div class="list">
            {allUsers.map((val, index) => {
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
                    {/*<p>{val.name}</p>
                    <p>{val.location}</p>*/}
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

export default RecommendedUsers;
