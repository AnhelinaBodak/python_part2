from fastapi import APIRouter
from datetime import datetime, timedelta
import json

router = APIRouter(tags=['Get all'])

def load_vulnerabilities(file_path='data/known_exploited_vulnerabilities.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def filter_recent_vulnerabilities(vulnerabilities, limit, days=30):
    filtered_vulnerabilities = {}
    some_days_ago = datetime.now() - timedelta(days=days)

    count = 0
    for idx, vulnerability in enumerate(vulnerabilities["vulnerabilities"], start=1):
        if count >= limit:  
            break
        date_added = datetime.strptime(vulnerability["dateAdded"], "%Y-%m-%d")
        if date_added >= some_days_ago:
            filtered_vulnerabilities[f"vulnerability_{idx}"] = vulnerability
            count += 1

    return filtered_vulnerabilities

@router.get("/get/all")
def get_all_vulnerabilities(limit: int = 20):
    data = load_vulnerabilities()
    recent_vulnerabilities = filter_recent_vulnerabilities(data, limit)
    return {
        "limit": limit,
        "count": len(recent_vulnerabilities),
        "vulnerabilities": recent_vulnerabilities
    }
