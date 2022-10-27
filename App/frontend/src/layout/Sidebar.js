import React from "react";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import { FiLogOut } from "react-icons/fi";
import { SidebarData } from "./data/SidebarData";

import "./styles/Sidebar.css";

function Sidebar(props) {
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
        <Button className="btn-light sidebar-footer-btn">Settings</Button>
        <Button className="btn-light sidebar-footer-btn">
          Log out
          <FiLogOut
            style={{
              marginLeft: "8px",
              marginBottom: "2px",
              fontSize: "15px",
            }}
          />
        </Button>
      </div>
    </div>
  );
}

export default Sidebar;
