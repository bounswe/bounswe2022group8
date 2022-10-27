import React from "react";
import IntroImage from "../components/IntroImage";
import Layout from "../layout/Layout";
import GalleryCard from "../components/GalleryCard";

import "./styles/Homepage.css";

function Homepage(props) {
  return (
    <Layout>
      <IntroImage />
      <GalleryCard />
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
