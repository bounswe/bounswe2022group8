import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import Signup from "../SignupModal";
import { AuthProvider } from "../../auth/authentication";
import { BrowserRouter } from "react-router-dom";

const MockSignup = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Signup />
      </BrowserRouter>
    </AuthProvider>
  );
};

it("should render the placeholder of the username correctly", async () => {
  render(<MockSignup />);
  expect(screen.getByPlaceholderText("Username")).toBeInTheDocument();
});

it("should render the placeholder of the email correctly", async () => {
    render(<MockSignup />);
    expect(screen.getByPlaceholderText("Email")).toBeInTheDocument();
  });

it("should render the placeholder of the password correctly", async () => {
  render(<MockSignup />);
  expect(screen.getByPlaceholderText("Choose a password")).toBeInTheDocument();
});

it("should render the placeholder of the confirm password correctly", async () => {
    render(<MockSignup />);
    expect(screen.getByPlaceholderText("Confirm password")).toBeInTheDocument();
  });
