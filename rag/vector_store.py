from rag.report_loader import (
    load_reports
)


def create_style_library():

    documents = load_reports()

    style_library = []

    for doc in documents:

        chunks = doc.page_content.split("\n\n")

        for chunk in chunks:

            if len(chunk.strip()) > 100:

                style_library.append(
                    chunk.strip()
                )

    return style_library