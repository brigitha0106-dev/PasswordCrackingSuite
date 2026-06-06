from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class ReportGenerator:

    @staticmethod
    def generate(result):

        filename = (
            "reports/security_audit_report.pdf"
        )

        document = (
            SimpleDocTemplate(filename)
        )

        styles = (
            getSampleStyleSheet()
        )

        content = []

        content.append(

            Paragraph(
                "Password Security Audit Report",
                styles["Title"]
            )

        )

        content.append(
            Spacer(1, 20)
        )

        for key, value in result.items():

            content.append(

                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )

            )

            content.append(
                Spacer(1, 10)
            )

        document.build(content)

        return filename
