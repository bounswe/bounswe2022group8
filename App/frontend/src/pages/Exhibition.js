import React, { useState, useEffect } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import Layout from "../layout/Layout";
import * as dotenv from "dotenv";

import { SampleGallery } from "./data/SampleGallery";
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

  const [focusIdx, setFocusIdx] = useState(0);
  const [focusSrc, setFocusSrc] = useState(SampleGallery[0].src);

  function handleFocus(src, index) {
    setFocusIdx(index);
    setFocusSrc(src);
  }

  function handleNext() {
    if (focusIdx !== SampleGallery.length - 1) {
      setFocusIdx(focusIdx + 1);
      setFocusSrc(SampleGallery[focusIdx + 1].src);
    }
  }

  function handlePrevious() {
    if (focusIdx !== 0) {
      setFocusIdx(focusIdx - 1);
      setFocusSrc(SampleGallery[focusIdx - 1].src);
    }
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
              {SampleGallery.map((val, index) => {
                return (
                  <div
                    className="exhibition-linear-image-wrap"
                    onClick={() => handleFocus(val.src, index)}
                    style={{
                      border: index === focusIdx ? "2px solid white" : "none",
                    }}
                  >
                    <img
                      className="exhibition-linear-image"
                      src={val.src}
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
                  src={""}
                  alt=""
                />
              </div>
              <div className="exhibition-owner">
                <img
                  className="exhibition-owner-profile-photo"
                  src={""}
                  alt=""
                />
              </div>
              <div className="exhibition-owner">
                <img
                  className="exhibition-owner-profile-photo"
                  src={""}
                  alt=""
                />
              </div>
              <div className="exhibition-owner">
                <img
                  className="exhibition-owner-profile-photo"
                  src={""}
                  alt=""
                />
              </div>
            </div>

            <header className="exhibition-title">Title comes here</header>
            <div className="exhibition-description">
              Description comes here here here here herer herer hehre ehr her h
            </div>
            <div className="exhibition-date">
              Start Date: <span style={{ color: "#bcb1c1" }}>25.12.2022</span>
            </div>
            <div className="exhibition-date">
              End Date: <span style={{ color: "#bcb1c1" }}>27.12.2022</span>
            </div>
            <div className="exhibition-status">
              Status: <i style={{ color: "#bcb1c1" }}>Ongoing</i>
            </div>
            <Link className="exhibition-visit-link">Visit Art Item</Link>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default Exhibition;
