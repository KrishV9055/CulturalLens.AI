# CulturalLensAI 🌍📸

Discover the rich heritage of Indian monuments with CulturalLensAI! Our project helps tourists, especially foreigners, by providing the exact location, multi-lingual information, and nearby monuments for any given image of an Indian monument.

## Table of Contents

- [CulturalLensAI 🌍📸](#culturallensai-)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)

## About the Project

CulturalLensAI aims to enhance the experience of tourists visiting Indian monuments by offering detailed information and nearby attractions. Simply upload an image of an Indian monument, and our system will provide:

- 📍 Exact location of the monument using Leaflet library
- 🌐 Multi-lingual information about the monument from Wikipedia
- 🏛️ List of Nearby monuments and their locations based on the city

### Built With

- HTML, CSS, JS, Python, Flask

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.8+ 🐍
- pip 📦


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KrishV9055/CulturalLensAI.git
   ```
2. Navigate to the project directory
   ```sh
   cd CulturalLensAI
   ```
   
3. Install the required packages

4. Ensure the following directory structure is present:
   ```
   CulturalLensAI/
   ├── other/
   ├── static/
   ├── templates/
   ├── uploads/
   ├── app.py
   ├── monument_model.h5
   ├── updated_model.h5
   ```
   - The `static` folder should contain static assets (CSS, JS, images).
   - The `templates` folder should contain HTML templates.
   - The `uploads` folder will store uploaded images.

8. Run the application
   ```sh
   python app.py
   ```

## Usage

To use the application, follow these steps:

1. Run the application:
  
2. Open your web browser and navigate to `http://127.0.0.1:5000`.

Upload an image of an Indian monument and explore the information provided by CulturalLensAI.

## Features

- 📍 Locate Indian monuments from an image
- 🌐 Access multi-lingual information about the monument
- 🏛️ Discover nearby monuments
- 🔍 Use Leaflet for interactive maps

## Demo

- Interface
![image](https://github.com/KrishV9055/CulturalLensAI/assets/152723874/59a67550-9581-4a70-82f1-ee594820ff04)
- After the image input
![image](https://github.com/KrishV9055/CulturalLensAI/assets/152723874/21a0b551-b642-49d6-9532-8fdf85f3c14a)
![image](https://github.com/KrishV9055/CulturalLensAI/assets/152723874/2caca097-1627-47e8-959c-96c0a23d9af2)







