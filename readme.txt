# Automatic Contact Saver

This project automates the process of adding contacts to your Gmail account using Python.

## Features

- Add single or multiple contacts automatically.
- Uses Google People API for secure integration.
- Supports CSV and JSON input formats.

## Requirements

- Python 3.7+
- Google API Client Library
- Google account with API access

## Setup

1. Clone this repository.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up Google People API credentials:
    - Go to [Google Cloud Console](https://console.cloud.google.com/).
    - Create a project and enable the People API.
    - Download `credentials.json` and place it in the project directory.

## Usage

1. Prepare your contacts in `contacts.csv` or `contacts.json`.
2. Run the script:
    ```
    python add_contacts.py
    ```
3. Follow the authentication prompt.

## Notes

- Your contacts will be added to the authenticated Gmail account.
- Do not share your credentials file.

## License

MIT License