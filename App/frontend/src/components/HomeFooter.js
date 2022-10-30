import { Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import "./styles/HomeFooter.css";

function Footer(props) {
  return (
    <div className="homefooter-container">
      <Container className="homefooter">
        <Row align="center">
          <Col className="homefooter-header">Verification</Col>
          <Col className="homefooter-header">Copyright Issues</Col>
          <Col className="homefooter-header">Contact Us</Col>
          <Col className="homefooter-header">About</Col>
        </Row>
        <Row align="center" className="mb-2">
          <Col>
            <Link to="./" className="homefooter-element">
              Request a verified badge
            </Link>
          </Col>
          <Col>
            <Link to="./" className="homefooter-element">
              Claim copyright
            </Link>
          </Col>
          <Col>
            <a
              href="https://github.com/bounswe/bounswe2022group8"
              className="homefooter-element"
            >
              Github
            </a>
          </Col>
          <Col>
            <Link to="./" className="homefooter-element">
              License
            </Link>
          </Col>
        </Row>
        <Row align="center" className="mb-2">
          <Col>
            <Link to="./" className="homefooter-element">
              Need help?
            </Link>
          </Col>
          <Col>
            <Link to="./" className="homefooter-element">
              Report infringement
            </Link>
          </Col>
          <Col></Col>
          <Col>
            <Link to="./" className="homefooter-element">
              Terms and Conditions
            </Link>
          </Col>
        </Row>
        <Row align="center" className="mb-2">
          <Col></Col>
          <Col>
            <Link to="./" className="homefooter-element">
              Need help?
            </Link>
          </Col>
          <Col></Col>
          <Col>
            <Link to="./" className="homefooter-element">
              FAQ
            </Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Footer;
