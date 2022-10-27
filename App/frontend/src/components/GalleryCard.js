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
          <ImageCard source={lost} name="Lost Highway" />
          <ImageCard source={buddhists} name="Four Noble Truths" />
          <ImageCard source={haybales} name="Agriculture in the Netherlands" />
          <ImageCard source={wheat} name="Fauvism" />
        </div>
        <div className="gallery-row">
          <ImageCard source={greenFace} name="To Pimp a Butterfly" />
          <ImageCard source={greenFood} name="Green Life" />
          <ImageCard source={greenCadillac} name="1957 Cadillac Eldorado Biarritz " />
          <ImageCard source={angel} name="Forgotten Statues" />
        </div>
        <div className="gallery-row">
          <ImageCard source={cyber} name="One Night in Shangai" />
          <ImageCard source={bluebuilding} name="Architecture in Movies" />
          <ImageCard source={rome} name="Rome: A History of the Eternal City" />
          <ImageCard source={beach} name="West Coast" />
        </div>
      </div>
    </>
  );
}

export default GalleryCard;
