import "./styles/Tag.css";

function Tag(props) {
  return (
    <>
      <button className="artitem-tag">{props.tagname}</button>
    </>
  );
}

export default Tag;
