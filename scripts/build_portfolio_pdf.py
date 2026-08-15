from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "Omar-BinAlshaikh-Portfolio.pdf"
W, H = letter
NAVY, INK, GOLD = HexColor("#101A2B"), HexColor("#293548"), HexColor("#B68A20")
PAPER, LINE, MUTED, SAGE = HexColor("#FBFAF8"), HexColor("#DED9CF"), HexColor("#657083"), HexColor("#2D5F4C")

font_dir = Path("/System/Library/Fonts/Supplemental")
serif = font_dir / "Georgia.ttf"
serif_bold = font_dir / "Georgia Bold.ttf"
sans = font_dir / "Arial.ttf"
sans_bold = font_dir / "Arial Bold.ttf"
if all(p.exists() for p in (serif, serif_bold, sans, sans_bold)):
    pdfmetrics.registerFont(TTFont("PortfolioSerif", str(serif)))
    pdfmetrics.registerFont(TTFont("PortfolioSerifBold", str(serif_bold)))
    pdfmetrics.registerFont(TTFont("PortfolioSans", str(sans)))
    pdfmetrics.registerFont(TTFont("PortfolioSansBold", str(sans_bold)))
else:
    pdfmetrics.registerFont(TTFont("PortfolioSerif", str(serif)))

SERIF, SERIF_B, SANS, SANS_B = "PortfolioSerif", "PortfolioSerifBold", "PortfolioSans", "PortfolioSansBold"


def para(c, text, x, y, width, size=10, leading=14, color=INK, font=SANS, align=0):
    style = ParagraphStyle("p", fontName=font, fontSize=size, leading=leading, textColor=color, alignment=align)
    p = Paragraph(text, style)
    _, height = p.wrap(width, H)
    p.drawOn(c, x, y - height)
    return y - height


def label(c, text, x, y, color=GOLD):
    c.setFillColor(color); c.setFont(SANS_B, 7.5); c.drawString(x, y, text.upper())


def footer(c, page):
    c.setStrokeColor(LINE); c.line(42, 35, W - 42, 35)
    c.setFillColor(MUTED); c.setFont(SANS, 7.5)
    c.drawString(42, 21, "OMAR BINALSHAIKH  /  PRODUCT - AI/ML - DATA - FINTECH")
    c.drawRightString(W - 42, 21, f"{page:02d}")


def page_bg(c):
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)


def metric(c, x, y, number, text, width=116):
    c.setFillColor(GOLD); c.setFont(SERIF_B, 22); c.drawString(x, y, number)
    para(c, text.upper(), x, y - 9, width, 6.8, 9, MUTED, SANS_B)


def card(c, x, y, w, h, number, title, result, body, accent=GOLD):
    c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(LINE); c.roundRect(x, y - h, w, h, 10, fill=1, stroke=1)
    c.setFillColor(accent); c.rect(x, y - 3, w, 3, fill=1, stroke=0)
    label(c, number, x + 17, y - 22, accent)
    c.setFillColor(NAVY); c.setFont(SERIF_B, 15); c.drawString(x + 17, y - 43, title)
    c.setFillColor(accent); c.setFont(SANS_B, 8); c.drawString(x + 17, y - 62, result)
    para(c, body, x + 17, y - 75, w - 34, 8.2, 11.5, MUTED)


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=letter, pageCompression=1)
    c.setTitle("Omar BinAlshaikh - Product Leadership Portfolio")
    c.setAuthor("Omar BinAlshaikh")

    # Cover
    c.setFillColor(NAVY); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(HexColor("#1B2A42")); c.circle(W + 10, H - 80, 220, fill=1, stroke=0)
    c.setStrokeColor(GOLD); c.setLineWidth(1); c.circle(84, H - 82, 27, fill=0, stroke=1); c.circle(84, H - 82, 22, fill=0, stroke=1)
    c.setFillColor(HexColor("#FFFFFF")); c.setFont(SERIF_B, 18); c.drawCentredString(79, H - 89, "O")
    c.setFillColor(HexColor("#F2D274")); c.drawCentredString(90, H - 89, "B")
    c.setFillColor(HexColor("#F2D274")); c.setFont(SANS_B, 8); c.drawString(42, H - 150, "PRINCIPAL PRODUCT LEADER  /  AI - DATA - FINTECH")
    para(c, "I turn operational<br/>complexity into<br/><font color='#F2D274'>intelligent products.</font>", 42, H - 188, 505, 35, 39, HexColor("#FFFFFF"), SERIF_B)
    para(c, "12+ years building AI and data products inside regulated financial workflows - where trust is earned in the details and every launch must create a measurable business outcome.", 42, 325, 345, 11, 17, HexColor("#C4CDDA"))
    c.setStrokeColor(HexColor("#34435A")); c.line(42, 218, W - 42, 218)
    metric(c, 42, 185, "12+", "Years in product")
    metric(c, 177, 185, "$3.3M+", "Annual overhead removed")
    metric(c, 337, 185, "100K+", "Transactions / month")
    metric(c, 485, 185, "15 -> 5", "Days to close")
    c.setFillColor(HexColor("#FFFFFF")); c.setFont(SERIF_B, 13); c.drawString(42, 68, "Omar BinAlshaikh")
    c.setFillColor(HexColor("#AEB9C8")); c.setFont(SANS, 8); c.drawRightString(W - 42, 68, "oabinalshaikh@gmail.com  /  linkedin.com/in/omarbinalshaikh")
    c.showPage()

    # Work
    page_bg(c); label(c, "Selected product work", 42, H - 55)
    para(c, "The ledger, not the resume.", 42, H - 72, 500, 27, 31, NAVY, SERIF_B)
    para(c, "Products measured in cycle time, operating cost, decision quality, and scalable volume.", 42, H - 114, 430, 10, 14, MUTED)
    card(c, 42, H - 166, 250, 205, "CASE 01", "Loan Origination Reform", "15 DAYS -> 5 DAYS", "Redesigned the workflow end-to-end with AI-enhanced intake, automated document and income validation, and rules-based underwriting automation.")
    card(c, 320, H - 166, 250, 205, "CASE 04", "Data Validation Platform", "B2B  /  AI-ML", "Owned a platform combining document classification, extraction, deterministic validation, human review, and partner-facing APIs.", SAGE)
    card(c, 42, H - 400, 250, 145, "CASE 02", "Audit Automation", "$3M ANNUAL OVERHEAD REMOVED", "Replaced manual compliance review with an AI-driven automation layer that improved consistency and traceability.")
    card(c, 320, H - 400, 250, 145, "CASE 03", "Recording Automation", "$300K ANNUAL SAVINGS", "Built an API-based workflow that eliminated manual data entry and reconciliation at operational scale.", HexColor("#8B1E3F"))
    card(c, 42, H - 574, 250, 112, "CASE 05", "B2B Integrations", "PARTNER-READY", "Aligned API contracts, data schemas, SLAs, and partner enablement for reliable platform integrations.", SAGE)
    card(c, 320, H - 574, 250, 112, "CASE 06", "Cloud Migration", "ON-PREM -> AWS", "Led migration of core data infrastructure to improve scalability and reduce operational overhead.")
    footer(c, 2); c.showPage()

    # Approach and expertise
    page_bg(c); label(c, "Operating approach", 42, H - 55)
    para(c, "Clarity before velocity.", 42, H - 72, 500, 28, 32, NAVY, SERIF_B)
    steps = [
        ("01", "Start with the problem", "Keep the solution space open until the underlying business problem is understood."),
        ("02", "Make the workflow visible", "Map friction, decisions, failure points, and the size of the opportunity before writing code."),
        ("03", "Use AI where it creates leverage", "Apply models where they remove meaningful effort, improve decisions, or unlock a previously impractical capability."),
        ("04", "Keep humans where judgment matters", "Design explicit review paths for regulated and high-risk decisions instead of treating AI as a black box."),
        ("05", "Measure outcomes", "Define success as time saved, cost removed, quality improved, revenue created, or risk reduced."),
    ]
    y = H - 145
    for no, title, body in steps:
        c.setStrokeColor(LINE); c.line(42, y, W - 42, y)
        c.setFillColor(GOLD); c.setFont(SERIF_B, 18); c.drawString(42, y - 28, no)
        c.setFillColor(NAVY); c.setFont(SERIF_B, 13); c.drawString(92, y - 24, title)
        para(c, body, 92, y - 31, 430, 8.4, 11.5, MUTED)
        y -= 85
    c.setFillColor(NAVY); c.roundRect(42, 105, W - 84, 98, 10, fill=1, stroke=0)
    label(c, "Core practice", 61, 178, HexColor("#F2D274"))
    para(c, "AI & ML Products  /  Data Products  /  0-to-1 Development  /  Technical Leadership  /  Process Automation  /  Product Strategy", 61, 160, W - 122, 11, 18, HexColor("#FFFFFF"), SERIF_B)
    footer(c, 3); c.showPage()

    # Credentials/contact
    page_bg(c); label(c, "Background", 42, H - 55)
    para(c, "Built for complex environments.", 42, H - 72, 500, 27, 31, NAVY, SERIF_B)
    c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(LINE); c.roundRect(42, 470, 250, 205, 10, fill=1, stroke=1)
    label(c, "Education", 60, 648)
    para(c, "Master's - Management", 60, 625, 210, 14, 18, NAVY, SERIF_B)
    para(c, "Harvard University<br/><br/><b>BBA - Finance</b><br/>Eastern Michigan University", 60, 597, 210, 9, 14, MUTED)
    c.setFillColor(HexColor("#FFFFFF")); c.roundRect(320, 470, 250, 205, 10, fill=1, stroke=1)
    label(c, "Certifications and training", 338, 648)
    para(c, "SAFe PM/PO<br/>Certified Scrum Product Owner<br/>Six Sigma Green Belt<br/>Advanced Negotiations - Harvard<br/>Strategic Management<br/>Organizational Behavior and Change", 338, 622, 210, 9, 18, INK)
    c.setFillColor(NAVY); c.roundRect(42, 142, W - 84, 260, 14, fill=1, stroke=0)
    label(c, "Connect", 66, 368, HexColor("#F2D274"))
    para(c, "Let's build AI products<br/>that have to be right.", 66, 338, 445, 25, 30, HexColor("#FFFFFF"), SERIF_B)
    para(c, "Open to product leadership opportunities across AI, data products, FinTech, and technical product management.", 66, 250, 385, 10, 15, HexColor("#B9C4D2"))
    c.setFillColor(HexColor("#F2D274")); c.roundRect(66, 174, 214, 35, 17, fill=1, stroke=0)
    c.setFillColor(NAVY); c.setFont(SANS_B, 8.5); c.drawCentredString(173, 187, "OABINALSHAIKH@GMAIL.COM")
    footer(c, 4); c.save()
    print(OUT)


if __name__ == "__main__":
    build()
