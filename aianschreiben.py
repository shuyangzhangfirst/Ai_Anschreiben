
from Person import Person
from Jobinfo import jobinfo
from langchain_google_genai import ChatGoogleGenerativeAI

from Skills import skill,skills
from Experience import experience,experiences
from Education import education,educations

class ai_anschreiben:
    def __init__(self, person: Person, jobinfo: jobinfo,api_key:str,language:str="Germany"):
        self.person = person
        self.jobinfo = jobinfo
        self.api_key=api_key
        self.language = language
    
    def generate_cover_letter(self):
        llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7, api_key=self.api_key)
        prompt = f"Write a cover letter for the following job application with {self.language} language:\n\nJob Title: {self.jobinfo.jobtitle}\nCompany Name: {self.jobinfo.companyname}\nJob Description: {self.jobinfo.jobdescription}\n\nPersonal Information:{self.person.to_string()}"
        
        
        response = llm.invoke(prompt)
        return response





    