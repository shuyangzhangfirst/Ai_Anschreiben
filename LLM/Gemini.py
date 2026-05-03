from langchain_google_genai import ChatGoogleGenerativeAI

class LLM:
    def __init__(self, api_Key:str):
        self.llm=ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7, api_key=api_Key)