"""Build the blank agreement: Python 3.8+ and reportlab are required."""

import argparse
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


POLICY_VERSION = "1.1"
POLICY_DATE = "29 October 2026"
EMAIL = "cvlina@mail.nwpu.edu.cn"
REPOSITORY = "https://github.com/cvNXE/TibSenCorpus"
SUBJECT = "TibSenCorpus Data Access Request"
STEM = "TibSenCorpus_Dataset_Release_Agreement"
INTRO = (
    "TibSenCorpus is a Tibetan-Chinese parallel corpus for five-level sensitive content "
    "grading (S0-S4). This agreement records the applicant's research purpose and "
    "commitment to the conditions below. Access to the unencrypted data is granted "
    "only after the maintainer has reviewed the completed and signed application."
)
TERMS = [
    ("Non-commercial research", "Use the dataset only for the non-commercial research "
     "described in this application. Do not use it in commercial products or services, "
     "or sell, resell, or otherwise commercially exploit the data."),
    ("No redistribution", "Do not publish, re-upload, or pass the unencrypted dataset, "
     "subsets, record-level copies, or extraction password to third parties. Keep "
     "access within the approved research project. Other research groups must "
     "apply independently; changes to the approved scope must be agreed with the maintainer."),
    ("Security and sensitive content", "Store and process the data in a protected "
     "research environment. Do not upload plaintext data or the password to public "
     "repositories or services that expose them. Do not attempt to identify individuals "
     "or publish sensitive source passages or identifying information."),
    ("Research processing and reporting", "Preprocessing, tokenization, model training, "
     "evaluation, and internal research copies are permitted for the approved "
     "non-commercial project. Papers, code, aggregate statistics, and visualizations "
     "may be shared only without exposing or enabling reconstruction of restricted records."),
    ("Attribution and source rights", "Acknowledge TibSenCorpus and link to its repository "
     "in research outputs that use the data. Rights in third-party source material "
     "remain with the respective rights holders; access does not transfer those "
     "rights or authorize uses beyond these research conditions."),
    ("Responsible use", "Treat sensitivity levels as context-dependent research "
     "annotations, not legal determinations. Do not use predictions as the sole "
     "basis for consequential decisions about people; high-risk uses require "
     "human review and compliance with applicable data-protection requirements."),
]
SUBMISSION = (
    "Type the information on page 2, print both pages, sign by hand, and scan the "
    "complete agreement into one legible PDF. Send it from your institutional email "
    "address to " + EMAIL + " with the subject '" + SUBJECT + "'. If you do not "
    "have an institutional address, contact the maintainer before submitting. The "
    "password will be sent by email after approval. Do not submit signed forms "
    "through public GitHub issues, pull requests, or commits."
)
ROLES = (
    "Student applicants must obtain their supervisor's or principal investigator's "
    "signature. Other applicants may act as the responsible researcher themselves "
    "and do not need a separate supervisor signature. Provide a contact email and "
    "institutional affiliation; do not include identity-document numbers."
)
DECLARATION = (
    "I have read both pages and agree to the conditions of use. The information "
    "provided is accurate, and the dataset will be used only for the stated "
    "non-commercial research. I will keep the data and password restricted as "
    "described above. A signed application is subject to review and is not itself approval."
)
SOURCES = [
    ("SUSTech1K release agreement", "https://lidargait.github.io/static/resources/SUSTech1KAgreement.pdf"),
    ("EPHOIE access procedure", "https://github.com/HCIILAB/EPHOIE"),
]

WIDTH, HEIGHT = A4
LEFT = 43
RIGHT = WIDTH - LEFT
CONTENT = RIGHT - LEFT
INK = colors.HexColor("#17272C")
ACCENT = colors.HexColor("#17675E")
RULE = colors.HexColor("#B9C5C6")
BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=10,
                      leading=14, textColor=INK, alignment=TA_LEFT)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=8.6, leading=11.5)
LABEL = ParagraphStyle("label", parent=BODY, fontName="Helvetica-Bold", fontSize=9, leading=12)


def paragraph(pdf, text, x, top, width=CONTENT, style=BODY):
    block = Paragraph(text, style)
    _, height = block.wrap(width, HEIGHT)
    block.drawOn(pdf, x, top - height)
    return top - height


def section(pdf, title, top):
    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 10.5)
    pdf.drawString(LEFT, top - 11, title)
    return top - 23


def page_header(pdf, subtitle):
    pdf.setFillColor(ACCENT)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(LEFT, HEIGHT - 45, "TibSenCorpus")
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(LEFT, HEIGHT - 65, subtitle)
    pdf.setFont("Helvetica", 8.5)
    pdf.drawString(LEFT, HEIGHT - 81, "Non-commercial research access")
    pdf.drawRightString(RIGHT, HEIGHT - 81, "Version " + POLICY_VERSION + " | " + POLICY_DATE)
    pdf.setStrokeColor(ACCENT)
    pdf.setLineWidth(1)
    pdf.line(LEFT, HEIGHT - 91, RIGHT, HEIGHT - 91)


def footer(pdf, number):
    pdf.setStrokeColor(RULE)
    pdf.setLineWidth(0.5)
    pdf.line(LEFT, 38, RIGHT, 38)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 8)
    pdf.drawString(LEFT, 25, "TibSenCorpus | Agreement v" + POLICY_VERSION)
    pdf.drawRightString(RIGHT, 25, str(number) + " / 2")


def field(pdf, name, x, y, width, height=22, multiline=False):
    pdf.acroForm.textfield(
        name=name, tooltip=name.replace("_", " ").title(), value="",
        x=x, y=y, width=width, height=height,
        fontName="Helvetica", fontSize=9.5, textColor=INK,
        fillColor=colors.white, borderColor=RULE, borderWidth=0.6,
        forceBorder=True, fieldFlags="multiline" if multiline else "",
        maxlen=1600 if multiline else 240,
    )


def make_pdf(path):
    pdf = canvas.Canvas(str(path), pagesize=A4, pageCompression=1, invariant=1)
    pdf.setTitle("TibSenCorpus Dataset Release and Non-commercial Research Agreement")
    pdf.setAuthor("TibSenCorpus")
    pdf.setSubject("Blank research access agreement; handwritten signatures required")
    page_header(pdf, "Dataset Release and Research Use Agreement")
    y = section(pdf, "Purpose and release", HEIGHT - 110)
    y = paragraph(pdf, INTRO, LEFT, y) - 13
    y = section(pdf, "Conditions of use", y)
    for index, (title, body) in enumerate(TERMS, 1):
        y = paragraph(pdf, "<b>" + str(index) + ". " + title + ".</b> " + body, LEFT, y) - 10
    y = section(pdf, "How to submit", y)
    y = paragraph(pdf, SUBMISSION, LEFT, y) - 13
    y = paragraph(pdf, "<b>Repository:</b> " + REPOSITORY, LEFT, y, style=SMALL) - 8
    y = paragraph(pdf, "Workflow references: public SUSTech1K and EPHOIE access procedures. "
                  "The wording is adapted for Tibetan-Chinese text research; no affiliation "
                  "with either project is implied.", LEFT, y, style=SMALL)
    if y < 53:
        raise ValueError("Agreement terms exceed the first page.")
    footer(pdf, 1)
    pdf.showPage()

    page_header(pdf, "Applicant Information and Handwritten Signatures")
    y = paragraph(pdf, ROLES, LEFT, HEIGHT - 111, style=SMALL) - 15
    y = section(pdf, "Researcher information - type before printing", y)
    label_width = 98
    column_width = (CONTENT - label_width) / 2
    first = LEFT + label_width
    second = first + column_width
    paragraph(pdf, "Applicant / point of contact", first + 5, y, column_width - 10, LABEL)
    paragraph(pdf, "Responsible researcher / supervisor", second + 5, y, column_width - 10, LABEL)
    y -= 32
    rows = [("Full name", "name"), ("Institution", "institution"),
            ("Department / lab", "department"), ("Position / role", "position"),
            ("Institutional email", "email"), ("Academic webpage", "webpage")]
    for label, key in rows:
        paragraph(pdf, label, LEFT, y + 18, label_width - 7, SMALL)
        field(pdf, "applicant_" + key, first + 4, y, column_width - 8)
        field(pdf, "responsible_" + key, second + 4, y, column_width - 8)
        y -= 29
    y -= 4
    y = section(pdf, "Proposed research", y + 10)
    paragraph(pdf, "Project title", LEFT, y, style=LABEL)
    field(pdf, "project_title", LEFT, y - 37, CONTENT, 22)
    y -= 51
    paragraph(pdf, "Research purpose and planned use of TibSenCorpus", LEFT, y, style=LABEL)
    field(pdf, "research_purpose", LEFT, y - 81, CONTENT, 64, multiline=True)
    y -= 96
    y = paragraph(pdf, DECLARATION, LEFT, y, style=SMALL) - 12
    if y < 165:
        raise ValueError("Insufficient room for handwritten signatures.")
    signature_top = min(y - 5, 176)
    gap = 24
    half = (CONTENT - gap) / 2
    for x, title in [(LEFT, "Applicant signature (required)"),
                     (LEFT + half + gap, "Supervisor / PI signature (for students)")]:
        paragraph(pdf, title, x, signature_top, half, LABEL)
        pdf.setStrokeColor(INK)
        pdf.setLineWidth(0.7)
        pdf.line(x, signature_top - 57, x + half, signature_top - 57)
        pdf.setFont("Helvetica", 8.5)
        pdf.drawString(x, signature_top - 72, "Date (YYYY-MM-DD): ____________________")
    paragraph(pdf, "Sign by hand. Email a legible scan of both pages to " + EMAIL + ". "
              "Do not post completed forms publicly.", LEFT, 70, style=SMALL)
    footer(pdf, 2)
    pdf.save()


def make_markdown(path):
    lines = ["# TibSenCorpus Dataset Release and Non-commercial Research Agreement", "",
             "Policy version: " + POLICY_VERSION + " | " + POLICY_DATE, "",
             "## Purpose and release", "", INTRO, "", "## Conditions of use", ""]
    lines.extend(str(i) + ". **" + title + ".** " + body for i, (title, body) in enumerate(TERMS, 1))
    lines += ["", "## Submission", "", SUBMISSION, "", "## Applicant information", "", ROLES, "",
              "| Information | Applicant / point of contact | Responsible researcher / supervisor |",
              "| --- | --- | --- |", "| Full name | | |", "| Institution | | |",
              "| Department / lab | | |", "| Position / role | | |", "| Institutional email | | |",
              "| Academic webpage | | |", "", "Project title: ____________________", "",
              "Research purpose and planned use: ____________________", "", "## Declaration and signatures",
              "", DECLARATION, "", "Applicant handwritten signature: ____________________", "",
              "Date (YYYY-MM-DD): ____________________", "",
              "Supervisor / PI handwritten signature (required for students): ____________________", "",
              "Date (YYYY-MM-DD): ____________________", "", "## Workflow references", ""]
    lines.extend("- [" + title + "](" + url + ")" for title, url in SOURCES)
    lines += ["", "These are workflow references, not licences applied to TibSenCorpus. "
              "The supplied signed example is not part of the public release.", "",
              "Repository: " + REPOSITORY, ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "agreements")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    make_pdf(args.output_dir / (STEM + ".pdf"))
    make_markdown(args.output_dir / (STEM + ".md"))
    print("Created blank agreement PDF and Markdown in " + str(args.output_dir))


if __name__ == "__main__":
    main()
