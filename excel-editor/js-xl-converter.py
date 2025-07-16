import json
import pandas as pd

# Load JSON from external file
with open("contacts.json", "r", encoding="utf-8") as file:
    data = json.load(file)

contacts_list = data["contacts"]["list"]
formatted_contacts = [
    {
        "fname": contact["first_name"],
        "sname": contact["last_name"],
        "p.hno": contact["phone_number"]
    }
    for contact in contacts_list
]

# Create DataFrame
df = pd.DataFrame(formatted_contacts)

# Write to Excel
df.to_excel("contacts.xlsx", index=False)

print("Excel file 'contacts.xlsx' created successfully.")