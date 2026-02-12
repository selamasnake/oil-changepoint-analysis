import React, { useState } from "react";
import PriceChart from "./components/PriceChart";
import EventList from "./components/EventList";
import Filters from "./components/Filters";

function App() {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [changePoint, setChangePoint] = useState(null);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Brent Oil Price Dashboard</h1>

      <Filters
        startDate={startDate}
        endDate={endDate}
        setStartDate={setStartDate}
        setEndDate={setEndDate}
      />

      <PriceChart
        startDate={startDate}
        endDate={endDate}
        setChangePoint={setChangePoint}
      />

      <EventList
        startDate={startDate}
        endDate={endDate}
        changePoint={changePoint}
      />
    </div>
  );
}

export default App;
