import React from 'react'
import { useNavigate } from 'react-router-dom'

const LoginForm = () => {
    const navigate = useNavigate()

    const handleSubmit = async (e) =>{
        e.preventDefault()
        const formData = new FormData(e.target)
        const loginObj = Object.fromEntries(formData.entries())

        try {
            const response = await fetch("http://localhost:8000/api/login/",{
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    },
                    body: JSON.stringify(loginObj),     
            });
            const data = await response.json()
            if(!data.token){
                alert("Login Failed")
            }else{
                localStorage.setItem("token", data.token)
                navigate("/")
            }
        } catch (error) {
            console.error("Error In Login",error)
        }
    }

  return (
    <div>
        <h2>Login Form</h2>
        <div>
            <form action="" onSubmit={handleSubmit}>
                <input type="email" name='email' placeholder='Enter Email ID' />
                <input type=" password " name='password' placeholder='Enter Password' />
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
  )
}

export default LoginForm