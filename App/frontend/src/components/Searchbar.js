import { useState } from "react";
import InputGroup from "react-bootstrap/InputGroup";
import Form from "react-bootstrap/Form";
import { AiOutlineSearch } from "react-icons/ai";
import "./styles/Searchbar.css";

function Searchbar(props) {
  const [searchInput, setSearchInput] = useState("");

  function handleSearchInput(e) {
    setSearchInput(e.target.value);
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
        value={searchInput}
        onChange={(e) => handleSearchInput(e)}
      />
    </InputGroup>
  );
}

export default Searchbar;
