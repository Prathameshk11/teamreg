import streamlit as st
import gspread
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import pandas as pd
from gspread_dataframe import set_with_dataframe
FOLDER_ID="1T3RiNpcYS-vbtSa_AN7z_ZlQbiZtLJfj"





# Function to write data to Google Sheet
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("litforms.json", scope)
client = gspread.authorize(creds)

# Replace 'Sheet Name' with your actual+ sheet name
sheet = client.open_by_key("1VeWt6NBUGqc_4TldxqFfrw9qWhd_4n_FKM0H0XEvoLw").worksheet("Sheet1")
st.title("Team Registration")

st.write("Welcome!")
st.write('To register for team event access the sidebar using the button in the top left corner') 

import streamlit as st

st.title('Time-Warped Brainiac: Teams, Rewind Your Maps!')


def display_brainiac_event():
    st.markdown("## Brainiac Challenge Solo Participants:")
    st.markdown("🚀 Greetings Time-Traveling Brainiac! 🧠⏳")
    st.markdown("Whoa! You've bravely embarked on the Brainiac Challenge solo journey. "
                "No need for a sidekick when you're the superhero of intellect! 🦸‍♂️💡\n\n"
                "Prepare for mind-bending aptitude tests, intellectual debates, and a mock interview "
                "(don't worry, the interviewers are nice time-traveling folks). "
                "Your solo mission: to conquer brains across the space-time continuum! 🌌✨\n\n"
                "Solo maestro, your wit is the DeLorean, and you're about to hit 88 mph into "
                "the solo adventure of a lifetime!\n\n"
                "P.S. Remember, in the time-traveling circus of brilliance, you're the solo acrobat! 🎩🌟")


