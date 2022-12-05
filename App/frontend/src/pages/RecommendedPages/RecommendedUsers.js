import React, { useState, useEffect } from "react";
import Layout from "../../layout/Layout";
import { HOST } from "../../constants/host";
import * as dotenv from "dotenv";

import defaultUserImage from "../../images/defaultUserImage.png";
import "../styles/RecommendedUsers.css";

function RecommendedUsers(props) {
  var host = HOST;

  const [allUsers, setAllUsers] = useState([]);
  const [allUsersPhotos, setAllUsersPhotos] = useState([]);

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

  return (
    <Layout>
      <div className="recommendation-container">
        <div class="recommended-users">
          <div class="userlist">
            {allUsers.map((val, index) => {
              return (
                <div key={val.id} className="user">
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
    </Layout>
  );
}

export default RecommendedUsers;
