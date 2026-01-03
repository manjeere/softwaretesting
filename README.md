# GitHub–JIRA Automation Tool

This project automates the creation of JIRA tickets when GitHub events (e.g. push or PR) are triggered, using a Python Flask API and JIRA REST API integration.

## 🔧 Tech Stack

- Python 3.x
- Flask
- GitHub Webhooks
- JIRA REST API

## 📦 Setup

1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`:
```env
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_USERNAME=your-email@example.com
JIRA_API_TOKEN=your-api-token
JIRA_PROJECT_KEY=PROJ
```

3. Run the Flask app:
```bash
python app.py
```

4. Use a tool like `ngrok` to expose your local port:
```bash
ngrok http 5000
```

5. Add the ngrok URL to your GitHub repo as a webhook:
```
https://<your-ngrok-url>/webhook
```

## 🛡️ Security

Keep your `.env` file private and never commit it to version control.
