import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the required Google API scopes
SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive']


def get_services(token_file='token.json'):
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    docs_service = build('docs', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    return docs_service, drive_service


def create_doc(docs_service):
    title = "SWE Evaluation Sample Doc"
    doc = docs_service.documents().create(body={"title": title}).execute()
    doc_id = doc.get('documentId')
    print(f"📄 Document created: {title} (ID: {doc_id})")

    content = (
        "This is a test document for the SWE evaluation.\n\n"
        "Sections:\n"
        "1. Introduction\n"
        "2. Features\n"
        "3. Timeline\n"
        "4. Feedback\n"
    )
    requests = [{
        'insertText': {
            'location': {'index': 1},
            'text': content
        }
    }]
    docs_service.documents().batchUpdate(
        documentId=doc_id, body={'requests': requests}
    ).execute()
    print("📝 Content inserted into the document.")
    return doc_id


def share_doc(drive_service, doc_id, emails):
    for email in emails:
        permission = {
            "type": "user",
            "role": "writer",
            "emailAddress": email
        }
        drive_service.permissions().create(
            fileId=doc_id,
            body=permission,
            sendNotificationEmail=True
        ).execute()
    print(f"🔗 Document shared with: {', '.join(emails)}")


def add_real_comments_and_replies(drive_service, file_id):
    sample_comments = [
        {
            "comment": "Can we rephrase the introduction?",
            "reply": "Sure, I’ll update it."
        },
        {
            "comment": "Add a section for future scope.",
            "reply": "Good idea, I’ll include that."
        },
        {
            "comment": "Please clarify the timeline here.",
            "reply": "I’ll add specific dates."
        }
    ]

    for item in sample_comments:
        comment = {
            'content': item["comment"]
        }
        created_comment = drive_service.comments().create(
            fileId=file_id,
            body=comment,
            fields="*"
        ).execute()
        print(f"💬 Added comment: {item['comment']}")

        reply = {
            'content': item["reply"]
        }
        drive_service.replies().create(
            fileId=file_id,
            commentId=created_comment['id'],
            body=reply,
            fields="*"
        ).execute()
        print(f"↪️ Replied: {item['reply']}")


def main():
    docs_service, drive_service = get_services()
    doc_id = create_doc(docs_service)
    share_doc(drive_service, doc_id, [
        "evalswe02@gmail.com", "evalswe03@gmail.com"
    ])
    add_real_comments_and_replies(drive_service, doc_id)


if __name__ == '__main__':
    main()
