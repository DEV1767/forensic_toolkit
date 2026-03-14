# 🎙️ VeriVox AI — Audio Deepfake Detector
 
> **The world's first AI-powered Forensic Audio Audit system with browser extension support.**
 
[![Live Demo](https://img.shields.io/badge/Live%20Demo-forensictoolkithack.vercel.app-blue?style=for-the-badge)](https://forensictoolkithack.vercel.app)
[![Backend](https://img.shields.io/badge/Backend-Hugging%20Face-yellow?style=for-the-badge)](https://huggingface.co/spaces/DEV1767/verivoxxx)
[![Python](https://img.shields.io/badge/Python-3.11-green?style=for-the-badge)](https://python.org)
[![React](https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge)](https://vitejs.dev)
 
---
 
## 🚨 Problem
 
Audio deepfakes are being used for fraud, misinformation, and voice cloning scams. Existing tools require technical expertise and there is no easy platform for everyday users to verify if an audio clip is real or AI-generated.
 
---
 
## ✅ Solution
 
VeriVox AI lets anyone upload any audio file and instantly know if it is **REAL** or **AI-GENERATED** — with a confidence score, waveform analysis, and a plain-language explanation powered by Gemini AI.
 
---
 
## ✨ Features
 
- 🔍 **Audio Deepfake Detection** — Upload any audio file and get instant REAL/FAKE verdict
- 📊 **Confidence Score** — Percentage-based confidence with detailed forensic breakdown
- 🧠 **AI Explanation** — Gemini AI explains the result in plain language
- 🎤 **Voice Comparison** — Upload two audio clips to detect voice cloning attacks
- 📄 **PDF Report** — Download a full forensic report for any analysis
- 📜 **History Dashboard** — View all past scans with timestamps
- 🔐 **JWT Authentication** — Secure user login and registration
- 🌐 **Chrome Extension** — Detect deepfakes directly on any webpage with one click
 
---
 
## 🏗️ Project Structure
 
```
forensic_toolkit/
├── audio-notary-backend/     # FastAPI Backend
│   ├── app/
│   │   ├── main.py           # FastAPI app entry point
│   │   ├── auth.py           # JWT authentication
│   │   ├── database.py       # MongoDB connection
│   │   ├── routes/
│   │   │   ├── analyze.py    # Audio detection endpoints
│   │   │   ├── auth_routes.py
│   │   │   ├── compare.py    # Voice comparison endpoint
│   │   │   └── explain.py    # Gemini AI explanation
│   │   └── services/
│   │       ├── forensics.py  # Core ML analysis logic
│   │       └── pdf_service.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── audio-notary-frontend/    # React Frontend
    ├── src/
    │   ├── pages/
    │   │   ├── Home.jsx      # Audio upload & scan page
    │   │   ├── Compare.jsx   # Voice comparison page
    │   │   ├── Dashboard.jsx # History page
    │   │   ├── Explain.jsx   # AI explanation page
    │   │   └── Login.jsx     # Authentication page
    │   ├── components/
    │   └── context/
    ├── vercel.json
    └── package.json
```
 
---
 
## 🛠️ Tech Stack
 
### Backend
| Technology | Purpose |
|---|---|
| FastAPI | REST API framework |
| Python 3.11 | Core language |
| PyTorch + Torchaudio | Deep learning model |
| Whisper (OpenAI) | Audio transcription |
| Librosa | Audio feature extraction |
| MongoDB Atlas | Database |
| Google Gemini AI | Plain-language explanations |
| JWT + bcrypt | Authentication |
| Docker | Containerization |
 
### Frontend
| Technology | Purpose |
|---|---|
| React + Vite | UI framework |
| Tailwind CSS | Styling |
| React Router | Navigation |
| Axios | API calls |
| React Dropzone | File upload |
 
---
 
## 🚀 Getting Started
 
### Prerequisites
- Python 3.11
- Node.js 18+
- MongoDB Atlas account
- Google Gemini API key
 
### Backend Setup
 
```bash
cd audio-notary-backend
 
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
 
# Install PyTorch first
pip install torch==2.3.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cpu
 
# Install dependencies
pip install -r requirements.txt
 
# Create .env file
cp .env.example .env
# Add your MONGO_URI, SECRET_KEY, GEMINI_API_KEY
 
# Start server
python -m uvicorn app.main:app --reload
```
 
### Frontend Setup
 
```bash
cd audio-notary-frontend
 
# Install dependencies
npm install
 
# Start dev server
npm run dev
```
 
Open `http://localhost:5173`
 
---
 
## 🌐 Chrome Extension
 
A Chrome extension that adds a **"Check with VeriVox"** button on any webpage with audio content.
 
### Install
1. Download the `verivox-extension` folder
2. Open Chrome → `chrome://extensions`
3. Enable **Developer mode**
4. Click **Load unpacked** → select the folder
 
### How it works
- Automatically scans any webpage for audio/video elements
- Adds a purple "Check with VeriVox" button next to each player
- One click opens VeriVox with the audio URL ready to analyze
 
---
 
## 📡 API Endpoints
 
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/detect` | Analyze uploaded audio file |
| POST | `/api/detect-url` | Analyze audio from URL |
| POST | `/api/compare` | Compare two audio files |
| GET | `/api/history` | Get user's scan history |
| GET | `/api/report/{id}/download` | Download PDF report |
| DELETE | `/api/report/{id}` | Delete a report |
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |
 
---
 
## 🎯 Use Cases
 
- **Journalists** verifying audio evidence in news stories
- **Legal teams** checking voice recordings for court
- **HR teams** verifying interview recordings
- **General public** protecting against voice scam calls
- **Social media platforms** flagging fake audio content
 
---
 
## 🔐 Environment Variables
 
Create a `.env` file in `audio-notary-backend/`:
 
```
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
```
 
---
 
## 📦 Deployment
 
- **Frontend** → Vercel (auto-deploy on push)
- **Backend** → Hugging Face Spaces (Docker)
 
---
 
## 👨‍💻 Team
 
Built with ❤️ for hackathon — VeriVox AI Team
 
---
 
## 📄 License
 
MIT License
 
