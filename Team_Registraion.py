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
import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("hourglass-with-sand-middle-word-sand-it.jpg")

st.set_page_config(
    page_title="Team Registration for Acunetix 11.0",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)
page_by_img = '''
<style>
[data-testid="stApp"] >.block-container st-emotion-cache-z5fcl4 ea3mdgi2 ::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: url("https://images.unsplash.com/photo-1505506874110-6a7a69069a08?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8fA%3D%3D") center center / cover;
    opacity: 0.5; /* Adjust the overlay opacity value as needed (0.0 to 1.0) */
    background-repeat:no repeat;
    background-attachment:local;

[data-testid="stHeader"]{
    background-color:rgba(0,0,0,0);
}
[data-testid="stMainMenu"] {
right: 2rem;
}
[data-testid="stSidebarNavItems"]> div:first-child {
background-image: url("data:image/jpg;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}
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


# You can add more content or information here based on your needs



