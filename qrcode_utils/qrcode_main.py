import qrcode
import argparse

def generate_qrcode(url, filename):
    # Create a QR Code object
    img = qrcode.make(url)

    # Save the image to a file
    img.save(filename)
    print(f"QR Code saved as {filename}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Generate a QR code from a URL.')
    parser.add_argument('--url', required=True, help='URL to encode in the QR code')
    parser.add_argument('--file', required=True, help='Filename to save the QR code image')

    # Parse the arguments
    args = parser.parse_args()

    # Generate the QR code and save it to the specified file
    generate_qrcode(args.url, args.file)

if __name__ == '__main__':
    main()
