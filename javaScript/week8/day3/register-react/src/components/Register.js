import React from "react";

class Register extends React.Component {
  constructor() {
    super();
    this.state = {
      firstname: "",
      lastname: "",
      email: "",
      username: "",
      password: "",
      message: "",
    };
  }

  //every time we call handleChange it will set the propety according to the name
  handleChange = (e) => {
    // console.log(e.target.value);
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = () => {
    const { firstname, lastname, email, username, password } = this.state;
    console.log(firstname, lastname, email, username, password);
    fetch("http://localhost:5000/register", {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({ firstname, lastname, email, username, password }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        this.setState({ message: data.message });
      })
      .catch((e) => {
        console.log(e);
      });
  };

  render() {
    return (
      <>
        <h4>Register</h4> <br />
        <div>
          <input
            onChange={this.handleChange}
            type="text"
            name="firstname"
            placeholder="First Name"
          ></input>{" "}
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="lastname"
            placeholder="Last Name"
          ></input>{" "}
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="email"
            placeholder="Email"
          ></input>{" "}
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="username"
            placeholder="Username"
          ></input>{" "}
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="password"
            placeholder="Password"
          ></input>{" "}
          <br />
          <button onClick={this.handleSubmit}>Submit</button> <br />
          <div>{this.state.message}</div>
        </div>
      </>
    );
  }
}

export default Register;
