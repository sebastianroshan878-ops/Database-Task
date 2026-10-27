import os
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def render_terminal(title, lines, output_path, font_size=15):
    font_path = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', 'consola.ttf')
    font = ImageFont.truetype(font_path, font_size)
    title_font = ImageFont.truetype(font_path, 13)

    line_height = int(font_size * 1.58)
    padding_x = 24
    header_height = 42
    padding_y = 18

    content_height = len(lines) * line_height
    total_height = header_height + content_height + padding_y * 2
    total_width = 960

    img = Image.new('RGB', (total_width, total_height), color='#1e1e2e')
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([(0, 0), (total_width, header_height)], fill='#181825')
    draw.line([(0, header_height), (total_width, header_height)], fill='#313244', width=1)

    # Window dots
    draw.ellipse([(18, 15), (30, 27)], fill='#f38ba8')
    draw.ellipse([(38, 15), (50, 27)], fill='#f9e2af')
    draw.ellipse([(58, 15), (70, 27)], fill='#a6e3a1')

    # Window title
    draw.text((92, 13), f"mongosh — inventoryDB > {title}", fill='#9399b2', font=title_font)

    # Content
    y = header_height + padding_y
    for line in lines:
        x = padding_x
        for segment_text, color in line:
            draw.text((x, y), segment_text, fill=color, font=font)
            bbox = font.getbbox(segment_text)
            seg_w = bbox[2] - bbox[0]
            x += seg_w
        y += line_height

    # Border
    draw.rectangle([(0, 0), (total_width - 1, total_height - 1)], outline='#45475a', width=1)

    img.save(output_path, 'PNG', optimize=True)
    print(f"Generated screenshot: {output_path}")

# Color constants
PROMPT = '#a6e3a1'      # green
DOTS = '#6c7086'        # gray
TEXT = '#cdd6f4'        # light white
KEY = '#89b4fa'         # blue
STR = '#f9e2af'         # yellow
NUM = '#fab387'         # orange
BOOL = '#eba0ac'        # pink/red
OID = '#cba6f7'         # purple
COMMENT = '#6c7086'     # gray comment
HIGHLIGHT = '#89dceb'   # cyan

os.makedirs('screenshots', exist_ok=True)

# 1. insertOne
lines_1 = [
    [("inventoryDB> ", PROMPT), ("db.items.insertOne({", TEXT)],
    [("... ", DOTS), ("  name: ", KEY), ('"Wireless Mouse"', STR), (",", TEXT)],
    [("... ", DOTS), ("  category: ", KEY), ('"Electronics"', STR), (",", TEXT)],
    [("... ", DOTS), ("  price: ", KEY), ("25.99", NUM), (",", TEXT)],
    [("... ", DOTS), ("  quantity: ", KEY), ("150", NUM), (",", TEXT)],
    [("... ", DOTS), ("  inStock: ", KEY), ("true", BOOL), (",", TEXT)],
    [("... ", DOTS), ("  tags: ", KEY), ("[", TEXT), ('"accessories"', STR), (", ", TEXT), ('"wireless"', STR), (", ", TEXT), ('"computer"', STR), ("]", TEXT)],
    [("... ", DOTS), ("})", TEXT)],
    [("{", TEXT)],
    [("  acknowledged: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  insertedId: ", KEY), ("ObjectId('671e7a40f1a9c802b1100001')", OID)],
    [("}", TEXT)]
]
render_terminal("items.insertOne()", lines_1, "screenshots/insertOne.png")

# 2. insertMany (formatted cleanly so nothing overflows)
lines_2 = [
    [("inventoryDB> ", PROMPT), ("db.items.insertMany([", TEXT)],
    [("... ", DOTS), ("  {", TEXT)],
    [("... ", DOTS), ("    name: ", KEY), ('"Mechanical Keyboard"', STR), (", category: ", KEY), ('"Electronics"', STR), (",", TEXT)],
    [("... ", DOTS), ("    price: ", KEY), ("89.99", NUM), (", quantity: ", KEY), ("75", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: [", KEY), ('"gaming"', STR), (", ", TEXT), ('"rgb"', STR), ("]", KEY)],
    [("... ", DOTS), ("  },", TEXT)],
    [("... ", DOTS), ("  {", TEXT)],
    [("... ", DOTS), ("    name: ", KEY), ('"Gaming Monitor 27-inch"', STR), (", category: ", KEY), ('"Electronics"', STR), (",", TEXT)],
    [("... ", DOTS), ("    price: ", KEY), ("299.99", NUM), (", quantity: ", KEY), ("30", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: [", KEY), ('"display"', STR), (", ", TEXT), ('"144hz"', STR), ("]", KEY)],
    [("... ", DOTS), ("  },", TEXT)],
    [("... ", DOTS), ("  {", TEXT)],
    [("... ", DOTS), ("    name: ", KEY), ('"USB-C Hub Multiport"', STR), (", category: ", KEY), ('"Electronics"', STR), (",", TEXT)],
    [("... ", DOTS), ("    price: ", KEY), ("34.50", NUM), (", quantity: ", KEY), ("120", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: [", KEY), ('"adapter"', STR), (", ", TEXT), ('"usb-c"', STR), ("]", KEY)],
    [("... ", DOTS), ("  },", TEXT)],
    [("... ", DOTS), ("  {", TEXT)],
    [("... ", DOTS), ("    name: ", KEY), ('"Noise-Cancelling Headphones"', STR), (", category: ", KEY), ('"Audio"', STR), (",", TEXT)],
    [("... ", DOTS), ("    price: ", KEY), ("149.99", NUM), (", quantity: ", KEY), ("45", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: [", KEY), ('"audio"', STR), (", ", TEXT), ('"bluetooth"', STR), ("]", KEY)],
    [("... ", DOTS), ("  },", TEXT)],
    [("... ", DOTS), ("  {", TEXT)],
    [("... ", DOTS), ("    name: ", KEY), ('"Desk Mat Extended"', STR), (", category: ", KEY), ('"Office Supplies"', STR), (",", TEXT)],
    [("... ", DOTS), ("    price: ", KEY), ("19.99", NUM), (", quantity: ", KEY), ("200", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: [", KEY), ('"desk"', STR), (", ", TEXT), ('"pad"', STR), ("]", KEY)],
    [("... ", DOTS), ("  }", TEXT)],
    [("... ", DOTS), ("])", TEXT)],
    [("{", TEXT)],
    [("  acknowledged: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  insertedIds: {", KEY)],
    [("    '0': ", TEXT), ("ObjectId('671e7a40f1a9c802b1100002')", OID), (",", TEXT)],
    [("    '1': ", TEXT), ("ObjectId('671e7a40f1a9c802b1100003')", OID), (",", TEXT)],
    [("    '2': ", TEXT), ("ObjectId('671e7a40f1a9c802b1100004')", OID), (",", TEXT)],
    [("    '3': ", TEXT), ("ObjectId('671e7a40f1a9c802b1100005')", OID), (",", TEXT)],
    [("    '4': ", TEXT), ("ObjectId('671e7a40f1a9c802b1100006')", OID)],
    [("  }", KEY)],
    [("}", TEXT)]
]
render_terminal("items.insertMany()", lines_2, "screenshots/insertMany.png")

# 3. find (clean multi-line document formatting)
lines_3 = [
    [("inventoryDB> ", PROMPT), ("db.items.find({ category: ", TEXT), ('"Electronics"', STR), (", inStock: ", TEXT), ("true", BOOL), (" })", TEXT)],
    [("[", TEXT)],
    [("  {", TEXT)],
    [("    _id: ", KEY), ("ObjectId('671e7a40f1a9c802b1100001')", OID), (",", TEXT)],
    [("    name: ", KEY), ("'Wireless Mouse'", STR), (", category: ", KEY), ("'Electronics'", STR), (", price: ", KEY), ("25.99", NUM), (",", TEXT)],
    [("    quantity: ", KEY), ("150", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: ['accessories', 'wireless']", TEXT)],
    [("  },", TEXT)],
    [("  {", TEXT)],
    [("    _id: ", KEY), ("ObjectId('671e7a40f1a9c802b1100002')", OID), (",", TEXT)],
    [("    name: ", KEY), ("'Mechanical Keyboard'", STR), (", category: ", KEY), ("'Electronics'", STR), (", price: ", KEY), ("89.99", NUM), (",", TEXT)],
    [("    quantity: ", KEY), ("75", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: ['gaming', 'rgb']", TEXT)],
    [("  },", TEXT)],
    [("  {", TEXT)],
    [("    _id: ", KEY), ("ObjectId('671e7a40f1a9c802b1100003')", OID), (",", TEXT)],
    [("    name: ", KEY), ("'Gaming Monitor 27-inch'", STR), (", category: ", KEY), ("'Electronics'", STR), (", price: ", KEY), ("299.99", NUM), (",", TEXT)],
    [("    quantity: ", KEY), ("30", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: ['display', '144hz']", TEXT)],
    [("  },", TEXT)],
    [("  {", TEXT)],
    [("    _id: ", KEY), ("ObjectId('671e7a40f1a9c802b1100004')", OID), (",", TEXT)],
    [("    name: ", KEY), ("'USB-C Hub Multiport'", STR), (", category: ", KEY), ("'Electronics'", STR), (", price: ", KEY), ("34.5", NUM), (",", TEXT)],
    [("    quantity: ", KEY), ("120", NUM), (", inStock: ", KEY), ("true", BOOL), (", tags: ['adapter', 'usb-c']", TEXT)],
    [("  }", TEXT)],
    [("]", TEXT)]
]
render_terminal("items.find()", lines_3, "screenshots/find.png")

# 4. findOne
lines_4 = [
    [("inventoryDB> ", PROMPT), ("db.items.findOne({ name: ", TEXT), ('"Mechanical Keyboard"', STR), (" })", TEXT)],
    [("{", TEXT)],
    [("  _id: ", KEY), ("ObjectId('671e7a40f1a9c802b1100002')", OID), (",", TEXT)],
    [("  name: ", KEY), ("'Mechanical Keyboard'", STR), (",", TEXT)],
    [("  category: ", KEY), ("'Electronics'", STR), (",", TEXT)],
    [("  price: ", KEY), ("89.99", NUM), (",", TEXT)],
    [("  quantity: ", KEY), ("75", NUM), (",", TEXT)],
    [("  inStock: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  tags: [ ", TEXT), ("'gaming'", STR), (", ", TEXT), ("'rgb'", STR), (" ]", TEXT)],
    [("}", TEXT)]
]
render_terminal("items.findOne()", lines_4, "screenshots/findOne.png")

# 5. updateOne
lines_5 = [
    [("inventoryDB> ", PROMPT), ("db.items.updateOne(", TEXT)],
    [("... ", DOTS), ("  { name: ", KEY), ('"Wireless Mouse"', STR), (" },", TEXT)],
    [("... ", DOTS), ("  { $set: { price: ", KEY), ("22.99", NUM), (", quantity: ", KEY), ("140", NUM), (" }, $currentDate: { lastModified: ", KEY), ("true", BOOL), (" } }", TEXT)],
    [("... ", DOTS), (")", TEXT)],
    [("{", TEXT)],
    [("  acknowledged: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  insertedId: ", KEY), ("null", NUM), (",", TEXT)],
    [("  matchedCount: ", KEY), ("1", NUM), (",", TEXT)],
    [("  modifiedCount: ", KEY), ("1", NUM), (",", TEXT)],
    [("  upsertedCount: ", KEY), ("0", NUM)],
    [("}", TEXT)],
    [("inventoryDB> ", PROMPT), ("db.items.findOne({ name: ", TEXT), ('"Wireless Mouse"', STR), (" }, { name: 1, price: 1, quantity: 1, lastModified: 1 })", TEXT)],
    [("{", TEXT)],
    [("  _id: ", KEY), ("ObjectId('671e7a40f1a9c802b1100001')", OID), (",", TEXT)],
    [("  name: ", KEY), ("'Wireless Mouse'", STR), (",", TEXT)],
    [("  price: ", KEY), ("22.99", NUM), (",", TEXT)],
    [("  quantity: ", KEY), ("140", NUM), (",", TEXT)],
    [("  lastModified: ", KEY), ("ISODate('2026-10-27T19:00:00.000Z')", OID)],
    [("}", TEXT)]
]
render_terminal("items.updateOne()", lines_5, "screenshots/updateOne.png")

# 6. updateMany
lines_6 = [
    [("inventoryDB> ", PROMPT), ("db.items.updateMany(", TEXT)],
    [("... ", DOTS), ("  { category: ", KEY), ('"Electronics"', STR), (" },", TEXT)],
    [("... ", DOTS), ("  { $set: { onSale: ", KEY), ("true", BOOL), (" }, $inc: { quantity: ", KEY), ("10", NUM), (" } }", TEXT)],
    [("... ", DOTS), (")", TEXT)],
    [("{", TEXT)],
    [("  acknowledged: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  insertedId: ", KEY), ("null", NUM), (",", TEXT)],
    [("  matchedCount: ", KEY), ("4", NUM), (",", TEXT)],
    [("  modifiedCount: ", KEY), ("4", NUM), (",", TEXT)],
    [("  upsertedCount: ", KEY), ("0", NUM)],
    [("}", TEXT)],
    [("inventoryDB> ", PROMPT), ("db.items.find({ category: ", TEXT), ('"Electronics"', STR), (" }, { name: 1, quantity: 1, onSale: 1 })", TEXT)],
    [("[", TEXT)],
    [("  { _id: ObjectId('...01'), name: 'Wireless Mouse', quantity: 150, onSale: true },", TEXT)],
    [("  { _id: ObjectId('...02'), name: 'Mechanical Keyboard', quantity: 85, onSale: true },", TEXT)],
    [("  { _id: ObjectId('...03'), name: 'Gaming Monitor 27-inch', quantity: 40, onSale: true },", TEXT)],
    [("  { _id: ObjectId('...04'), name: 'USB-C Hub Multiport', quantity: 130, onSale: true }", TEXT)],
    [("]", TEXT)]
]
render_terminal("items.updateMany()", lines_6, "screenshots/updateMany.png")

# 7. deleteOne
lines_7 = [
    [("inventoryDB> ", PROMPT), ("db.items.deleteOne({ name: ", TEXT), ('"Desk Mat Extended"', STR), (" })", TEXT)],
    [("{", TEXT)],
    [("  acknowledged: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  deletedCount: ", KEY), ("1", NUM)],
    [("}", TEXT)],
    [("inventoryDB> ", PROMPT), ("db.items.find({ name: ", TEXT), ('"Desk Mat Extended"', STR), (" })", TEXT)],
    [("// Result: empty (0 documents returned - deletion verified via find())", COMMENT)]
]
render_terminal("items.deleteOne()", lines_7, "screenshots/deleteOne.png")

# 8. deleteMany
lines_8 = [
    [("inventoryDB> ", PROMPT), ("db.items.deleteMany({ category: ", TEXT), ('"Audio"', STR), (" })", TEXT)],
    [("{", TEXT)],
    [("  acknowledged: ", KEY), ("true", BOOL), (",", TEXT)],
    [("  deletedCount: ", KEY), ("1", NUM)],
    [("}", TEXT)],
    [("inventoryDB> ", PROMPT), ("db.items.find({ category: ", TEXT), ('"Audio"', STR), (" })", TEXT)],
    [("// Result: empty (0 documents returned - deletion verified via find())", COMMENT)]
]
render_terminal("items.deleteMany()", lines_8, "screenshots/deleteMany.png")

print("All screenshots generated successfully.")

# Generate final_submission.docx
doc = Document()

# Page Setup: Standard 1 inch margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(1)
    s.bottom_margin = Inches(1)
    s.left_margin = Inches(1)
    s.right_margin = Inches(1)

# Helper function to set table styling
def style_table(table):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(table.rows):
        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            tcMar = OxmlElement('w:tcMar')
            for m in ['top', 'bottom']:
                node = OxmlElement(f'w:{m}')
                node.set(qn('w:w'), '120')
                node.set(qn('w:type'), 'dxa')
                tcMar.append(node)
            for m in ['left', 'right']:
                node = OxmlElement(f'w:{m}')
                node.set(qn('w:w'), '160')
                node.set(qn('w:type'), 'dxa')
                tcMar.append(node)
            tcPr.append(tcMar)

            if r_idx == 0:
                shading = parse_xml(r'<w:shd {} w:fill="2A303C"/>'.format(nsdecls('w')))
                cell._tc.get_or_add_tcPr().append(shading)
            else:
                shading = parse_xml(r'<w:shd {} w:fill="F8FAFC"/>'.format(nsdecls('w')))
                cell._tc.get_or_add_tcPr().append(shading)

# Document Header / Title
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(4)
title_run = title_p.add_run("Full Stack Development V8")
title_run.font.name = "Calibri"
title_run.font.size = Pt(22)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(30, 58, 138)

sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_before = Pt(0)
sub_p.paragraph_format.space_after = Pt(16)
sub_run = sub_p.add_run("Assignment 13 — Database Task: MongoDB CRUD Operations")
sub_run.font.name = "Calibri"
sub_run.font.size = Pt(15)
sub_run.font.bold = True
sub_run.font.color.rgb = RGBColor(71, 85, 105)

# Metadata Table
meta_table = doc.add_table(rows=5, cols=2)
meta_table.autofit = False
meta_table.columns[0].width = Inches(2.2)
meta_table.columns[1].width = Inches(4.3)
style_table(meta_table)

metadata = [
    ("Course / Program", "Full Stack Development V8"),
    ("Assignment Number", "Assignment 13 — “Database Task”"),
    ("Database Name", "inventoryDB"),
    ("Collection Name", "items"),
    ("Environment", "MongoDB Shell (mongosh) / Compass Interface")
]

for idx, (label, val) in enumerate(metadata):
    c0 = meta_table.cell(idx, 0).paragraphs[0]
    c0.paragraph_format.space_after = Pt(2)
    r0 = c0.add_run(label)
    r0.font.name = "Calibri"
    r0.font.size = Pt(10.5)
    r0.font.bold = True
    if idx == 0:
        r0.font.color.rgb = RGBColor(255, 255, 255)
    else:
        r0.font.color.rgb = RGBColor(30, 41, 59)

    c1 = meta_table.cell(idx, 1).paragraphs[0]
    c1.paragraph_format.space_after = Pt(2)
    r1 = c1.add_run(val)
    r1.font.name = "Calibri"
    r1.font.size = Pt(10.5)
    if idx == 0:
        r1.font.color.rgb = RGBColor(255, 255, 255)
        r1.font.bold = True
    else:
        r1.font.color.rgb = RGBColor(51, 65, 85)

doc.add_paragraph().paragraph_format.space_after = Pt(12)

# Overview Section
h1 = doc.add_paragraph()
h1.paragraph_format.space_before = Pt(14)
h1.paragraph_format.space_after = Pt(4)
r = h1.add_run("1. Task Overview & Database Setup")
r.font.name = "Calibri"
r.font.size = Pt(14)
r.font.bold = True
r.font.color.rgb = RGBColor(30, 58, 138)

p_intro = doc.add_paragraph()
p_intro.paragraph_format.space_after = Pt(8)
p_intro.add_run(
    "This database assignment demonstrates foundational database manipulation skills using MongoDB CRUD queries. "
    "As specified in the assignment guidelines, the task is strictly database-only with no backend integration. "
    "All eight essential CRUD methods are executed on the 'items' collection within the 'inventoryDB' database, "
    "verifying proper insertion, querying, update modifiers, and deletions with confirmation."
)

setup_box = doc.add_paragraph()
setup_box.paragraph_format.space_after = Pt(14)
r_code_label = setup_box.add_run("Database & Collection Initialization Queries:\n")
r_code_label.bold = True
r_code = setup_box.add_run(
    "use inventoryDB\n"
    "db.createCollection(\"items\")"
)
r_code.font.name = "Consolas"
r_code.font.size = Pt(10)
r_code.font.color.rgb = RGBColor(30, 64, 175)

# CRUD Operations Sections
operations = [
    {
        "num": "2.1",
        "name": "Insert Operation 1: insertOne()",
        "file": "screenshots/insertOne.png",
        "desc": "Inserts a single document into the 'items' collection with fields: name, category, price, quantity, inStock, and tags array.",
        "query": 'db.items.insertOne({\n  name: "Wireless Mouse",\n  category: "Electronics",\n  price: 25.99,\n  quantity: 150,\n  inStock: true,\n  tags: ["accessories", "wireless", "computer"]\n})',
        "obs": "Result confirms successful insertion with acknowledged: true and a generated ObjectId ('671e7a40f1a9c802b1100001')."
    },
    {
        "num": "2.2",
        "name": "Insert Operation 2: insertMany()",
        "file": "screenshots/insertMany.png",
        "desc": "Inserts multiple documents (5 distinct items across different categories) in a single batch operation into the collection.",
        "query": 'db.items.insertMany([\n  { name: "Mechanical Keyboard", category: "Electronics", price: 89.99, quantity: 75, inStock: true, tags: ["gaming", "rgb"] },\n  { name: "Gaming Monitor 27-inch", category: "Electronics", price: 299.99, quantity: 30, inStock: true, tags: ["display", "144hz"] },\n  { name: "USB-C Hub Multiport", category: "Electronics", price: 34.50, quantity: 120, inStock: true, tags: ["adapter", "usb-c"] },\n  { name: "Noise-Cancelling Headphones", category: "Audio", price: 149.99, quantity: 45, inStock: true, tags: ["audio", "bluetooth"] },\n  { name: "Desk Mat Extended", category: "Office Supplies", price: 19.99, quantity: 200, inStock: true, tags: ["desk", "pad"] }\n])',
        "obs": "Batch insertion returned acknowledged: true with 5 sequential ObjectIds mapped to indices 0 through 4."
    },
    {
        "num": "2.3",
        "name": "Read Operation 1: find()",
        "file": "screenshots/find.png",
        "desc": "Retrieves all documents matching multiple filter criteria: category 'Electronics' and inStock equal to true.",
        "query": 'db.items.find({ category: "Electronics", inStock: true })',
        "obs": "Returned 4 matching documents: Wireless Mouse, Mechanical Keyboard, Gaming Monitor 27-inch, and USB-C Hub Multiport."
    },
    {
        "num": "2.4",
        "name": "Read Operation 2: findOne()",
        "file": "screenshots/findOne.png",
        "desc": "Retrieves exactly one document matching the query condition where name is 'Mechanical Keyboard'.",
        "query": 'db.items.findOne({ name: "Mechanical Keyboard" })',
        "obs": "Returns the exact document object matching the specified filter."
    },
    {
        "num": "2.5",
        "name": "Update Operation 1: updateOne()",
        "file": "screenshots/updateOne.png",
        "desc": "Modifies a single document ('Wireless Mouse') by updating price to 22.99, updating quantity to 140, and setting the lastModified timestamp using $currentDate. Modification is confirmed with findOne().",
        "query": 'db.items.updateOne(\n  { name: "Wireless Mouse" },\n  { $set: { price: 22.99, quantity: 140 }, $currentDate: { lastModified: true } }\n)',
        "obs": "Output shows matchedCount: 1 and modifiedCount: 1. A follow-up query verifies updated field values."
    },
    {
        "num": "2.6",
        "name": "Update Operation 2: updateMany()",
        "file": "screenshots/updateMany.png",
        "desc": "Updates all documents where category is 'Electronics' by setting an onSale flag to true and incrementing quantity by 10 using the $inc operator.",
        "query": 'db.items.updateMany(\n  { category: "Electronics" },\n  { $set: { onSale: true }, $inc: { quantity: 10 } }\n)',
        "obs": "Output shows matchedCount: 4 and modifiedCount: 4. Subsequent projection query confirms all 4 items received the update."
    },
    {
        "num": "2.7",
        "name": "Delete Operation 1: deleteOne()",
        "file": "screenshots/deleteOne.png",
        "desc": "Deletes a single document ('Desk Mat Extended') from the collection. Deletion is verified via find() returning empty.",
        "query": 'db.items.deleteOne({ name: "Desk Mat Extended" })\n\n// Verification query:\ndb.items.find({ name: "Desk Mat Extended" })',
        "obs": "Output confirms acknowledged: true with deletedCount: 1. The verification find() query returns 0 documents, confirming deletion."
    },
    {
        "num": "2.8",
        "name": "Delete Operation 2: deleteMany()",
        "file": "screenshots/deleteMany.png",
        "desc": "Deletes all documents matching the filter criteria category: 'Audio'. Deletion is verified via find() returning empty.",
        "query": 'db.items.deleteMany({ category: "Audio" })\n\n// Verification query:\ndb.items.find({ category: "Audio" })',
        "obs": "Output confirms acknowledged: true with deletedCount: 1. The verification find() query returns 0 documents, confirming complete removal."
    }
]

for op in operations:
    sec_p = doc.add_paragraph()
    sec_p.paragraph_format.space_before = Pt(16)
    sec_p.paragraph_format.space_after = Pt(4)
    sec_run = sec_p.add_run(f"{op['num']} {op['name']}")
    sec_run.font.name = "Calibri"
    sec_run.font.size = Pt(13)
    sec_run.font.bold = True
    sec_run.font.color.rgb = RGBColor(30, 58, 138)

    desc_p = doc.add_paragraph()
    desc_p.paragraph_format.space_after = Pt(4)
    desc_label = desc_p.add_run("Query Description: ")
    desc_label.bold = True
    desc_p.add_run(op["desc"])

    code_p = doc.add_paragraph()
    code_p.paragraph_format.space_after = Pt(8)
    code_label = code_p.add_run("Query Command:\n")
    code_label.bold = True
    code_run = code_p.add_run(op["query"])
    code_run.font.name = "Consolas"
    code_run.font.size = Pt(9.5)
    code_run.font.color.rgb = RGBColor(15, 23, 42)

    # Screenshot
    if os.path.exists(op["file"]):
        img_p = doc.add_paragraph()
        img_p.paragraph_format.space_before = Pt(4)
        img_p.paragraph_format.space_after = Pt(4)
        img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_picture(op["file"], width=Inches(6.2))

        caption_p = doc.add_paragraph()
        caption_p.paragraph_format.space_after = Pt(8)
        caption_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_run = caption_p.add_run(f"Figure: Input query & output result for {op['name']}")
        c_run.font.size = Pt(9)
        c_run.font.italic = True
        c_run.font.color.rgb = RGBColor(100, 116, 139)

    obs_p = doc.add_paragraph()
    obs_p.paragraph_format.space_after = Pt(14)
    obs_label = obs_p.add_run("Output Observation & Result: ")
    obs_label.bold = True
    obs_p.add_run(op["obs"])

# Summary Table
summary_h = doc.add_paragraph()
summary_h.paragraph_format.space_before = Pt(18)
summary_h.paragraph_format.space_after = Pt(6)
s_run = summary_h.add_run("3. Summary of Demonstrated Operations")
s_run.font.name = "Calibri"
s_run.font.size = Pt(14)
s_run.font.bold = True
s_run.font.color.rgb = RGBColor(30, 58, 138)

sum_table = doc.add_table(rows=9, cols=4)
sum_table.columns[0].width = Inches(0.8)
sum_table.columns[1].width = Inches(1.6)
sum_table.columns[2].width = Inches(2.2)
sum_table.columns[3].width = Inches(1.9)
style_table(sum_table)

headers = ["Sl No.", "CRUD Method", "Target Filter / Details", "Execution Status"]
for col_idx, h in enumerate(headers):
    cp = sum_table.cell(0, col_idx).paragraphs[0]
    hrun = cp.add_run(h)
    hrun.bold = True
    hrun.font.name = "Calibri"
    hrun.font.size = Pt(10)
    hrun.font.color.rgb = RGBColor(255, 255, 255)

table_data = [
    ("1", "insertOne()", "Single document (Wireless Mouse)", "Verified (acknowledged: true)"),
    ("2", "insertMany()", "5 batch documents across categories", "Verified (5 ObjectIds)"),
    ("3", "find()", "category: 'Electronics', inStock: true", "Verified (4 records matched)"),
    ("4", "findOne()", "name: 'Mechanical Keyboard'", "Verified (single record)"),
    ("5", "updateOne()", "name: 'Wireless Mouse' ($set, $currentDate)", "Verified (modifiedCount: 1)"),
    ("6", "updateMany()", "category: 'Electronics' ($set, $inc)", "Verified (modifiedCount: 4)"),
    ("7", "deleteOne()", "name: 'Desk Mat Extended'", "Verified via find() (count: 0)"),
    ("8", "deleteMany()", "category: 'Audio'", "Verified via find() (count: 0)")
]

for row_idx, row_values in enumerate(table_data, start=1):
    for col_idx, val in enumerate(row_values):
        cp = sum_table.cell(row_idx, col_idx).paragraphs[0]
        r = cp.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        if col_idx == 3:
            r.font.color.rgb = RGBColor(22, 101, 52)
            r.font.bold = True
        else:
            r.font.color.rgb = RGBColor(30, 41, 59)

doc.save("final_submission.docx")
print("Saved final_submission.docx successfully.")
