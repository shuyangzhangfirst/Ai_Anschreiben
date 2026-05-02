
class skill:
    def __init__(self,skill_type:str,skill_name:str,proficiency_level:str):
        self.skill_type =skill_type
        self.skill_name = skill_name
        self.proficiency_level = proficiency_level
    
    def to_dict(self):
        return {
            "skill_type": self.skill_type,
            "skill_name": self.skill_name,
            "proficiency_level": self.proficiency_level
        }
    

class skills:
    def __init__(self):
        self.skills:list[dict] = []
    
    def add_skill(self,new_skill:skill):
        self.skills.append(new_skill.to_dict())
    
    def get_skills(self):
        return self.skills

