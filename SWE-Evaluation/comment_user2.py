from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_drive_service(token_file):
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    return build('drive', 'v3', credentials=creds)


def comment_on_doc():
    with open("doc_id.txt") as f:
        doc_id = f.read().strip()

    service = get_drive_service('token_user2.json')

    comment = {
        'content': "Can we improve this introduction?",
    }
    created = service.comments().create(
        fileId=doc_id, body=comment, fields='*').execute()
    print(f"User2 Commented: {created['content']} (ID: {created['id']})")

    with open("comment_id_user2.txt", "w") as f:
        f.write(created['id'])


if __name__ == '__main__':
    comment_on_doc()
