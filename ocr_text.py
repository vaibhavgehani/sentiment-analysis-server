try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/intel/AppData/Local/Tesseract-OCR/tesseract.exe'
    text=pytesseract.image_to_string(Image.open(filename))
    return(text)
    