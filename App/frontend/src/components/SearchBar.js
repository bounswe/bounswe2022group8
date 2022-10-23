import InputGroup from "react-bootstrap/InputGroup";
import Form from "react-bootstrap/Form";
import { BsSearch } from "react-icons/bs";

function SearchBar() {
  return (
    <InputGroup>
      <InputGroup.Text
        id="search-icon"
        style={{ backgroundColor: "white", borderRadius: "0" }}
      >
        <BsSearch />
      </InputGroup.Text>
      <Form.Control
        type="search"
        placeholder="Search"
        className="shadow-sm"
        style={{ width: "30vw" }}
        aria-label="Search"
      />
    </InputGroup>
  );
}

export default SearchBar;
