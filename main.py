import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is harizz and you can't generate image " + txt)
    return response.text

st.title("Welcome to Harizz Ai Assistant")

command = st.chat_input("how can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "who created you" in command:
        with st.chat_message("BOT"):
            st.write("The AI assistent is created by hariharan ethical hacker and aspiring cloud security engineer ")
            st.session_state.message.append({"role":"BOT","message":"The AI assistent is created by hariharan ethical hacker and aspiring cloud security engineer"})
    elif "kavi" in command:
        with st.chat_message("BOT"):
            st.write("kavi is hariharan's sister")
            st.session_state.message.append({"role":"BOT","message":"kavi is hariharan's sister"})

    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})


print(st.session_state.message)
