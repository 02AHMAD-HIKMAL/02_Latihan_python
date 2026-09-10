import gspread
import getpass
from google.oauth2.service_account import Credentials
from datetime import datetime

# Lokasi credentials.json
SERVICE_ACCOUNT_FILE = "credentials.json"

# Hak akses Google Sheets dan Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Login Google
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

gc = gspread.authorize(credentials)

# Buka Google Spreadsheet
sheet = gc.open("database").sheet1

# Input data
nama = input("Masukkan nama : ")
kelas = input("Masukkan kelas : ")
password = getpass.getpass("Masukkan password : ")

# Waktu saat data dimasukkan
timer = datetime.now().strftime("%H:%M:%S")

# Simpan ke Google Sheets
sheet.append_row([nama, kelas, timer,password])

print("\nData berhasil disimpan!")
print("Nama  :", nama)
print("Kelas :", kelas)
print("password:", "*" * len(password))
print("Timer :", timer)
