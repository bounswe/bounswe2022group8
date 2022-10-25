import React from "react";
import { SidebarData } from "./data/SidebarData";
import "./styles/Sidebar.css";
import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="sidebar-container">
      <div className="sidebar">
        <ul className="sidebar-list">
          {SidebarData.map((val, key) => {
            return (
              <li key={key} className="sidebar-row">
                <Link to={val.link}>{val.title}</Link>
              </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
}

export default Sidebar;
