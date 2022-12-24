import "./styles/Tag.css";

function Tag(props) {
  return (
    <>
      <button className="artitem-tag" onClick={props.onClick} role="link">
        {props.tagname}
      </button>
    </>
  );
}

export default Tag;
