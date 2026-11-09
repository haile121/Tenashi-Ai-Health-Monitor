# AI-Powered Health Monitoring System

A full-stack app that simulates wearable sensor data, detects anomalies in real time using an ML model, and displays live metrics on a React dashboard.

---

## Tech Stack

| Layer     | Tech                                      |
|-----------|-------------------------------------------|
| Backend   | Python 3.9+, Flask, scikit-learn, joblib  |
| Frontend  | React 18, Vite, Chart.js                  |
| Container | Docker, docker-compose                    |

---

## How It Works

1. The backend simulates wearable readings (heart rate, blood oxygen, activity level).
2. An `IsolationForest` model (trained on startup if no saved model exists) scores each reading for anomalies.
3. `GET /api/metrics` returns a fresh simulated sample with an anomaly flag.
4. `POST /api/score` accepts `{ heart_rate, blood_oxygen }` and returns `{ anomaly: true/false }`.
5. The React dashboard polls `/api/metrics` every 2 seconds and renders a live line chart.

---

## Prerequisites

- Python 3.9+ and pip
- Node.js 16+ and npm
- (Optional) Docker and docker-compose

---

## Local Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python app.py                # runs on http://localhost:5000
```

### Frontend

```bash
cd frontend
npm install
npm run dev                  # runs on http://localhost:5173
```

Open `http://localhost:5173` — the dashboard will start polling the backend automatically.

---

## Docker

```bash
docker-compose up --build
```

- Backend → `http://localhost:5000`
- Frontend → `http://localhost:5173`

---

## API Reference

| Method | Endpoint      | Description                                              |
|--------|---------------|----------------------------------------------------------|
| GET    | `/api/metrics`| Returns a simulated reading with anomaly flag            |
| POST   | `/api/score`  | Scores a custom `{ heart_rate, blood_oxygen }` payload   |

### Example POST `/api/score`

```json
// Request
{ "heart_rate": 140, "blood_oxygen": 88 }

// Response
{ "anomaly": true }
```

---

## Project Structure

```
.
├── backend/
│   ├── app.py              # Flask routes
│   ├── model.py            # IsolationForest train/load/predict
│   ├── data_simulator.py   # Wearable data simulator
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── App.jsx
│       └── components/
│           └── Dashboard.jsx   # Live metrics + Chart.js graph
└── docker-compose.yml
```
