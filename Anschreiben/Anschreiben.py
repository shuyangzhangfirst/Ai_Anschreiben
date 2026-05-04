
from datetime import datetime
from jinja2 import Template
import os
import webbrowser
from playwright.sync_api import sync_playwright


class anschreiben:
    def __init__(self,content,greeting="Sehr geehrte Damen und Herren",close_phrase="Mit freundlichen Grüßen",name=None,email=None,phone_number=None,address=None,company_name=None,contact_person=None,company_address=None):
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.address=address
        self.company_name=company_name
        self.contact_person=contact_person
        self.company_address=company_address
        self.content=content
        self.greeting=greeting
        self.close_phrase=close_phrase
    
    
    def Generate_anschreiben_json(self):
        person_info={}
        company_info={}
        
        content=self.content
        if self.name is not None:
            person_info["name"]=self.name
        if self.email is not None:
            person_info["email"]=self.email
        if self.phone_number is not None:
            person_info["phone_number"]=self.phone_number
        if self.address is not None:
            person_info["address"]=self.address
        if self.company_name is not None:
            company_info["company_name"]=self.company_name
        if self.contact_person is not None:
            company_info["contact_person"]=self.contact_person
        if self.company_address is not None:
            company_info["company_address"]=self.company_address
        date=datetime.now().strftime("%d-%m-%Y")
        anschreiben_json={
            "person_info":person_info,
            "company_info":company_info,
            "date":date,
            "content":content,
            "greeting":self.greeting,
            "close_phrase":self.close_phrase
        }
        
        
        
        return anschreiben_json
    def Generate_anschreiben_html(self,json_data,template_path):
        
        with open(template_path,"r",encoding="utf-8") as f:
            template=Template(f.read())
        html=template.render(**json_data)
        return html
    def Generate_anschreiben_pdf(self,template_path,output_path):
        html=self.Generate_anschreiben_html(self.Generate_anschreiben_json(),template_path)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.set_content(html)
            page.pdf(path=output_path)
    





