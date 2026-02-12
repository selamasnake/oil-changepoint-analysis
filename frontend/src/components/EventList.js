import React, { useEffect, useState } from "react";
import { getEvents } from "../services/api";

const EventList = ({ changePoint, startDate, endDate }) => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const eventsData = await getEvents();
      setEvents(eventsData);
    };
    fetchData();
  }, []);

  const filteredEvents = events.filter((e) => {
    const date = new Date(e.date);
    return (!startDate || date >= new Date(startDate)) && (!endDate || date <= new Date(endDate));
  });

  return (
    <div style={{ marginTop: "2rem" }}>
      <h3>Key Events</h3>
      <ul>
        {filteredEvents.map((event, index) => {
          const isNearCP =
            changePoint &&
            Math.abs(new Date(event.date) - new Date(changePoint)) <= 30 * 24 * 60 * 60 * 1000; // ±30 days
          return (
            <li key={index} style={{ color: isNearCP ? "red" : "black" }}>
              {new Date(event.date).toLocaleDateString()} – {event.event} {isNearCP && "(Near Change Point)"}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default EventList;
