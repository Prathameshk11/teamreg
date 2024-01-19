
import streamlit as st

# Setting page style
st.set_page_config(
    page_title="404: Teams Lost in Cosmic Time Warp!",
    page_icon="⏳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Adding a title with style
st.title("404: Teams Lost in Cosmic Time Warp! 🌌⏳")
st.markdown("---")

# Adding the main content with style
st.write("Oops! Teams seem stuck in a cosmic time warp, where seconds feel like light-years. ")
st.write("But hey, Brainiac Buddy! While teams navigate time loops, you're all set for a solo adventure that defies the clock. "
         "Break out of your comfort zone, show off your skills in tests and discussions, and get ready for the big placement journey! 🚀🌠💼")

# Adding a styled separator
st.markdown("---")

gif_url = "https://media1.tenor.com/images/fbcad0ba0bf7432ead187816ff7cc8a7/tenor.gif?itemid=5065430"  # Replace with your GIF URL
st.image(gif_url, caption="Embark on your solo adventure!", use_column_width=True)