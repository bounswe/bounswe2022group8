import React from "react";
import { SidebarData } from "./data/SidebarData";
import "./styles/Sidebar.css";
import Button from "react-bootstrap/Button";
import { Link } from "react-router-dom";

function Sidebar(props) {
  return (
    <div className="sidebar-container">
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
    </div>
  );
}

export default Sidebar;
