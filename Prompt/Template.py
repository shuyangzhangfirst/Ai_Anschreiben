
from .Person.Person import person
from .Target_Job.Jobinfo import jobinfo

class PromptTemplate:
    def __init__(self,language:str="Germany",style:str="formal"):
        self.person=person()
        self.target_job=None
        self.language=language
        self.style=style
    def load_person_profile(self,json_data_path):
        self.person.load_profile_from_json(json_data_path)
    def save_person_profile(self,json_data_path):
        self.person.save_profile_to_json(json_data_path)
    def add_person_information(self,name:str=None,age:int=None,phone_number:str=None,email:str=None,address:str=None):
        
        self.person.name=name
        
        self.person.age=age
        
        self.person.phone_number=phone_number
        
        self.person.email=email
        
        self.person.address=address
    def add_person_skill(self,skill_name:str , skill_level:str):
        self.person.add_skill(skill_name, skill_level)
    def add_person_hobby(self,hobby:str):
        self.person.add_hobby(hobby)
    def add_person_experience(self,job_title:str,company_name:str=None,job_description:str=None,start_date:str=None,end_date:str=None):
        self.person.add_experience(job_title,company_name,job_description,start_date,end_date)
    def add_person_education_background(self,degree:str,school_name:str,field_of_study:str,start_date:str=None,end_date:str=None):
        self.person.add_education_background(degree,school_name,field_of_study,start_date,end_date)
    def set_target_job(self,jobtitle:str,jobdescription:str,companyname:str,companyadress:str,hr):
        self.target_job=jobinfo(jobtitle,jobdescription,companyname,companyadress,hr)
    def generate_prompt(self):
        PromptTemplate=f"Write a cover Letter for the job application with {self.language} language and with {self.style} style \n"
        PromptTemplate += f"to the following job:\n \n Job Title: {self.target_job.jobtitle}\n Company Name: {self.target_job.companyname}\n Job Description: {self.target_job.jobdescription}\n\n"
        PromptTemplate += f"Personal Information:\n {self.person.to_dict()}"
        return PromptTemplate



