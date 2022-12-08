import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import IntroImage from "../IntroImage";
import { AuthProvider } from "../../auth/authentication";

const MockIntroImage = () => {
  return (
    <AuthProvider>
      <IntroImage />
    </AuthProvider>
  );
};

it("should render header of the intro image correctly", async () => {
  render(<MockIntroImage />);
  expect(
    screen.getByText("Present, Manage And Sell Your Art")
  ).toBeInTheDocument();
});

it("should render the content of the intro image correctly", async () => {
  render(<MockIntroImage />);
  expect(
    screen.getByText(
      "Revolutionize the way you promote your art online – with Artopia tools."
    )
  ).toBeInTheDocument();
});
