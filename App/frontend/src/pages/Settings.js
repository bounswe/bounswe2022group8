import React, { useEffect, useState, useReducer } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../layout/Layout";
import SettingsProfilePopUp from "../components/SettingsProfilePopUp";
import SettingsPasswordPopUp from "../components/SettingsPasswordPopUp";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import * as dotenv from "dotenv";

import "./styles/Settings.css";
import Backdrop from "../components/Backdrop";

function Settings() {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  const { token } = useAuth();
  var host = HOST;

  // profile_image = base64 encoded version of the image --> for updating the profile photo -- PUT
  // profile_path = response from GET e.g --> avatar/default.png  --> private version of the image requested --> ACCESS_DENIED -- GET
  // profile_image_url = signed version of the profile_path  --> for display -- GET

  // For the initial GET
  const [profileInfo, setProfileInfo] = useState({
    username: null,
    email: null,
    name: null,
    about: null,
    location: null,
    profile_image_url: null,
  });

  // For PUT
  const [profileInput, setProfileInput] = useReducer(
    (state, newState) => ({ ...state, ...newState }),
    []
  );

  // For PASSWORD-RESET PUT
  const [newPassword, setNewPassword] = useState("");
  const [newPasswordStatus, setNewPasswordStatus] = useState(null);
  const [newPasswordResponse, setNewPasswordResponse] = useState(null);

  const [isProfilePopUpOpen, setIsProfilePopUpOpen] = useState(false);
  const [isPasswordPopUpOpen, setIsPasswordPopUpOpen] = useState(false);

  const navigate = useNavigate();

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
        });
      })
      .catch((error) => console.error("Error:", error));
  }, [host, token]);

  // console.log(newPassword);

  function handlePasswordChange(e) {
    e.preventDefault();

    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/profile/me/password-reset/`, {
      method: "PUT",
      body: JSON.stringify({
        new_password: newPassword,
      }),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => {
        setNewPasswordStatus(response.status);
        if (response.status === 200) {
          setIsPasswordPopUpOpen(true);
        }
        return response.json();
      })
      .then((response) => {
        // if successfull detail is string,
        // if not and empty detail is string
        // else detail is an array
        if (Array.isArray(response.detail)) {
          setNewPasswordResponse(response.detail[0]);
        } else {
          setNewPasswordResponse(response.detail);
        }
        console.log(response.detail);
      })
      .catch((error) => console.error("Error:", error));

      setNewPassword("");
  }

  async function handlePreview(e) {
    if (e.target.files) {
      let imageFile = e.target.files[0];
      var reader = new FileReader();
      reader.onload = function (e) {
        var img = document.createElement("img");
        img.onload = function () {
          var MAX_WIDTH = 400;
          var MAX_HEIGHT = 400;

          var width = img.width;
          var height = img.height;

          // Change the resizing logic
          if (width > height) {
            if (width > MAX_WIDTH) {
              height = height * (MAX_WIDTH / width);
              width = MAX_WIDTH;
            }
          } else {
            if (height > MAX_HEIGHT) {
              width = width * (MAX_HEIGHT / height);
              height = MAX_HEIGHT;
            }
          }

          var canvas = document.createElement("canvas");
          canvas.width = width;
          canvas.height = height;
          var ctx = canvas.getContext("2d");
          ctx.drawImage(img, 0, 0, width, height);

          // Show resized image in preview element
          var dataurl = canvas.toDataURL(imageFile.type);
          document.getElementById("preview").src = dataurl;
          setProfileInput({ ["profile_image"]: dataurl });
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(imageFile);
    }
  }

  function handleProfileSubmit(e) {
    e.preventDefault();

    // console.log(profileInput);
    fetch(`${host}/api/v1/users/profile/me/`, {
      method: "PUT",
      body: JSON.stringify(profileInput),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => {
        setIsProfilePopUpOpen(true);
        return response.json();
      })
      .then((response) => {})
      .catch((error) => console.error("Error:", error));
  }

  const handleInput = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setProfileInput({ [name]: value });
    // console.log(value);
  };

  function goToProfile() {
    setIsProfilePopUpOpen(false);
    navigate("/my-profile");
    scrollToTop();
  }

  return (
    <Layout>
      {isProfilePopUpOpen && (
        <>
          <SettingsProfilePopUp
            onClickProfile={() => goToProfile()}
            onClickStay={() => setIsProfilePopUpOpen(false)}
          />
          <Backdrop onClick={() => setIsProfilePopUpOpen(false)} />
        </>
      )}
      {isPasswordPopUpOpen && (
        <>
          <SettingsPasswordPopUp
            onClickOkay={() => setIsPasswordPopUpOpen(false)}
          />
          <Backdrop onClick={() => setIsPasswordPopUpOpen(false)} />
        </>
      )}
      <div className="settings-container">
        <header className="settings-header">Settings</header>

        <form className="settings-card">
          <header className="settings-card-header">Profile</header>
          <p className="settings-card-describe">Customize your profile.</p>

          <div className="mt-3">
            <label className="access-label">Profile Photo</label>
            <div className="pp-container mt-1 shadow-sm">
              <img
                src={profileInfo.profile_image_url}
                alt=""
                className="pp-preview"
                id="preview"
              />

              <span className="pp-text">
                <div>Choose an image from your files.</div>
                <div style={{ fontSize: "13px" }}>
                  Min. resolution: 400x400px
                </div>
                <label className="btn btn-primary btn-pp" htmlFor="input-image">
                  Choose Photo
                </label>
                <input
                  type="file"
                  className="mt-1"
                  name="profile_image"
                  id="input-image"
                  accept="image/*"
                  onChange={handlePreview}
                />
              </span>
            </div>
          </div>

          <div className="form-group mt-3">
            <label className="access-label">Name</label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Name"
              name="name"
              id="name"
              defaultValue={profileInfo.name}
              onChange={handleInput}
            />
          </div>

          <div className="form-group mt-3">
            <label className="access-label">Bio</label>
            <textarea
              type="text"
              className="form-control mt-1"
              placeholder="Make yourself known to people"
              name="about"
              id="about"
              defaultValue={profileInfo.about}
              rows="3"
              style={{ resize: "none" }}
              onChange={handleInput}
            />
          </div>

          <div className="form-group mt-3 mb-5">
            <label className="access-label">Location</label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Location"
              name="location"
              id="location"
              defaultValue={profileInfo.location}
              onChange={handleInput}
            />
          </div>

          <div className="settings-btn-container">
            <button className="btn btn-primary" onClick={handleProfileSubmit}>
              Save Changes
            </button>
          </div>
        </form>

        <form className="settings-card">
          <header className="settings-card-header">Password</header>
          <p className="settings-card-describe">Change your password.</p>

          {newPasswordStatus === 400 && (
            <div
              className="form-error"
              style={{
                fontSize: "14px",
              }}
            >
              {newPasswordResponse}
            </div>
          )}

          <div className="form-group mt-3 mb-5">
            <label className="access-label">Password</label>
            <input
              type="password"
              className="form-control mt-1"
              placeholder="New Password"
              id="password"
              name="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
          </div>

          <div className="settings-btn-container">
            <button className="btn btn-primary" onClick={handlePasswordChange}>
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </Layout>
  );
}

export default Settings;
