import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('hbcred.json', scope)
client = gspread.authorize(credentials)

## Creating & Sharing New Google Sheet
# sheet = client.create("FirstSheet")
# sheet.share('carlglibrary@gmail.com', perm_type='user', role="writer")

## Opening existing Google Sheet
sheet = client.open("FirstSheet").sheet1

## Open CSV file & Write to Google Sheet using panda
df = pd.read_csv('football_news.csv')

sheet.update([df.columns.values.tolist()] + df.values.tolist())

