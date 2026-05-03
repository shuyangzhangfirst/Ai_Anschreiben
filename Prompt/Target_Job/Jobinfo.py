
class jobinfo:
    def __init__ (self,jobtitle,jobdescription,companyname):
        self.jobtitle = jobtitle
        self.jobdescription = jobdescription
        self.companyname = companyname
    
    def to_dict(self):
        return {
            "jobtitle": self.jobtitle,
            "jobdescription": self.jobdescription,
            "companyname": self.companyname
        }
    