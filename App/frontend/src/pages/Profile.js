import React, { useEffect, useState, useReducer } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../layout/Layout";
import UploadCard from "../components/UploadCard";

import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import { CiLocationOn } from "react-icons/ci";
import * as dotenv from "dotenv";
import "./styles/Profile.css";

function Profile(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  const { token } = useAuth();
  var host = HOST;

  const navigate = useNavigate();

  const [profileInfo, setProfileInfo] = useState({
    username: null,
    email: null,
    name: null,
    about: null,
    location: null,
    profile_image_url: null,
    followers: 0,
    followings: 0,
  });

  const [userGallery, setUserGallery] = useState([]);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  useEffect(() => {
    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/users/profile/me/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        //console.log(response);

        var params = {
          Bucket: process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME,
          Key: response.profile_path,
        };

        // signed profile image url --> for display in frontend
        var profile_image_url = s3.getSignedUrl("getObject", params);

        setProfileInfo({
          username: response.username,
          email: response.email,
          name: response.name,
          about: response.about,
          location: response.location,
          profile_image_url: profile_image_url,
          followers: response.followers,
          followings: response.followings,
        });
      })
      .catch((error) => console.error("Error:", error));
  }, [host, token]);

  // THIS IS BAD.
  useEffect(() => {
    if (profileInfo.username) {
      fetch(`${host}/api/v1/artitems/users/username/${profileInfo.username}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => response.json())
        .then((response) => {
          console.log(response.length);

          var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
          var gallery = [];

          for (let i = 0; i < response.length; i++) {
            var params = {
              Bucket: bucket,
              Key: response[i].artitem_path,
            };

            var artitem_url = s3.getSignedUrl("getObject", params);

            gallery.push({
              id: response[i].id,
              owner: response[i].owner,
              title: response[i].title,
              description: response[i].description,
              type: response[i].type,
              tags: response[i].tags,
              artitem_path: artitem_url,
              created_at: response[i].created_at,
            });
          }

          setUserGallery(gallery);
        })
        .catch((error) => console.error("Error:", error));
    }
  }, [host, token, profileInfo.username]);

  // true -> art item --- false -> exhibition
  const [navTab, setNavTab] = useState(true);
  const [upload, setUpload] = useState(false);
  const [postError, setPostError] = useState(false); // essentially for the upload card
  const [uploadInfoError, setUploadInfoError] = useState(false); // essentially for the upload card

  function handleArtItems() {
    setNavTab(true);
    setUpload(false);
  }

  function handleExhibitions() {
    setNavTab(false);
    setUpload(false);
  }

  function handleUpload() {
    setUpload(!upload);
    setPostError(false);
    setUploadInfoError(false);
  }

  function goToArtItem(id, artitem_path, description, owner, title) {
    fetch(`${host}/api/v1/artitems/${id}/comments/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        console.log(response.data);
        props.onArtItemClick(artitem_path, description, owner, title, response.data);
        navigate(`/artitems/${id}`);
        scrollToTop();
      })
      .catch((error) => console.error("Error:", error));
  }

  return (
    <Layout>
      <div className="profile-page-container">
        <header>
          <div className="profile-container">
            <div className="profile-photo-container">
              <img
                className="profile-photo"
                src={profileInfo.profile_image_url}
                alt=""
              />
            </div>
            <div>
              <div>
                <h1 className="profile-username">{profileInfo.username} </h1>
              </div>

              {profileInfo.name && (
                <p className="profile-name">{profileInfo.name}</p>
              )}
              {profileInfo.about && (
                <p className="profile-bio">{profileInfo.about}</p>
              )}
              {profileInfo.location && (
                <p className="profile-location">
                  <CiLocationOn
                    style={{
                      marginBottom: "0.2rem",
                      marginLeft: "-0.3rem",
                      marginRight: "0.1rem",
                    }}
                  />

                  {profileInfo.location}
                </p>
              )}

              <div className="profile-stat-count">
                {/* dont forget the space after the number */}
                <span className="profile-follow-number">
                  {profileInfo.followers}{" "}
                </span>
                <span className="profile-follow">Followers</span>
                <span className="profile-follow-number">
                  {profileInfo.followings}{" "}
                </span>
                <span className="profile-follow">Following</span>
              </div>
            </div>
          </div>
        </header>

        <div className="tab-container">
          <button
            className={`btn btn-navtab + ${
              navTab ? "btn-navtab-underline" : ""
            }`}
            onClick={() => handleArtItems()}
          >
            Art Items
          </button>
          <button
            className={`btn btn-navtab + ${
              !navTab ? "btn-navtab-underline" : ""
            }`}
            onClick={() => handleExhibitions()}
          >
            Exhibitions
          </button>
          <button className="btn btn-upload" onClick={() => handleUpload()}>
            Upload
          </button>
        </div>

        <hr className="tab-line"></hr>

        <main>
          <UploadCard
            height={upload ? "535px" : "0px"}
            border={upload ? "2px dashed #bcb1c1" : "2px dashed transparent"}
            marginBottom={upload ? "1rem" : "0rem"}
            postError={postError}
            setPostError={(error) => setPostError(error)}
            uploadInfoError={uploadInfoError}
            setUploadInfoError={(error) => setUploadInfoError(error)}
          />
          {navTab ? (
            // what if gallery is empty ?
            <div className="gallery">
              {userGallery.map((val, key) => {
                return (
                  <div key={val.id} className="gallery-item">
                    <img
                      src={val.artitem_path}
                      className="gallery-image"
                      alt={val.description}
                      onClick={() =>
                        goToArtItem(
                          val.id,
                          val.artitem_path,
                          val.description,
                          val.owner,
                          val.title
                        )
                      }
                    />
                  </div>
                );
              })}
            </div>
          ) : (
            <div className="gallery">
              <div className="gallery-item" tabIndex="0">
                <img
                  src="https://i.pinimg.com/564x/c9/e3/a0/c9e3a04419c70017ce6bfd2bd7c88a67.jpg"
                  className="gallery-image"
                  alt=""
                />
              </div>
              <div className="gallery-item" tabIndex="0">
                <img
                  src="https://i.pinimg.com/564x/26/ca/72/26ca72d8a74429381c310677c0bfc576.jpg"
                  className="gallery-image"
                  alt=""
                />
              </div>
              <div className="gallery-item" tabIndex="0">
                <img
                  src="https://i.pinimg.com/564x/26/ca/72/26ca72d8a74429381c310677c0bfc576.jpg"
                  className="gallery-image"
                  alt=""
                />
              </div>
            </div>
          )}
        </main>
      </div>
    </Layout>
  );
}

export default Profile;
