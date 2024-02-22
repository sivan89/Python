import os
import img2pdf

def imag(image_folder_path):
    if os.path.exists(image_folder_path):
        print("valid path")
    else:
        print("provide the valied path")
        
    image = [img for img in os.listdir(image_folder_path) if img.endswith((".JPG",".jpeg",".png"))]
    
    #for img in os.listdir(image_folder_path):
        #image = img.endswith((".JPG",".jpeg",".png"))
    
    image.sort()
    images_bytes = list()
    
    for i in image:
        with open(os.path.join(image_folder_path,i),"rb") as pd:  #rb - opens the file in binary format for reading
            images_bytes.append(pd.read())
    
    pdf_image_byts = img2pdf.convert(images_bytes)
    with open("Output.pdf", "wb") as sd:
        sd.write(pdf_image_byts)




folder_path = input ("provide the payh :")
imag((folder_path))
