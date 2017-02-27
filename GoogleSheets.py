import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Gspead project-e9983b499213.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("Read_data_from GSheet")
wks = gc.open("Read_data_from GSheet").sheet1
list_of_lists=wks.get_all_values()
