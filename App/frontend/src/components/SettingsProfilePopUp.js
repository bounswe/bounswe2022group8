import { BsCheckCircle } from "react-icons/bs";
import "./styles/SettingsProfilePopUp.css";

function SettingsProfilePopUp(props) {
  return (
    <div className="settings-profile-pop-up-container">
      <header className="settings-profile-pop-up-header">
        <BsCheckCircle
          style={{
            marginBottom: "0.25rem",
            marginRight: "0.5rem",
            fontSize: "28px",
            color: "#198754",
            strokeWidth: "0px",
          }}
        />
        Your changes have been saved successfully
      </header>
      <div className="settings-profile-pop-up-buttons">
        <button
          onClick={props.onClickProfile}
          className="btn btn-primary settings-profile-pop-up-btn"
        >
          Go to my profile
        </button>
        <button
          onClick={props.onClickStay}
          className="btn btn-primary settings-profile-pop-up-btn"
        >
          Stay
        </button>
      </div>
    </div>
  );
}

export default SettingsProfilePopUp;
