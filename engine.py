import os
import openai
import hidden

openai.api_key = hidden.key
import betterprompt
import os

os.environ["OPENAI_API_KEY"] = hidden.key


def generate(prompt, num_prompts):
    prompts = []
    s = "Improve the following prompt: " + "\n\n" + "'" + prompt + "'"
    for i in range(num_prompts):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=s,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0,
        )
        prompt_generated = response.choices[0].text
        prompts.append(prompt_generated.strip())
        s = "Improve the following prompt: " + "\n\n" + "'" + prompts[-1] + "'"
    return prompts


def calculate(prompt):
    perplexity = betterprompt.calculate_perplexity(prompt)
    return perplexity


def execute(input_field):
    streamlit_input = input_field
    prompts = generate(streamlit_input, 3)
    perplixity_l = []
    for prompt in prompts:
        perplixity_l.append(calculate(prompt))
    final = prompts[perplixity_l.index(min(perplixity_l))]
    return final


############################################################################################################################################################################
import streamlit as st

st.header("Prompt-Improver")
st.markdown("##")
st.markdown(
    "**Example prompt:** \n\n I want to set a random number which is not 0 in a list to a different number. If the list contains only 0s than I want to do nothing:\n\n[0 0 0 0 0 1 2 0 0 1 2 0 0 0 0 0 0 1 2 0 0 5 6 0]\n\nWhats the best way of doing this?"
)
st.markdown("##")

input_field = st.text_input("Enter your prompt:")

if input_field:
    output = execute(input_field)
    st.write("Output: ", output)

st.markdown("##")
st.header("How it works:")
st.image("image.png")
