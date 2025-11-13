#!/usr/bin/env python3
import subprocess
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(script_dir, 'student-friendly-tutorial.html')
pdf_file = os.path.join(script_dir, 'student-friendly-tutorial.pdf')

# Read the HTML file
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add some CSS styling for better PDF output
styled_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 5px;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
        }
        pre {
            background: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            border: 1px solid #e1e4e8;
        }
        pre code {
            background: none;
            padding: 0;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        strong {
            color: #e74c3c;
        }
        ul, ol {
            padding-left: 30px;
        }
        hr {
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 30px 0;
        }
        @media print {
            body {
                margin: 0;
                padding: 20px;
            }
        }
    </style>
</head>
<body>
""" + html_content.split('<body>')[1] if '<body>' in html_content else html_content + """
</body>
</html>
"""

# Write styled HTML to a temporary file
temp_html = os.path.join(script_dir, 'temp_styled.html')
with open(temp_html, 'w', encoding='utf-8') as f:
    f.write(styled_html)

# Use macOS's textutil or cupsfilter to convert to PDF
try:
    # Try using cupsfilter (works on macOS)
    subprocess.run([
        'cupsfilter',
        temp_html,
        '>', pdf_file
    ], shell=True, check=True)
    print(f"PDF created successfully: {pdf_file}")
except:
    print("cupsfilter failed, trying alternative method...")
    # Alternative: use Python's weasyprint if available, or print instructions
    print(f"Please open {temp_html} in a browser and use 'Print to PDF'")
    print(f"Or install weasyprint: pip install weasyprint")

# Clean up temp file
if os.path.exists(temp_html):
    os.remove(temp_html)
