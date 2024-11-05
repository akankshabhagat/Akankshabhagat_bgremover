from rembg import remove
import easygui as eg
from PIL import Image
input_path=eg.fileopenbox(title= "Select image file")
output_path="D:\\AKANKSHABBGREMOVER\\output_image.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
image=Image.open(output_path)
image.show()

