import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/api";

export const getHistoricalPrices = async () => {
  const res = await axios.get(`${BASE_URL}/historical_prices`);
  return res.data;
};

export const getChangePoints = async () => {
  const res = await axios.get(`${BASE_URL}/change_points`);
  return res.data;
};

export const getEvents = async () => {
  const res = await axios.get(`${BASE_URL}/events`);
  return res.data;
};
