import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from gspread_dataframe import set_with_dataframe

# Function to write data to Google Sheet
if 'submit_clicked' not in st.session_state:
    st.session_state.submit_clicked = False

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("litforms.json", scope)
client = gspread.authorize(creds)

# Replace 'Sheet Name' with your actual sheet name
sheet = client.open_by_key("1VeWt6NBUGqc_4TldxqFfrw9qWhd_4n_FKM0H0XEvoLw").worksheet("Sheet8")

st.title("Team Registration for Gamestorm")
search_id = st.text_input("Enter your ID:")

if search_id:

    # Fetch entire row corresponding to the ID
    cell = sheet.find(search_id)
    if cell:
        row_values = sheet.row_values(cell.row)
        name_str = row_values[cell.col]
        st.write(f"Hallo, {name_str} 👋!")

        game_str = row_values[cell.col + 7]
        game_list = game_str.split(",") if game_str else []
        st.write(f"Game for ID {search_id}:")
        st.write(game_list)

        with st.form("Team_Reg"):
            teammate_info_list = []
            for game in game_list:
                st.title(f"Teammates for : {game}")

                # Dynamically set the number of teammates based on the game
                if game in ["BGMI", "FreeFire"]:
                    game_modes = ["Duo", "Squad"]
                    selected_mode = st.selectbox(f"Select the game mode for {game}:", game_modes, key=f"{game}_mode")
                    num_mapping = {"Duo": 2, "Squad": 4}
                    num = num_mapping[selected_mode]
                else:
                    num = 5  # Default number of teammates for other games

                for i in range(num):
                    
                    teammate_name = st.text_input(f"Name of Teammate {i + 1}:", key=f"{game}_name_{i}")
                    teammate_number = st.text_input(f"Number of Teammate {i + 1}:", max_chars=10,
                                                    key=f"{game}_num_{i}")
                    teammate_email = st.text_input(f"Email of Teammate {i + 1}:", key=f"{game}_em_{i}")

                    teammate_info = {
                        'ID': search_id,
                        'For Event': game,
                        'Name': teammate_name,
                        'Number': teammate_number,
                        'Email': teammate_email
                    }

                    teammate_info_list.append(teammate_info)

            submit_button = st.form_submit_button("Submit")
            if submit_button:
                df = pd.DataFrame(teammate_info_list)
                w = client.open_by_key("1VeWt6NBUGqc_4TldxqFfrw9qWhd_4n_FKM0H0XEvoLw").worksheet("TeamReg")
                last = len(w.col_values(1)) + 1
                set_with_dataframe(w, df, row=last, include_index=False, include_column_header=False)
                st.success("Team Registered! ✨")
                st.dataframe(df)
                st.info("Thank You")

elif not search_id:
    st.warning("Enter valid ID")
