from Prompt.Template import PromptTemplate
from LLM.Gemini import LLM
from OutputFormat.Parser import AnschreibenOutputParser 
from Anschreiben.Anschreiben import anschreiben
class Ai_Anschreiben_Generator:
    def __init__(self,api_key:str,template_path:str,output_path:str,):
        self.api_key=api_key
        self.template_path=template_path
        self.output_path=output_path
        self.prompt_template: PromptTemplate = PromptTemplate()
        self.llm=LLM(api_key)
        self.parser=AnschreibenOutputParser()
        
        
        
        
    
    def load_person_profile(self,json_data_path):
        self.prompt_template.load_person_profile(json_data_path)
    
    def set_target_job(self,jobtitle:str,jobdescription:str,companyname:str,companyadress=None,hr=None):
        self.prompt_template.set_target_job(jobtitle,jobdescription,companyname,companyadress,hr)
    
    def add_person_information(self,name:str=None,age:int=None,phone_number:str=None,email:str=None,address:str=None):
        self.prompt_template.add_person_information(name,age,phone_number,email,address)
    
    def add_person_skill(self,skill_name:str , skill_level:str):
        self.prompt_template.add_person_skill(skill_name,skill_level)
    
    def add_person_hobby(self,hobby):
        self.prompt_template.add_person_hobby(hobby)
    def add_person_experience(self,job_title:str,company_name:str=None,job_description:str=None,start_date:str=None,end_date:str=None):
        self.prompt_template.add_person_experience(job_title,company_name,job_description,start_date,end_date)
    
    def add_person_education_background(self,degree:str,school_name:str,field_of_study:str,start_date:str=None,end_date:str=None):
        self.prompt_template.add_person_education_background(degree,school_name,field_of_study,start_date,end_date)
    
    def generate_pdf(self):
        prompt=self.prompt_template.generate_prompt()
        format=self.parser.get_format_instructions()
        prompt_with_format=prompt + "\n\n" + format
        result=self.llm.llm.invoke(prompt_with_format).content[0]['text']
        result=self.parser.parse(result)
        
        an=anschreiben(result.cover_letter,result.greeting,result.closing_phrase,self.prompt_template.person.name,self.prompt_template.person.email,self.prompt_template.person.phone_number,self.prompt_template.person.address,self.prompt_template.target_job.companyname,self.prompt_template.target_job.hr,self.prompt_template.target_job.companyaddress)
        an.Generate_anschreiben_pdf(self.template_path,self.output_path)
        

        

""" pa=PromptTemplate(language="Germany",style="formal")
pa.load_person_profile("my_profile.json")
pa.set_target_job(jobtitle="Software Engineer",jobdescription="We are looking for a skilled software engineer to join our team. The ideal candidate should have experience in Python and JavaScript, and be familiar with cloud technologies.",companyname="Tech Company")
LLM=LLM("your_api_key_here")
anschreibenparser=AnschreibenOutputParser()
prompt=pa.generate_prompt()

format=anschreibenparser.get_format_instructions()
prompt_with_format=prompt + "\n\n" + format
response=LLM.llm.invoke(prompt_with_format)
response.content[0]['text']   """

ai=Ai_Anschreiben_Generator("AIzaSyCMj4EESwf-fj7hDbC5le3kQ8jyUgkezSY","Ai_Anschreiben/template.html","anschreiben.pdf")
ai.load_person_profile("Ai_Anschreiben/my_profile.json")
ai.set_target_job(jobtitle="Software Engineer",jobdescription="We are looking for a skilled software engineer to join our team. The ideal candidate should have experience in Python and JavaScript, and be familiar with cloud technologies.",companyname="Tech Company")
ai.generate_pdf()








