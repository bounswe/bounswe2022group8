import React, { useState, useEffect, useRef } from "react";
import { useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { ANNOHOST, HOST } from "../constants/host";
import Tag from "../components/Tag";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import "./styles/ArtItem.css";

import { Annotorious } from "@recogito/annotorious";
import "@recogito/annotorious/dist/annotorious.min.css";

function ArtItem(props) {
  const { artitem_id } = useParams();

  var host = HOST;
  var annotationhost = ANNOHOST;
  const { token } = useAuth();
  const [userid, setUserid] = useState();

  /*Image Annotation*/
  // Ref to the image DOM element
  const imageElement = useRef(null);

  // The current Annotorious instance
  const [anno, setAnno] = useState();

  const [isHideAnnoButtonClicked, setIsHideAnnoButtonClicked] = useState(false);

  const [clickedAnnotationText, setClickedAnnotationText] = useState(null);
  const [clickedAnnotationOwner, setClickedAnnotationOwner] = useState(null);
  /*Image Annotation*/

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

  useEffect(() => {
    if (token) {
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
          setUserid(response.id);
        })
        .catch((error) => console.error("Error:", error));
    }
  }, [host, token]);

  useEffect(() => {
    /*Image Annotation*/
    if (token) {
      let annotorious = null;

      if (imageElement.current) {
        annotorious = new Annotorious({
          image: imageElement.current,
          widgets: ["COMMENT"],
        });

        //console.log(imageElement);

        // Load annotations in W3C Web Annotation format
        //Loads annotations from a JSON URL.
        //The method returns a promise, in case you want to perform an action after the annotations have loaded
        annotorious
          .loadAnnotations(
            `${annotationhost}/api/v1/annotations/image/artitems/${artitem_id}`
          )
          .catch((error) => console.error("Error:", error));
        /* If there are no annotations on an art item, such error
           Error: TypeError: (e || []).map is not a function at jc.setAnnotations
           may be seen on console 
      */
        annotorious.on("clickAnnotation", function (annotation, element) {
          console.log("annotation", annotation);
          setClickedAnnotationText(annotation.body[0].value);
          fetch(`${host}/api/v1/users/profile/${annotation.creator}`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Token ${token}`,
            },
          })
            .then((response) => response.json())
            .then((response) => {
              //console.log(response);
              setClickedAnnotationOwner(response.username);
            })
            .catch((error) => console.error("Error:", error));
        });

        annotorious.on("cancelSelected", function (selection) {
          setClickedAnnotationText(null);
          setClickedAnnotationOwner(null);
        });

        annotorious.on("changeSelected", function (selected, previous) {
          setClickedAnnotationText(selected.body[0].value);
          fetch(`${host}/api/v1/users/profile/${selected.creator}`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Token ${token}`,
            },
          })
            .then((response) => response.json())
            .then((response) => {
              //console.log(response);
              setClickedAnnotationOwner(response.username);
            })
            .catch((error) => console.error("Error:", error));
        });

        //...annotation backend connection...
        // Event handlers
        annotorious.on("createAnnotation", (annotation) => {
          annotation["creator"] = `${userid}`;
          annotation["target"]["source"] =
            annotation["target"]["source"].split(/[?]/)[0];
          console.log("created", annotation);
          //console.log("JSON.stringfy", JSON.stringify(annotation));
          //fetch with method 'POST'
          fetch(`${annotationhost}/api/v1/annotations/`, {
            method: "POST",
            body: JSON.stringify(annotation),
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((response) => response.json())
            .then((response) => {
              annotation.id = response.id;
            })
            .catch((error) => console.error("Error:", error));
        });

        annotorious.on("updateAnnotation", (annotation, previous) => {
          console.log("updated", annotation);
          console.log("previous", previous);
          //console.log("annotation id", annotation.id);
          //fetch with method 'PUT'
          fetch(`${annotationhost}/api/v1/annotations/`, {
            method: "PUT",
            body: JSON.stringify(annotation),
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then(setClickedAnnotationText(annotation.body[0].value))
            .then(
              fetch(`${host}/api/v1/users/profile/${annotation.creator}`, {
                method: "GET",
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `Token ${token}`,
                },
              })
                .then((response) => response.json())
                .then((response) => {
                  //console.log(response);
                  setClickedAnnotationOwner(response.username);
                })
                .catch((error) => console.error("Error:", error))
            )
            .catch((error) => console.error("Error:", error));
        });

        annotorious.on("deleteAnnotation", (annotation) => {
          console.log("deleted", annotation);
          let annotId = annotation.id.split(/[@]/)[1];
          //console.log("annot id", annotId);
          //fetch with method 'DELETE'
          fetch(`${annotationhost}/api/v1/annotations/${annotId}`, {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then(setClickedAnnotationText(null))
            .then(setClickedAnnotationOwner(null))
            .catch((error) => console.error("Error:", error));
        });
      }
      // Keep current Annotorious instance in state
      setAnno(annotorious);

      // Cleanup: destroy current instance
      return () => annotorious.destroy();
    }
  }, [annotationhost, token, userid]);

  function hideAnnotations() {
    anno.setVisible(false);
    setIsHideAnnoButtonClicked(true);
    setClickedAnnotationText(null);
    setClickedAnnotationOwner(null);
  }
  function showAnnotations() {
    anno.setVisible(true);
    setIsHideAnnoButtonClicked(false);
  }
  return (
    <Layout>
      <div className="artitem-post-container">
        <div className="artitem-post">
          <div id="image-container">
            {token ? (
              <img
                ref={imageElement}
                id="image"
                src={artitemSrc}
                alt={artitemDescription}
              />
            ) : (
              <img id="image" src={artitemSrc} alt={artitemDescription} />
            )}
            <div className="tag-container">
              <Tag tagname="nature"></Tag>
              <Tag tagname="human"></Tag>
              <Tag tagname="architecture"></Tag>
              <Tag tagname="black"></Tag>
              <Tag tagname="pink"></Tag>
              <Tag tagname="night"></Tag>
            </div>

            <div>
              {token ? (
                <button
                  className="anno-show-hide-button"
                  onClick={() => {
                    isHideAnnoButtonClicked
                      ? showAnnotations()
                      : hideAnnotations();
                  }}
                >
                  {isHideAnnoButtonClicked
                    ? "Show Annotations"
                    : "Hide Annotations"}
                </button>
              ) : null}
            </div>

            {token ? (
              <div
                className={
                  clickedAnnotationText
                    ? "display-image-annotation-text-container"
                    : ""
                }
              >
                {clickedAnnotationOwner}
                {" : "}
                {clickedAnnotationText}
              </div>
            ) : null}
          </div>
          <div id="info-container">
            <div id="owner">
              <img id="owner-profile-photo" src={artitemOwnerPhoto} alt="" />
              <div id="owner-username"> {artitemOwnerUsername} </div>
            </div>
            <div id="title-and-description">
              <div id="title">{artitemTitle} </div>
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
