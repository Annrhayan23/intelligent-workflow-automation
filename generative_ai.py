"""Lightweight summarizer and email generator (offline)."""
import re
from typing import Dict, List

def summarize_document(text: str, max_sentences: int = 3) -> str:
    if not text:
        return ""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    summary = ' '.join([s.strip() for s in sentences if s.strip()][:max_sentences])
    return summary

def generate_email(entities: Dict[str, List[str]], summary: str) -> str:
    orgs = entities.get('ORG', [])
    money = entities.get('MONEY', [])
    dates = entities.get('DATE', [])
    to_org = orgs[0] if orgs else 'Recipient'

    lines = []
    lines.append(f"Hello {to_org},")
    if summary:
        lines.append('\n' + summary + '\n')
    if money:
        lines.append(f"We noted an amount mentioned: {', '.join(money)}.")
    if dates:
        lines.append(f"Relevant dates: {', '.join(dates)}.")
    lines.append('\nRegards,\nIntelligent Workflow Bot')
    return '\n'.join(lines)
