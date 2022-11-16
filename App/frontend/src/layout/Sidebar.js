import React from "react";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import { FiLogOut } from "react-icons/fi";
import { SidebarData } from "./data/SidebarData";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";

import "./styles/Sidebar.css";

function Sidebar(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  const { token, clearToken } = useAuth();

  function handleLogOut() {
    var host = HOST;

    fetch(`${host}/api/v1/auth/logout/`, {
      method: "POST",
      body: "",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token " + { token },
      },
    })
      .then(() => {
        clearToken();
        props.onClickLogOut();
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
                <Link to={val.link} onClick={scrollToTop}>
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
            <Link
              to="/settings"
              style={{ display: "contents" }}
              onClick={scrollToTop}
            >
              <Button className="btn-light sidebar-footer-btn">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 25 25"
                  strokeWidth="1.3"
                  stroke="currentColor"
                  style={{
                    height: "1.4rem",
                    marginRight: "0.2rem",
                  }}
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z"
                  />
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
                Settings
              </Button>
            </Link>
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
