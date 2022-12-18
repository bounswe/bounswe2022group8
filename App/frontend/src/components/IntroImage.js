import React from "react";
import Button from "react-bootstrap/Button";
import background from "../images/aurora.jpg";
import { useAuth } from "../auth/authentication";

import "./styles/IntroImage.css";

function IntroImage(props) {
  const { token } = useAuth();

  return (
    <div>
      <div className="background-image-container">
        <img className="background-image" src={background} alt="Aurora" />
        <div className="input-on-background-image">
          <div className="text-on-background-image">
            <p className="main-header"> Present, Manage And Sell Your Art </p>
            <p>
              Revolutionize the way you promote your art online – with Artopia
              tools.
            </p>
          </div>
          {!token && (
            <div className="btn-on-background-image-container">
              <Button
                className="btn-on-background-image"
                as="a"
                variant=""
                onClick={props.onJoinClick}
              >
                JOIN NOW
              </Button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default IntroImage;
