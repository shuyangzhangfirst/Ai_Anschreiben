
import datetime
class experience:
    def __init__(self , job_title:str,company_name:str,description:str,startDate:datetime=None,endDate:datetime=None):
        self.job_title = job_title
        self.company_name = company_name
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
        pass
    
    def to_dict(self):
        if self.startDate is not None and self.endDate is not None:
            return {
                "job_title": self.job_title,
                "company_name": self.company_name,
                "description": self.description,
                "startDate": self.startDate.strftime("%m-%Y"),
                "endDate": self.endDate.strftime("%m-%Y")
            }
        else:
            return {
                "job_title": self.job_title,
                "company_name": self.company_name,
                "description": self.description
            }

class experiences:
    def __init__(self):
        self.experiences:list[dict] = []
    
    def add_experience(self,new_experience:experience):
        self.experiences.append(new_experience.to_dict())
    
    def get_experiences(self):
        return self.experiences