import React from "react";

const Filters = ({ startDate, endDate, setStartDate, setEndDate }) => {
  return (
    <div style={{ marginBottom: "1.5rem" }}>
      <label>
        Start Date:{" "}
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />
      </label>
      <label style={{ marginLeft: "1rem" }}>
        End Date:{" "}
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
      </label>
    </div>
  );
};

export default Filters;
