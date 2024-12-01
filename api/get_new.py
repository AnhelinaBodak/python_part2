from fastapi import APIRouter
import json

router = APIRouter(tags=['10 latest CVEs'])

def load_vulnerabilities(file_path='data/known_exploited_vulnerabilities.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_latest_vulnerabilities(vulnerabilities, limit):
    sorted_vulnerabilities = sorted(
        vulnerabilities["vulnerabilities"], 
        key=lambda x: x.get("dateAdded", ""), 
        reverse=True
    )
    return sorted_vulnerabilities[:limit]

@router.get("/get/new")

def get_new(limit: int = 10):
    data = load_vulnerabilities()
    latest_vulnerabilities = get_latest_vulnerabilities(data, limit)
    return {
        "limit": limit,
        "count": len(latest_vulnerabilities),
        "vulnerabilities": latest_vulnerabilities
    }
