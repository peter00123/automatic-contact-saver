import pandas as pd
import os.path
import pickle
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh()
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('people', 'v1', credentials=creds)

def log_contact_creation(contact_name):
    # Write to log file every time a contact is successfully created
    with open('contact_creation_log.txt', 'a') as log_file:
        log_file.write(f"Successfully added contact: {contact_name}\n")

def add_contacts_from_excel(file_path):
    df = pd.read_excel(file_path)
    service = get_service()

    for index, row in df.iterrows():
        # Skip rows with missing essential data (e.g., missing both name and phone)
        if pd.isna(row['Phone']):
            print(f"Skipping row {index + 1}: Missing phone number")
            continue
        
        # Prepare contact data
        contact_body = {
            "phoneNumbers": [{"value": str(row['Phone'])}]
        }
        
        # Handle first name and last name if available
        if not pd.isna(row['First Name']):
            contact_body["names"] = [{"givenName": row['First Name']}]
        if not pd.isna(row['Last Name']):
            if "names" not in contact_body:
                contact_body["names"] = []
            contact_body["names"].append({"familyName": row['Last Name']})

        # Add email if it's not empty or NaN
        if not pd.isna(row.get('Email')):
            contact_body["emailAddresses"] = [{"value": row['Email']}]

        try:
            # Send contact creation request
            service.people().createContact(body=contact_body).execute()
            contact_name = f"{row['First Name'] or ''} {row.get('Last Name', '')}".strip()
            print(f"Added contact: {contact_name}")
            
            # Log the successful addition
            log_contact_creation(contact_name)
            
            time.sleep(1)  # Avoid hitting the rate limit
        except Exception as e:
            print(f"Error adding contact at row {index + 1}: {e}")

if __name__ == '__main__':
    add_contacts_from_excel('contacts.xlsx')
