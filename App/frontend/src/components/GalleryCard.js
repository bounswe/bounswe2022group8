import { useNavigate } from "react-router-dom";
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
  const navigate = useNavigate();

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
  }

  return (
    <>
      <div className="gallery-container">
        <div className="gallery-header">Discover Exhibitions</div>
        <div className="gallery-row">
          <ImageCard
            onClick={() => goToArtItem(13)}
            source={lost}
            name="Lost Highway"
          />
          <ImageCard
            onClick={() => goToArtItem(14)}
            source={buddhists}
            name="Four Noble Truths"
          />
          <ImageCard
            onClick={() => goToArtItem(15)}
            source={haybales}
            name="Agriculture in the Netherlands"
          />
          <ImageCard
            onClick={() => goToArtItem(16)}
            source={wheat}
            name="Fauvism"
          />
        </div>
        <div className="gallery-row">
          <ImageCard
            onClick={() => goToArtItem(17)}
            source={greenFace}
            name="To Pimp a Butterfly"
          />
          <ImageCard
            onClick={() => goToArtItem(18)}
            source={greenFood}
            name="Green Life"
          />
          <ImageCard
            onClick={() => goToArtItem(19)}
            source={greenCadillac}
            name="1957 Cadillac Eldorado Biarritz "
          />
          <ImageCard
            onClick={() => goToArtItem(20)}
            source={angel}
            name="Forgotten Statues"
          />
        </div>
        <div className="gallery-row">
          <ImageCard
            onClick={() => goToArtItem(21)}
            source={cyber}
            name="One Night in Shangai"
          />
          <ImageCard
            onClick={() => goToArtItem(22)}
            source={bluebuilding}
            name="Architecture in Movies"
          />
          <ImageCard
            onClick={() => goToArtItem(23)}
            source={rome}
            name="Rome: A History of the Eternal City"
          />
          <ImageCard
            onClick={() => goToArtItem(24)}
            source={beach}
            name="West Coast"
          />
        </div>
      </div>
    </>
  );
}

export default GalleryCard;
