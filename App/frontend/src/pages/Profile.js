import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../layout/Layout";

import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import { CiLocationOn } from "react-icons/ci";
import * as dotenv from "dotenv";
import UploadCard from "../components/UploadCard";
import FirstUploadCard from "../components/FirstUploadCard";
import { BsThreeDotsVertical } from "react-icons/bs";
import DeleteArtItemPopUp from "../components/DeleteArtItemPopUp";
import Backdrop from "../components/Backdrop";
import "./styles/Profile.css";

function Profile(props) {
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

  // just to decide after two unnecessary renders whether the gallery is empty or not
  const [emptyGallery, setEmptyGallery] = useState(null);

  // JUST TO CAUSE A STATE CHANGE AFTER AN ART ITEM POSTED
  const [newImageUploaded, setNewImageUploaded] = useState(true);
  const [artItemDeleted, setArtItemDeleted] = useState(false);

  const [deleteButton, setDeleteButton] = useState(false);
  const [isDeletePopUpOpen, setIsDeletePopUpOpen] = useState(false);
  const [artItemToBeDeletedID, setArtItemToBeDeletedID] = useState(null);
  const [tags, setTags] = useState([]);

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

          if (gallery.length === 0) {
            setEmptyGallery(true);
          } else {
            setEmptyGallery(false);
          }
        })
        .catch((error) => console.error("Error:", error));
    }
  }, [host, token, profileInfo.username, newImageUploaded, artItemDeleted]);

  useEffect(() => {
    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/tags/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        var tagOptions = [];

        for (let i = 0; i < response.length; i++) {
          tagOptions.push({
            value: response[i].id,
            label: response[i].tagname,
          });
        }

        setTags(tagOptions);
      })
      .catch((error) => console.error("Error:", error));
  }, [host, token]);

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

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
    scrollToTop();
  }

  function openDeletePopUp(id) {
    setDeleteButton(false);
    setIsDeletePopUpOpen(true);
    setArtItemToBeDeletedID(id);
  }

  function handleDeleteArtItem() {
    fetch(`${host}/api/v1/artitems/me/remove/${artItemToBeDeletedID}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => {
        setIsDeletePopUpOpen(false);
        setArtItemDeleted(!artItemDeleted);
        scrollToTop();
      })
      .catch((error) => console.error("Error:", error));
  }

  // renders unnecessarily twice --> PROBLEM
  // console.log(userGallery.length);

  return (
    <Layout>
      {isDeletePopUpOpen && (
        <>
          <DeleteArtItemPopUp
            onClickCancel={() => setIsDeletePopUpOpen(false)}
            onClickDelete={(id) => handleDeleteArtItem(id)}
          />
          <Backdrop onClick={() => setIsDeletePopUpOpen(false)} />
        </>
      )}
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
            newImageUploaded={newImageUploaded}
            setNewImageUploaded={() => setNewImageUploaded(!newImageUploaded)}
            closeUploadCard={() => setUpload(false)}
            tags={tags}
          />
          {navTab ? (
            // what if gallery is empty ?
            <>
              {emptyGallery === true && !upload && (
                <div className="gallery-item">
                  <FirstUploadCard onClick={() => handleUpload()} />
                </div>
              )}

              <div className="gallery">
                {userGallery.map((val, key) => {
                  return (
                    <div
                      key={val.id}
                      className="gallery-item"
                      onMouseLeave={() => setDeleteButton(false)}
                    >
                      <img
                        src={val.artitem_path}
                        className="gallery-image"
                        alt={val.description}
                      />
                      <div className="gallery-image-options-container">
                        <div
                          role="link"
                          className="gallery-image-link"
                          onClick={() => goToArtItem(val.id)}
                          style={{
                            pointerEvents: deleteButton ? "none" : "auto",
                            cursor: deleteButton ? "auto" : "pointer",
                          }}
                        ></div>
                        <BsThreeDotsVertical
                          role="select"
                          className="gallery-image-options"
                          onClick={() => setDeleteButton(!deleteButton)}
                        />
                        {deleteButton && (
                          <div
                            role="button"
                            className="delete-card"
                            onClick={() => openDeletePopUp(val.id)}
                          >
                            Delete
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </>
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
