#!/usr/bin/env osascript

-- AppleScript to convert HTML to PDF using Safari
set htmlPath to "/Users/muditatrey/Desktop/gcloud turrtorial/student-friendly-tutorial.html"
set pdfPath to "/Users/muditatrey/Desktop/gcloud turrtorial/student-friendly-tutorial.pdf"

tell application "Safari"
	activate
	open (POSIX file htmlPath as text)
	delay 3
end tell

tell application "System Events"
	tell process "Safari"
		-- Open Print dialog
		keystroke "p" using command down
		delay 2
		
		-- Click on PDF button (bottom left of print dialog)
		keystroke tab using {shift down, command down}
		delay 1
		
		-- Select "Save as PDF"
		keystroke return
		delay 1
		
		-- Type the filename
		keystroke "g" using {command down, shift down}
		delay 1
		keystroke pdfPath
		delay 1
		keystroke return
		delay 1
		keystroke return
	end tell
end tell

delay 2
tell application "Safari" to quit
