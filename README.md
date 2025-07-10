# QA Insight Tool: AI-Powered Test Intelligence Dashboard

## 📊 Project Overview

The **QA Insight Tool** is an end-to-end test intelligence platform that helps QA engineers:

* 📈 Monitor flaky tests and analyze failure patterns
* 🧠 Use OpenAI to generate smart test suggestions from PR and bug descriptions
* ⚙️ Automate test artifact ingestion from Pytest
* 🚀 Deploy to the cloud with Docker, Render, Vercel, and GitHub Actions

---

## 🛠️ Architecture

```
Frontend (React + Chart.js)
  └─→ GET /artifacts ➞ Leaderboard Chart
  └─→ POST /suggest  ➞ Generate AI Test Scenarios

Backend (FastAPI)
  └─→ /artifacts  ➞ Store + Fetch Test Results
  └─→ /suggest    ➞ OpenAI ChatCompletion API

Database (in-memory or persistent store)
```

---

## 📚 Features

### 🤖 AI Test Suggestion Generator

* Input: PR description and bug summary
* Output: 3 test ideas (Functional, Edge, Regression)
* Backed by OpenAI API (gpt-3.5-turbo)

### 📊 Flaky Test Dashboard

* Visual leaderboard of test failures
* Useful for identifying unstable tests and patterns
* Filterable by `run_id` or time (enhancement ready)

### ⚖️ Auto-post Pytest Failures

* Pytest plugin that auto-posts to `/artifacts`
* Captures `test_name`, `status`, `reason`, `timestamp`, and `run_id`

### 🚜 CI/CD + Deployment

* GitHub Actions for CI/CD
* Dockerized backend (`Dockerfile`)
* Deployed backend to **Render**
* Deployed frontend to **Vercel**

---

## 📂 Technologies Used

| Layer    | Stack                               |
| -------- | ----------------------------------- |
| Frontend | React, Chart.js, Axios              |
| Backend  | FastAPI, Uvicorn, Pydantic          |
| AI       | OpenAI API (ChatCompletion)         |
| CI/CD    | GitHub Actions + Docker             |
| Hosting  | Render (backend), Vercel (frontend) |

---

## 🔹 Usage

### 🌐 Web Dashboard

* View flaky test leaderboard from `/artifacts`
* Generate test ideas via form `/suggest`

### 💻 API Endpoints

```http
POST /artifacts
GET /artifacts
POST /suggest
```

### 🎓 Example AI Prompt Output

```
PR: Refactored login flow with new OTP handling
Bug: Previous OTP mismatch issue fixed

Suggestions:
1. Verify user can enter OTP and login successfully
2. Submit an expired OTP and check for error
3. Ensure password login works after OTP refactor
```

---

## 📅 Roadmap

* [x] OpenAI-based test suggestion feature
* [x] Pytest failure tracking + dashboard
* [x] Dockerized backend + GitHub CI/CD
* [x] Deployment to cloud (Render + Vercel)
* [ ] Add filter support by `run_id` or time
* [ ] Add authentication layer (optional)
* [ ] Persistent DB (SQLite or PostgreSQL)

---

## 👩‍🚀 Author

**Gokulakrishnan**
SDET | Test Automation Engineer | AI-in-Testing Innovator

---

## 🔗 Links

* GitHub: [github.com/Gokulakrishnan24/qa-insight-tool](https://github.com/Gokulakrishnan24/qa-insight-tool)
* OpenAI API Key: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
* Render: [https://render.com](https://render.com)
* Vercel: [https://vercel.com](https://vercel.com)
