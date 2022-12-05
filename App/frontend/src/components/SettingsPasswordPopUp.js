import { BsCheckCircle } from "react-icons/bs";
import "./styles/SettingsPasswordPopUp.css";

function SettingsPasswordPopUp(props) {
  return (
    <div className="settings-password-pop-up-container">
      <header className="settings-password-pop-up-header">
        <BsCheckCircle
          style={{
            marginBottom: "0.25rem",
            marginRight: "0.5rem",
            fontSize: "28px",
            color: "#198754",
            strokeWidth: "0px",
          }}
        />
        Your password has been updated successfully 
      </header>
      <div className="settings-password-pop-up-buttons">
        <button
          onClick={props.onClickOkay}
          className="btn btn-primary settings-password-pop-up-btn"
        >
          Okay
        </button>
      </div>
    </div>
  );
}

export default SettingsPasswordPopUp;
