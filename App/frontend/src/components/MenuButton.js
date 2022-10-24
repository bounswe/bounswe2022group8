import Button from "react-bootstrap/Button";
// import { AiOutlineMenu } from "react-icons/ai";
import { SlMenu } from "react-icons/sl";
import { useState } from "react";
import "./styles/MenuButton.css";

function MenuButton() {
  const [rotateMenuButton, setRotateMenuButton] = useState(false);

  const handleRotate = () => setRotateMenuButton(!rotateMenuButton);

  const rotate = rotateMenuButton ? "rotate(90deg)" : "rotate(0)";

  return (
    <Button
      as="a"
      variant="light"
      className="me-4 menu-button"
      onClick={handleRotate}
    >
      <SlMenu
        style={{
          fontSize: "1.7rem",
          transform: rotate,
          transition: "all 0.2s linear",
        }}
      />
    </Button>
  );
}
export default MenuButton;
