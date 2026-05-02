

from datetime import datetime


class education:
    def __init__(self,degree:str,institution:str,startDate:datetime,endDate:datetime):
        self.degree = degree
        self.institution = institution
        self.startDate = startDate
        self.endDate = endDate
    
    def to_dict(self):
        if self.startDate is not None and self.endDate is not None:
            return {
                "degree": self.degree,
                "institution": self.institution,
                "startDate": self.startDate.strftime("%m-%Y"),
                "endDate": self.endDate.strftime("%m-%Y")
            }
        else:
            return {
                "degree": self.degree,
                "institution": self.institution,
                
            }

class educations:
    def __init__(self):
        self.educations:list[dict] = []
    
    def add_education(self,new_education:education):
        self.educations.append(new_education.to_dict())
    
    def get_educations(self):
        return self.educations