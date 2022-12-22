import React, { useState, useEffect, useRef } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import Tag from "../components/Tag";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import "./styles/ArtItem.css";

function ArtItem(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  var host = HOST;
  const { token } = useAuth();
  const { artitem_id } = useParams();
  const navigate = useNavigate();

  const [artitemSrc, setArtitemSrc] = useState("");
  const [artitemDescription, setArtitemDescription] = useState("");
  const [artitemOwnerUsername, setArtitemOwnerUsername] = useState("");
  // const [artitemOwnerID, setArtitemOwnerID] = useState(null);
  const [artitemTitle, setArtitemTitle] = useState("");
  const [artitemComments, setArtitemComments] = useState([]);
  const [artitemOwnerPhoto, setArtitemOwnerPhoto] = useState("");
  const [commentPhotos, setCommentPhotos] = useState([]);
  const [myID, setMyID] = useState(null);

  // COMMENT BODY TO BE POSTED
  const [newComment, setNewComment] = useState("");

  // JUST TO CAUSE A STATE CHANGE AFTER A COMMENT POSTED
  const [updateComments, setUpdateComments] = useState(true);

  // SEND COMMENT CLICK ACTION FOR GUEST USERS
  const [guestClick, setGuestClick] = useState(false);

  // DUMMY DIV IN ORDER TO DETECT THE END OF THE MESSAGES
  const bottomRef = useRef(null);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  // GET THE ART ITEM'S PROPERTIES
  useEffect(() => {
    fetch(`${host}/api/v1/artitems/${artitem_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        // console.log(response);
        setArtitemDescription(response.description);
        setArtitemOwnerUsername(response.owner.username);
        setArtitemTitle(response.title);

        var params_artitem = {
          Bucket: process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME,
          Key: response.artitem_path,
        };

        setArtitemSrc(s3.getSignedUrl("getObject", params_artitem));

        var params_owner_pp = {
          Bucket: process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME,
          Key: response.owner.profile_path,
        };

        setArtitemOwnerPhoto(s3.getSignedUrl("getObject", params_owner_pp));
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

  // GET THE ART ITEM'S COMMENTS
  useEffect(() => {
    fetch(`${host}/api/v1/artitems/${artitem_id}/comments/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        // console.log(response)
        setArtitemComments(response.data);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;
        var comment_photos = [];

        for (let i = 0; i < response.data.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.data[i].commented_by.profile_path,
          };

          var profile_url = s3.getSignedUrl("getObject", params);
          comment_photos.push(profile_url);
        }

        setCommentPhotos(comment_photos);
      })
      .catch((error) => console.error("Error:", error));
  }, [host, updateComments]);

  // GET CURRENTLY LOGGED IN USERS' ID
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

  function handleSendComment(e) {
    e.preventDefault();
    if (token) {
      if (newComment !== "") {
        fetch(`${host}/api/v1/artitems/${artitem_id}/comments/`, {
          method: "POST",
          body: JSON.stringify({
            body: newComment,
          }),
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        })
          .then((response) => response.json())
          .then((response) => {
            setUpdateComments(!updateComments);
          })
          .catch((error) => console.error("Error:", error));
      }
    } else {
      setGuestClick(true);
    }

    // clear the input box after the message is sent
    setNewComment("");
  }

  useEffect(() => {
    // scroll to bottom every time messages change
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [artitemComments]);

  function goToProfile(id) {
    if (myID === id) {
      navigate(`/my-profile`);
    } else {
      navigate(`/users/${id}`);
    }

    scrollToTop();
  }

  return (
    <Layout
      guestClick={guestClick}
      cancelGuestClick={() => setGuestClick(false)}
    >
      <div className="artitem-post-container">
        <div className="artitem-post">
          <div id="image-container">
            <img id="image" src={artitemSrc} alt={artitemDescription} />
            <div className="tag-container">
              <Tag tagname="nature"></Tag>
              <Tag tagname="human"></Tag>
              <Tag tagname="architecture"></Tag>
              <Tag tagname="black"></Tag>
              <Tag tagname="pink"></Tag>
              <Tag tagname="night"></Tag>
            </div>
          </div>
          <div id="info-container">
            <div id="owner">
              <img
                id="owner-profile-photo"
                src={artitemOwnerPhoto}
                alt=""
                onClick={() => goToProfile(artitemOwnerID)}
              />
              <div id="owner-username"> {artitemOwnerUsername} </div>
            </div>
            <div id="title-and-description">
              <div id="title">{artitemTitle}</div>
              <div id="description">{artitemDescription}</div>
            </div>
            <br></br>
            <div id="comments">
              {artitemComments.length === 0 && (
                <div
                  style={{
                    color: "#bcb1c1",
                    fontSize: "14px",
                    textAlign: "center",
                  }}
                >
                  No comments yet
                </div>
              )}
              {artitemComments.map((val, index) => {
                return (
                  <div key={val.id} className="comment">
                    <img
                      className="comment-owner-profile-photo"
                      src={commentPhotos[index]}
                      alt=""
                      onClick={() => goToProfile(val.commented_by.id)}
                    />
                    <div>
                      <div className="comment-owner">
                        {val.commented_by.username}
                      </div>
                      <div className="comment-text">{val.body}</div>
                      <div className="comment-info"> {val.created_at} </div>
                    </div>
                  </div>
                );
              })}
              <div ref={bottomRef} />
            </div>
            <div id="stats">
              <span id="likes">0 likes</span>
              <span>{artitemComments.length} comments</span>
            </div>
            <div className="add-comment-container">
              <div>
                <textarea
                  type="text"
                  className="add-comment-input"
                  placeholder="Add comment..."
                  name="comment"
                  rows="3"
                  value={newComment}
                  onChange={(e) => setNewComment(e.target.value)}
                ></textarea>
              </div>
              <div className="btn-comment-container">
                <button
                  className="btn btn-comment"
                  type="submit"
                  onClick={handleSendComment}
                >
                  Send
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/*<div className="artitem-post-properties">
        <div className="tag-container">
          <div className="tag"></div>
        </div>
      </div>*/}
    </Layout>
  );
}

export default ArtItem;
