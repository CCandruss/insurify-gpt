import getpass
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ[f"{OPENAI_API_KEY}"] = getpass.getpass()


llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
