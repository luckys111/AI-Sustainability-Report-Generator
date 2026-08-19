from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(report_text):

    output_file = (
        "Generated_Sustainability_Report.pdf"
    )

    document = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Sustainability Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    paragraphs = report_text.split("\n")

    for paragraph in paragraphs:

        if paragraph.strip():

            content.append(
                Paragraph(
                    paragraph,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 8)
            )

    document.build(
        content
    )

    return output_file