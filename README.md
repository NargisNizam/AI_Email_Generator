<div align="center">

![Wave Banner](https://capsule-render.vercel.app/api?type=waving&color=0:2563eb,100:1e293b&height=160&section=header&text=AI%20Email%20Generator&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Segoe+UI&size=20&pause=1000&color=2563EB&center=true&vCenter=true&width=500&lines=Generate+professional+emails+with+AI;Powered+by+FastAPI+%2B+Gemini+API;Recipient+%2B+Purpose+%2B+Tone+%3D+Instant+Email)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

A simple FastAPI app that generates a professional email using Google's Gemini API.

## Features
- Accepts **Recipient Name**, **Email Purpose**, and **Tone** (Professional / Friendly / Formal)
- Generates a complete, ready-to-send email using Gemini
- Displays the generated email on a simple HTML page

## Project Structure
```
ai-email-generator/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Setup & Run

1. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Gemini API key**
   - Copy `.env.example` to `.env`
   - Get a free key from https://aistudio.google.com/app/apikey
   - Paste it into `.env`:
     ```
     GEMINI_API_KEY=your_actual_key_here
     ```

4. **Run the app**
   ```bash
   uvicorn main:app --reload
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:8000
   ```

## Push to GitHub

```bash
git init
git add .
git commit -m "AI Email Generator - FastAPI + Gemini"
git branch -M main
git remote add origin https://github.com/NargisNizam/ai-email-generator.git
git push -u origin main
```

## Submission Checklist
- [ ] GitHub repository link
- [ ] Screenshot of the working application (form filled + generated email shown)

<div align="center">

![Wave Footer](https://capsule-render.vercel.app/api?type=waving&color=0:1e293b,100:2563eb&height=100&section=footer)

</div>
