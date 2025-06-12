from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_drive_service(token_file):
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    return build('drive', 'v3', credentials=creds)


def comment_and_reply():
    with open("doc_id.txt") as f:
        doc_id = f.read().strip()
    with open("comment_id_user2.txt") as f:
        comment_id = f.read().strip()

    service = get_drive_service('token_user3.json')

    comment = {'content': "Add a separate section for features?"}
    service.comments().create(fileId=doc_id, body=comment).execute()
    print("User3 added another comment")

    reply = {'content': "Yes, I agree. It could be clearer."}
    service.replies().create(fileId=doc_id, commentId=comment_id, body=reply).execute()
    print("User3 replied to User2")


if __name__ == '__main__':
    comment_and_reply()
