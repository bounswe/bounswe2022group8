import React from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import "./styles/Access.css";

function Signup(props) {
  function handleSubmit() {
    props.onSubmitSignUp();
  }

  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose} />
      </div>
      <div className="access-content">
        <h3 className="access-title">Sign Up</h3>
        <div className="text-center">
          Already registered? <Link onClick={props.onClickLogIn}>Log in</Link>
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Username</label>
          <input
            type="text"
            className="form-control mt-1"
            placeholder="Username"
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Email</label>
          <input
            type="email"
            className="form-control mt-1"
            placeholder="Email"
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className="form-control mt-1"
            placeholder="Choose a password"
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Confirm password</label>
          <input
            type="password"
            className="form-control mt-1"
            placeholder="Confirm password"
          />
        </div>
        <div className="d-grid gap-2 mt-4 mb-4">
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            Sign Up
          </button>
        </div>
      </div>
    </form>
  );
}

export default Signup;
