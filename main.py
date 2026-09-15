import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import google.generativeai as genai

# ---------------------------------------------------------
# Load environment variables (Gemini API key)
# ---------------------------------------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY not found. Add it to your .env file.")
else:
    genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-flash-lite-latest")

# ---------------------------------------------------------
# FastAPI app setup
# ---------------------------------------------------------
app = FastAPI(title="AI Email Generator")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def build_prompt(recipient_name: str, purpose: str, tone: str) -> str:
    """Builds the prompt sent to the Gemini model."""
    return f"""
You are a professional email-writing assistant.

Write a complete, ready-to-send email with the following details:
- Recipient Name: {recipient_name}
- Purpose of the email: {purpose}
- Tone: {tone}

Instructions:
- Include an appropriate subject line (start the line with "Subject:").
- Write a proper greeting using the recipient's name.
- Write a clear, well-structured body that fulfills the stated purpose.
- Match the requested tone ({tone}) throughout.
- End with a suitable sign-off (e.g., "Best regards," / "Sincerely,") followed by "[Your Name]".
- Do not add any explanation before or after the email — output only the email itself.
"""


def generate_email(recipient_name: str, purpose: str, tone: str) -> str:
    """Calls the Gemini API and returns the generated email text."""
    prompt = build_prompt(recipient_name, purpose, tone)
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating email: {e}"


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"email_output": None}
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    recipient_name: str = Form(...),
    purpose: str = Form(...),
    tone: str = Form(...),
):
    email_output = generate_email(recipient_name, purpose, tone)
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "email_output": email_output,
            "recipient_name": recipient_name,
            "purpose": purpose,
            "tone": tone,
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
