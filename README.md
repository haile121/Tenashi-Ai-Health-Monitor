# AI-Powered Health Monitoring System


One-line setup and run instructions are below.


## Prerequisites
- Python 3.9+ and pip on Windows.
- Node.js 16+ and npm.
- (Optional) Docker and docker-compose.


## Backend (Flask + scikit-learn)
1. `cd backend` and create a venv: `python -m venv venv`.
2. Activate venv: `venv\Scripts\activate`.
3. Install: `pip install -r requirements.txt`.
4. Run: `python app.py`.


## Frontend (React + Vite)
1. `cd frontend`.
2. Install: `npm install`.
3. Run: `npm run dev`.


## Using docker-compose
Run `docker-compose up --build` from project root to start both services.


## Notes
This project simulates wearable data and exposes an API for real-time metrics and anomaly flags.