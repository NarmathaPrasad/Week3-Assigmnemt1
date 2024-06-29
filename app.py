import streamlit as st
from datetime import datetime

user_db = {
    'admin': 'admin',
    'user1': 'password1',
}

# Task 1: Login
def login(username, password):
    if username in user_db and user_db[username] == password:
        return True
    return False

def main():
    st.title("Welcome to my webpage")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'date' not in st.session_state:
        st.session_state['date'] = None

    if 'time' not in st.session_state:
        st.session_state['time'] = None

    if 'profile_pic' not in st.session_state:
        st.session_state['profile_pic'] = None

    if st.session_state['logged_in']:
        st.write(f"Welcome, {st.session_state['username']}!")

        # Option to upload profile picture
        uploaded_file = st.file_uploader("Upload a profile picture", type=['jpg', 'png', 'jpeg'])

        if uploaded_file is not None:
            st.session_state['profile_pic'] = uploaded_file

        if st.session_state['profile_pic'] is not None:
            st.image(st.session_state['profile_pic'], caption='Uploaded profile picture', use_column_width=True)

        # Task 2: Date and time input
        date = st.date_input("Select a date")
        time = st.time_input("Select a time")

        if st.button("Submit"):
            st.session_state['date'] = date
            st.session_state['time'] = time
            st.write(f"Selected date: {date}")
            st.write(f"Selected time: {time}")

        # Task 3 Display section
        if st.session_state['date'] and st.session_state['time']:
            st.write("Previously selected:")
            st.write(f"Date: {st.session_state['date']}")
            st.write(f"Time: {st.session_state['time']}")

            show_info = st.checkbox("Show additional information")
            if show_info:
                st.write("Use slider to enlarge the font size...")

                st.balloons()

                # Text size slider
                text_size = st.slider("Adjust text size", 10, 50, 20)
                st.markdown(f"<p style='font-size:{text_size}px;'>Selected date: {st.session_state['date']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size:{text_size}px;'>Selected time: {st.session_state['time']}</p>", unsafe_allow_html=True)

        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['date'] = None
            st.session_state['time'] = None
            st.session_state['profile_pic'] = None

    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")


if __name__ == "__main__":
    main()
