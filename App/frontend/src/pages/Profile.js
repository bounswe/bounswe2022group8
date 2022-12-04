import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../layout/Layout";
import { SampleGallery } from "./data/SampleGallery";

import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import defaultUserImage from "../images/defaultUserImage.png";
import { CiLocationOn } from "react-icons/ci";
import "./styles/Profile.css";

function Profile(props) {
  const { token } = useAuth();
  var host = HOST;

  const navigate = useNavigate();

  const [profileInfo, setProfileInfo] = useState({
    username: null,
    email: null,
    name: null,
    about: null,
    location: null,
    profile_image: null,
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
        setProfileInfo({
          username: response.username,
          email: response.email,
          name: response.name,
          about: response.about,
          location: response.location,
          profile_image: response.profile_image,
        });
      })
      .catch((error) => console.error("Error:", error));
  }, [host, token]);

  // true -> art item --- false -> exhibition
  const [navTab, setNavTab] = useState(true);

  function handleArtItems() {
    setNavTab(true);
  }

  function handleExhibitions() {
    setNavTab(false);
  }

  function goToArtItem() {
    navigate("/artitems/:id");
  }

  return (
    <Layout>
      <div className="profile-page-container">
        <header>
          <div className="profile-container">
            <div className="profile-photo-container">
              <img className="profile-photo" src={defaultUserImage} alt="" />
            </div>
            <div>
              <div>
                <h1 className="profile-username">Kostanya </h1>
              </div>

              <p className="profile-name">Furkan Keskin</p>
              <p className="profile-bio">
                Hello! I am a junior Computer Engineering student at Boğaziçi
                University.
              </p>
              <p className="profile-location">
                <CiLocationOn
                  style={{
                    marginBottom: "0.2rem",
                    marginLeft: "-0.3rem",
                    marginRight: "0.1rem",
                  }}
                />
                Istanbul, Turkey
              </p>

              <div className="profile-stat-count">
                {/* dont forget the space after the number */}
                <span className="profile-follow-number">123 </span>
                <span className="profile-follow">Followers</span>
                <span className="profile-follow-number">0 </span>
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
          <button className="btn btn-upload">Upload</button>
        </div>

        <hr className="tab-line"></hr>

        <main>
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
