import "./styles/DeleteArtItemPopUp.css";

function DeleteArtItemPopUp(props) {
  return (
    <div className="delete-artitem-pop-up-container">
      <header className="delete-artitem-pop-up-header">
        {props.navTab === 0 ? (
          <>Are you sure you want to delete your Art Item?</>
        ) : (
          <>Are you sure you want to delete your exhibition?</>
        )}
      </header>
      <div className="delete-artitem-pop-up-buttons">
        <button
          onClick={props.onClickCancel}
          className="btn btn-secondary delete-artitem-pop-up-btn"
        >
          Cancel
        </button>
        <button
          onClick={props.onClickDelete}
          className="btn btn-primary delete-artitem-pop-up-btn"
        >
          Delete
        </button>
      </div>
    </div>
  );
}

export default DeleteArtItemPopUp;
