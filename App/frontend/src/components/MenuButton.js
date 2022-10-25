import Button from "react-bootstrap/Button";
// import { AiOutlineMenu } from "react-icons/ai";
import { SlMenu } from "react-icons/sl";
import "./styles/MenuButton.css";

function MenuButton(props) {
  return (
    <Button
      as="a"
      variant="light"
      className= {props.sidebarStyle ? "me-4 menu-button-sidebar"  : "me-4 menu-button"}
      onClick={props.onClick}
    >
      <SlMenu
        style={{
          fontSize: "1.7rem",
          transform: props.rotate,
          transition: "all 0.2s linear",
        }}
      />
    </Button>
  );
}
export default MenuButton;
