
from ocr import image_to_text

if __name__ == "__main__":
    image_path = "sample_images/sample.png"
    text = image_to_text(image_path)
    print("Extracted Text:\n")
    print(text)
