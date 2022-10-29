import "./styles/ImageCard.css";

function ImageCard(props) {
  return (
    <div className="ic-container">
      <img className="ic-image" src={props.source} alt="" />
      <button className="ic-button">{props.name}</button>
    </div>
  );
}

export default ImageCard;