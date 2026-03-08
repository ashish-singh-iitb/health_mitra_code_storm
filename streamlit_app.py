import boto3
import streamlit as st

AWS_REGION = "us-east-1"
MODEL_ID = "arn:aws:bedrock:us-east-1:096293429276:inference-profile/global.amazon.nova-2-lite-v1:0"

bedrock = boto3.client("bedrock-runtime", region_name=AWS_REGION)

st.title("🤖 HealthMitra Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def ask_nova(prompt):

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        inferenceConfig={
            "maxTokens": 1000,
            "temperature": 0.7
        }
    )

    return response["output"]["message"]["content"][0]["text"]

prompt = st.chat_input("Ask something")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    reply = ask_nova(prompt)

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})