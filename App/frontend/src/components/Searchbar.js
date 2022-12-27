import { useState } from "react";
import InputGroup from "react-bootstrap/InputGroup";
import Form from "react-bootstrap/Form";
import { AiOutlineSearch } from "react-icons/ai";
import "./styles/Searchbar.css";

function Searchbar() {
  const [input, setInput] = useState("");

  function handleInput(e) {
    setInput(e.target.value);
  }

  return (
    <InputGroup>
      <InputGroup.Text id="search-icon" className="search-icon">
        <AiOutlineSearch />
      </InputGroup.Text>
      <Form.Control
        type="search"
        placeholder="Search for art items, exhibitions, artists..."
        className="search-bar"
        aria-label="Search"
        value={input}
        onChange={(e) => handleInput(e)}
      />
    </InputGroup>
  );
}

export default Searchbar;
