import React, { useEffect, useState } from "react";
import Layout from "../layout/Layout";

import { HOST } from "../constants/host";
import defaultUserImage from "../images/defaultUserImage.png";
import "./styles/ArtItem.css";
import { useParams } from "react-router-dom";

function ArtItem(props) {
  const { id } = useParams();

  return (
    <Layout>
      <div className="post-container">
        <div className="post">
          <div id="image-container">
            <img
              id="image"
              src="https://i.pinimg.com/564x/b5/f3/09/b5f309be0e4c2c67057e53f2ec336def.jpg"
              alt=""
            />
          </div>

          <div id="info-container">
            <div id="owner">
              <img id="owner-profile-photo" src={defaultUserImage} alt="" />
              <div id="owner-username"> Kostanya</div>
            </div>
            <div id="description-and-comments">
              <div id="description">
                If people knew how hard I worked to get my mastery, it wouldn’t
                seem so wonderful at all. - Michelangelo.
              </div>
              <br></br>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div className="comment-owner"> comment owner </div>
                <div className="comment-text"> comment text </div>
                <div className="comment-info"> comment info </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div className="comment-owner"> comment owner </div>
                <div className="comment-text"> comment text </div>
                <div className="comment-info"> comment info </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div className="comment-owner"> comment owner </div>
                <div className="comment-text"> comment text </div>
                <div className="comment-info"> comment info </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div className="comment-owner"> comment owner </div>
                <div className="comment-text"> comment text </div>
                <div className="comment-info"> comment info </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div className="comment-owner"> comment owner </div>
                <div className="comment-text"> comment text </div>
                <div className="comment-info"> comment info </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div className="comment-owner"> comment owner </div>
                <div className="comment-text"> comment text </div>
                <div className="comment-info"> comment info </div>
              </div>
            </div>
            <span id="stats">0 likes</span>

            <div className="add-comment-container">
              <input
                className="add-comment-input"
                placeholder="Add comment..."
                name="comment"
              ></input>
              <button className="btn-comment">Send</button>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default ArtItem;
