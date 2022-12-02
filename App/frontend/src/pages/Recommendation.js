import React from "react";
import Layout from "../layout/Layout";

import defaultUserImage from "../images/defaultUserImage.png";
import "./styles/Recommendation.css";
import { SampleArtItems } from "./data/SampleArtItems";
import { SampleExhibitions } from "./data/SampleExhibitions";
import { SampleUsers } from "./data/SampleUsers";

function Recommendation(props) {
  return (
    <Layout>
      <main>
        <div class="recommendation-container">
          <div class="recommended-artitems">
            <h1>
              Discover Art Items <a href="/discover-artitems">SEE MORE</a>
            </h1>

            <div class="list">
              {SampleArtItems.map((val, key) => {
                return (
                  <div key={key} className="artitem">
                    <img src={val.src} alt="" />
                    <div class="context">
                      <h4>{val.name}</h4>
                      <p>{val.description}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div class="recommended-exhibitions">
            <h1>
              Discover Exhibitions{" "}
              <a href="/discover-exhibitions">SEE MORE</a>
            </h1>
            <div class="list">
              {SampleExhibitions.map((val, key) => {
                return (
                  <div key={key} className="exhibition">
                    <img src={val.src} alt="" />
                    <div class="context">
                      <h4>{val.name}</h4>
                      <p>{val.owner}</p>
                      <p>{val.date}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          <div class="recommended-users">
            <h1>
              Users you may want to follow...{" "}
              <a href="/discover-users">SEE MORE</a>
            </h1>
            <div class="list">
              {SampleUsers.map((val, key) => {
                return (
                  <div key={key} className="user">
                    <img src={defaultUserImage} alt="" />
                    <div class="context">
                      <h4>{val.username}</h4>
                      <p>{val.name}</p>
                      <p>{val.location}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}

export default Recommendation;
