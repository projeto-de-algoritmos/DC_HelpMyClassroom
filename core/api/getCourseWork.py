from __future__ import print_function
import gc
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/classroom.coursework.students.readonly',
    'https://www.googleapis.com/auth/classroom.coursework.me.readonly',
    'https://www.googleapis.com/auth/classroom.coursework.students',
    'https://www.googleapis.com/auth/classroom.coursework.me'
]


def getRooms(idRoom):
   
    creds = None
    try:
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'certificados/classroom/testes.json', SCOPES)
                creds = flow.run_local_server(port=0)
                print(creds)
            # Save the credentials for the next run
            try:
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())
            except Exception as error:
                print(error)       
    except Exception as error:
        print(error)          
    

    try:
        service = build('classroom', 'v1', credentials=creds)
        studentsFormated = []
        # Call the Classroom API
        results = service.courses().courseWork().list(courseId = idRoom).execute()
        print(results)

    except Exception as error:
        print(error)    
    
        
if __name__ == '__main__':
    getRooms('525987525315')