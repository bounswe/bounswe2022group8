import React from "react";
import Layout from "../../layout/Layout";
import { SampleUsers } from "../data/SampleUsers";

import defaultUserImage from "../../images/defaultUserImage.png";
import "../styles/RecommendedUsers.css";

function RecommendedUsers(props) {
  return (
    <Layout>
      <div className="recommendation-container">
        <div class="recommended-users">
            <div class="userlist">
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
    </Layout>
    );}

export default RecommendedUsers;