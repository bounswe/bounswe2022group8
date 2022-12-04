import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { HOST } from "../constants/host";
import Tag from "../components/Tag";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import defaultUserImage from "../images/defaultUserImage.png";
import "./styles/ArtItem.css";

function ArtItem(props) {
  const { artitem_id } = useParams();

  var host = HOST;

  const [artitemSrc, setArtitemSrc] = useState("");
  const [artitemDescription, setArtitemDescription] = useState("");
  const [artitemOwnerUsername, setArtitemOwnerUsername] = useState("");
  const [artitemOwnerID, setArtitemOwnerID] = useState(null);
  const [artitemTitle, setArtitemTitle] = useState("");
  const [artitemComments, setArtitemComments] = useState([]);
  const [artitemOwnerPhoto, setArtitemOwnerPhoto] = useState("");
  const [commentPhotos, setCommentPhotos] = useState([]);

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

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
        // console.log(response);
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
  }, [host]);

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
                ></textarea>
              </div>
              <div className="btn-comment-container">
                <button className="btn btn-comment">Send</button>
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
