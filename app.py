import streamlit as st
import openai
import os
import time
import numpy as np
from langchain.prompts import ChatPromptTemplate
import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import json
from langflow.load import run_flow_from_json



st.title ("ReadAid.ai : Dyslexia & ADHD reader friendly content search and display")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

css = """
<style>
.stApp {
    background-color:#fdfd96; /* Replace with your desired color */
}
</style>
"""


st.markdown(css, unsafe_allow_html=True)

import datetime
current_date = datetime.datetime.now().date()
# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"
    
llm = ChatOpenAI(temperature=0.7, model=llm_model, api_key=OPENAI_API_KEY)


def generate_content(users_input):

    TWEAKS = {
      "ChatInput-eRZ4s": {},
      "Prompt-WxrOa": {},
      "ChatOutput-G3OiS": {},
      "OpenAIModel-RZuxG": {}
    }

    print('**********')
    print(users_input)
    print('**********')
    result = run_flow_from_json(flow="LangFlow_Hackathon.json",input_value=users_input,fallback_to_env_vars=True, tweaks=TWEAKS)
    #Saving HTML
    result = result[0].outputs[0].results['message'].data['text']
    result = result.replace("```html","").replace("```","")
    print('Result:')
    print('______________________')
    print(result)
    print('______________________')
    st.html(result)
    #st.write(response.content)

users_input = st.text_area("Enter the Topic on which you want Information:")
button_pressed = st.button("Generate Content with Readability")

if button_pressed:
    generate_content(users_input)
    
