from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive']


def get_services(token_file):
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    docs_service = build('docs', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    return docs_service, drive_service


def create_and_share_doc():
    docs_service, drive_service = get_services('token.json')

    doc = docs_service.documents().create(
        body={'title': 'SWE Multi-User Comments'}).execute()
    doc_id = doc['documentId']
    print(f"Document Created: https://docs.google.com/document/d/{doc_id}")

    # Insert content
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': [{
            'insertText': {
                'location': {'index': 1},
                'text': 'This document is for testing multi-user commenting.\n\n'
            }
        }]}
    ).execute()

    for email in ["evalswe02@gmail.com", "evalswe03@gmail.com"]:
        drive_service.permissions().create(
            fileId=doc_id,
            body={'type': 'user', 'role': 'writer', 'emailAddress': email},
            sendNotificationEmail=False
        ).execute()
        print(f"Shared with {email}")

    return doc_id


def user2_add_comment(doc_id):
    _, drive_service = get_services('token_evalswe02.json')

    comment = {'content': "Can we improve this introduction?"}
    created = drive_service.comments().create(
        fileId=doc_id, body=comment, fields='*').execute()

    comment_id = created['id']
    print(f"User2 Commented: {created['content']} (ID: {comment_id})")

    return comment_id


def user3_reply_comment(doc_id, comment_id):
    _, drive_service = get_services('token_evalswe03.json')

    reply = {'content': "Yes, that's a good idea. Let's revise it."}
    drive_service.replies().create(
        fileId=doc_id,
        commentId=comment_id,
        body=reply
    ).execute()
    print(f"User3 Replied: {reply['content']}")


if __name__ == '__main__':
    doc_id = create_and_share_doc()
    comment_id = user2_add_comment(doc_id)
    user3_reply_comment(doc_id, comment_id)
