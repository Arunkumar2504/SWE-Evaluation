import random
import requests


JIRA_URL = "https://evalswe01.atlassian.net"

users = [
    {
        "email": "evalswe01@gmail.com",
        "api_token": "ATATT3xFfGF0Ds1CW9rB-n6xPLjKTV4JleKBfc4r4HSCFaR7_8a0Z4Ytvou2cF2ufGj2cHXqP82zu80Lduph-28dSnotoM__pJeGSLA5_iGpkcrt4O8RJ1jwmTmTHijPsHY65y_BOKWHHubxdKfJu3J1jFmHy28uOqXUeozwtyZQXjZ9csWxYWA=CB0516DF",
        "project_key": "WM"
    },
    {
        "email": "evalswe02@gmail.com",
        "api_token": "ATATT3xFfGF0sqdSmU8P45p0uBOFwhuQ7xJCxf-D3hxUmHS-TvMfLYemWarAFYnCGPx0Tny6O7aNMa9RF2ICnTYYFk3eflEinzK827st-S2BaDuFq3Q95ckTe1ev4v15rfT62tLPxKa7-HwxgMKTHrz8hSCIdncEHJBapu-gvIzK0FlafZf3Da4=11B4E133",
        "project_key": "WM"
    },
    {
        "email": "evalswe03@gmail.com",
        "api_token": "ATATT3xFfGF0lxB9CfaKZmWridZnCeZMYwoTMxFvMsAkHWnqX4rpWGFICb4IQG9uDZ6cUHdJYfKSuS62BrJ90_e_ylGx66-mhOVj1DaeL0el6mX6g8jiKrBI3X8sBAxs-9O4CjqvEnRcap6h5iMf1c2FTOU-Gfr7mq47XaJxoWtB9g8p7qTTA28=51ACEA68",
        "project_key": "BC"
    }
]

titles = [
    "Fix login page design issue", "UI glitch in dashboard",
    "Optimize database query", "Create profile page"
]

descriptions = [
    "Reported by QA team.", "Requested by client.", "Found during testing.",
    "Blocking issue in sprint.", "High priority."
]


def create_issue(user):
    url = f"{JIRA_URL}/rest/api/3/issue"
    auth = (user["email"], user["api_token"])
    issue_data = {
        "fields": {
            "project": {
                "key": user["project_key"]
            },
            "summary": random.choice(titles),
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": random.choice(descriptions)
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"
            }
        }
    }

    response = requests.post(url, json=issue_data, auth=auth)
    if response.status_code == 201:
        print(f"Issue created successfully by {user['email']}")
    else:
        print(f"Failed for {user['email']}: {response.status_code}")
        print(response.text)


for user in users:
    create_issue(user)
