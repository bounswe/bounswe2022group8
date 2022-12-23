import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Layout from "../layout/Layout";

import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import { CiLocationOn } from "react-icons/ci";
import * as dotenv from "dotenv";
import "./styles/Profile.css";

function ProfileOther(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  var host = HOST;
  const { token } = useAuth();
  const { user_id } = useParams();
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
    is_followed: null,
  });

  const [userGallery, setUserGallery] = useState([]);

  // JUST TO CAUSE A STATE CHANGE AFTER A FOLLOW ACTION
  const [updateFollow, setUpdateFollow] = useState(true);

  // FOLLOW CLICK ACTION FOR GUEST USERS
  const [guestClick, setGuestClick] = useState(false);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

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

    fetch(`${host}/api/v1/users/profile/${user_id}`, {
      method: "GET",
      headers: config,
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
          is_followed: response.isFollowed,
        });
      })
      .catch((error) => console.error("Error:", error));
  }, [host, token, updateFollow]);

  // THIS IS BAD.
  useEffect(() => {
    if (profileInfo.username) {
      fetch(`${host}/api/v1/artitems/users/username/${profileInfo.username}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((response) => {
          // console.log(response.length);

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

  function handleArtItems() {
    setNavTab(true);
  }

  function handleExhibitions() {
    setNavTab(false);
  }

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
    scrollToTop();
  }

  function handleFollow() {
    if (token) {
      fetch(`${host}/api/v1/users/follow/${user_id}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => response.json())
        .then((response) => {
          setUpdateFollow(!updateFollow);
        })
        .catch((error) => console.error("Error:", error));
    } else {
      setGuestClick(true);
    }
  }

  function handleUnfollow() {
    fetch(`${host}/api/v1/users/unfollow/${user_id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => {
        setUpdateFollow(!updateFollow);
      })
      .catch((error) => console.error("Error:", error));
  }

  function handleFollowAction() {
    if (profileInfo.is_followed) handleUnfollow();
    else handleFollow();
  }

  // renders unnecessarily twice --> PROBLEM
  // console.log(userGallery.length);

  return (
    <Layout
      guestClick={guestClick}
      cancelGuestClick={() => setGuestClick(false)}
    >
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
              <div style={{ display: "inline" }}>
                <div style={{ display: "inline-block" }}>
                  <h1 className="profile-username">{profileInfo.username} </h1>
                  {profileInfo.name && (
                    <p className="profile-name">{profileInfo.name}</p>
                  )}
                </div>

                <button
                  className="btn profile-follow-btn"
                  style={{ marginBottom: profileInfo.name ? "2.8rem" : "6px" }}
                  onClick={() => handleFollowAction()}
                >
                  {profileInfo.is_followed ? "Following" : "Follow"}
                </button>
              </div>

              {profileInfo.about && (
                <p
                  className="profile-bio"
                  style={{ marginTop: profileInfo.name ? "0.0rem" : "0.8rem" }}
                >
                  {profileInfo.about}
                </p>
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
        </div>

        <hr className="tab-line"></hr>

        <main>
          {navTab ? (
            // what if gallery is empty ?  --> do nothing for the other profile
            <div className="gallery">
              {userGallery.map((val, key) => {
                return (
                  <div key={val.id} className="gallery-item">
                    <img
                      src={val.artitem_path}
                      className="gallery-image"
                      alt={val.description}
                      onClick={() => goToArtItem(val.id)}
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

export default ProfileOther;
