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
        style={{
          width: "30vw",
          borderRightColor: "white",
          borderTopLeftRadius: "8px",
          borderBottomLeftRadius: "8px",
          borderTopRightRadius: "0px",
          borderBottomRightRadius: "0px",
        }}
        aria-label="Search"
      />
      <InputGroup.Text
        id="search-icon"
        style={{
          backgroundColor: "white",
          borderLeftColor: "white",
          borderTopLeftRadius: "0px",
          borderBottomLeftRadius: "0px",
          borderTopRightRadius: "8px",
          borderBottomRightRadius: "8px",
        }}
      >
        <AiOutlineSearch />
      </InputGroup.Text>
    </InputGroup>
  );
}

export default SearchBar;
