
import streamlit as st
import streamlit.components.v1 as components
from app import linkedin_post_generator
import json

st.set_page_config(
    page_title="LinkedIn Post Generator",
    layout="centered"
)

st.title("LinkedIn Post Generator")
st.caption("Generate professional LinkedIn posts using AI.")

if "messages" not in st.session_state:
    st.session_state.messages = []

language = st.selectbox(
    "Select Language",
    ["English", "Bengali", "Spanish"]
)

def copy_button(text, key):
    safe_text = json.dumps(text)

    components.html(
        f"""
        <button id="{key}" style="
            background: white;
            border: 1px solid #ccc;
            border-radius: 6px;
            padding: 6px 14px;
            cursor: pointer;
            font-size: 13px;
        ">Copy</button>

        <script>
        document.getElementById("{key}").addEventListener("click", async function() {{
            const text = {safe_text};

            try {{
                await navigator.clipboard.writeText(text);
                this.innerText = "Copied!";
            }} catch (err) {{
                this.innerText = "Copy failed";
            }}
        }});
        </script>
        """,
        height=40
    )


# Display chat history
for i, message in enumerate(st.session_state.messages):

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant":
            copy_button(message["content"], f"copy_{i}")


# Chat input
if prompt := st.chat_input("Enter your topic..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Generating post..."):

            try:
                response = linkedin_post_generator(
                    topic=prompt,
                    language=language
                )

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

                copy_button(
                    response,
                    f"copy_new_{len(st.session_state.messages)}"
                )

            except Exception as e:
                st.error(str(e))
