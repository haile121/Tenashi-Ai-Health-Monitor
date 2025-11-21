// top-level app that renders dashboard
import React from "react";
import Dashboard from "./components/Dashboard";


export default function App() {
// one-line UI wrapper
return (
<div className="app-root">
<header className="header">AI Health Monitor</header>
<main>
<Dashboard />
</main>
</div>
);
}