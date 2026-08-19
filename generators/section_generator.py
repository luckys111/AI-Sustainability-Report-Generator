from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="openai.o4-mini",
    temperature=0,
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("URL"),
    default_headers={
        "x-api-key": os.getenv("API_KEY")
    }
)

section_prompt = PromptTemplate(
    input_variables=[
        "section_name",
        "style_examples",
        "kpi_data"
    ],

    template="""
You are an ESG Sustainability Report Writer.

Style Reference:

{style_examples}

Current Section:

{section_name}

Current KPI Data:

{kpi_data}

Requirements:

1. Follow the same writing style.
2. Follow the same tone.
3. Use corporate sustainability language.
4. Use KPI values while explaining.
5. Generate a detailed section.

Return only the section.
"""
)


def generate_section(
        section_name,
        style_examples,
        kpi_data):

    prompt = section_prompt.format(
        section_name=section_name,
        style_examples=style_examples,
        kpi_data=kpi_data
    )

    response = llm.invoke(prompt)

    return response.content