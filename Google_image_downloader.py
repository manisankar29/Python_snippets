import requests
from io import BytesIO
from PIL import Image

def download_google_image(image_url, output_path='downloaded_image.jpg'):
    try:
        response = requests.get(image_url)
        img_data = response.content

        with open(output_path, 'wb') as img_file:
            img_file.write(img_data)

        print(f"Image downloaded successfully to {output_path}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    image_url = input("Enter the Google image URL: ")

    output_path = input("Enter the output path for the downloaded image (default is 'downloaded_image.jpg'): ") or 'downloaded_image.jpg'

    download_google_image(image_url, output_path)
