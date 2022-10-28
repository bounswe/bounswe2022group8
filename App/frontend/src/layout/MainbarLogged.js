import React from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Searchbar from "../components/Searchbar";
import MenuButton from "../components/MenuButton";
import { CgProfile } from "react-icons/cg";
import { BiEnvelope } from "react-icons/bi";
import { FiUser } from "react-icons/fi";
import { HiOutlineUserCircle } from "react-icons/hi";
import { SlEnvolope } from "react-icons/sl";

import "./styles/Mainbar.css";

function MainbarLogged(props) {
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
        <Navbar.Brand
          className="ms-4 me-5"
          href="./"
          style={{ color: "white" }}
        >
          App Name
        </Navbar.Brand>
        <Navbar.Collapse>
          <Nav className="me-auto">
            <Searchbar />
          </Nav>
        </Navbar.Collapse>
        <Nav className="ms-auto">
          <Button
            variant="light"
            className={
              !props.mainbarOpen && props.sidebarOpen
                ? "me-4 btn-logged-sidebar"
                : "me-4 btn-logged"
            }
          >
            <HiOutlineUserCircle style={{ fontSize: "2rem", marginRight: "0.4rem" }} />
          </Button>
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
            <SlEnvolope style={{ fontSize: "2rem", marginRight: "0.3rem" }} />
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
