from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_drive_service(token_file):
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    return build('drive', 'v3', credentials=creds)


def reply_as_user1():
    with open("doc_id.txt") as f:
        doc_id = f.read().strip()
    with open("comment_id_user2.txt") as f:
        comment_id = f.read().strip()

    service = get_drive_service('token_user1.json')

    reply1 = {'content': "Thanks! I’ll rework the intro section."}
    service.replies().create(fileId=doc_id, commentId=comment_id, body=reply1).execute()

    print("User1 replied to User2")


if __name__ == '__main__':
    reply_as_user1()
