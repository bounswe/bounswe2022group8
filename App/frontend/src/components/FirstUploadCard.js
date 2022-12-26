import "./styles/FirstUploadCard.css";

function FirstUploadCard(props) {
  return (
    <div className="first-upload-card-container">
      <div className="first-upload-card-content">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={0.2}
          stroke="currentColor"
          className="first-upload-btn"
          onClick={props.onClick}
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>

        <div className="first-upload-card-header">{props.children}</div>
      </div>
    </div>
  );
}

export default FirstUploadCard;
