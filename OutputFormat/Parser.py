from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
class anschreiben_output(BaseModel):
    greeting:str = Field(description="The salutation of the letter. Example: 'Sehr geehrte Damen und Herren' or 'Sehr geehrter Herr Müller'.")
    cover_letter: str = Field(description="The generated cover letter without any personal information.dont mention the name,email or phone number of the person in the cover letter")
    closing_phrase:str = Field(description="The closing phrase of a letter. Example: 'Sincerely' or 'Best regards'.")

class AnschreibenOutputParser(PydanticOutputParser):
    def __init__(self):
        super().__init__(pydantic_object=anschreiben_output)

    def parser_result(self,llmresult:str):
        llmresult.replace("\n\n", "</p><p>").replace("\n", "<br>")
        return llmresult