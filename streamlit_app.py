import streamlit as st
import openai
# import os
# import click

def sample_app():
    st.title("Sample Code Generator app with OpenAI ")
    st.write("Welcome")
    number=st.slider("Select a number",0,100,30)
    st.write("You selected",number)

    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    language = st.selectbox("Select the programming language", ["Python", "JavaScript", "Java"])
    question_prompt = st.text_area("Enter your question prompt")


    openai.api_key = api_key
    # models = openai.Engine.list()
    # st.write(models)

    if st.button("Click me to answer your question!"):
        code = submit_question(api_key, question_prompt, language)
        st.write(code)

def submit_question(api_key, question,language):
    print(f"{api_key} \n {question}\n {language}")
    openai.api_key=api_key#os.getenv("API_KEY")
    prompt=f"## Generate {language}  code for: {question}"
    try:
        result=openai.Completion.create(model="gpt-3.5-turbo-16k-0613",
                                        max_tokens=300,prompt=prompt,temperature=0,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0,
                                        )


        return result.choices[0].text.strip("\n")
    
    except openai.error.AuthenticationError:
        return "Invalid API key. Please check and try again."



if(__name__=="__main__"):
    sample_app()