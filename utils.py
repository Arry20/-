from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from prompt_template import user_template_text,system_template_text
from Xiaohongshu import  Xiaohongshu
import os
def generate(theme,openai_api_key):
    prompt=ChatPromptTemplate.from_messages(
        [
            ("system",system_template_text),
            ("user",user_template_text)
        ]
    )
    model=ChatOpenAI(model="gpt-3.5-turbo",api_key=openai_api_key,openai_api_base = "https://api.aigc369.com/v1")
    output_parser=PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain=prompt|model|output_parser
    result=chain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),
        "theme":theme
    })
    return result
#print(generate("大模型",os.getenv("OPENAI_API_KEY")))

