import { useNavigate } from "react-router-dom";
import HomeImageCard from "./HomeImageCard";
import "./styles/HomeGalleryCard.css";

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

function HomeGalleryCard(props) {
  const navigate = useNavigate();

  function goToArtItem(id) {
    navigate(`/artitems/${id}`);
  }

  return (
    <>
      <div className="gallery-container">
        <div className="gallery-header">Featured Art Items</div>
        <div className="gallery-row">
          <HomeImageCard
            onClick={() => goToArtItem(1)}
            source={lost}
            name="Lost Highway"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={buddhists}
            name="Four Noble Truths"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={haybales}
            name="Agriculture in the Netherlands"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={wheat}
            name="Fauvism"
          />
        </div>
        <div className="gallery-row">
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={greenFace}
            name="To Pimp a Butterfly"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={greenFood}
            name="Green Life"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={greenCadillac}
            name="1957 Cadillac Eldorado Biarritz "
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={angel}
            name="Forgotten Statues"
          />
        </div>
        <div className="gallery-row">
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={cyber}
            name="One Night in Shangai"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={bluebuilding}
            name="Architecture in Movies"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={rome}
            name="Rome: A History of the Eternal City"
          />
          <HomeImageCard
            onClick={
              {
                /*() => goToArtItem(13)*/
              }
            }
            source={beach}
            name="West Coast"
          />
        </div>
      </div>
    </>
  );
}

export default HomeGalleryCard;
