from rag.style_retriever import (
    get_style_examples
)

from generators.section_generator import (
    generate_section
)

REPORT_SECTIONS = [

    "Executive Summary",

    "Company Overview",

    "Reporting Boundary & Methodology",

    "Stakeholder Engagement",

    "Environmental Performance",

    "Social Responsibility",

    "Governance",

    "Sustainability Achievements",

    "Risks And Mitigation",

    "Future Sustainability Roadmap",

    "Assurance Statement",

    "Conclusion"
]


def build_full_report(kpi_data):

    report = ""

    for section in REPORT_SECTIONS:

        style = get_style_examples(
            section,
            k=5
        )

        content = generate_section(
            section,
            style,
            kpi_data
        )

        report += (
            f"\n\n# {section}\n\n"
        )

        report += content

        report += "\n\n"

    return report