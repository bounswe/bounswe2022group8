import InputGroup from "react-bootstrap/InputGroup";
import Form from "react-bootstrap/Form";
import { AiOutlineSearch } from "react-icons/ai";
import "./styles/Searchbar.css";

function Searchbar() {
  return (
    <InputGroup>
      <InputGroup.Text id="search-icon" className="search-icon">
        <AiOutlineSearch />
      </InputGroup.Text>
      <Form.Control
        type="search"
        placeholder="Search for images, galleries, artists..."
        className="search-bar"
        aria-label="Search"
      />
    </InputGroup>
  );
}

export default Searchbar;
