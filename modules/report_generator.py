from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


class ReportGenerator:

    @staticmethod
    def generate(result):

        filename = "reports/security_audit_report.pdf"

        document = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Password Security Audit Report",
                styles["Title"]
            )
        )

        content.append(
            Paragraph(
                f"Generated: {datetime.now()}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        content.append(
            Paragraph(
                "Executive Summary",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Overall Risk Level: {result['risk']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                "Password Analysis",
                styles["Heading2"]
            )
        )

        analysis_items = [

            ("Password Length",
             result["password_length"]),

            ("Strength Score",
             f"{result['score']}/100"),

            ("Strength Level",
             result["strength"]),

            ("Entropy",
             f"{result['entropy']} bits"),

            ("Dictionary Match",
             str(result["dictionary_match"])),

            ("Risk Severity",
             result["risk"])

        ]

        for key, value in analysis_items:

            content.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                "Security Recommendations",
                styles["Heading2"]
            )
        )

        if result["recommendations"]:

            for recommendation in result["recommendations"]:

                content.append(
                    Paragraph(
                        f"• {recommendation}",
                        styles["BodyText"]
                    )
                )

        else:

            content.append(
                Paragraph(
                    "Password follows recommended security practices.",
                    styles["BodyText"]
                )
            )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                "Risk Interpretation",
                styles["Heading2"]
            )
        )

        risk = result["risk"]

        if risk == "CRITICAL":

            text = (
                "Password appears in a common password set "
                "and can be compromised very quickly."
            )

        elif risk == "HIGH":

            text = (
                "Password exhibits weak characteristics "
                "and should be changed immediately."
            )

        elif risk == "MEDIUM":

            text = (
                "Password provides moderate protection "
                "but should be strengthened."
            )

        else:

            text = (
                "Password demonstrates good security "
                "characteristics."
            )

        content.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

        document.build(content)

        return filename
