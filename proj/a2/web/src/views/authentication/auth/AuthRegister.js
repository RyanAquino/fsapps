import React, {useState} from 'react';
import { useNavigate } from "react-router-dom";
import { Box, Typography, Button } from '@mui/material';
import CustomTextField from '../../../components/forms/theme-elements/CustomTextField';
import { Stack } from '@mui/system';
import {registerUser} from "../../../api/utils";

const AuthRegister = ({ title, subtitle, subtext }) => {
    const navigate = useNavigate();
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();

    const registerHandler = async (e) => {
        e.preventDefault();
        const response = await registerUser({"username": username, "password": password}).catch((err) => {
            const statusCode = err.response.status;
            const { detail } = err.response.data;
            console.log(statusCode, detail);
        });

        if (response) {
            navigate("/auth/login");
        }
    }

    return <>
        {title ? (
            <Typography fontWeight="700" variant="h2" mb={1}>
                {title}
            </Typography>
        ) : null}

        {subtext}

        <Box>
            <form onSubmit={registerHandler}>
                <Stack mb={3}>
                    <Typography variant="subtitle1"
                                fontWeight={600} component="label" htmlFor='email' mb="5px" mt="25px">Username</Typography>
                    <CustomTextField id="username" variant="outlined" fullWidth onChange={e => setUserName(e.target.value)} required/>

                    <Typography variant="subtitle1"
                                fontWeight={600} component="label" htmlFor='password' mb="5px"
                                mt="25px">Password</Typography>
                    <CustomTextField id="password" variant="outlined" fullWidth type="password" onChange={e => setPassword(e.target.value)} required/>
                </Stack>
                <Button color="primary" variant="contained" size="large" fullWidth type="submit">
                    Sign Up
                </Button>
            </form>
        </Box>
        {subtitle}
    </>
};

export default AuthRegister;
