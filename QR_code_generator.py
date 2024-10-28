# Importing necessary modules
import qrcode
from PIL import Image
import os

# Define function to create and save a customized QR code
def generate_qr_code(url, file_name="Qr_code.png", box_size=10, border=4, fill_color="black", back_color="white"):
    
    
    # Create QR code instance with specified settings
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    
    # Add data to the QR code
    qr_code.add_data(url)
    qr_code.make(fit=True)
    
    # Generate the QR code image
    img = qr_code.make_image(fill_color=fill_color, back_color=back_color)
    
    # Check if the QR code file already exists
    if os.path.exists(file_name):
        existing_img = Image.open(file_name)
        # Compare the existing image with the new image
        if list(existing_img.getdata()) == list(img.getdata()):
            print("QR code is already generated.")
            return
    
    # Save the QR code as an image file if it's new
    img.save(file_name)
    print(f"QR Code saved as {file_name}")

# Usage example
generate_qr_code("https://github.com/cyberDude404/python_projects.git", "Custom_Qr_code.png", box_size=8, border=4, fill_color="blue", back_color="white")

