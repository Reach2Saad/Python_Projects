import qrcode

# Get input.
URL = input("Enter the text or URL: ").strip()
filename = input("Enter the file name: ").strip()

# Create QR code.
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(URL)

# Save image.
image = qr.make_image(fill_color= "black", back_color="white")
image.save(filename)
print(f"QR code save as {filename}")