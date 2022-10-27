import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import ImageCard from "./ImageCard";
import "./styles/GalleryCard.css";

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

function GalleryCard(props) {
  return (
    <>
      <div className="gallery-container">
        <div className="gallery-header">Discover Exhibitions</div>
        <div className="gallery-row">
          <ImageCard source={lost} name="To Pimp a Butterfly" />
          <ImageCard source={buddhists} name="To Pimp a Butterfly" />
          <ImageCard source={haybales} name="To Pimp a Butterfly" />
          <ImageCard source={wheat} name="To Pimp a Butterfly" />
        </div>
        <div className="gallery-row">
          <ImageCard source={greenFace} name="To Pimp a Butterfly" />
          <ImageCard source={greenFood} name="To Pimp a Butterfly" />
          <ImageCard source={greenCadillac} name="To Pimp a Butterfly" />
          <ImageCard source={angel} name="To Pimp a Butterfly" />
        </div>
        <div className="gallery-row">
          <ImageCard source={cyber} name="To Pimp a Butterfly" />
          <ImageCard source={bluebuilding} name="To Pimp a Butterfly" />
          <ImageCard source={rome} name="To Pimp a Butterfly" />
          <ImageCard source={beach} name="To Pimp a Butterfly" />
        </div>
      </div>
    </>
  );
}

export default GalleryCard;
