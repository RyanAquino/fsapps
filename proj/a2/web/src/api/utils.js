import axios from 'axios';



const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8080";

export const authenticate = (auth) => {
  return axios.post(`${API_URL}/api/v1/auth/login`, auth).then(({ data }) => data);
};


export const dtsTable = (dtsTableName) => {
  return axios.get(`${API_URL}/api/v1/dts_tables`, {"params": {"table_name": dtsTableName}}).then(({ data }) => data);
}