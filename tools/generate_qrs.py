import qrcode

# List of data (URLs) for each QR code - replace with your real URLs later
qr_data = [
    'https://prajwalmangaji.github.io/pamphlets/1.html',      # QR1: Intro
    'https://prajwalmangaji.github.io/pamphlets/2.html',   # QR2: Benefits
    'https://prajwalmangaji.github.io/pamphlets/3.html',       # QR3: Tech
    'https://prajwalmangaji.github.io/pamphlets/4.html', # QR4: Challenges
    'https://prajwalmangaji.github.io/pamphlets/5.html'      # QR5: Future
]

# Special QR code for all images
qr_all_url = 'https://prajwalmangaji.github.io/pamphlets/6.html'

# Generate each QR code
for i, data in enumerate(qr_data, start=1):
    # Create QRCode object with settings
    qr = qrcode.QRCode(
        version=1,              # Size/version (1 is small; auto-adjusts)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # High error correction (up to 30% damage tolerance)
        box_size=10,            # Pixel size per module (increase for larger images)
        border=4                # Border thickness (minimum 4 for scannability)
    )
    
    # Add data (URL)
    qr.add_data(data)
    qr.make(fit=True)  # Auto-fit data to QR size
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save as PNG
    filename = f"qr_code_{i}.png"
    img.save(filename)
    print(f"Generated: {filename} for data: {data}")

# Generate the special "all" QR code
qr_all = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr_all.add_data(qr_all_url)
qr_all.make(fit=True)

img_all = qr_all.make_image(fill_color="black", back_color="white")
img_all.save("qr_code_all.png")
print(f"Generated: qr_code_all.png for data: {qr_all_url}")