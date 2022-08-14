from __future__ import print_function
import gc
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/classroom.topics.readonly'
]


def getTopicos(idRoom):
   
    creds = None
    try:
        if os.path.exists('core/api/tokentopicos.json'):
            creds = Credentials.from_authorized_user_file('core/api/tokentopicos.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'core/api/cred.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            try:
                with open('core/api/tokentopicos.json', 'w') as token:
                    token.write(creds.to_json())
            except Exception as error:
                print(error)       
    except Exception as error:
        print(error)          
    

    try:
        service = build('classroom', 'v1', credentials=creds)
        studentsFormated = []
        # Call the Classroom API
        results = service.courses().topics().list(courseId = idRoom).execute()
        courses = results.get('topic', [])
        
        return courses

    except Exception as error:
        print(error)    
    
        
if __name__ == '__main__':
    getTopics('525987525315')