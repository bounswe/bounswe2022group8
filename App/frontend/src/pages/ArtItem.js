import React, { useState, useEffect, useRef } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { ANNOHOST, HOST } from "../constants/host";
import { CategoryDict } from "./data/Categories";
import Tag from "../components/Tag";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";
import { IoIosHeartEmpty } from "react-icons/io";
import { IoIosHeart } from "react-icons/io";

import "./styles/ArtItem.css";

import { Annotorious } from "@recogito/annotorious";
import "@recogito/annotorious/dist/annotorious.min.css";

import { Recogito } from "@recogito/recogito-js";
import "@recogito/recogito-js/dist/recogito.min.css";

//import { BiMessageAltDetail } from "react-icons/bi";

function ArtItem(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

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

  /*Text Annotation*/
  const textElement = useRef(null);

  const [textAnno, setTextAnno] = useState([]);

  //const [displayableTextAnno, setDisplayableTextAnno] = useState(null);
  /*Text Annotation*/
  const { artitem_id } = useParams();
  const navigate = useNavigate();

  const [artitemSrc, setArtitemSrc] = useState("");
  const [artitemTitle, setArtitemTitle] = useState("");
  const [artitemDescription, setArtitemDescription] = useState("");
  const [artitemCategory, setArtitemCategory] = useState("");
  const [artitemOwnerUsername, setArtitemOwnerUsername] = useState("");
  const [artitemOwnerID, setArtitemOwnerID] = useState(null);
  const [artitemComments, setArtitemComments] = useState([]);
  const [artitemLikes, setArtitemLikes] = useState(0);
  const [artitemOwnerPhoto, setArtitemOwnerPhoto] = useState("");
  const [commentPhotos, setCommentPhotos] = useState([]);
  const [isLiked, setIsLiked] = useState(false);
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
    var config = {};

    if (token) {
      config = {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      };
    } else {
      config = { "Content-Type": "application/json" };
    }

    fetch(`${host}/api/v1/artitems/${artitem_id}`, {
      method: "GET",
      headers: config,
    })
      .then((response) => response.json())
      .then((response) => {
        // console.log(response);
        setArtitemTitle(response.title);
        setArtitemDescription(response.description);
        setArtitemCategory(response.category);
        setArtitemOwnerUsername(response.owner.username);
        setArtitemOwnerID(response.owner.id);
        setIsLiked(response.isLiked);

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

  // GET THE ART ITEM'S LIKES
  useEffect(() => {
    fetch(`${host}/api/v1/artitems/${artitem_id}/likers/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        // Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((response) => {
        // console.log(response);
        setArtitemLikes(response.length);
      })
      .catch((error) => console.error("Error:", error));
  }, [host]);

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
          .then(() => {
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

  function handleLike() {
    if (token) {
      if (isLiked) {
        fetch(`${host}/api/v1/users/artitems/${artitem_id}/unlike/`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        })
          .then(() => {
            setIsLiked(!isLiked);
            setArtitemLikes(artitemLikes - 1);
          })
          .catch((error) => console.error("Error:", error));
      } else {
        fetch(`${host}/api/v1/users/artitems/${artitem_id}/like/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        })
          .then(() => {
            setIsLiked(!isLiked);
            setArtitemLikes(artitemLikes + 1);
          })
          .catch((error) => console.error("Error:", error));
      }
    } else {
      setGuestClick(true);
    }
  }

  useEffect(() => {
    // scroll to bottom every time messages change
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [artitemComments]);

  // GET user id of currently logged-in user
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

  /*Image Annotation*/
  useEffect(() => {
    if (token && userid && artitemSrc) {
      let annotorious = null;

      if (imageElement.current) {
        annotorious = new Annotorious({
          image: imageElement.current,
          widgets: ["COMMENT"],
        });

        //console.log(imageElement);

        // Load annotations in W3C Web Annotation format
        // Loads annotations from a JSON URL.
        // The method returns a promise, in case you want to perform an action after the annotations have loaded
        annotorious
          .loadAnnotations(
            `${annotationhost}/api/v1/annotations/image/artitems/${artitem_id}`
          )
          .catch((error) => console.error("Error:", error));
        /* If there are no annotations on an art item, such error
           Error: TypeError: (e || []).map is not a function at jc.setAnnotations
           may be seen on console 
        */

        // Following 3 event handler are to display annotation body under the image
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
          //fetch with method 'POST'
          fetch(`${annotationhost}/api/v1/annotations/`, {
            method: "POST",
            body: JSON.stringify(annotation),
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((response) => response.json())
            .catch((error) => console.error("Error:", error));
        });

        annotorious.on("updateAnnotation", (annotation, previous) => {
          if (annotation.creator === previous.creator) {
            console.log("updated", annotation);
            console.log("previous", previous);
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
          }
        });

        annotorious.on("deleteAnnotation", (annotation) => {
          console.log("deleted", annotation);
          let annotId = annotation.id.split(/[#]/)[1];
          //console.log("annot id", annotId);
          //fetch with method 'DELETE'
          fetch(`${annotationhost}/api/v1/annotations/?id=${annotId}`, {
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
  }, [annotationhost, token, userid, artitemSrc]);

  /*Text Annotation*/
  useEffect(() => {
    if (token && userid && artitemSrc) {
      if (textElement.current) {
        const r = new Recogito({
          content: textElement.current,
          widgets: ["COMMENT"],
        });

        r.loadAnnotations(
          `${annotationhost}/api/v1/annotations/text/artitems/${artitem_id}`
        )
          .then((response) => {
            console.log(response);
          })
          .catch((error) => console.error("Error:", error));

        // Event handlers
        r.on("createAnnotation", (annotation) => {
          console.log("i am here");
          annotation["creator"] = userid;
          annotation["target"]["source"] = artitemSrc.split(/[?]/)[0];
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
              console.log("created in db", response);
            })
            .catch((error) => console.error("Error:", error));
        });

        r.on("updateAnnotation", function (annotation, previous) {
          console.log("updated in frontend", annotation);
          console.log("previous", previous);
          //fetch with method 'PUT'
          fetch(`${annotationhost}/api/v1/annotations/`, {
            method: "PUT",
            body: JSON.stringify(annotation),
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((response) => response.json())
            .then((response) => {
              console.log("updated in db", response);
            })
            .catch((error) => console.error("Error:", error));
        });

        r.on("deleteAnnotation", function (annotation) {
          console.log("deleted", annotation);
          let annotId = annotation.id.split(/[#]/)[1];
          //console.log("annot id", annotId);
          //fetch with method 'DELETE'
          fetch(`${annotationhost}/api/v1/annotations/?id=${annotId}`, {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
            },
          }).catch((error) => console.error("Error:", error));
        });

        setTextAnno(r);

        return () => r.destroy();
      }
    }
  }, [annotationhost, userid, token, artitemSrc]);

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
            {token ? (
              <div id="image-wrap">
                <img
                  id="image"
                  ref={imageElement}
                  src={artitemSrc}
                  alt={artitemDescription}
                  style={{ height: "100%" }}
                />
              </div>
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

            {token ? (
              <div>
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
              </div>
            ) : null}

            <div
              className={
                token && clickedAnnotationText
                  ? "display-image-annotation-text-container"
                  : ""
              }
            >
              {token ? clickedAnnotationOwner : null}
              {token && clickedAnnotationText && clickedAnnotationOwner
                ? " : "
                : null}
              {token ? clickedAnnotationText : null}
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

            <div ref={token ? textElement : null} id="title-and-description">
              <div id="title">{artitemTitle}</div>
              <div id="description">{artitemDescription}</div>
              <em id="category">Category: {CategoryDict[artitemCategory]}</em>
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
              <div id="likes">{artitemLikes} likes</div>
              <div>{artitemComments.length} comments</div>
              <div>
                {isLiked ? (
                  <IoIosHeart
                    style={{
                      fontSize: "1.5rem",
                      cursor: "pointer",
                      strokeWidth: "0.8rem",
                      color: "#ffc9ff",
                    }}
                    onClick={handleLike}
                  />
                ) : (
                  <IoIosHeartEmpty
                    style={{
                      fontSize: "1.5rem",
                      cursor: "pointer",
                      strokeWidth: "0.8rem",
                      color: "#ffffff",
                    }}
                    onClick={handleLike}
                  />
                )}
              </div>
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
