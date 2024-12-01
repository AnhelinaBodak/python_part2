from fastapi import APIRouter
import json

router = APIRouter(tags=['Get known'])

def load_vulnerabilities(file_path='data/known_exploited_vulnerabilities.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def filter_known_ransomware_vulnerabilities(vulnerabilities, limit=10):
    known_ransomware_vulnerabilities = [
        vulnerability for vulnerability in vulnerabilities["vulnerabilities"]
        if vulnerability.get("knownRansomwareCampaignUse") == "Known"
    ]
    return known_ransomware_vulnerabilities[:limit]

@router.get("/get/known")
def get_known_vulnerabilities(limit: int = 10):
    data = load_vulnerabilities()
    known_vulnerabilities = filter_known_ransomware_vulnerabilities(data, limit)
    return {
        "limit": limit,
        "count": len(known_vulnerabilities),
        "vulnerabilities": known_vulnerabilities
    }
