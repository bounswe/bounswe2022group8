import React, { useState } from "react";
import MainNavigation from "../layout/MainNavigation";
import IntroImage from "../components/IntroImage";
import "./styles/Homepage.css";

function Homepage(props) {
  const [marginWidth, setMarginWidth] = useState("0px");

  function handleSidebar(width) {
    setMarginWidth(width);
  }

  return (
    <div>
      <MainNavigation rightMargin={handleSidebar}/>
      <IntroImage rightMargin={marginWidth}/>
      <div className="slide-deneme" style={{}}>
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
    </div>
  );
}

export default Homepage;
