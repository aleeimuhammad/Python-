import pyqrcode

# Get user input for the URL
content = input("Enter your URL: ")

# Generate QR Code
url = pyqrcode.create(content)

# Get user input for the file name 
file_name = input("Enter file name : ")

# Save QR Code as an SVG file using the provided file name
url.svg(f"{file_name}.svg", scale=8)

# Print QR Code to terminal
print(url.terminal(quiet_zone=1))
