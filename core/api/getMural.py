from __future__ import print_function
import gc
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/classroom.announcements.readonly'
]


def getMural(idRoom):
   
    creds = None
    try:
        if os.path.exists('core/api/tokenmural.json'):
            creds = Credentials.from_authorized_user_file('core/api/tokenmural.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'core/api/cred.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            try:
                with open('core/api/tokenmural.json', 'w') as token:
                    token.write(creds.to_json())
            except Exception as error:
                print(error)       
    except Exception as error:
        print(error)          
    # foto': x['materials']['title']['fullName'], 'foto':x['profile']['thumbnailUrl']
    # 'materials': x['materials']['title']

    try:
        service = build('classroom', 'v1', credentials=creds)
        studentsFormated = []
        # Call the Classroom API
        results = service.courses().announcements().list(courseId = idRoom).execute()
        
        if 'announcements' in results:
            for x in results['announcements']:
                try:
                    if 'materials' in x:
                        studentsFormated.append({'id': x['id'],'text': x['text'],'alternateLink':x['alternateLink'],'foto': x['materials'][0]['driveFile']['driveFile']['thumbnailUrl']})
                    else:
                        studentsFormated.append({'id': x['id'],'text': x['text'], 'alternateLink':x['alternateLink']})               
                except Exception:
                    continue
        
        return(studentsFormated)

    except Exception as error:
        print(error)    
    
        
if __name__ == '__main__':
    getMural('525987525315')