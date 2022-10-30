import React, { useReducer } from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import "./styles/Access.css";

import { useAuth } from "../auth/authentication";

function Login(props) {
  const [loginInput, setLoginInput] = useReducer(
    (state, newState) => ({ ...state, ...newState }),
    {
      credential: "",
      password: "",
    }
  );

  const { saveToken } = useAuth();

  function handleSubmit(event) {
    // props.onSubmitLogIn();

    event.preventDefault();

    saveToken(loginInput.credential);

    //let data = { loginInput };

    fetch("http://127.0.0.1:8000/api/v1/auth/login/", {
      method: "POST",
      body: JSON.stringify(loginInput),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        console.log("Success:", JSON.stringify(response));
        console.log(loginInput);
        props.onSubmitLogIn();
      })
      .catch((error) => console.error("Error:", error));
  }

  const handleInput = (event) => {
    const name = event.target.name;
    const newValue = event.target.value;
    setLoginInput({ [name]: newValue });
  };

  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose} />
      </div>
      <div className="access-content">
        <h3 className="access-title">Log In</h3>
        <div className="form-group mt-3">
          <label className="access-label">Email or username</label>
          <input
            type="email"
            className="form-control mt-1"
            placeholder="Email or username"
            name="credential"
            id="credential"
            required
            defaultValue={loginInput.credential}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className="form-control mt-1"
            placeholder="Password"
            name="password"
            id="password"
            required
            defaultValue={loginInput.password}
            onChange={handleInput}
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
          <a href="./"> Forgot password?</a>
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
