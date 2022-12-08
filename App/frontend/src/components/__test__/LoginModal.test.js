import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import Login from "../LoginModal";
import { AuthProvider } from "../../auth/authentication";
import { BrowserRouter } from "react-router-dom";

const MockLogin = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    </AuthProvider>
  );
};

it("should render the placeholder of the credentials correctly", async () => {
  render(<MockLogin />);
  expect(screen.getByPlaceholderText("Email or username")).toBeInTheDocument();
});

it("should render the placeholder of the password correctly", async () => {
  render(<MockLogin />);
  expect(screen.getByPlaceholderText("Password")).toBeInTheDocument();
});
