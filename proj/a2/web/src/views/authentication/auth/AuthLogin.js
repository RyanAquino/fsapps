import React from 'react';
import { useNavigate } from "react-router-dom";
import {
    Box,
    Typography,
    FormGroup,
    FormControlLabel,
    Button,
    Stack,
    Checkbox
} from '@mui/material';
import { Link } from 'react-router-dom';

import CustomTextField from '../../../components/forms/theme-elements/CustomTextField';

const AuthLogin = ({ title, subtitle, subtext }) => {
    const navigate = useNavigate();

    const loginHandler = async (e) => {
      e.preventDefault();
      console.log("Insert login logic here")
      navigate("/dashboard");
    }

    return (
      <>
        {title ? (
          <Typography fontWeight="700" variant="h2" mb={1}>
            {title}
          </Typography>
        ) : null}

        {subtext}

        <form onSubmit={loginHandler}>
          <Stack>
            <Box>
              <Typography variant="subtitle1"
                          fontWeight={600} component="label" htmlFor='username' mb="5px">Username</Typography>
              <CustomTextField id="username" variant="outlined" fullWidth />
            </Box>
            <Box mt="25px">
              <Typography variant="subtitle1"
                          fontWeight={600} component="label" htmlFor='password' mb="5px">Password</Typography>
              <CustomTextField id="password" type="password" variant="outlined" fullWidth />
            </Box>
            <Stack justifyContent="space-between" direction="row" alignItems="center" my={2}>
              <FormGroup>
                <FormControlLabel
                  control={<Checkbox defaultChecked />}
                  label="Remeber this Device"
                />
              </FormGroup>
              <Typography
                component={Link}
                to="/"
                fontWeight="500"
                sx={{
                  textDecoration: 'none',
                  color: 'primary.main',
                }}
              >
                Forgot Password ?
              </Typography>
            </Stack>
          </Stack>
          <Box>
            <Button
              color="primary"
              variant="contained"
              size="large"
              fullWidth
              type="submit"
            >
              Sign In
            </Button>
          </Box>
        </form>
        {subtitle}
      </>
    )
};

export default AuthLogin;
