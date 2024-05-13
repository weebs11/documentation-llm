import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI

load_dotenv()

client = OpenAI()
llm = ChatOpenAI()

st.title('Streamlit Test')
st.write('This is a test of Streamlit.')

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"You are a teacher helping me understand the following documentation on the aiR for Review product in Relativity."},
    {"role": "user", "content": f"What permissions are needed to run aiR for Review?"}
  ]
)

st.write(completion.choices[0].message.content)