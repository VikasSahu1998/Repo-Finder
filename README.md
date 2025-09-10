# 🔎 Repo Finder

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)

Repo Finder is a **simple, category-based repository search tool** for GitHub.  
Users can select categories like **AI, Music, Weather, Images, Games**, and get the top starred repositories.  
It now supports **both CLI and browser-based web UI**.

---

## 📌 Features
- Search GitHub repositories by **predefined categories**.
- Categories include: AI, Music, Weather, Images, Games, and more.
- User-friendly CLI and browser interface.
- Configurable number of results.
- Docker-ready for easy portability.
- Minimal, modular, and production-preparable.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/repo-finder.git
cd repo-finder
````

### 2. Setup Python environment

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux / Mac
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### CLI Mode

```bash
python -m repo_finder.cli
```

* Select a category from the list.
* Enter the number of results to fetch.
* Results are printed with stars, repo name, language, and URL.

---

### Web UI Mode

```bash
python -m repo_finder.web
```

* Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.
* Select a category and number of results.
* Results are displayed in a clean table with repository info.

---

### Docker Mode

#### Build Docker Image

```bash
docker build -t repo-finder .
```

#### Run Web UI in Docker

```bash
docker run --rm -p 5000:5000 repo-finder
```

* Open **[http://localhost:5000](http://localhost:5000)** in your browser.

#### Optional: Docker Compose

```bash
docker compose up --build
```

---

## 📂 Project Structure

```
repo-finder/
├── repo_finder/              
│   ├── __init__.py
│   ├── core.py               
│   ├── categories.py
│   ├── cli.py                
│   ├── web.py                # Web UI
│   └── templates/
│       └── index.html        # Browser interface template
├── Dockerfile                
├── docker-compose.yml        
├── requirements.txt          
└── README.md                 
```

---

## 📜 License

MIT License © 2025 Your Name

---

## 🙌 Contributing

* Pull requests welcome.
* Open an issue for suggestions or bugs.