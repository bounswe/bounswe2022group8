import Button from "react-bootstrap/Button";
import { SlMenu } from "react-icons/sl";
import "./styles/MenuButton.css";

function MenuButton(props) {
  return (
    <Button
      variant="light"
      className={
        props.sidebarStyle ? "me-4 menu-button-sidebar" : "me-4 menu-button"
      }
      onClick={props.onClick}
    >
      <SlMenu
        style={{
          fontSize: "1.7rem",
          transform: props.rotate,
          transition: "transform 0.2s linear",
        }}
      />
    </Button>
  );
}

export default MenuButton;
