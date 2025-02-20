import os
import streamlit as st
import requests
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def lungcancer_llm(get_this_id):
    output = []

    if get_this_id:
        get_this_id = get_this_id.lower()

        if get_this_id in ['adenocarcinoma_lung_cancer', 'neuroendocrine_tumors', 'squamous_cell_carcinoma']:
            response = requests.get('https://canceproit.pythonanywhere.com/hereignore')
            data = response.json()
            take_this = data[0]

            os.environ["OPENAI_API_KEY"] = take_this

            # Create an OpenAI client.
            stream = openai.ChatCompletion.create(
                model="gpt-4",  # Use a valid model name
                messages=[{
                    "role": "user",
                    "content": f"You are a helpful assistant to tell only about Cancer and health related questions. "
                               f"You have to give information about {get_this_id} only from World Health Organization, "
                               f"Tata Memorial Cancer Institute, and other well established Medical institutes. "
                               f"Give in 400 words, try to highlight symptoms and necessary precautions about the cancer type {get_this_id}."
                }],
                stream=True,
            )
        
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content is not None:
                    output.append(chunk.choices[0].delta.content)

        
            # # Create an OpenAI client.
            # stream = openai.ChatCompletion.create(
            #     model="gpt-4o-mini",
            #     messages=[{"role": "user", "content": f"You are a helpful assistant to tell only about Cancer and health related questions. You have to give information about {get_this_id} only from World Health Organization, Tata Memorial Cancer Institute, and other well established Medical institutes. Give in 400 words, try to highlight symptoms and necessary precautions about the cancer type {get_this_id}."}],
            #     stream=True,
            # )
            # for chunk in stream:
            #     if chunk.choices[0].delta.content is not None:
            #         output.append(chunk.choices[0].delta.content)

        else:
            output = ["I am learning on daily basis, let's try another thing."]
    else:
        output = ["Invalid response, please try again."]

    return ''.join(output)

# Streamlit UI
get_this_id = st.query_params.get("get_parameterss")
output = lungcancer_llm(get_this_id)
st.write(output)



# from flask import Flask, render_template, request
# import json
# # import speech_recognition as sr
# # import request
# #Chat
# import warnings
# warnings.filterwarnings('ignore')
# import os
# import streamlit as st
# from openai import OpenAI
# import requests
# # from langdetect import detect
# # import io


# def lungcancer_llm():
#     # https://canceproit.pythonanywhere.com/lungcancer_llm?get_parameterss=Adenocarcinoma_Lung_Cancer
#     get_this_id = st.query_params.get("get_parameterss")

#     # get_this_id = request.query_params.get(get_parameterss)

#     output = []

#     if get_this_id:
#         get_this_id = get_this_id.lower()

#         if get_this_id == 'adenocarcinoma_lung_cancer' or get_this_id == 'neuroendocrine_tumors' or get_this_id == 'squamous_cell_carcinoma':
#             response = requests.get('https://canceproit.pythonanywhere.com/hereignore')
#             data = response.json()
#             take_this = data[0]

#             os.environ["OPENAI_API_KEY"] = take_this
#             # api_key = take_this

#             # Create an OpenAI client.
#             client = OpenAI()

#             stream = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[{"role": "user", "content": "You are a helpful assistant to tell only about Cancer and health related questions. You have to give information about {get_this_id} only from World Health Organization, Tata Memorial Cancer Institute, and other well established Medical instisutes. Give in 400 words, try to highlight symptoms and necessary precautions about the cancer type {get_this_id}."}],
#                 stream=True,
#             )
#             for chunk in stream:
#                 if chunk.choices[0].delta.content is not None:
#                     output.append(chunk.choices[0].delta.content, end="")


#         else:

#             output = ["I am learning on daily basis, let's try another thing."]
#     else:

#         output = ["Invalid response, please try again."]

#     return output


# st.write(output)
