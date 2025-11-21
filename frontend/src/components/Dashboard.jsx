// dashboard that polls backend and shows metrics + anomaly alert
import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import {
Chart as ChartJS,
CategoryScale,
LinearScale,
PointElement,
LineElement,
Title,
Tooltip,
Legend
} from "chart.js";


ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);


export default function Dashboard() {
// state
const [history, setHistory] = useState([]);
const [latest, setLatest] = useState(null);


useEffect(() => {
// polling interval to fetch simulated metrics
const id = setInterval(async () => {
const res = await fetch("http://localhost:5000/api/metrics");
const j = await res.json();
setLatest(j);
setHistory(h => [...h.slice(-49), { t: new Date().toLocaleTimeString(), hr: j.heart_rate }]);
}, 2000);
return () => clearInterval(id);
}, []);


const data = {
labels: history.map(h => h.t),
datasets: [
{ label: "Heart Rate", data: history.map(h => h.hr), tension: 0.3 }
]
};


return (
<section className="dashboard">
<h2>Real-time Metrics</h2>
{latest && (
<div className="cards">
<div className="card">HR: {latest.heart_rate}</div>
<div className="card">SpO₂: {latest.blood_oxygen}</div>
<div className="card">Activity: {latest.activity_level}</div>
<div className="card">Anomaly: {String(latest.anomaly)}</div>
</div>
)}
<div className="chart">
<Line data={data} />
</div>
</section>
);
}