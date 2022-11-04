import React from "react";
import IntroImage from "../components/IntroImage";
import Layout from "../layout/Layout";
import HomeFooter from "../components/HomeFooter"
import GalleryCard from "../components/GalleryCard";

import "./styles/Home.css";

function Home(props) {
  return (
    <Layout>
      <IntroImage />
      <GalleryCard />
      <HomeFooter />
    </Layout>
  );
}

export default Home;