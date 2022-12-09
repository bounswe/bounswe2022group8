import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import SettingsPasswordPopUp from "../SettingsPasswordPopUp";
import { AuthProvider } from "../../auth/authentication";

const MockSettingsPasswordPopUp = () => {
  return (
    <AuthProvider>
      <SettingsPasswordPopUp />
    </AuthProvider>
  );
};

it("should render header of the settings password pop up correctly", async () => {
  render(<MockSettingsPasswordPopUp />);
  expect(
    screen.getByText("Your password has been updated successfully")
  ).toBeInTheDocument();
});

it("should render okay button", async () => {
    render(<SettingsPasswordPopUp />);
    const okayButton = screen.getByRole('button', {
      name: /Okay/i
    })
    expect(okayButton).toBeInTheDocument();
  });
