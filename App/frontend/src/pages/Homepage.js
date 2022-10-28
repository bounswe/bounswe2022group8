import React from "react";
import IntroImage from "../components/IntroImage";
import Layout from "../layout/Layout";
import HomeFooter from "../layout/HomeFooter"
import GalleryCard from "../components/GalleryCard";

import "./styles/Homepage.css";

function Homepage(props) {
  return (
    <Layout>
      <IntroImage />
      <GalleryCard />
      <HomeFooter />
    </Layout>
  );
}

export default Homepage;
