import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8080';

export const authenticate = (auth) => {
  let formData = new FormData();
  formData.append('username', auth.username);
  formData.append('password', auth.password);
  return axios.post(`${API_URL}/api/v1/auth/login`, formData).then(({ data }) => data);
};

export const registerUser = (auth) => {
  return axios.post(`${API_URL}/api/v1/auth/register`, auth).then(({ data }) => data);
};

export const fetchDTSTables = (dtsTableName) => {
  const headers = {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
  };
  return axios
    .get(`${API_URL}/api/v1/dts-tables/`, {
      params: { table_name: dtsTableName },
      headers: headers,
    })
    .then(({ data }) => data);
};

export const fetchSentimentSurvey = () => {
  const headers = {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
  };
  return axios
    .get(`${API_URL}/api/v1/sentiment-survey/`, {
      headers: headers,
    })
    .then(({ data }) => data);
};

export const fetchSPYFinance = () => {
  const headers = {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
  };
  return axios
    .get(`${API_URL}/api/v1/spy-finance/`, {
      headers: headers,
    })
    .then(({ data }) => data);
};
