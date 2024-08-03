import React from "react";
import { useNavigate } from "react-router-dom";

const SIgnUpForm = () => {
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const signUpObj = Object.fromEntries(formData.entries());

    fetch("http://localhost:8000/api/signup/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(signUpObj),
    })
      .then((response) => {
        if (response.status === 201) {
          alert("signUp Successful ");
          navigate("/login");
        } else {
          alert("signUp failed ");
        }
      })
      .catch((error) => {
        console.error("Error In signUp", error);
      });
  };

  return (
    <div>
      <h2>SignUp Form</h2>
      <div>
        <form action="" onSubmit={handleSubmit}>
          <input type="text" name="first_name" placeholder="Enter first name" />
          <input type="text" name="last_name" placeholder="Enter last name" />
          <input type="text" name="username" placeholder="Enter username" />
          <input type="email" name="email" placeholder="Enter Email ID" />
          <input
            type=" password "
            name="password"
            placeholder="Enter Password"
          />
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
};

export default SIgnUpForm;
