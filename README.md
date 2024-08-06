# AI_Image_Generator

## Description
This project is an AI-powered image generator application built using Python. The application leverages the OpenAI (DALL-E 2) API to generate images based on user prompts and specific styles, offering an intuitive and interactive user interface created with the customtkinter library.

## Features
- **User Prompt Input:** Users can enter a text prompt describing the desired image.
- **Style Selection:** Users can choose from various styles such as Realistic, Dusk, Crayon, Cartoon, Hand Drawn, 3D Illustration, and Flat Art.
- **Image Quantity:** Users can specify the number of images to generate using a slider.
- **Image Display:** The generated images are displayed in a slideshow format on the application's canvas.

## Technologies

- **Python 3.10.5:**
  - The core programming language used to develop the application.
  - Provides the main runtime environment for the application.

- **customtkinter:**
  - Standard Python library for creating graphical user interfaces (GUI).

- **Pillow (PIL):**
  - Python Imaging Library (PIL) fork, used for opening, manipulating, and saving many different image file formats.
  - Version 10.3.0 used in this project.
  - Enables the application to process and display images fetched from the OpenAI API.

- **Requests:**
  - HTTP library for Python, used to fetch images from URLs.
  - Version 2.32.2 used in this project.

- **OpenAI DALL-E 2 API:**
  - Used to generate images based on user prompts

## Prerequisites
- Python 3.x
- Virtualenv

## Installation

1. **Create a virtual environment:**
   ```sh
   pip install virtualenv
   virtualenv image # 'image' is just a name for the virtual environment, you can choose any name
2. **Activate the virtual environment:**
   
     **On Windows:**
   
       .\image\Scripts\activate
   
     **On macOS/Linux:**
   
       source image/bin/activate

3. **Install OpenAI:**
   
        pip install openai

4. **Install required packages:**
   
        pip install pillow
        
        pip install requests

## Dependencies (may vary)
  - Pillow: 10.3.0
  - Requests: 2.32.2
     - certifi: 2024.2.2
     - charset-normalizer: 3.3.2
     - idna: 3.7
     - urllib3: 2.2.1
       
## Setting up your OpenAI API key

1. **Obtain your API key:**

  - Go to the https://beta.openai.com/signup/, sign up, and log in to your account.
  - Navigate to the API section and generate your API key.
    
2. **Set your API key in the code (Recommended: Set API key as an Environment Variable):**

  - Open the main.py file in your preferred code editor.
    
        openai.api_key = 'your_api_key_here'

## Project Structure
**main.py**: The main script containing the code for the Book Recommendation System.

## Usage
python main.py

