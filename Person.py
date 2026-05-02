

from Skills import skill,skills
from Experience import experience,experiences
from Education import education,educations

class Person:
    def __init__(self,name:str,age:int,skills:skills=None,experience:experiences=None,education_backgrounds:educations=None,hobbies:list=[]):
        self.name = name
        self.age = age
        self.skills:dict = skills.get_skills() if skills is not None else []
        self.experiences:dict = experience.get_experiences() if experience is not None else []
        self.education_backgrounds:dict = education_backgrounds.get_educations() if education_backgrounds is not None else []
        
        self.hobbies = hobbies
    
    def to_string(self):
        return f"Name: {self.name}\nAge: {self.age}\nSkills: {self.skills}\nExperiences: {self.experiences}\nEducation Backgrounds: {self.education_backgrounds}\nHobbies: {self.hobbies}"

    

""" name="shuyang"
age=22
skills = skills()
skills.add_skill(skill("programming","python","proficient"))
experiences = experiences()
experiences.add_experience(experience("software engineer","google","developed software",startDate=None,endDate=None))
experiences.add_experience(experience("data analyst","facebook","analyzed data",startDate=None,endDate=None))
education_backgrounds = educations()
education_backgrounds.add_education(education("bachelor","MIT",startDate=None,endDate=None))
hobbies = ["reading","traveling"]
person = Person(name,age,skills,experiences,education_backgrounds,hobbies)
print(person.to_string()) """
    
    
    
    