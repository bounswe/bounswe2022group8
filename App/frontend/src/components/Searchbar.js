import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import InputGroup from "react-bootstrap/InputGroup";
import Form from "react-bootstrap/Form";
import { AiOutlineSearch } from "react-icons/ai";
import "./styles/Searchbar.css";

function Searchbar() {
  const navigate = useNavigate();

  const [searchInput, setSearchInput] = useState("");

  function handleSearchInput(e) {
    setSearchInput(e.target.value);
  }

  useEffect(() => {
    const keyDownHandler = (e) => {
      if (e.key === "Enter") {
        e.preventDefault();

        navigate(`/search/${searchInput}`);
      }
    };

    document.addEventListener("keydown", keyDownHandler);

    return () => {
      document.removeEventListener("keydown", keyDownHandler);
    };
  }, [searchInput]);

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
