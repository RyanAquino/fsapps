import axios from 'axios';



const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8080";

export const authenticate = (auth) => {
  return axios.post(`${API_URL}/v1/auth/login/`, auth).then(({ data }) => data);
};
