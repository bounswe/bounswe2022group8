import React, { useState } from "react";
import IntroImage from "../components/IntroImage";
import Layout from "../layout/Layout";
import HomeFooter from "../components/HomeFooter";
import HomeGalleryCard from "../components/HomeGalleryCard";

import "./styles/Home.css";

function Home() {
  const [joinClicked, setJoinClicked] = useState(false);

  return (
    <Layout
      joinClicked={joinClicked}
      cancelJoinClick={() => setJoinClicked(false)}
    >
      <IntroImage onJoinClick={() => setJoinClicked(true)} />
      <HomeGalleryCard />
      <HomeFooter />
    </Layout>
  );
}

export default Home;
