from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "solution_packet.pdf"


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.line(0.72 * inch, 0.55 * inch, 7.78 * inch, 0.55 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(0.72 * inch, 0.34 * inch, "fa_banach_001 - literature resolution")
    canvas.drawRightString(7.78 * inch, 0.34 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build():
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=LETTER,
        leftMargin=0.78 * inch,
        rightMargin=0.78 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.72 * inch,
        title="Literature resolution: cyclic polynomials on the bidisk",
        author="fa_banach_001, lane 13",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="status", frames=[frame], onPage=footer)])

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    kicker = ParagraphStyle(
        "Kicker",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#2563EB"),
        alignment=TA_CENTER,
        spaceAfter=18,
    )
    heading = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=10,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.4,
        textColor=colors.HexColor("#1F2937"),
        spaceAfter=7,
    )
    small = ParagraphStyle(
        "SmallCustom",
        parent=body,
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#475569"),
    )
    table_header = ParagraphStyle(
        "TableHeader",
        parent=body,
        fontName="Helvetica-Bold",
        textColor=colors.white,
        spaceAfter=0,
    )

    story = [
        Paragraph("Literature resolution:<br/>cyclic polynomials on the bidisk", title),
        Paragraph("ARXIV:1310.4094  |  ANSWERED BY ARXIV:1408.3616", kicker),
    ]

    badge = Table(
        [[Paragraph("<b>STATUS</b><br/>Complete later-literature answer", body),
          Paragraph("<b>SCOPE</b><br/>Source Problem 5.2", body)]],
        colWidths=[3.35 * inch, 3.35 * inch],
    )
    badge.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#93C5FD")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFDBFE")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story += [badge, Spacer(1, 10)]

    story += [
        Paragraph("Source question", heading),
        Paragraph(
            "Problem 5.2 of arXiv:1310.4094 asks for a characterization, for every "
            "<i>alpha</i> at most 1, of cyclic polynomials in the product-weight "
            "Dirichlet-type space on the bidisk.",
            body,
        ),
        Paragraph("Exact later answer", heading),
        Paragraph(
            "ArXiv:1408.3616 explicitly names the source's Problem 5.2 and says: "
            "<i>In the present paper, we solve this problem and provide a complete "
            "characterization.</i> Its Main Theorem applies to an irreducible polynomial "
            "<i>f</i> with no zero in the open bidisk.",
            body,
        ),
    ]

    rows = [
        [Paragraph("Parameter", table_header), Paragraph("Classification", table_header)],
        [Paragraph("alpha <= 1/2", body), Paragraph("Every such irreducible polynomial is cyclic.", body)],
        [Paragraph("1/2 < alpha <= 1", body), Paragraph(
            "Cyclic exactly when the torus zero set is empty or finite, or the polynomial "
            "is a constant multiple of zeta - z1 or zeta - z2 for a unimodular zeta.", body)],
        [Paragraph("alpha > 1", body), Paragraph("Cyclic exactly when the torus zero set is empty.", body)],
    ]
    table = Table(rows, colWidths=[1.55 * inch, 5.15 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8FAFC")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [table]

    story += [
        Paragraph("How to use the theorem", heading),
        Paragraph(
            "A general polynomial is cyclic exactly when each irreducible factor is cyclic, "
            "because polynomials are multipliers. Any zero in the open bidisk rules out "
            "cyclicity before the boundary classification is applied.",
            body,
        ),
        Paragraph("Why the identification is exact", heading),
        Paragraph(
            "Both papers use the same coefficient norm: the squared norm is the sum over "
            "k,l >= 0 of (k+1) raised to alpha times (l+1) raised to alpha, times "
            "the squared modulus of the "
            "coefficient a(k,l). The 2014 theorem is therefore an answer in the identical "
            "space, not an analogy using a different Dirichlet scale.",
            body,
        ),
        Paragraph("Boundary of this packet", heading),
        Paragraph(
            "This resolves only the polynomial-classification problem. The preceding "
            "Brown-Shields question concerns arbitrary outer functions and is not claimed "
            "to be settled here.",
            body,
        ),
        Paragraph("References", heading),
        Paragraph(
            "[1] C. Beneteau, A. A. Condori, C. Liaw, D. Seco, and A. A. Sola, "
            "<i>Cyclicity in Dirichlet-type spaces and extremal polynomials II: functions "
            "on the bidisk</i>, arXiv:1310.4094.",
            small,
        ),
        Paragraph(
            "[2] C. Beneteau, G. Knese, L. Kosinski, C. Liaw, D. Seco, and A. A. Sola, "
            "<i>Cyclic polynomials in two variables</i>, arXiv:1408.3616, Main Theorem.",
            small,
        ),
    ]

    doc.build(story)


if __name__ == "__main__":
    build()
