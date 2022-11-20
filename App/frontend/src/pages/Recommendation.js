import React from "react";
import Layout from "../layout/Layout";

import defaultUserImage from "../images/defaultUserImage.png";
import "./styles/Recommendation.css";

import "../components/styles/IntroImage.css";

function Recommendation(props) {
  return (
    <Layout>
      <main>
        <div class="recommendation-container">
          <div class="recommended-artitems">
            <h1>
              Discover Art Items <a href="/recommended-artitems">SEE MORE</a>
            </h1>

            <div class="list">
              <div class="artitem">
                <img
                  src="https://i.pinimg.com/564x/6d/a3/b0/6da3b07175eb76fc0f08811ece758e17.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Man in Asia</h4>
                <p>about</p>
              </div>

              <div class="artitem">
                <img
                  src="https://i.pinimg.com/564x/20/d7/6b/20d76bf8d7a9412bdce78791870125b8.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Colorful Faces</h4>
                <p>about</p>
              </div>

              <div class="artitem">
                <img
                  src="https://i.pinimg.com/564x/3e/92/67/3e9267325f7869285126b2a34cf8d932.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Surreal Photography</h4>
                <p>about...</p>
              </div>

              <div class="artitem">
                <img
                  src="https://i.pinimg.com/564x/8c/46/57/8c4657c4fdb8a063e5480fb83b35ddff.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Innovation of Art</h4>
                <p>about</p>
              </div>

              <div class="artitem">
                <img
                  src="https://i.pinimg.com/564x/c4/9e/ad/c49eadf6e0c1d0e0c7caf1cd69f5ed2e.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Power of Red</h4>
                <p>about...</p>
              </div>
            </div>
          </div>

          <div class="recommended-exhibitions">
            <h1>
              Discover Exhibitions{" "}
              <a href="/recommended-exhibitions">SEE MORE</a>
            </h1>
            <div class="list">
              <div class="exhibition">
                <img
                  src="https://i.pinimg.com/564x/54/d1/fd/54d1fd5ba4b122300de1c2a395539034.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Black&White</h4>
                <p>By Edward Bloom on 19/03/2023</p>
              </div>

              <div class="exhibition">
                <img
                  src="https://i.pinimg.com/564x/57/30/f2/5730f27b61b170d9db35f70847a87eab.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Soul of a Woman</h4>
                <p>By Kim Wexler on 12/02/2023</p>
              </div>

              <div class="exhibition">
                <img
                  src="https://i.pinimg.com/564x/4e/cb/f1/4ecbf18f81c68c26246fc6d33b3e2c30.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Reflection Of Light</h4>
                <p>By Ates Arbay on 23/11/2022</p>
              </div>

              <div class="exhibition">
                <img
                  src="https://i.pinimg.com/564x/81/c5/87/81c58779b796cd0d0cd7d4bc9c800941.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Inception</h4>
                <p>By Amelie Poulain</p>
              </div>

              <div class="exhibition">
                <img
                  src="https://i.pinimg.com/564x/c1/0b/91/c10b916b9fe7769833d05c17a7aa42dc.jpg"
                  alt=""
                />
                <div class="context"></div>
                <h4>Guest From The Past</h4>
                <p>By Jake Epping </p>
              </div>
            </div>
          </div>

          <div class="recommended-users">
            <h1>
              Users you may want to follow...{" "}
              <a href="/recommended-users">SEE MORE</a>
            </h1>
            <div class="list">
              <div class="user">
                <img src={defaultUserImage} alt="" />
                <div class="context"></div>
                <h4>EdwardBloom</h4>
                <p>Edward Bloom</p>
                <p>London, UK</p>
              </div>

              <div class="user">
                <img src={defaultUserImage} alt="" />
                <div class="context"></div>
                <h4>worldsBestLawyer</h4>
                <p>Kim Wexler</p>
                <p>Nebraska, USA</p>
              </div>

              <div class="user">
                <img src={defaultUserImage} alt="" />
                <div class="context"></div>
                <h4>BeyzaBoss </h4>
                <p>Beyza Bostan</p>
                <p>Istanbul, Türkiye</p>
              </div>

              <div class="user">
                <img src={defaultUserImage} alt="" />
                <div class="context"></div>
                <h4>AmeliePoulain</h4>
                <p>Paris, France</p>
              </div>

              <div class="user">
                <img src={defaultUserImage} alt="" />
                <div class="context"></div>
                <h4>JakeEppingg</h4>
                <p>USA</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}

export default Recommendation;
