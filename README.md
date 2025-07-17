

# Automatic Contact Saver

Automatically add contacts to your Gmail account using Python and the Google People API.

---

## 📌 About

This project is designed to simplify the process of adding large quantities of contacts into a Gmail account.
It is especially useful for:

* 📞 **Sales professionals** who manage extensive lead lists
* 🤝 **Networkers** regularly connecting with new people
* 🏫 **Institutions or organizations** needing to upload a large number of candidate/student records

By automating the contact addition process, it saves time and eliminates manual errors.
89 contacats can be added in a minute.

---

## 🚀 Features

* 🔄 Convert **JSON** and **CSV** files into a clean, structured **Excel** format
* 🧹 Includes basic **cleaning** and **sorting** methods for contact data
* 📊 Final input is processed through a standardized **Excel sheet**
* 🔒 Uses Google People API for secure contact creation

---

## 📦 Requirements

* Python 3.7 or higher
* [Google API Client Library](https://pypi.org/project/google-api-python-client/)
* A Google account with access to the People API

---

## ⚙️ Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/peter00123/automatic-contact-saver.git
   cd automatic-contact-saver
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google People API credentials**

   * Visit the [Google Cloud Console](https://console.cloud.google.com/)
   * Create a project and enable the **People API**
   * Configure the OAuth consent screen
   * Create **OAuth 2.0 Client ID** (Desktop type)
   * Download the `credentials.json` file
   * Place `credentials.json` in the root of the project directory

---

## 📁 Usage

1. Prepare your contact data in a `.csv` or `.json` file.
   The script will help convert and clean it into an Excel format.

2. Run the main script:

   ```bash
   python add_contacts.py
   ```

3. Authenticate via your Google account when prompted.
   Contacts will be added to your Gmail account from the cleaned Excel input.


---



## 📄 License

This project is **free to use** for personal and commercial purposes.
No attribution is required, but contributions are welcome.
Use responsibly and respect API usage limits.
