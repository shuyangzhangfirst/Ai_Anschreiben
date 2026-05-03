from Prompt.Template import PromptTemplate
from LLM.Gemini import LLM
from OutputFormat.Parser import AnschreibenOutputParser 



pa=PromptTemplate(language="Germany",style="formal")
pa.load_person_profile("my_profile.json")
pa.set_target_job(jobtitle="Software Engineer",jobdescription="We are looking for a skilled software engineer to join our team. The ideal candidate should have experience in Python and JavaScript, and be familiar with cloud technologies.",companyname="Tech Company")
LLM=LLM("your_api_key_here")
anschreibenparser=AnschreibenOutputParser()
prompt=pa.generate_prompt()

format=anschreibenparser.get_format_instructions()
prompt_with_format=prompt + "\n\n" + format
response=LLM.llm.invoke(prompt_with_format)
print("Raw LLM Response:", response.content[0]['text']  )







