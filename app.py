import streamlit as st
import hmac

import os
from helpers import text_to_speech, speech_to_text
from generate_answer import base_model_chatbot
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

def main(answer_mode: str):
    float_init()

    def initialize_session_state():
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi I'm Speech2Speech LLM bot! How may I assist you today?"}
            ]


    initialize_session_state()

    st.title("Speech2Speech LLM bot 🤖")

    # Create footer container for the microphone
    footer_container = st.container()
    with footer_container:
        audio_bytes = audio_recorder()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if audio_bytes:
        # Write the audio bytes to a file
        with st.spinner("Transcribing..."):
            webm_file_path = "temp_audio.mp3"
            with open(webm_file_path, "wb") as f:
                f.write(audio_bytes)

            transcript = speech_to_text(webm_file_path)
            if transcript:
                st.session_state.messages.append({"role": "user", "content": transcript})
                with st.chat_message("user"):
                    st.write(transcript)
                os.remove(webm_file_path)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking🤔..."):
                if answer_mode == 'base_model':
                    final_response = base_model_chatbot(st.session_state.messages)
            with st.spinner("Generating audio response..."):
                 st.write(final_response)
                 text_to_speech(final_response)
            st.session_state.messages.append({"role": "assistant", "content": final_response})
            # os.remove(audio_file)

    # Float the footer container and provide CSS to target it with
    footer_container.float("bottom: 0rem;")
 
if __name__ == "__main__":
    main(answer_mode='base_model') # Or: answer_mode='pdf_chat' # To chat with your data