import React, { useReducer } from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import "./styles/Access.css";

function Signup(props) {
  const [signupInput, setSignupInput] = useReducer(
    (state, newState) => ({ ...state, ...newState }),
    {
      email: "",
      username: "",
      password: "",
      password_confirm: "",
    }
  );

  function handleSubmit(event) {
    // props.onSubmitSignUp();

    event.preventDefault();

    //let data = { signupInput };

    fetch("http://127.0.0.1:8000/api/v1/auth/register/", {
      method: "POST",
      body: JSON.stringify(signupInput),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => {
        console.log("Success:", JSON.stringify(response));
        props.onSubmitSignUp();
      })
      .catch((error) => console.error("Error:", error));
  }

  const handleInput = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setSignupInput({ [name]: value });
  };

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
            id="username"
            required
            name="username"
            defaultValue={signupInput.username}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Email</label>
          <input
            type="email"
            className="form-control mt-1"
            placeholder="Email"
            id="email"
            required
            name="email"
            defaultValue={signupInput.email}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className="form-control mt-1"
            placeholder="Choose a password"
            id="password"
            required
            name="password"
            defaultValue={signupInput.password}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Confirm password</label>
          <input
            type="password"
            className="form-control mt-1"
            placeholder="Confirm password"
            id="password_confirm"
            required
            name="password_confirm"
            defaultValue={signupInput.password_confirm}
            onChange={handleInput}
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
