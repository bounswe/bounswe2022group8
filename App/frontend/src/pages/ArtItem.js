import React from "react";
import Tag from "../components/Tag";
import Layout from "../layout/Layout";

import defaultUserImage from "../images/defaultUserImage.png";
import "./styles/ArtItem.css";

function ArtItem(props) {
  return (
    <Layout>
      <div className="artitem-post-container">
        <div className="artitem-post">
          <div id="image-container">
            <img id="image" src={props.src} alt={props.description} />
            <div className="tag-container">
              <Tag tagname="nature"></Tag>
              <Tag tagname="casualTag"></Tag>
              <Tag tagname="fauvism"></Tag>
            </div>
          </div>
          <div id="info-container">
            <div id="owner">
              <img id="owner-profile-photo" src={defaultUserImage} alt="" />
              <div id="owner-username"> {props.owner.username} </div>
            </div>
            <div id="title-and-description">
              <div id="title">{props.title}</div>
              <div id="description">{props.description}</div>
            </div>
            <br></br>
            <div id="comments">
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s aşsdlkfj asd aslkdjf laskdjf asdfk
                    jlaskdjf asldfj lakjsd{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s asdf asdf df asdfasdf kldfjkld fkjdlfk
                    jslkdafjl a{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
              <div className="comment">
                <img
                  className="comment-owner-profile-photo"
                  src={defaultUserImage}
                  alt=""
                />
                <div>
                  <div className="comment-owner"> comment owner </div>
                  <div className="comment-text">
                    {" "}
                    asdf asdfas dfaşlskdf asdfjk asdkflaks jflaskdjfl kasdjf
                    lasdkfj asdfkasdjf s{" "}
                  </div>
                  <div className="comment-info"> comment info </div>
                </div>
              </div>
            </div>
            <div id="stats">
              <span id="likes">0 likes</span>
              <span>8 comments</span>
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
