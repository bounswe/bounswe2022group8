import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import HomeFooter from "../HomeFooter";
import { BrowserRouter } from "react-router-dom";

const MockFooter = () => {
  return (
    <BrowserRouter>
      <HomeFooter />
    </BrowserRouter>
  );
};

it("should render the correct amount of links in the footer", async () => {
  render(<MockFooter />);
  expect(screen.getAllByRole("link").length).toBe(9);
});
