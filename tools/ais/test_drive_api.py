import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.

#values = result.get('values', [])
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1oCSdX22gftKHzokHcAlGy0JphlgJjB71NWsrEIyMyKc'
SAMPLE_RANGE_NAME = 'n'
tag_list = ['n','v','a','e','r']

if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
total = 0
for each_tag in tag_list:
    xlsx = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=each_tag).execute()
    values = xlsx.get('values', [])
    count = 0
    amb = 0
    for each in values:
        count += len(each)
        if len(each) == 2 and each[0] == each[1]:
            amb += 1
    count -= len(values)
    total += count
    print(each_tag ," : ", count)
    print(each_tag ," - amb: ", amb)

print("total : ",total)

