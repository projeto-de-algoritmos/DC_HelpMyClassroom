from __future__ import print_function
import gc
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = [
    'https://www.googleapis.com/auth/classroom.rosters',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/classroom.profile.emails',
    'https://www.googleapis.com/auth/classroom.profile.photos'
]

def getRooms(idRoom):
   
    creds = None
    try:
        if os.path.exists('core/api/token.json'):
            creds = Credentials.from_authorized_user_file('core/api/token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'core/api/cred.json', SCOPES)
                creds = flow.run_local_server(port=0)
                print(creds)
            # Save the credentials for the next run
            try:
                with open('core/api/token.json', 'w') as token:
                    token.write(creds.to_json())
            except Exception as error:
                print(error)       
    except Exception as error:
        print(error)          
    

    try:
        service = build('classroom', 'v1', credentials=creds)
        studentsFormated = []
        # Call the Classroom API
        results = service.courses().students().list(courseId = idRoom, pageSize=10).execute()
        
        if 'students' in results:
            for x in results['students']:
                try:
                    studentsFormated.append({'id': x['userId'],'email': x['profile']['emailAddress'], 'nome': x['profile']['name']['fullName'], 'foto':x['profile']['photoUrl']})
                except Exception:
                    continue

        
        return studentsFormated     
    
    except Exception as error:
        print(error)   

if __name__ == '__main__':
    getRooms('525987525315')
    
        
