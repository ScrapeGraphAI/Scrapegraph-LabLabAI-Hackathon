import os
import base64
import streamlit as st
import json
import pandas as pd
from helper import (
    playwright_install,
    add_download_options
)
from task import task
from text_to_speech import text_to_speech

st.set_page_config(page_title="Scrapegraph-ai demo", page_icon="🕷️")

# Install playwright browsers
playwright_install()

def save_email(email):
    with open("mails.txt", "a") as file:
        file.write(email + "\n")

with st.sidebar:
    st.write("Official demo for [Scrapegraph-ai](https://github.com/VinciGit00/Scrapegraph-ai) library")
    st.markdown("""---""")
    st.write("# Usage Examples")
    st.write("## Prompt 1")
    st.write("- Give me all the news with their abstracts")
    st.write("## Prompt 2")
    st.write("- Create a voice summary of the webpage")
    st.write("## Prompt 3")
    st.write("- List me all the images with their visual description")
    st.write("## Prompt 4")
    st.write("- Read me the summary of the news")
    st.markdown("""---""")
    st.write("You want to suggest tips or improvements? Contact me through email to mvincig11@gmail.com")
    st.markdown("""---""")
    st.write("Follow our [Github page](https://github.com/ScrapeGraphAI)")


st.title("Scrapegraph-ai")
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("assets/scrapegraphai_logo.png")

key = st.text_input("Openai API key", type="password")
model = st.radio(
    "Select the model",
    ["gpt-3.5-turbo", "gpt-3.5-turbo-0125", "gpt-4", "text-to-speech", "gpt-4o", "gpt-4o-mini"],
    index=0,
)

url = st.text_input("base url (optional)")
link_to_scrape = st.text_input("Link to scrape")
prompt = st.text_input("Write the prompt")

if st.button("Run the program", type="primary"):
    if not key or not model or not link_to_scrape or not prompt:
        st.error("Please fill in all fields except the base URL, which is optional.")
    else:
        st.write("Scraping phase started ...")

        if model == "text-to-speech":
            res = text_to_speech(key, prompt, link_to_scrape)
            st.write(res["answer"])
            st.audio(res["audio"])
        else:
            # Pass url only if it's provided
            if url:
                graph_result = task(key, link_to_scrape, prompt, model, base_url=url)
            else:
                graph_result = task(key, link_to_scrape, prompt, model)

            print(graph_result)
            st.write("# Answer")
            st.write(graph_result)

            if graph_result:
                add_download_options(graph_result)

left_co2, *_, cent_co2, last_co2, last_c3 = st.columns([1] * 18)

with cent_co2:
    discord_link = "https://discord.com/invite/gkxQDAjfeX"
    discord_logo = base64.b64encode(open("assets/discord.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{discord_link}" target="_blank">
        <img src="data:image/png;base64,{discord_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )

with last_co2:
    github_link = "https://github.com/VinciGit00/Scrapegraph-ai"
    github_logo = base64.b64encode(open("assets/github.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{github_link}" target="_blank">
        <img src="data:image/png;base64,{github_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )

with last_c3:
    twitter_link = "https://twitter.com/scrapegraphai"
    twitter_logo = base64.b64encode(open("assets/twitter.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{twitter_link}" target="_blank">
        <img src="data:image/png;base64,{twitter_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )
