import React from "react";
import IntroImage from "../components/IntroImage";
import Layout from "../layout/Layout";
import HomeFooter from "../components/HomeFooter"
import HomeGalleryCard from "../components/HomeGalleryCard";

import "./styles/Home.css";

function Home(props) {
  return (
    <Layout>
      <IntroImage />
      <HomeGalleryCard />
      <HomeFooter />
    </Layout>
  );
}

export default Home;
