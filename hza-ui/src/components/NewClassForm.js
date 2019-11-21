import React from "react";
import _ from "lodash";
import { Form, Button, Container, Row, Col } from "react-bootstrap";

class NewClassForm extends React.Component {
  constructor(props) {
    super(props);
    this.formInput = {
      professor: React.createRef(),
      course_num: React.createRef(),
      semester: React.createRef(),
      confidence: React.createRef()
    };
  }

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  submit = async () => {
    const bodyJSON = {};
    _.forEach(this.formInput, (v, k) => (bodyJSON[k] = v.current.value));

    await fetch("http://localhost:8000/class/", {
      method: "POST",
      headers: {
        Authorization: `JWT ${localStorage.getItem("token")}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(bodyJSON)
    });
  };

  render() {
    return (
      <Container>
        <Col md={{ span: 4, offset: 4 }}>
          <Form>
            <Form.Label className="text-sm-left">Course Number</Form.Label>
            <Form.Control
              ref={this.formInput.course_num}
              type="text"
              placeholder="Ex: CS2500"
            />
            <Form.Text className="text-muted text-sm-left">
              Please do not include spaces/extra words!
            </Form.Text>

            <Form.Label className="text-sm-left">Semester</Form.Label>
            <Form.Control
              ref={this.formInput.semester}
              type="text"
              placeholder="Ex: Fall 2016"
            />

            <Form.Label className="text-sm-left">Confidence</Form.Label>
            <Form.Control
              ref={this.formInput.confidence}
              type="integer"
              placeholder="Ex: 7"
            />

            <Form.Label className="text-sm-left">Professor</Form.Label>
            <Form.Control
              ref={this.formInput.professor}
              type="integer"
              placeholder="Ex: Lerner"
            />
          </Form>
          <Button onClick={this.submit}>Submit</Button>
        </Col>
      </Container>
    );
  }
}

export default NewClassForm;
