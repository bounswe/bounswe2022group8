import React, { useState, useEffect, useRef } from "react";
import { useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import Tag from "../components/Tag";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import "./styles/ArtItem.css";

function ArtItem(props) {
  const { artitem_id } = useParams();

  var host = HOST;
  const { token } = useAuth();

  const [artitemSrc, setArtitemSrc] = useState("");
  const [artitemDescription, setArtitemDescription] = useState("");
  const [artitemOwnerUsername, setArtitemOwnerUsername] = useState("");
  const [artitemOwnerID, setArtitemOwnerID] = useState(null);
  const [artitemTitle, setArtitemTitle] = useState("");
  const [artitemComments, setArtitemComments] = useState([]);
  const [artitemOwnerPhoto, setArtitemOwnerPhoto] = useState("");
  const [commentPhotos, setCommentPhotos] = useState([]);

  // COMMENT BODY TO BE POSTED
  const [newComment, setNewComment] = useState("");

  // JUST TO CAUSE A STATE CHANGE AFTER A COMMENT POSTED
  const [updateComments, setUpdateComments] = useState(true);

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
        setArtitemOwnerID(response.owner.id);
        setArtitemTitle(response.title);

        var params = {
          Bucket: process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME,
          Key: response.artitem_path,
        };

        setArtitemSrc(s3.getSignedUrl("getObject", params));
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

  // UNNECESSARY API CALL JUST TO GET THE PROFILE PATH OF THE ART ITEM OWNER
  useEffect(() => {
    if (artitemOwnerID) {
      fetch(`${host}/api/v1/users/profile/${artitemOwnerID}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          // Authorization: `Token ${token}`,
        },
      })
        .then((response) => response.json())
        .then((response) => {
          var params = {
            Bucket: process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME,
            Key: response.profile_path,
          };

          setArtitemOwnerPhoto(s3.getSignedUrl("getObject", params));
        })
        .catch((error) => console.error("Error:", error));
    }
  }, [host, artitemOwnerID]);

  function handleSendComment(e) {
    e.preventDefault();
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

    // clear the input box after the message is sent
    setNewComment("");
  }

  useEffect(() => {
    // scroll to bottom every time messages change
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [artitemComments]);

  return (
    <Layout>
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
              <img id="owner-profile-photo" src={artitemOwnerPhoto} alt="" />
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
