# open image file
import os, sys
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

args = sys.argv[1:]
infile = args[0]
f, e = os.path.splitext(infile)
image_paths = []

def create_images():
    try:
    # if not e in ['jpg', 'png', 'jpeg']:
    #     raise ValueError
        with Image.open(infile) as im:
            if im.mode == "RGBA":
                im = im.convert("RGB")
            
            for i in range(100):
                im_copy = im.copy()
                # initialize the drawing context
                draw = ImageDraw.Draw(im_copy)
                # choose the font
                font = ImageFont.truetype('arial.ttf', 36)
                # define the position
                position = (50, 50)
                # color
                text_color = (255, 0, 0)

                # drawing the text on the image
                draw.text(position, f"{i}", fill=text_color, font=font)
                file = f"{f}_{i}{e}"
                image_paths.append(file)
                im_copy.save(file)
    except OSError:
        print("Invalid input")
# except ValueError:
#     print("can't open this file")


# make a pdf file from iamges
def images_to_pdf(image_paths, output_pdf):
    pdf = FPDF()
    for image_path in image_paths:
        pdf.add_page()
        pdf.image(image_path, 0, 0 , 210, 297)
        os.remove(image_path)
    
    pdf.output(output_pdf, 'F')


create_images()
images_to_pdf(image_paths, "output.pdf")