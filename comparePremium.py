import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('F:/mycred.json', scope)

client = gspread.authorize(credentials)

my_sheet = client.open('Business').sheet1

# Read the number and net_premium from the Google Sheet
number_from_sheet = int(my_sheet.acell('A1').value.replace(',',''))
net_premium =  float(my_sheet.acell('B1').value.replace(',',''))

# Compare the numbers
if net_premium > number_from_sheet:
    print(f"Net Premium {net_premium} is greater than the number {number_from_sheet} mentioned in the Google Sheet")
elif net_premium < number_from_sheet:
    print(f"Net Premium {net_premium} is lesser than the number {number_from_sheet} mentioned in the Google Sheet")
else:
    print(f"Net Premium is {net_premium} equal to the number {number_from_sheet} mentioned in the Google Sheet")