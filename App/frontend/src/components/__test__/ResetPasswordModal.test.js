import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import ResetPassword from "../ResetPasswordModal";

it("should render a go back button", async () => {
  render(<ResetPassword />);
  const goBackButton = screen.getByRole('button', {
    name: /Back to log in/i
  })
  expect(goBackButton).toBeInTheDocument();
});
