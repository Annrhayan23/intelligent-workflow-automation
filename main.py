# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel

from backend.workflow import decide_next_action
from backend.generative_ai import summarize_document, generate_email

app = FastAPI(title="Intelligent Workflow Automation")

API_KEY="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"

class Document(BaseModel):
    text: str
    entities: dict

@app.post("/analyze/")
def analyze_document(doc: Document):
    # Step 1: Decide next action based on entities
    action = decide_next_action(doc.entities)

    # Step 2: Summarize document
    summary = summarize_document(doc.text)

    # Step 3: Generate email
    email = generate_email(summary)

    return {
        "action": action,
        "summary": summary,
        "email": email
    }

# Test endpoint
@app.get("/")
def root():
    return {"message": "Intelligent Workflow Automation API is running"}
