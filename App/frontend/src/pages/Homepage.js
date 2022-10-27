import React from "react";
import IntroImage from "../components/IntroImage";
import Layout from "../layout/Layout";
import ImageCard from "../components/ImageCard";
import cyber from "../images/cyber.jpg";
import buddhists from "../images/buddhists.jpg";
import haybales from "../images/haybales.jpg";
import rome from "../images/rome.jpg";
import angel from "../images/angel.jpg";
import lost from "../images/lost.jpg";
import beach from "../images/beach.jpg";
import wheat from "../images/wheat.jpg";
import greenFace from "../images/greenface.jpg";
import greenFood from "../images/greenfood.jpg";
import bluebuilding from "../images/bluebuilding.jfif";
import greenCadillac from "../images/greencadillac.jfif";


import "./styles/Homepage.css";

function Homepage(props) {
  return (
    <Layout>
      <IntroImage />
      <ImageCard source={lost} name="To Pimp a Butterfly" />
      <ImageCard source={buddhists} name="To Pimp a Butterfly" />
      <ImageCard source={haybales} name="To Pimp a Butterfly" />
      <ImageCard source={wheat} name="To Pimp a Butterfly" />
      <ImageCard source={greenFace} name="To Pimp a Butterfly" />
      <ImageCard source={greenFood} name="To Pimp a Butterfly" />
      <ImageCard source={greenCadillac} name="To Pimp a Butterfly" />
      <ImageCard source={angel} name="To Pimp a Butterfly" />
      <ImageCard source={cyber} name="To Pimp a Butterfly" />
      <ImageCard source={bluebuilding} name="To Pimp a Butterfly" />
      <ImageCard source={rome} name="To Pimp a Butterfly" />
      <ImageCard source={beach} name="To Pimp a Butterfly" />
      <div className="slide-deneme">
        <div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
          <div className="deneme">HOMEPAGE5</div>
        </div>
      </div>
    </Layout>
  );
}

export default Homepage;
