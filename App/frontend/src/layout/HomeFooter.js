import { Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import "./styles/HomeFooter.css";

function Footer(props) {
  return (
    <div className="footer-container">
      <Container>
        <Row align="center">
          <Col className="footer-header">Verification</Col>
          <Col className="footer-header">Copyright Issues</Col>
          <Col className="footer-header">Contact Us</Col>
          <Col className="footer-header">About</Col>
        </Row>
        <Row align="center" className="mb-2">
          <Col>
            <Link to="./" className="footer-element">
              Request a verified badge
            </Link>
          </Col>
          <Col>
            <Link to="./" className="footer-element">
              Claim copyright
            </Link>
          </Col>
          <Col>
            <a
              href="https://github.com/bounswe/bounswe2022group8"
              className="footer-element"
            >
              Github
            </a>
          </Col>
          <Col>
            <Link to="./" className="footer-element">
              License
            </Link>
          </Col>
        </Row>
        <Row align="center" className="mb-2">
          <Col>
            <Link to="./" className="footer-element">
              Need help?
            </Link>
          </Col>
          <Col>
            <Link to="./" className="footer-element">
              Report infringement
            </Link>
          </Col>
          <Col></Col>
          <Col>
            <Link to="./" className="footer-element">
              Terms and Conditions
            </Link>
          </Col>
        </Row>
        <Row align="center" className="mb-2">
          <Col></Col>
          <Col>
            <Link to="./" className="footer-element">
              Need help?
            </Link>
          </Col>
          <Col></Col>
          <Col>
            <Link to="./" className="footer-element">
              FAQ
            </Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Footer;
