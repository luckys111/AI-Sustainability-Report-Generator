import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

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


def review_report(report):

    prompt = f"""
You are a Sustainability Report Reviewer.

Review the report below.

Tasks:

1. Remove duplicate content.
2. Improve consistency.
3. Verify sections are coherent.
4. Improve readability.
5. Improve professional tone.
6. Ensure KPI references remain accurate.
7. Ensure sustainability terminology is consistent.

Return a corrected version.

Report:

{report}
"""

    response = llm.invoke(
        prompt
    )

    return response.content