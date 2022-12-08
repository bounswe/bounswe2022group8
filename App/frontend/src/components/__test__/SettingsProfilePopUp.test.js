import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import SettingsProfilePopUp from "../SettingsProfilePopUp";
import { AuthProvider } from "../../auth/authentication";

const MockSettingsProfilePopUp = () => {
  return (
    <AuthProvider>
      <SettingsProfilePopUp />
    </AuthProvider>
  );
};

it("should render header of the settings password pop up correctly", async () => {
  render(<MockSettingsProfilePopUp />);
  expect(
    screen.getByText("Your changes have been saved successfully")
  ).toBeInTheDocument();
});

it("should render go to my profile button", async () => {
    render(<SettingsProfilePopUp />);
    const goToMyProfileButton = screen.getByRole('button', {
      name: /Go to my profile/i
    })
    expect(goToMyProfileButton).toBeInTheDocument();
});

  it("should render stay button", async () => {
    render(<SettingsProfilePopUp />);
    const stayButton = screen.getByRole('button', {
      name: /Stay/i
    })
    expect(stayButton).toBeInTheDocument();
});
