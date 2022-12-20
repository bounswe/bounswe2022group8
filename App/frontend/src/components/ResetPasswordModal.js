import React, { useState } from "react";
import { HOST } from "../constants/host";
import CloseButton from "react-bootstrap/CloseButton";
import { HiArrowLeft } from "react-icons/hi";
import { BsCheckCircle } from "react-icons/bs";
import "./styles/Access.css";

function ResetPassword(props) {
  var host = HOST;

  const [email, setEmail] = useState("");
  const [emailError, setEmailError] = useState(null);
  const [emailSuccess, setEmailSuccess] = useState(null);
  const [otp, setOtp] = useState("");
  const [otpError, setOtpError] = useState(null);
  const [newPassword, setNewPassword] = useState("");
  const [newPasswordError, setNewPasswordError] = useState(null);
  const [resetSuccess, setResetSuccess] = useState(null);

  function handleRequests(e) {
    if (!emailSuccess) handleRequestReset(e);
    else handlePasswordReset(e);
  }

  function handleRequestReset(e) {
    e.preventDefault();

    // dont forget the put the slash at the end
    fetch(`${host}/api/v1/auth/request-reset/`, {
      method: "POST",
      body: JSON.stringify({
        email: email,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.status === 400) {
          setEmailError("No user found with the given email address");
          setEmailSuccess(null);
        } else {
          setEmailError(null);
          setEmailSuccess(
            `Please enter the one-time password we sent and your new password.`
          );
        }

        return response.json();
      })
      .then((response) => {
        // console.log(response);
      })
      .catch((error) => console.error("Error:", error));

    // setEmail("");
  }

  function handlePasswordReset(e) {
    e.preventDefault();

    if (newPassword === "") {
      setNewPasswordError("Password cant be empty");
      setResetSuccess(null);
    } else {
      // dont forget the put the slash at the end
      fetch(`${host}/api/v1/auth/password-reset/`, {
        method: "PUT",
        body: JSON.stringify({
          email: email,
          otp: otp,
          new_password: newPassword,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          return response.json();
        })
        .then((response) => {
          console.log(response);

          if (Array.isArray(response.detail)) {
            setNewPasswordError(response.detail[0]);
            setOtpError(null);
            setResetSuccess(null);
          } else if (response.detail === "Password succesfully reset.") {
            setResetSuccess("Your password has been reset successfully");
            setNewPasswordError(null);
            setOtpError(null);
            setNewPassword("");
            setOtp("");
          } else if (response.detail === "OTP did not match") {
            setOtpError("OTP does not match");
            setNewPasswordError(null);
            setResetSuccess(null);
          }
        })
        .catch((error) => console.error("Error:", error));
    }
  }

  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose} />
      </div>
      <div className="access-content">
        <h3 className="access-title">Forgot password?</h3>

        {emailSuccess ? (
          <div> {emailSuccess}</div>
        ) : (
          <>
            <div>
              Don't worry, we will send you a link to reset your password.
            </div>

            <div className="form-group mt-3">
              <label className="access-label">Email</label>
              <input
                type="email"
                className={`form-control mt-1 + ${
                  emailError ? "form-control-error" : ""
                }`}
                placeholder="Email"
                id="email"
                name="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
          </>
        )}

        {emailError && <div className="form-error">{emailError}</div>}
        {emailSuccess && (
          <>
            {resetSuccess && (
              <div className="form-success mt-3">
                <BsCheckCircle
                  style={{
                    marginBottom: "0.25rem",
                    marginRight: "0.25rem",
                    fontSize: "17px",
                    color: "#198754",
                    strokeWidth: "0px",
                  }}
                />
                {resetSuccess}
              </div>
            )}

            <div className="form-group mt-3">
              <label className="access-label">One-time password</label>
              <input
                type="text"
                className="form-control mt-1"
                placeholder="OTP"
                id="otp"
                name="otp"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
              />
            </div>
            {otpError && <div className="form-error">{otpError}</div>}

            <div className="form-group mt-3">
              <label className="access-label">New password</label>
              <input
                type="password"
                className={`form-control mt-1 + ${
                  newPasswordError ? "form-control-error" : ""
                }`}
                placeholder="Enter your new password"
                id="newPassword"
                name="newPassword"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
              />
            </div>
            {newPasswordError && (
              <div className="form-error">{newPasswordError}</div>
            )}
          </>
        )}

        <div className="d-grid gap-2 mt-3 mb-4">
          <button
            type="submit"
            className="btn btn-primary"
            onClick={(e) => handleRequests(e)}
          >
            Reset Password
          </button>
        </div>
        <div>
          <button
            className="btn btn-light mb-3"
            style={{ color: "#87878b" }}
            onClick={props.onClickBack}
          >
            <HiArrowLeft
              style={{
                marginBottom: "0.2rem",
                marginRight: "0.1rem",
                marginLeft: "-0.5rem",
              }}
            />{" "}
            Back to log in
          </button>
        </div>
      </div>
    </form>
  );
}

export default ResetPassword;
