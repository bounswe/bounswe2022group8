import React, { useState, useReducer } from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import { HiArrowLeft } from "react-icons/hi";
import { HOST } from "../constants/host";
import "./styles/Access.css";

import { useAuth } from "../auth/authentication";

function ResetPassword(props) {
  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose} />
      </div>
      <div className="access-content">
        <h3 className="access-title">Forgot password?</h3>
        <div>No worries, we'll send you a link to reset your password.</div>

        <div className="form-group mt-3">
          <label className="access-label">Email</label>
          <input
            type="email"
            className="form-control mt-1"
            placeholder="Email"
            id="email"
            name="email"
            required
          />
        </div>
        <div className="d-grid gap-2 mt-3 mb-4">
          <button type="submit" className="btn btn-primary">
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
