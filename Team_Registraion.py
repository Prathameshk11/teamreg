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


st.set_page_config(
    page_title="Team Registration for Acunetix 11.0",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)
page_by_img = '''
<style>
[data-testid="stApp"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/aaf421ab-32a1-4f50-a205-3cf74d85063d/dfwcif4-045c2496-191e-4d7b-be5e-489e31d35dd5.png/v1/fill/w_1280,h_725,q_80,strp/time_traveling_machines__1_by_veesyrsfantasy_ai_dfwcif4-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2FhZjQyMWFiLTMyYTEtNGY1MC1hMjA1LTNjZjc0ZDg1MDYzZFwvZGZ3Y2lmNC0wNDVjMjQ5Ni0xOTFlLTRkN2ItYmU1ZS00ODllMzFkMzVkZDUucG5nIiwiaGVpZ2h0IjoiPD03MjUiLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS53YXRlcm1hcmsiXSwid21rIjp7InBhdGgiOiJcL3dtXC9hYWY0MjFhYi0zMmExLTRmNTAtYTIwNS0zY2Y3NGQ4NTA2M2RcL3ZlZXN5cnNmYW50YXN5LWFpLTQucG5nIiwib3BhY2l0eSI6OTUsInByb3BvcnRpb25zIjowLjQ1LCJncmF2aXR5IjoiY2VudGVyIn19.EhbE0PxnYj3QTPIubIuNRCH5vE1QqESpwB6nBu41nQ4") center center / cover;
    opacity: 0.5; /* Adjust the overlay opacity value as needed (0.0 to 1.0) */
}
[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

</style>
'''
st.markdown(page_by_img, unsafe_allow_html=True)


image_url = "https://i.ibb.co/GVR0QvY/acunetixheader.png"
st.image(image_url, use_column_width=True) 

# Function to write data to Google Sheet
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("litforms.json", scope)
client = gspread.authorize(creds)

# Replace 'Sheet Name' with your actual+ sheet name
sheet = client.open_by_key("1VeWt6NBUGqc_4TldxqFfrw9qWhd_4n_FKM0H0XEvoLw").worksheet("Sheet1")

# Adding a title with style
st.title("Team Registration for Acunetix 11.0 🛑🚀")

st.markdown("---")

# Adding the general guidelines with style
st.subheader("General Guidelines for Acunetix 11.0 Participants:")
st.write("🛑 Fill details of every team member.")
st.write("🔮 All participants are advised to report at the event venue 15 minutes before the event start time.")
st.write("📡If any candidate(s) fail to comply with the event rules, the team will be disqualified immediately.")
st.write("🌐Misbehavior or any acts that may lead to disruption of any event won't be tolerated. "
         "Any participant(s) found guilty will be disqualified immediately.")
st.write("🌌Team Acunetix will only engage in communication with the Team leads. "
         "Team leads are responsible for any further communication between Team members. "
         "Hence, we advise the team leads to check on updates.")
st.write("🕰️ Team Acunetix reserves the right to modify decisions in case of any fouls and won't be accountable.")
st.markdown("---")

st.subheader("Ready to Register?")
st.write("🚀 Secure your team's spot in the chronicles of Acunetix 11.0! Time waits for no one.")
st.write('To register for team event access the sidebar using the button in the top left corner') 
