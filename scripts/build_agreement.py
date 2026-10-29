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
    "grading (S0-S4). Access is granted only after the maintainer has reviewed this "
    "completed and signed agreement. Applicants agree to the following conditions."
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
    "Complete the form, print and sign by hand, then email a legible scan "
    "of this page from your institutional address to " + EMAIL + ". Subject: '" +
    SUBJECT + "'. If you have no institutional address, contact the maintainer first. "
    "The password is sent after approval. Do not post signed forms publicly."
)
ROLES = (
    "Student applicants must obtain their supervisor's or principal investigator's "
    "signature. Other applicants may act as the responsible researcher themselves; "
    "a separate supervisor signature is not required."
)
DECLARATION = (
    "I have read and accept the conditions above. The information provided is "
    "accurate. I will use the data only for the stated non-commercial research "
    "and keep the data and password restricted to the approved project."
)
SOURCES = [
    ("SUSTech1K release agreement", "https://lidargait.github.io/static/resources/SUSTech1KAgreement.pdf"),
    ("EPHOIE access procedure", "https://github.com/HCIILAB/EPHOIE"),
]

WIDTH, HEIGHT = A4
LEFT = 38
RIGHT = WIDTH - LEFT
CONTENT = RIGHT - LEFT
INK = colors.black
RULE = colors.black
BODY = ParagraphStyle("body", fontName="Times-Roman", fontSize=9.5,
                      leading=11.5, textColor=INK, alignment=TA_LEFT)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=8.5, leading=10.2)
LABEL = ParagraphStyle("label", parent=BODY, fontName="Times-Bold", fontSize=8.6, leading=10)


def paragraph(pdf, text, x, top, width=CONTENT, style=BODY):
    block = Paragraph(text, style)
    _, height = block.wrap(width, HEIGHT)
    block.drawOn(pdf, x, top - height)
    return top - height


def section(pdf, title, top):
    pdf.setFillColor(INK)
    pdf.setFont("Times-Bold", 10)
    pdf.drawString(LEFT, top - 10, title)
    return top - 16


def page_header(pdf):
    pdf.setFillColor(INK)
    pdf.setFont("Times-Bold", 14)
    pdf.drawCentredString(WIDTH / 2, HEIGHT - 35, "TibSenCorpus Dataset Release Agreement")
    pdf.setFont("Times-Roman", 9)
    pdf.drawCentredString(WIDTH / 2, HEIGHT - 49, "Non-commercial Research Use")
    pdf.setStrokeColor(INK)
    pdf.setLineWidth(0.6)
    pdf.line(LEFT, HEIGHT - 57, RIGHT, HEIGHT - 57)


def footer(pdf):
    pdf.setStrokeColor(RULE)
    pdf.setLineWidth(0.5)
    pdf.line(LEFT, 28, RIGHT, 28)
    pdf.setFillColor(INK)
    pdf.setFont("Times-Roman", 7.5)
    pdf.drawString(LEFT, 17, "Version " + POLICY_VERSION + " | " + POLICY_DATE)
    pdf.drawRightString(RIGHT, 17, "1 / 1")


def field(pdf, name, x, y, width, height=18, multiline=False, border=True):
    pdf.acroForm.textfield(
        name=name, tooltip=name.replace("_", " ").title(), value="",
        x=x, y=y, width=width, height=height,
        fontName="Helvetica", fontSize=8.5, textColor=INK,
        fillColor=colors.white, borderColor=RULE, borderWidth=0.5 if border else 0,
        forceBorder=border, fieldFlags="multiline" if multiline else "",
        maxlen=1600 if multiline else 240,
    )


def make_pdf(path):
    pdf = canvas.Canvas(str(path), pagesize=A4, pageCompression=1, invariant=1)
    pdf.setTitle("TibSenCorpus Dataset Release and Non-commercial Research Agreement")
    pdf.setAuthor("TibSenCorpus")
    pdf.setSubject("Blank research access agreement; handwritten signatures required")
    page_header(pdf)
    y = paragraph(pdf, INTRO, LEFT, HEIGHT - 69) - 6
    y = section(pdf, "Conditions of use", y)
    for index, (title, body) in enumerate(TERMS, 1):
        y = paragraph(pdf, "<b>" + str(index) + ". " + title + ".</b> " + body, LEFT, y) - 4
    y = section(pdf, "Applicant information - type before printing", y + 1)
    y = paragraph(pdf, ROLES, LEFT, y, style=SMALL) - 6
    label_width = 91
    column_width = (CONTENT - label_width) / 2
    first = LEFT + label_width
    second = first + column_width
    table_top = y
    header_height = 23
    row_height = 21
    paragraph(pdf, "Information", LEFT + 4, table_top - 6, label_width - 8, LABEL)
    paragraph(pdf, "Applicant / point of contact", first + 4, table_top - 6, column_width - 8, LABEL)
    paragraph(pdf, "Responsible researcher / supervisor", second + 4, table_top - 6, column_width - 8, LABEL)
    table_bottom = table_top - header_height - 6 * row_height
    y = table_top - header_height
    rows = [("Full name", "name"), ("Institution", "institution"),
            ("Department / lab", "department"), ("Position / role", "position"),
            ("Institutional email", "email"), ("Academic webpage", "webpage")]
    for label, key in rows:
        paragraph(pdf, label, LEFT + 4, y - 6, label_width - 8, SMALL)
        field(pdf, "applicant_" + key, first + 3, y - row_height + 2,
              column_width - 6, row_height - 4, border=False)
        field(pdf, "responsible_" + key, second + 3, y - row_height + 2,
              column_width - 6, row_height - 4, border=False)
        y -= row_height
    pdf.setStrokeColor(INK)
    pdf.setLineWidth(0.5)
    pdf.rect(LEFT, table_bottom, CONTENT, table_top - table_bottom, fill=0)
    for x in (first, second):
        pdf.line(x, table_bottom, x, table_top)
    for index in range(6):
        line_y = table_top - header_height - index * row_height
        pdf.line(LEFT, line_y, RIGHT, line_y)
    y = table_bottom - 9
    paragraph(pdf, "Project title", LEFT, y, label_width - 4, LABEL)
    field(pdf, "project_title", first, y - 16, CONTENT - label_width, 20)
    y -= 26
    paragraph(pdf, "Research purpose and planned use", LEFT, y, style=LABEL)
    field(pdf, "research_purpose", LEFT, y - 45, CONTENT, 32, multiline=True)
    y -= 53
    y = paragraph(pdf, DECLARATION, LEFT, y, style=SMALL) - 7
    signature_top = y
    gap = 24
    half = (CONTENT - gap) / 2
    for x, title in [(LEFT, "Applicant signature (required)"),
                     (LEFT + half + gap, "Supervisor / PI signature (for students)")]:
        paragraph(pdf, title, x, signature_top, half, LABEL)
        pdf.setStrokeColor(INK)
        pdf.setLineWidth(0.7)
        pdf.line(x, signature_top - 35, x + half, signature_top - 35)
        pdf.setFont("Times-Roman", 8.5)
        pdf.drawString(x, signature_top - 47, "Date (YYYY-MM-DD): ____________________")
    y = signature_top - 58
    y = paragraph(pdf, SUBMISSION, LEFT, y, style=SMALL) - 5
    y = paragraph(pdf, "Repository: " + REPOSITORY, LEFT, y, style=SMALL)
    if y < 37:
        raise ValueError("Single-page layout does not leave enough room for the footer.")
    footer(pdf)
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
