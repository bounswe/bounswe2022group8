import React from "react";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import { FiLogOut } from "react-icons/fi";
import { SidebarData } from "./data/SidebarData";
import { useAuth } from "../auth/authentication";

import "./styles/Sidebar.css";

function Sidebar(props) {
  const { token, clearToken } = useAuth();

  function handleLogOut() {

    fetch("http://127.0.0.1:8000/api/v1/auth/logout/", {
      method: "POST",
      body: "",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token " + { token },
      },
    })
      .then(() => {
        clearToken();
      })
      .catch((error) => console.error("Error:", error));
  }

  return (
    <div className="sidebar-container">
      <div className="sidebar-header" style={{ width: props.width }}></div>
      <div className="sidebar" style={{ width: props.width }}>
        <ul className="sidebar-list">
          {SidebarData.map((val, key) => {
            return (
              <li key={key} className="sidebar-row">
                <Link to={val.link}>
                  <Button className="btn-light sidebar-element">
                    {val.title}
                  </Button>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
      <div className="sidebar-footer" style={{ width: props.width }}>
        {props.auth && (
          <>
            <Button className="btn-light sidebar-footer-btn">Settings</Button>
            <Button
              className="btn-light sidebar-footer-btn"
              onClick={() => handleLogOut()}
            >
              Log out
              <FiLogOut
                style={{
                  marginLeft: "8px",
                  marginBottom: "2px",
                  fontSize: "15px",
                }}
              />
            </Button>
          </>
        )}
      </div>
    </div>
  );
}

export default Sidebar;
