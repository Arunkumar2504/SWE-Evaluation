# SWE-Evaluation

This repository contains three Python scripts that automate tasks across **Slack**, **JIRA**, and **Google Docs** using simulated user activity.

---

## ✅ Task Overview

You are asked to:

1. **Setup**
   - Create free Google accounts for 3 users and share credentials.
   - Setup a free **Slack Workspace** and **JIRA Project** using the provided evalswe Gmail account.
   - Create:
     - 5 Slack channels
     - 2 JIRA projects

2. **Python Automation**
   - 🟦 **Slack**: Simulate publishing messages from the 3 users.
   - 🟧 **JIRA**: Simulate creating random issues from the 3 users.
   - 🟩 **Google Docs**:
     - Create and share documents between all 3 users.
     - Add comments from 2 users.
     - Add reply from 3rd user.

---

Each script is responsible for automating one part of the evaluation:

1. **Slack Automation (`slack_message_bot.py`)**
   - Connects to Slack workspace
   - Sends messages to 5 channels from each user

2. **JIRA Automation (`create_jira_issues.py`)**
   - Logs into JIRA for each user
   - Creates random issues in the two projects

3. **Google Docs Automation (`main_user1.py`)**
   - Creates a Google Doc
   - Shares it between users
   - User 2 adds a comment
   - User 3 replies to the comment

---

## 🧪 Technologies Used

- Python 3.10
- `google-api-python-client` for Google Docs/Drive
- `slack_sdk` for Slack bot interaction
- `jira` (Atlassian SDK) for JIRA integration

---

## 🔐 Credentials
Mail ID: evalswe01@gmail.com

Password: Evalswe@1234

Mail ID: evalswe02@gmail.com

Password: Evalswe@1234

Mail ID: evalswe03@gmail.com

Password: Evalswe@1234


---
## ✅ Done

- [x] Setup 3 Google accounts
- [x] Create Slack workspace and channels 

  Slack name: https://sweevaluation.slack.com
  
  Channels: 
  1. #announcements
  2. #bugs
  3. #daily_updates
  4. #questions
  5. #tasks
- [x] Create 2 JIRA projects - Jira account: https://evalswe01.atlassian.net
- [x] Automate interactions across platforms
- [x] Exclude secrets from repo

---

## ▶️ How to Run

Run each script separately from the terminal:

```bash
python slack_message_bot.py
python create_jira_issues.py
python google_docs_script.py
python main_user1.py
```

## A Note of Thanks

I would like to sincerely thank the team for this opportunity. Working on this evaluation allowed me to explore and learn more about integrating automation with collaborative tools like Slack, JIRA, and Google APIs. I truly admired the workflow and the way modern tools can be orchestrated using Python. It was a great learning experience.

---
