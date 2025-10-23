"""Rule-based workflow decider."""
from typing import Dict, List

def decide_next_action(entities: Dict[str, List[str]]) -> Dict[str, str]:
    action = {'action': 'review_document', 'reason': 'No specific trigger found'}
    money = entities.get('MONEY', [])
    orgs = entities.get('ORG', [])
    dates = entities.get('DATE', [])

    if money:
        action = {'action': 'flag_finance', 'reason': f'Money amounts found: {money}'}
    elif any('termination' in (m.lower() if isinstance(m, str) else '') for m in entities.get('MISC', [])):
        action = {'action': 'notify_legal', 'reason': 'Termination clause mentioned'}
    elif orgs and dates:
        action = {'action': 'schedule_meeting', 'reason': f'Org(s) {orgs} and date(s) {dates} detected'}

    return action
