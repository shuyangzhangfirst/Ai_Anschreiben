
class person:
    def __init__(self):
        self.name:str = None
        self.age:int = None
        self.phone_number:str = None
        self.email:str = None
        self.skills:list = None
        self.experiences:dict = None
        self.education_backgrounds:dict = None
        
        self.hobbies = None
    
    def load_profile_from_json(self, json_data_path):
        import json
        with open(json_data_path, 'r') as file :
            data = json.load(file)
            for key, value in data.items():
                setattr(self, key, value)
    
    def save_profile_to_json(self, json_data_path):
        import json
        with open(json_data_path, 'w') as file :
            json.dump(self.__dict__, file, indent=4)
    def set_personal_info(self,name:str, age:int, phone_number:str=None, email:str=None):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email
    def add_skill(self,skill_name:str , skill_level:str):
        if self.skills is None:
            self.skills=[]
        skill = {"skill_name": skill_name, "skill_level": skill_level}
        self.skills.append(skill)
    
    def add_hobby(self,hobby:str):
        if self.hobbies is None:
            self.hobbies=[]
        self.hobbies.append(hobby)   
    
    def add_experience(self,job_title:str,company_name:str=None,job_description:str=None,start_date:str=None,end_date:str=None):
        if self.experiences is None:
            self.experiences={}
        experience = {}
        if company_name is not None:
            experience["company_name"]=company_name
        if job_description is not None:
            experience["job_description"]=job_description
        if start_date is not None:
            experience["start_date"]=start_date
        if end_date is not None:
            experience["end_date"]=end_date
        self.experiences[job_title]=experience
        
    def add_education_background(self,degree:str,school_name:str,field_of_study:str,start_date:str=None,end_date:str=None):
        if self.education_backgrounds is None:
            self.education_backgrounds={}
        education_background = {}
        if start_date is not None:
            education_background["start_date"]=start_date
        if end_date is not None:
            education_background["end_date"]=end_date
        education_background["school_name"]=school_name
        education_background["field_of_study"]=field_of_study
        self.education_backgrounds[degree]=education_background
        
    def to_string(self):
        result=""
        for key,value in self.__dict__.items():
            if value is not None:
                result+=f"{key}: {value}\n"
        return result
    
    def to_dict(self):
        dict_representation = {}
        for key,value in self.__dict__.items():
            if value is not None:
                if key in ["name","age","phone_number","email"]:
                    dict_representation[key]=value
                elif key == "skills" and self.skills is not None:
                    dict_representation["skills"]={}
                    for skill in self.skills:
                        dict_representation["skills"][f"{skill['skill_name']}"]=skill['skill_level']
                elif key == "experiences" and self.experiences is not None:
                    dict_representation["experiences"]={}
                    for job_title, experience in self.experiences.items():
                        dict_representation["experiences"][f"{job_title}"]={}
                        for exp_key, exp_value in experience.items():
                            dict_representation["experiences"][f"{job_title}"][f"{exp_key}"]=exp_value
                elif key == "education_backgrounds" and self.education_backgrounds is not None:
                    dict_representation["education_backgrounds"]={}
                    for degree, education in self.education_backgrounds.items():
                        dict_representation["education_backgrounds"][f"{degree}"]={}
                        for edu_key, edu_value in education.items():
                            dict_representation["education_backgrounds"][f"{degree}"][f"{edu_key}"]=edu_value
                elif key == "hobbies" and self.hobbies is not None:
                    dict_representation["hobbies"]=[]
                    for hobby in self.hobbies:
                        dict_representation["hobbies"].append(hobby)
        return dict_representation
                
    
    def print_profile(self):
        result=""
        
        for key,value in self.__dict__.items():
            if key in ["name","age","phone_number","email"]:
                result+=f"{key}: {value}\n"
            elif key == "skills" and self.skills is not None:
                result+="Skills:\n"
                for skill in self.skills:
                    result+=f"- {skill['skill_name']} (Level: {skill['skill_level']})\n"
            elif key == "experiences" and self.experiences is not None:
                result+="Experiences:\n"
                for job_title, experience in self.experiences.items():
                    result+=f"- {job_title} at {experience.get('company_name', 'N/A')} ({experience.get('start_date', 'N/A')} - {experience.get('end_date', 'N/A')})\n"
                    if experience.get("job_description") is not None:
                        result+=f"  Description: {experience['job_description']}\n"  
            elif key == "education_backgrounds" and self.education_backgrounds is not None:
                result+="Education Backgrounds:\n"
                for degree, education in self.education_backgrounds.items():
                    result+=f"- {degree} in {education.get('field_of_study', 'N/A')} from {education.get('school_name', 'N/A')} ({education.get('start_date', 'N/A')} - {education.get('end_date', 'N/A')})\n"
            elif key == "hobbies" and self.hobbies is not None:
                result+="Hobbies:\n"
                for hobby in self.hobbies:
                    result+=f"- {hobby}\n"
        print(result)    





    
    
    
    