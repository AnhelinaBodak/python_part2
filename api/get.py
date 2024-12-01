from fastapi import APIRouter, Query
import json

router = APIRouter(tags=['Search CVEs'])

def load_vulnerabilities(file_path='data/known_exploited_vulnerabilities.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def search_cves_by_keyword(vulnerabilities, keyword):
    matching_cves = [
        vulnerability for vulnerability in vulnerabilities["vulnerabilities"]
        if any(keyword.lower() in str(value).lower() for value in vulnerability.values())
    ]
    return matching_cves

@router.get("/get")
def search_vulnerabilities(query: str = Query(..., description="Keyword to search in CVE data")):
    data = load_vulnerabilities()

    matching_vulnerabilities = search_cves_by_keyword(data, query)
    no_vulnerabilities = "No vulnerabilities found("
    if(len(matching_vulnerabilities) < 1): return no_vulnerabilities

    return {
        "count": len(matching_vulnerabilities),
        "vulnerabilities": matching_vulnerabilities
    }
