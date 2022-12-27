import React, { useState, useEffect } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import { IoIosArrowBack } from "react-icons/io";
import { IoIosArrowForward } from "react-icons/io";

import "./styles/Exhibition.css";

function Exhibition(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  var host = HOST;
  const { token } = useAuth();
  const { online_id } = useParams();
  const navigate = useNavigate();

  const [exhbitionSrcs, setExhibitionSrcs] = useState([]);
  const [exhibitionIDs, setExhibitionIDs] = useState([]);
  const [artItemGallerySrcs, setArtItemGallerySrcs] = useState([]);
  const [artItemGalleryIDs, setArtItemGalleryIDs] = useState([]);
  const [artItemUploadSrcs, setArtItemUploadSrcs] = useState([]);
  const [artItemUploadIDs, setArtItemUploadIDs] = useState([]);
  const [ownerID, setOwnerID] = useState(null);
  const [ownerPhoto, setOwnerPhoto] = useState("");
  const [collaboratorSrcs, setCollaboratorSrcs] = useState([]);
  const [collaboratorIDs, setCollaboratorIDs] = useState([]);
  const [exhibitionTitle, setExhibitionTitle] = useState("");
  const [exhibitionDescription, setExhibitionDescription] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [status, setStatus] = useState("");

  const [myID, setMyID] = useState(null);

  const [focusIdx, setFocusIdx] = useState(0);
  const [focusSrc, setFocusSrc] = useState("");
  const [focusID, setFocusID] = useState(0);

  function handleFocus(src, index) {
    setFocusIdx(index);
    setFocusSrc(src);
    setFocusID(exhibitionIDs[index]);
  }

  function handleNext() {
    if (focusIdx !== exhbitionSrcs.length - 1) {
      setFocusIdx(focusIdx + 1);
      setFocusSrc(exhbitionSrcs[focusIdx + 1]);
    }
  }

  function handlePrevious() {
    if (focusIdx !== 0) {
      setFocusIdx(focusIdx - 1);
      setFocusSrc(exhbitionSrcs[focusIdx - 1]);
    }
  }

  const AWS = require("aws-sdk");
  dotenv.config();
  AWS.config.update({
    accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY,
  });

  const s3 = new AWS.S3();

  useEffect(() => {
    fetch(`${host}/api/v1/exhibitions/online/${online_id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        var artitem_gallery_ids = response.artitems_gallery.map(({ id }) => id);
        var artitem_upload_ids = response.artitems_upload.map(({ id }) => id);
        var exhibition_ids = artitem_gallery_ids.concat(artitem_upload_ids);

        setExhibitionTitle(response.title);
        setExhibitionDescription(response.description);
        setOwnerID(response.owner.id);
        setCollaboratorIDs(response.collaborators.map(({ id }) => id));
        setArtItemGalleryIDs(artitem_gallery_ids);
        setArtItemUploadIDs(artitem_upload_ids);
        setExhibitionIDs(exhibition_ids);
        setStartDate(response.start_date);
        setEndDate(response.end_date);
        setStatus(response.status);

        var bucket = process.env.REACT_APP_AWS_STORAGE_BUCKET_NAME;

        var artitem_gallery_srcs = [];
        var artitem_upload_srcs = [];
        var collaborator_srcs = [];

        for (let i = 0; i < response.artitems_gallery.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.artitems_gallery[i].artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);
          artitem_gallery_srcs.push(artitem_url);
        }

        for (let i = 0; i < response.artitems_upload.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.artitems_upload[i].artitem_path,
          };

          var artitem_url = s3.getSignedUrl("getObject", params);
          artitem_upload_srcs.push(artitem_url);
        }

        for (let i = 0; i < response.collaborators.length; i++) {
          var params = {
            Bucket: bucket,
            Key: response.collaborators[i].profile_path,
          };

          var collaborator_profile_url = s3.getSignedUrl("getObject", params);
          collaborator_srcs.push(collaborator_profile_url);
        }

        var params = {
          Bucket: bucket,
          Key: response.owner.profile_path,
        };

        var owner_src = s3.getSignedUrl("getObject", params);

        setArtItemGallerySrcs(artitem_gallery_srcs);
        setArtItemUploadSrcs(artitem_upload_srcs);
        setCollaboratorSrcs(collaborator_srcs);
        setOwnerPhoto(owner_src);

        var exhibition_srcs = artitem_gallery_srcs.concat(artitem_upload_srcs);

        //console.log(response.artitems_gallery);
        //console.log(response.artitems_upload);

        setFocusIdx(0);
        setFocusSrc(exhibition_srcs[0]);
        setFocusID(
          response.artitems_gallery.length > 0
            ? response.artitems_gallery[0].id
            : response.artitems_upload.length > 0
            ? response.artitems_upload[0].id
            : null
        );

        setExhibitionSrcs(exhibition_srcs);
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

  function goToProfile(id) {
    if (myID === id) {
      navigate(`/my-profile`);
    } else {
      navigate(`/users/${id}`);
    }

    scrollToTop();
  }

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
    scrollToTop();
  }

  return (
    <Layout>
      <div className="exhibition-post-container">
        <div className="exhibition-post">
          <div className="exhibition-arrow-container" onClick={handlePrevious}>
            <IoIosArrowBack className="exhibition-arrow" />
          </div>
          <div className="exhibition-container">
            <img className="artitem-focused" src={focusSrc} alt={""} />
            <div className="exhibition-linear-container">
              {exhbitionSrcs.map((source, index) => {
                return (
                  <div
                    key={index}
                    className="exhibition-linear-image-wrap"
                    onClick={() => handleFocus(source, index)}
                    style={{
                      border: index === focusIdx ? "2px solid white" : "none",
                    }}
                  >
                    <img
                      className="exhibition-linear-image"
                      src={source}
                      alt=""
                    />
                    <div className="exhibition-linear-image-cover"></div>
                  </div>
                );
              })}
            </div>
          </div>
          <div className="exhibition-arrow-container" onClick={handleNext}>
            <IoIosArrowForward className="exhibition-arrow" />
          </div>

          <div className="exhibition-info-container">
            <div className="exhibition-collaborators">
              <div className="exhibition-owner">
                <img
                  className="exhibition-owner-profile-photo"
                  src={ownerPhoto}
                  alt=""
                  onClick={() => goToProfile(ownerID)}
                />
              </div>
              {collaboratorSrcs.map((source, index) => {
                return (
                  <div key={index} className="exhibition-owner">
                    <img
                      className="exhibition-owner-profile-photo"
                      src={source}
                      alt=""
                      onClick={() => goToProfile(collaboratorIDs[index])}
                    />
                  </div>
                );
              })}
            </div>

            <header className="exhibition-title">{exhibitionTitle}</header>
            <div className="exhibition-description">
              {exhibitionDescription}
            </div>
            <div className="exhibition-date">
              Start Date: <span style={{ color: "#bcb1c1" }}>{startDate}</span>
            </div>
            <div className="exhibition-date">
              End Date: <span style={{ color: "#bcb1c1" }}>{endDate}</span>
            </div>
            <div className="exhibition-status">
              Status: <i style={{ color: "#bcb1c1" }}>{status}</i>
            </div>
            <Link className="exhibition-visit-link" to={`/artitems/${focusID}`}>
              Visit Art Item
            </Link>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default Exhibition;
