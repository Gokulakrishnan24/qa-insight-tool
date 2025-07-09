# 🧠 QA Insight Tool (POC)

A full-stack internal QA dashboard for visualizing test results and generating AI-based test case suggestions using OpenAI.

---

## 🔧 Tech Stack

- **Backend**: FastAPI + Uvicorn + OpenAI API
- **Frontend**: React + Chart.js + Axios
- **Testing**: Pytest
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions (planned)
- **Deployment**: Localhost / AWS EC2

---

## 📊 Features

- Track test artifacts (name, status, reason, run ID)
- Flaky test leaderboard (rank by fail count)
- Bar chart (pass/fail per test case)
- OpenAI-powered suggestions based on PRs + bug summary
- REST API powered by FastAPI
- React dashboard with Chart.js visualizations

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourname/qa-insight-tool.git
cd qa-insight-tool

# Add your OpenAI API key
export OPENAI_API_KEY=your_key_here
# OR use .env and docker-compose

# Build and start
docker-compose up --build
