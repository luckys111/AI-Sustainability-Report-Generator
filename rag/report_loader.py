import os

from langchain_community.document_loaders import (
    Docx2txtLoader
)

REPORT_FOLDER = "previous_reports"


def load_reports():

    documents = []

    for file in os.listdir(REPORT_FOLDER):

        if file.endswith(".docx"):

            path = os.path.join(
                REPORT_FOLDER,
                file
            )

            loader = Docx2txtLoader(path)

            docs = loader.load()

            documents.extend(docs)

    return documents