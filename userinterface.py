import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from deepface_file import deepface_main

FILE_PATH = None

def init():
    """
    Initialises window, buttons, labels, etc. ...
    """
    # create and configure window
    root = tk.Tk()
    root.title("Emotions")
    root.configure(background="white")
    root.minsize(1920, 1080)

    # simple label asking for image upload
    demand_image_label = tk.Label(root, text="Bitte laden Sie ein Bild hoch")
    demand_image_label.pack()

    # label needed to store/display the uploaded image
    img_label = tk.Label(root)
    img_label.pack()

    # result label
    result_label = tk.Label(root, text="Noch keine Emotion erkannt!")

    # button that enables user to upload an image file
    BTN_browse = tk.Button(root, text="Upload Image", command=lambda:upload_file(img_label))
    BTN_browse.pack()

    # button that executes the AI emotion detection
    BTN_calculate = tk.Button(root, text="Calculate emotion", command=lambda:change_result_label(deepface_main(get_filepath())))
    BTN_calculate.pack()

    def change_result_label(resultText):
        # result label
        result_label.config(text="Erkannte Emotion: "+resultText)
        result_label.pack()

    root.mainloop()

def upload_file(pImageLabel):
    """
    This function handles browsing, uploading and displaying of an image file
    """
    # allowed file types
    file_types = [('JPG files', '*.jpg'), ('PNG files', '*.png')]
    file_path = askopenfilename(filetypes=file_types) # NOTE: This returns nothing else rather than a directory path
    global FILE_PATH
    FILE_PATH = file_path

    if file_path: # if file directory exists
        # set maximum size of image
        max_width = 800
        max_height = 600

        # open image from directory
        img = Image.open(file_path)
        width, height = img.size

        # if image exceeds maximum size, rescale to an appropriate image size
        if width > max_width or height > max_height:
            ratio = min(max_width / width, max_height / height)
            width = int(width * ratio)
            height = int(height * ratio)
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        # add (new) image to the existing image label
        pImageLabel.configure(image=img)
        pImageLabel.image = img

def get_filepath():
    return FILE_PATH

def main():
    init()

if __name__ == "__main__":
    main()
