from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests

# If modifying these scopes, delete the file tokudo.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']


def main():
   
    
    creds = None
    if os.path.exists('tokudo.json'):
        creds = Credentials.from_authorized_user_file('tokudo.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'certificados/classroom/testes.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokudo.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('classroom', 'v1', credentials=creds)
        
        # Call the Classroom API
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # Prints the names of the first 10 courses.
        temp = []
        for course in courses:
            temp.append({'name':course['name'],'id':course['id'],'alternateLink':course['alternateLink'], 'courseState':course['courseState']})
           
        return temp

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()