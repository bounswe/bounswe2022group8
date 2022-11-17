import React, { useEffect, useState } from "react";
import Layout from "../layout/Layout";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import * as dotenv from "dotenv";

import "./styles/Settings.css";

function Settings() {
  const { token } = useAuth();
  var host = HOST;

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
        const AWS = require("aws-sdk");
        dotenv.config();
        AWS.config.update({
          accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
          secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
        });

        const s3 = new AWS.S3();

        var params = {
          Bucket: process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME,
          Key: "avatar/eye.jpg",
        };

        var profile_image_url = s3.getSignedUrl("getObject", params);

        setProfileInfo({
          username: response.username,
          email: response.email,
          name: response.name,
          about: response.about,
          location: response.location,
          profile_image: profile_image_url,
        });
      })
      .catch((error) => console.error("Error:", error));
  }, [host, token]);

  function handlePreview(e) {
    if (e.target.files) {
      console.log(e.target.files);
      let imageFile = e.target.files[0];
      var reader = new FileReader();
      reader.onload = function (e) {
        var img = document.createElement("img");
        img.onload = function () {
          var MAX_WIDTH = 300;
          var MAX_HEIGHT = 300;

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
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(imageFile);
    }
  }

  function handleSubmit(e) {
    e.preventDefault();
  }

  return (
    <Layout>
      <div className="settings-container">
        <header className="settings-header">Settings</header>

        <form className="settings-card">
          <header className="settings-card-header">Profile</header>
          <p className="settings-card-describe">Customize your profile.</p>

          <div className="mt-3">
            <label className="access-label">Profile Photo</label>
            <div className="pp-container mt-1 hadow-sm">
              <img
                src={profileInfo.profile_image}
                alt=""
                className="pp-preview"
                id="preview"
              />

              <span className="pp-text">
                <div>Choose an image from your files.</div>
                <div style={{ fontSize: "13px" }}>
                  Min. resolution: 300x300px
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
            />
          </div>

          <div className="form-group mt-3">
            <label className="access-label">Bio</label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Make yourself known to people"
              name="about"
              id="about"
              defaultValue={profileInfo.about}
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
            />
          </div>

          <div className="settings-btn-container">
            <button className="btn btn-primary" onClick={handleSubmit}>
              Save Changes
            </button>
          </div>
        </form>

        <form className="settings-card">
          <header className="settings-card-header">Password</header>
          <p className="settings-card-describe">Change your password.</p>

          <div className="form-group mt-3 mb-5">
            <label className="access-label">Password</label>
            <input
              type="password"
              className="form-control mt-1"
              placeholder="New Password"
              id="password"
              required
              name="password"
            />
          </div>

          <div className="settings-btn-container">
            <button className="btn btn-primary" onClick={handleSubmit}>
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </Layout>
  );
}

export default Settings;
