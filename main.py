import customtkinter as ctk # pip install customtkinter
import tkinter

import openai
import os

from PIL import Image, ImageTk # For image processing
import requests,io # To get the image from the url

# Generate button functionality
def generate():
    openai.api_key =  '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'
    user_prompt = prompt_entry.get("0.0", tkinter.END)
    user_prompt += "in style: " + style_dropdown.get()

    # Response from openai
    response = openai.Image.create(
    prompt = user_prompt,
    n = int(number_slider.get()),
    size = "512x512"
) 
    # Collecting the image urls
    image_urls = []
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])

    # Collecting the images
    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)

    # To slideshow the images
    def update_images(index=0):
        canvas.image = images[index]
        canvas.create_image(0,0,anchor="nw", image=images[index])
        index = (index + 1) % len(images)
        canvas.after(3000, update_images, index)
    update_images()

root = ctk.CTk()
root.title("AI Image Generator")
root.configure(bg="#0000FF")

# Follow System's default mode
ctk.set_appearance_mode("dark") 

# Input Frame
inner_frame = ctk.CTkFrame(root)
inner_frame.pack(side= "left", expand = True, padx=20, pady=20)

# Prompt Label & Textbox
prompt_label = ctk.CTkLabel(inner_frame, text="Prompt")
prompt_label.grid(row=0, column=-0, padx=10, pady=10)
prompt_entry = ctk.CTkTextbox(inner_frame,height=10)
prompt_entry.grid(row=0,column=1, padx=10, pady=10)

# Style Label & ComboBox
style_label = ctk.CTkLabel(inner_frame, text="Style")
style_label.grid(row=1,column=0,padx=10,pady=10)
style_dropdown = ctk.CTkComboBox(inner_frame, values= ["Realistic", "Dusk", "Crayon","Cartoon","Hand Drawn", "3D Illustration", "Flat Art"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Number Label & Slider
number_label = ctk.CTkLabel(inner_frame, text="# Images")
number_label.grid(row=2, column=0, padx=10, pady=10)
number_slider = ctk.CTkSlider(inner_frame, from_ = 1, to = 10, number_of_steps=9)
number_slider.grid(row=2, column=1, padx=10, pady=10)

# Generate Button
generate_button = ctk.CTkButton(inner_frame, text="Generate", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

# Canvas
canvas = tkinter.Canvas(root, width= 512, height= 512)
canvas.pack(side="right", padx=100)

root.mainloop()