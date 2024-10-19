import streamlit as st

# Title of the app
st.title("Call Answering App")

# Text input for the custom message
custom_message = st.text_area("Enter your custom message:", "Hello! I can't take your call right now.")

# Button to simulate saving the message
if st.button("Save Message"):
    st.success("Message saved!")

# Display the current message
st.write("Current message:")
st.write(custom_message)
