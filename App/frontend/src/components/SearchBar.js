import InputGroup from "react-bootstrap/InputGroup";
import Form from "react-bootstrap/Form";
import { AiOutlineSearch } from "react-icons/ai";

function SearchBar() {
  return (
    <InputGroup>
      <Form.Control
        type="search"
        placeholder="Search"
        className="shadow-none"
        style={{ width: "30vw", borderRightColor: "white", outline : "none",}}
        aria-label="Search"
      />
      <InputGroup.Text
        id="search-icon"
        style={{
          backgroundColor: "white",
          borderLeftColor: "white",
        }}
      >
        <AiOutlineSearch />
      </InputGroup.Text>
    </InputGroup>
  );
}

export default SearchBar;
