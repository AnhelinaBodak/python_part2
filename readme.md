# CVE FastAPI App

A FastAPI application to interact with CVE (Common Vulnerabilities and Exposures)data.

# Project Structure
- **api/**: Contains the logic for handling the various endpoints.
  - `get.py`: Endpoint for searching CVEs by keyword; loads data from specified json file; filters CVEs with the keyword (case-insensitive); defines '/get' endpoint , accepts query (string).
  - `get_all.py`: Endpoint for retrieving all vulnerabilities from last 30 days; loads data from specified json file; filters CVEs using datetime lib, retrives specified by limit amount; defines 'get/all' endpoint, accepts limit (number of CVEs to retrivie) as a query parameter (default: 20). 
  - `get_known.py`: Endpoint for retrieving known ransomware vulnerabilities; loads data from specified json file; filters CVEs where 'knownRansomwareCampaignUse' is marked known, retrives specified by limit amount; defines 'get/all' endpoint, accepts limit (number of CVEs to retrivie) as a query parameter (default: 10); 
  - `get_new.py`: Endpoint for retrieving the latest CVEs; loads data from specified json file; filters CVEs in descending order by 'dateAdded', retrives specified by limit amount; defines 'get/new' endpoint, accepts limit (number of CVEs to retrivie) as a query parameter (default: 10);
  - `info.py`: Endpoint for information about author.
- **data/**: Contains the `known_exploited_vulnerabilities.json` file, which holds the CVE data.
- **static/**: Contains static files like CSS and JS for frontend functionalities.
  - `script.js`: JavaScript file for handling frontend actions.
  - `styles.css`: Styling for the web interface.
- **templates/**: Contains HTML templates for rendering the web pages.
  - `index.html`: The main HTML page.
- **main.py**: The entry point for the FastAPI app, which defines start page; integrates API routes; sets up static files and templates.

