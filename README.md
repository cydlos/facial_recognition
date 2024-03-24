# Face Match App

## Overview

This Face Match App is a Python application that utilizes the `face_recognition` library to compare faces between two images. It detects all faces present in each image, extracts their features, and then compares these features to find matches. The app can identify if a person in the first image appears in the second image, making it useful for various applications such as verifying identities or finding similar faces in different photos.

## Requirements

- Python 3.6 or higher
- `face_recognition` library

## Installation

First, you need to install the `face_recognition` library. This can be done by running the following command in your terminal:

## Usage

1. Place the images you want to compare in a known directory.
2. Edit the script to update the paths to your images accordingly:

```python
imagem1 = face_recognition.load_image_file("path_to_your_first_image.jpg")
imagem2 = face_recognition.load_image_file("path_to_your_second_image.jpg")


```
