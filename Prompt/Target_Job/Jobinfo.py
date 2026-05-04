
class jobinfo:
    def __init__ (self,jobtitle,jobdescription,companyname,companyaddress,hr):
        self.jobtitle = jobtitle
        self.jobdescription = jobdescription
        self.companyname = companyname
        self.companyaddress=companyaddress
        self.hr=hr
    
    def to_dict(self):
        result={
            
        }
        for key,item in self.__dict__.items():
            if item == None:
                continue
            result[key]=item
        return result
    