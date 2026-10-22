"""Build two resume pages and append the reference PDF's unchanged third page.

Requires reportlab and pypdf, only for authoring, not for the portfolio runtime.
Run: python scripts/build_resume.py --reference path/to/current-resume.pdf
"""

import argparse
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
BLUE = HexColor('#002fa7')
INK = HexColor('#202124')
MUTED = HexColor('#555965')
RULE = HexColor('#dedee2')
WIDTH, HEIGHT = A4
LEFT = 44
RIGHT = WIDTH - 44
TEXT_WIDTH = RIGHT - LEFT
FONT_DIR = Path('/System/Library/Fonts/Supplemental')


def build(reference, output, font_dir):
    reader = PdfReader(reference)
    if len(reader.pages) != 3:
        raise ValueError('Expected a three-page reference, with the letter on page three.')
    for name, filename in [('Resume', 'Arial.ttf'), ('Resume-Bold', 'Arial Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily('Resume', normal='Resume', bold='Resume-Bold',
                                  italic='Resume', boldItalic='Resume-Bold')
    style = ParagraphStyle('Body', fontName='Resume', fontSize=10, leading=13.6,
                           textColor=INK, alignment=TA_LEFT)
    style_bold = ParagraphStyle('Entry', parent=style, fontName='Resume-Bold', fontSize=10.6,
                                leading=14.2)
    style_small = ParagraphStyle('Small', parent=style, fontSize=9.1, leading=12.2,
                                 textColor=MUTED)
    buffer = BytesIO()
    cv = canvas.Canvas(buffer, pagesize=A4, pageCompression=1)
    cv.setTitle('Daniel Mohamad | Full-Stack Software and AI Application Developer')
    cv.setAuthor('Daniel Ridzwan Bin Mohamad')
    y = HEIGHT - 44

    def paragraph(text, current_style=style, gap=5, indent=0, max_width=None):
        nonlocal y
        p = Paragraph(text, current_style)
        width = max_width or TEXT_WIDTH - indent
        _, height = p.wrap(width, HEIGHT)
        if y - height < 49:
            raise ValueError(f'Resume page overflow at: {text[:80]}')
        p.drawOn(cv, LEFT + indent, y - height)
        y -= height + gap

    def bullet(text):
        nonlocal y
        cv.setFillColor(BLUE)
        cv.setFont('Resume', 10)
        cv.drawString(LEFT + 2, y - 10, '-')
        paragraph(text, indent=11, gap=3)

    def section(title):
        nonlocal y
        y -= 8
        cv.setFillColor(BLUE)
        cv.setFont('Resume-Bold', 10)
        cv.drawString(LEFT, y - 10, title.upper())
        y -= 17
        cv.setStrokeColor(RULE)
        cv.setLineWidth(0.65)
        cv.line(LEFT, y, RIGHT, y)
        y -= 9

    def footer(number):
        cv.setStrokeColor(RULE)
        cv.setLineWidth(0.65)
        cv.line(LEFT, 36, RIGHT, 36)
        cv.setFont('Resume', 8)
        cv.setFillColor(MUTED)
        cv.drawString(LEFT, 23, 'Daniel Mohamad | Software & AI Application Development')
        cv.drawRightString(RIGHT, 23, f'{number} / 3')

    # Reuse the existing portrait, rather than inventing or replacing a photo.
    if reader.pages[0].images:
        portrait_data = BytesIO()
        photo = Image.open(BytesIO(reader.pages[0].images[0].data)).convert('RGB')
        photo.thumbnail((320, 380))
        photo.save(portrait_data, format='JPEG', quality=92, optimize=True)
        portrait_data.seek(0)
        portrait = ImageReader(portrait_data)
        cv.drawImage(portrait, RIGHT - 64, HEIGHT - 120, width=64, height=76,
                     preserveAspectRatio=True, anchor='c', mask='auto')
    cv.setFillColor(INK)
    cv.setFont('Resume-Bold', 25)
    cv.drawString(LEFT, y - 23, 'DANIEL MOHAMAD')
    y -= 33
    paragraph('Full-Stack Software Developer | AI Application Developer',
              ParagraphStyle('Role', parent=style, fontSize=10.5, textColor=BLUE),
              gap=6, max_width=TEXT_WIDTH-77)
    paragraph('Kuala Belait, Brunei Darussalam | +673 7148981', style_small, gap=1)
    paragraph('<link href="mailto:daniel.ridzwan.mohamad@gmail.com" color="#002fa7">daniel.ridzwan.mohamad@gmail.com</link>', style_small, gap=1)
    paragraph('<link href="https://github.com/DannyRidz" color="#002fa7">github.com/DannyRidz</link> | <link href="https://www.linkedin.com/in/danielmohamad/" color="#002fa7">linkedin.com/in/danielmohamad</link>', style_small, gap=1)
    paragraph('<link href="https://dannyridz.github.io/daniel.mohamad/" color="#002fa7">Portfolio: dannyridz.github.io/daniel.mohamad</link>', style_small, gap=4)

    section('Profile')
    paragraph('Brunei-based developer building full-stack web applications and AI-powered tools. Projects include a codebase explorer grounded in parsed dependencies, a published Android voice translator, and a coffee leaf screening application. Completed The Odin Project JavaScript curriculum. Previous engineering project delivery experience at Wood and NuQuest brings practical troubleshooting, documentation and coordination skills.')

    section('Technical skills')
    for heading, text in [
        ('Frontend', 'HTML, CSS, JavaScript, TypeScript, React, Next.js, Vite, Tailwind CSS'),
        ('Backend and data', 'Node.js, Express, REST APIs, PostgreSQL, Prisma, Supabase Edge Functions, Supabase Auth, Clerk, JWT, row-level security'),
        ('AI and mobile', 'OpenAI Realtime, WebRTC, Gemini, Managed Deep Agents, LangChain, LangSmith, Capacitor, RevenueCat'),
        ('Testing and delivery', 'Git, GitHub, Vitest, Testing Library, Firebase Hosting, Cloud Run'),
    ]:
        paragraph(f'<b>{heading}:</b> {text}', gap=5)

    section('Selected engineering projects')
    paragraph('Cartograph | Repository exploration and code understanding', style_bold, gap=2)
    paragraph('Next.js, TypeScript, ts-morph, React Flow, Supabase, OpenAI, Managed Deep Agents', style_small, gap=4)
    bullet('Built an interactive dependency explorer for public JavaScript and TypeScript repositories, resolving actual imports and reporting skipped files and unresolved connections.')
    bullet('Reused graph traversal across the map and repository Q&amp;A tools. Connected AI explanations to recorded facts, with organization access enforced through Supabase row-level security.')
    paragraph('<link href="https://github.com/DannyRidz/Cartograph" color="#002fa7">github.com/DannyRidz/Cartograph</link> | Public source and screenshot walkthrough', style_small, gap=8)

    paragraph('RidzTalk | Two-way AI voice translator', style_bold, gap=2)
    paragraph('React, TypeScript, OpenAI Realtime, WebRTC, Supabase, Capacitor', style_small, gap=4)
    bullet('Built and published an Android app for bilingual voice conversations; packaged the React app for Android and iOS with Capacitor. Integrated transcription, translation and spoken playback.')
    bullet('Handled asynchronous speech turns and response identities. Used server-side functions for temporary audio-session credentials, with authentication, usage and subscription handling.')
    paragraph('<link href="https://github.com/DannyRidz/RidzTalk-showcase" color="#002fa7">github.com/DannyRidz/RidzTalk-showcase</link> | <link href="https://play.google.com/store/apps/details?id=com.polytalk.app" color="#002fa7">Google Play</link> | Production source private', style_small, gap=8)

    paragraph('Crop Health Assistant | App developer, team J2D', style_bold, gap=2)
    paragraph('Next.js, TypeScript, Gemini, Zod, pdf-lib, Firebase Hosting, Cloud Run', style_small, gap=4)
    bullet('Developed a photo-to-report application in a two-person team, with structured AI response validation, English and Tok Pisin support, and downloadable PDF reports.')
    bullet('Kept visible observations distinct from tentative causes and sourced regional care suggestions. The app does not claim confirmed diagnoses or measured agricultural accuracy.')
    paragraph('<link href="https://github.com/DannyRidz/Crop-Health-Assistant" color="#002fa7">github.com/DannyRidz/Crop-Health-Assistant</link> | <link href="https://coffee-leaf-check.web.app" color="#002fa7">coffee-leaf-check.web.app</link>', style_small, gap=3)

    footer(1)
    print(f'Page 1 content ends at {y:.1f}pt from bottom')
    cv.showPage()
    y = HEIGHT - 44
    paragraph('DANIEL MOHAMAD', style_bold, gap=2)
    paragraph('Experience and education', style_small, gap=7)

    section('Professional experience')
    paragraph('Project Engineer | Wood (Amec Foster Wheeler (B) Sdn Bhd)', style_bold, gap=1)
    paragraph('December 2022 - March 2025', style_small, gap=4)
    bullet('Coordinated onshore and offshore workstreams for BSP rejuvenation projects, working with technical teams, contractors and vendors to resolve delivery issues.')
    bullet('Prepared and reviewed construction work packs against engineering, safety and regulatory requirements, maintaining clear documentation and audit readiness.')
    bullet('Improved planning and resource allocation, reducing execution time by 15%.')
    y -= 4
    paragraph('Project Coordinator | Wood (Amec Foster Wheeler (B) Sdn Bhd)', style_bold, gap=1)
    paragraph('January 2021 - December 2022', style_small, gap=4)
    bullet('Tracked milestones, risks and dependencies across turnaround scopes, contributing to a 98% on-time completion rate.')
    bullet('Worked with contractors, vendors and internal stakeholders to investigate constraints, coordinate decisions and keep work moving.')
    y -= 4
    paragraph('Project Coordinator | NuQuest Sdn Bhd', style_bold, gap=1)
    paragraph('May 2020 - December 2020', style_small, gap=4)
    bullet('Maintained progress reporting and project documentation, coordinating stakeholders around milestones, risks and next actions.')

    section('Additional backend work')
    paragraph('<b>Blog API:</b> Built an Express REST API with Prisma, PostgreSQL and JWT authentication, connected to separate public reader and private admin applications. <link href="https://github.com/DannyRidz/Project-Blog-API" color="#002fa7">Source</link>', gap=5)
    paragraph('<b>Messaging App:</b> Built a React, Express and PostgreSQL app with server-enforced conversation membership, message handling and loading, empty and error states. <link href="https://github.com/DannyRidz/Project-Messaging-App" color="#002fa7">Source</link>', gap=3)

    section('Education and learning')
    paragraph('<b>Bachelor of Industrial Engineering &amp; Management</b><br/>International University of Applied Sciences (IU), Germany | Completed December 2025', gap=5)
    paragraph('<b>BA/BSc (Hons) Audio Production</b> | SAE Institute London, UK | 2016', gap=5)
    paragraph('<b>BTEC Extended Diploma, Electrical/Electronic Engineering</b><br/>City of Westminster College, UK | 2013', gap=5)
    paragraph('<b>The Odin Project:</b> Completed the JavaScript curriculum, with projects covering web interfaces, APIs, databases, authentication, testing and deployment.', gap=3)

    section('Languages')
    paragraph('English (fluent) | Malay (native) | Mandarin (conversational)', gap=0)
    footer(2)
    print(f'Page 2 content ends at {y:.1f}pt from bottom')
    cv.save()
    buffer.seek(0)
    new_pages = PdfReader(buffer)
    if len(new_pages.pages) != 2:
        raise ValueError('Expected exactly two new resume pages.')
    writer = PdfWriter()
    writer.add_page(new_pages.pages[0])
    writer.add_page(new_pages.pages[1])
    writer.add_page(reader.pages[2])
    writer.add_metadata({'/Title': 'Daniel Mohamad | Full-Stack Software and AI Application Developer',
                         '/Author': 'Daniel Ridzwan Bin Mohamad',
                         '/Subject': 'Developer resume with original recommendation letter'})
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('wb') as stream:
        writer.write(stream)
    print(f'Wrote {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference', type=Path, default=ROOT / 'assets/documents/daniel-mohamad-cv.pdf')
    parser.add_argument('--output', type=Path, default=ROOT / 'output/pdf/daniel-mohamad-cv.pdf')
    parser.add_argument('--font-dir', type=Path, default=FONT_DIR)
    args = parser.parse_args()
    build(args.reference, args.output, args.font_dir)
