import React from "react";
import { Link } from "react-router-dom";

function Signup(props) {

  function handleSubmit(){
    props.onSubmitSignUp();
  }

  return (
    <div className="form-container">
      <form className="form">
        <div className="form-content">
          <h3 className="form-title">Sign Up</h3>
          <div className="text-center">
            Already registered? <Link onClick={props.onClickLogIn}>Log in</Link>
          </div>
          <div className="form-group mt-3">
            <label>Username</label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Username"
            />
          </div>
          <div className="form-group mt-3">
            <label>Email</label>
            <input
              type="email"
              className="form-control mt-1"
              placeholder="Email"
            />
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              type="password"
              className="form-control mt-1"
              placeholder="Password"
            />
          </div>
          <div className="d-grid gap-2 mt-4 mb-4">
            <button type="submit" className="btn btn-primary" onClick={handleSubmit}>
              Sign Up
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default Signup;
