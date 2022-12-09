import { render, screen } from "@testing-library/react";
import '@testing-library/jest-dom';
import Searchbar from "../Searchbar";

it("should render placeholder of the searchbar correctly", async () => {
  render(<Searchbar />);
  const placeholder = screen.getByPlaceholderText(
    "Search for images, exhibitions, artists..."
  );
  expect(placeholder).toBeInTheDocument();
});
