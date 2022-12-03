import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../layout/Layout";
import UploadCard from "../components/UploadCard";
import { SampleGallery } from "./data/SampleGallery";

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
        console.log(response);
        const AWS = require("aws-sdk");
        dotenv.config();
        AWS.config.update({
          accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
          secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
        });

        const s3 = new AWS.S3();

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

  // true -> art item --- false -> exhibition
  const [navTab, setNavTab] = useState(true);
  const [upload, setUpload] = useState(false);
  const [postError, setPostError] = useState(false); // essentially for the upload card

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
  }

  function goToArtItem() {
    navigate("/artitems/:id");
    scrollToTop();
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
          />
          {navTab ? (
            // what if gallery is empty ?
            <div className="gallery">
              {SampleGallery.map((val, key) => {
                return (
                  <div key={key} className="gallery-item">
                    <img
                      src={val.src}
                      className="gallery-image"
                      alt=""
                      onClick={() => goToArtItem()}
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
