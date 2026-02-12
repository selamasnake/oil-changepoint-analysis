import React, { useEffect, useState } from "react";
import { getHistoricalPrices, getEvents, getChangePoints } from "../services/api";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";

const PriceChart = ({ startDate, endDate, setChangePoint }) => {
  const [data, setData] = useState([]);
  const [events, setEvents] = useState([]);
  const [localCP, setLocalCP] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const prices = await getHistoricalPrices();
      const eventsData = await getEvents();
      const cpData = await getChangePoints();

      setData(prices);
      setEvents(eventsData);

      // Use the first change point for now
      if (cpData.length > 0) {
        setLocalCP(cpData[0].change_date);
        setChangePoint(cpData[0].change_date);
      }
    };
    fetchData();
  }, [setChangePoint]);

  // Filter and map data
  const filteredData = data
    .filter((d) => {
      const date = new Date(d.Date);
      return (!startDate || date >= new Date(startDate)) && (!endDate || date <= new Date(endDate));
    })
    .map((d) => {
      const dateStr = new Date(d.Date).toISOString().split("T")[0]; // YYYY-MM-DD
      const eventList = events
        .filter((e) => new Date(e.date).toISOString().split("T")[0] === dateStr)
        .map((e) => e.event)
        .join("; ");
      return { ...d, events: eventList, Date: dateStr };
    });

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div style={{ backgroundColor: "#fff", border: "1px solid #ccc", padding: "0.5rem" }}>
          <p><strong>Date:</strong> {label}</p>
          <p><strong>Log Return:</strong> {payload[0].value.toFixed(5)}</p>
          {payload[0].payload.events && <p><strong>Events:</strong> {payload[0].payload.events}</p>}
        </div>
      );
    }
    return null;
  };

console.log("Filtered Data Dates:", filteredData.map(d => d.Date));
console.log("Change Point:", localCP);

  return (
    <div>
      <h3>Brent Daily Log Returns</h3>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={filteredData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip content={<CustomTooltip />} />
          <Line type="monotone" dataKey="log_return" stroke="#007bff" dot={false} />
          {localCP && (
            <ReferenceLine
              x={new Date(localCP).toISOString().split("T")[0]}
              stroke="red"
              strokeDasharray="5 5"
              label={{ value: "Change Point", position: "top", fill: "red" }}
            />
          )}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PriceChart;
