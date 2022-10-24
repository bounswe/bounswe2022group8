import "./styles/IntroImage.css";
import background from "../media/aurora-high-res.jpg";
import Button from "react-bootstrap/Button";


function IntroImage(props) {
  return (
    <div className="background-image-container">
      <img className="background-image" src={background} alt="Aurora" />
      <div className="input-on-background-image">
        <div className="text-on-background-image">
          <p className="main-header"> PRESENT, MANAGE AND SELL YOUR ART </p>
          <p>
            Revolutionize the way you promote your art online – with APPNAME
            tools.
          </p>
        </div>
        <div className="btn-on-background-image">
          <Button
            as="a"
            variant="secondary"
            style={{
              width: "150px",
              padding: "15px 10px",
              verticalAlign: "middle",
            }}
            onClick={props.onJoinNowClick}
          >
            JOIN NOW
          </Button>
        </div>
      </div>
    </div>
  );
}

export default IntroImage;
