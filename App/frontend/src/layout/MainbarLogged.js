import React from "react";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Searchbar from "../components/Searchbar";
import MenuButton from "../components/MenuButton";
import { SlEnvolope } from "react-icons/sl";

import "./styles/Mainbar.css";

function MainbarLogged(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  return (
    <Navbar
      sticky="top"
      expand="md"
      className={
        props.mainbarOpen
          ? "navigation-bar navigation-bar-bg"
          : "navigation-bar"
      }
    >
      <Container fluid>
        <Link to="/" onClick={scrollToTop} style={{ textDecoration: "none" }}>
          <Navbar.Brand className="ms-4 me-5" style={{ color: "white" }}>
            App Name
          </Navbar.Brand>
        </Link>
        <Navbar.Collapse>
          <Nav className="me-auto">
            <Searchbar />
          </Nav>
        </Navbar.Collapse>
        <Nav className="ms-auto">
          <Link to="/:username" onClick={scrollToTop}>
            <Button
              variant="light"
              className={
                !props.mainbarOpen && props.sidebarOpen
                  ? "me-4 btn-logged-sidebar"
                  : "me-4 btn-logged"
              }
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.3}
                stroke="currentColor"
                style={{
                  height: "2.4rem",
                  marginRight: "0.4rem",
                  marginBottom: "0.1rem",
                }}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </Button>
          </Link>
        </Nav>
        <Nav>
          <Button
            variant="light"
            className={
              !props.mainbarOpen && props.sidebarOpen
                ? "me-4 btn-logged-sidebar"
                : "me-4 btn-logged"
            }
          >
            <SlEnvolope style={{ fontSize: "2.1rem", marginRight: "0.4rem" }} />
          </Button>
        </Nav>
        <Nav>
          <MenuButton
            onClick={props.onClickMenu}
            rotate={props.sidebarOpen ? "rotate(90deg)" : "rotate(0)"}
            sidebarStyle={
              !props.mainbarOpen && props.sidebarOpen ? true : false
            }
          />
        </Nav>
      </Container>
    </Navbar>
  );
}

export default MainbarLogged;
