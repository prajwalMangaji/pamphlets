import qrcode

# List of data (URLs) for each QR code - replace with your real URLs later
qr_data = [
    'https://example.com/1',      # QR1: Intro
    'https://example.com/2',   # QR2: Benefits
    'https://example.com/3',       # QR3: Tech
    'https://example.com/4', # QR4: Challenges
    'https://example.com/5'      # QR5: Future
]

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