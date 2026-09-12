import os
import io
import zipfile
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

base_dir = r'D:\WorkBuddy\the-architects-dream'
chapters_dir = os.path.join(base_dir, 'chapters')
output_dir = os.path.join(base_dir, 'dist')
os.makedirs(output_dir, exist_ok=True)

# Chapter order and titles
chapters = [
    ('00-prologue.md', 'Prologue: Laplace\'s Demon at 2 AM'),
    ('01-descartes-ghost.md', 'Chapter 1: Descartes\' Ghost'),
    ('02-godels-loop.md', 'Chapter 2: Gödel\'s Loop'),
    ('03-nietzsches-hammer.md', 'Chapter 3: Nietzsche\'s Hammer'),
    ('04-turings-crush.md', 'Chapter 4: Turing\'s Crush'),
    ('05-schrodingers-cat.md', 'Chapter 5: Schrödinger\'s Cat'),
    ('06-einsteins-verdict.md', 'Chapter 6: Einstein\'s Verdict'),
    ('07-kants-space.md', 'Chapter 7: Kant\'s Space'),
    ('08-the-position-of-pi.md', 'Chapter 8: The Position of π'),
    ('09-the-shadow-of-the-cave.md', 'Chapter 9: The Shadow of the Cave'),
    ('10-epilogue.md', 'Epilogue: The Calibration Device in Ash'),
]

# Read all chapters
chapter_contents = []
for fname, title in chapters:
    fpath = os.path.join(chapters_dir, fname)
    if os.path.exists(fpath):
        with io.open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        chapter_contents.append((title, content))
        print(f"Read: {title} ({len(content)} chars)")
    else:
        print(f"WARNING: {fname} not found")

print(f"\nTotal chapters: {len(chapter_contents)}")

# ===== Generate EPUB =====
print("\n=== Generating EPUB ===")
epub_path = os.path.join(output_dir, 'the-architects-dream.epub')

with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    # mimetype (must be first, uncompressed)
    zf.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
    
    # META-INF/container.xml
    zf.writestr('META-INF/container.xml', '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>''')
    
    # OEBPS/content.opf
    manifest_items = ''
    spine_items = ''
    for i, (title, content) in enumerate(chapter_contents):
        item_id = f'chapter{i}'
        href = f'chapter{i}.xhtml'
        manifest_items += f'    <item id="{item_id}" href="{href}" media-type="application/xhtml+xml"/>\n'
        spine_items += f'    <itemref idref="{item_id}"/>\n'
    
    content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="BookId">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>The Architect's Dream</dc:title>
    <dc:creator>banbanry</dc:creator>
    <dc:language>en</dc:language>
    <dc:identifier id="BookId">urn:uuid:architects-dream-2026</dc:identifier>
    <dc:description>Nine Hammers of Self-Trial — A philosophical science-fiction novella about an architect who thought he was Laplace's Demon.</dc:description>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
{manifest_items}  </manifest>
  <spine toc="ncx">
{spine_items}  </spine>
</package>'''
    zf.writestr('OEBPS/content.opf', content_opf)
    
    # OEBPS/toc.ncx
    nav_points = ''
    for i, (title, content) in enumerate(chapter_contents):
        nav_points += f'''    <navPoint id="navPoint-{i}" playOrder="{i+1}">
      <navLabel><text>{title}</text></navLabel>
      <content src="chapter{i}.xhtml"/>
    </navPoint>
'''
    
    toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:architects-dream-2026"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>The Architect's Dream</text></docTitle>
  <navMap>
{nav_points}  </navMap>
</ncx>'''
    zf.writestr('OEBPS/toc.ncx', toc_ncx)
    
    # OEBPS/chapter*.xhtml
    for i, (title, content) in enumerate(chapter_contents):
        # Convert markdown to HTML
        html_body = markdown.markdown(content, extensions=['extra'])
        xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>{title}</title>
  <style>
    body {{ font-family: Georgia, serif; line-height: 1.6; margin: 1em; }}
    h1, h2, h3 {{ font-family: Georgia, serif; }}
    blockquote {{ border-left: 3px solid #666; margin-left: 0; padding-left: 1em; color: #555; }}
    code {{ background: #f4f4f4; padding: 2px 4px; }}
  </style>
</head>
<body>
{html_body}
</body>
</html>'''
        zf.writestr(f'OEBPS/chapter{i}.xhtml', xhtml)

print(f"EPUB generated: {epub_path} ({os.path.getsize(epub_path)} bytes)")

# ===== Generate PDF =====
print("\n=== Generating PDF ===")
pdf_path = os.path.join(output_dir, 'the-architects-dream.pdf')

doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                         leftMargin=1*inch, rightMargin=1*inch,
                         topMargin=1*inch, bottomMargin=1*inch)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('CustomTitle', parent=styles['Title'], fontSize=24, spaceAfter=30, alignment=TA_CENTER)
subtitle_style = ParagraphStyle('CustomSubtitle', parent=styles['Normal'], fontSize=14, spaceAfter=20, alignment=TA_CENTER, textColor='#555555')
h1_style = ParagraphStyle('CustomH1', parent=styles['Heading1'], fontSize=18, spaceBefore=20, spaceAfter=12)
h2_style = ParagraphStyle('CustomH2', parent=styles['Heading2'], fontSize=14, spaceBefore=15, spaceAfter=10)
body_style = ParagraphStyle('CustomBody', parent=styles['Normal'], fontSize=11, leading=16, spaceAfter=8, alignment=TA_JUSTIFY)
quote_style = ParagraphStyle('CustomQuote', parent=styles['Normal'], fontSize=10, leading=14, leftIndent=20, rightIndent=20, textColor='#555555', spaceAfter=8)

story = []

# Title page
story.append(Spacer(1, 2*inch))
story.append(Paragraph("The Architect's Dream", title_style))
story.append(Paragraph("Nine Hammers of Self-Trial", subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("An architect thought he had mastered Subject–Variable–Result.<br/>He thought he was Laplace's Demon.<br/>Then seven philosophers, plus π, plus a shadow,<br/>smashed his nine layers of illusion with nine hammers.", subtitle_style))
story.append(Spacer(1, 2*inch))
story.append(Paragraph("banbanry", subtitle_style))
story.append(PageBreak())

# Chapters
for i, (title, content) in enumerate(chapter_contents):
    # Convert markdown to HTML for reportlab
    lines = content.split('\n')
    in_blockquote = False
    
    for line in lines:
        line = line.strip()
        if not line:
            story.append(Spacer(1, 6))
            continue
        
        # Handle headers
        if line.startswith('# '):
            story.append(Paragraph(line[2:], h1_style))
        elif line.startswith('## '):
            story.append(Paragraph(line[3:], h2_style))
        elif line.startswith('### '):
            story.append(Paragraph(line[4:], h2_style))
        # Handle blockquotes
        elif line.startswith('> '):
            import re
            text = line[2:]
            text = text.replace('&', '&amp;')
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
            story.append(Paragraph(text, quote_style))
        elif line.startswith('>'):
            import re
            text = line[1:]
            text = text.replace('&', '&amp;')
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
            story.append(Paragraph(text, quote_style))
        # Handle horizontal rule
        elif line.startswith('---'):
            story.append(Spacer(1, 10))
        # Handle bold/italic in regular text
        else:
            import re
            text = line
            # Escape & first
            text = text.replace('&', '&amp;')
            # Bold: **text** -> <b>text</b>
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            # Italic: *text* -> <i>text</i> (careful not to match **)
            text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
            # Code: `text` -> <font face="Courier">text</font>
            text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
            story.append(Paragraph(text, body_style))
    
    if i < len(chapter_contents) - 1:
        story.append(PageBreak())

doc.build(story)
print(f"PDF generated: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

print("\n=== Done ===")
print(f"EPUB: {epub_path}")
print(f"PDF: {pdf_path}")
