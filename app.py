from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Extract commit message or PR title
    summary = data.get("head_commit", {}).get("message", "Auto-created JIRA issue from GitHub event")
    description = f"GitHub Event Payload:\n{data}"

    jira_payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}
        }
    }

    auth = (JIRA_USERNAME, JIRA_API_TOKEN)
    headers = {"Content-Type": "application/json"}

    response = requests.post(
        f"{JIRA_BASE_URL}/rest/api/2/issue",
        auth=auth,
        headers=headers,
        json=jira_payload
    )

    if response.status_code == 201:
        return jsonify({"msg": "JIRA issue created successfully"}), 201
    else:
        return jsonify({"msg": "Failed to create JIRA issue", "error": response.text}), 400

if __name__ == "__main__":
    app.run(port=5000)