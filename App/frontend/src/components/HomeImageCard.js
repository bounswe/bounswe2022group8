import "./styles/HomeImageCard.css";

function HomeImageCard(props) {
  return (
    <div className="ic-container">
      <img className="ic-image" src={props.source} alt="" />
      <button onClick={props.onClick} className="ic-button">
        {props.name}
      </button>
    </div>
  );
}

export default HomeImageCard;
