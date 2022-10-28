import React from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import "./styles/Access.css";

function Login(props) {
  function handleSubmit() {
    props.onSubmitLogIn();
  }

  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose}/>
      </div>
      <div className="access-content">
        <h3 className="access-title">Log In</h3>
        <div className="form-group mt-3">
          <label className="access-label">Email or username</label>
          <input
            type="email"
            className="form-control mt-1"
            placeholder="Email or username"
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className="form-control mt-1"
            placeholder="Password"
          />
        </div>
        <div className="d-grid gap-2 mt-4">
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            Log in
          </button>
        </div>
        <p className="forgot-password text-center mt-3">
          <a href=""> Forgot password?</a>
        </p>
        <p className="text-center mt-2">
          Not on (AppName) yet?{" "}
          <Link onClick={props.onClickSignUp}>Sign up</Link>
        </p>
      </div>
    </form>
  );
}

export default Login;
