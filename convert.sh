#!/bin/bash

# HTML to PDF converter for macOS
HTML_FILE="/Users/muditatrey/Desktop/gcloud turrtorial/student-friendly-tutorial.html"
PDF_FILE="/Users/muditatrey/Desktop/gcloud turrtorial/student-friendly-tutorial.pdf"

# Use textutil (works on macOS)
/usr/bin/textutil -convert html -output "$HTML_FILE.tmp" "$HTML_FILE" 2>/dev/null

# Try cupsfilter
cupsfilter "$HTML_FILE" > "$PDF_FILE" 2>/dev/null

if [ -f "$PDF_FILE" ]; then
    echo "PDF created successfully: $PDF_FILE"
else
    echo "Using browser automation to create PDF..."
    # Use osascript to open in Safari and print to PDF
    osascript <<EOF
set htmlFile to POSIX file "$HTML_FILE"
set pdfFile to POSIX file "$PDF_FILE"

tell application "Safari"
    activate
    open htmlFile
    delay 2
end tell

tell application "System Events"
    keystroke "p" using command down
    delay 1
    keystroke return
end tell
EOF
fi
