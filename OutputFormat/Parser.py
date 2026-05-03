from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
class anschreiben_output(BaseModel):
    cover_letter: str = Field(description="The generated cover letter without any personal information.dont mention the name,email or phone number of the person in the cover letter")

class AnschreibenOutputParser(PydanticOutputParser):
    def __init__(self):
        super().__init__(pydantic_object=anschreiben_output)
