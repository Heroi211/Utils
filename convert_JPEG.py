import os
from PIL import Image

def convert_to_jpeg(file_path) -> str:

        image = Image.open(file_path)
        
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB") #converto para RGB por que png tem transparencia e jpeg não
            
        base = os.path.splitext(file_path)[0] #removendo a extensão
        new_image_path = f"{base}.jpeg" #incluindo a extensão jpeg
        
        image.save(new_image_path, "JPEG")
        
        return new_image_path