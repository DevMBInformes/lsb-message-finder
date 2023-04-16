# Script for LSB Method to Find Hidden Messages in RGBA Images

This Python script uses the Least Significant Bit (LSB) method to find hidden messages in RGBA images. If the image is RGB, the value of n should be 3.
Requirements

   * Python 3.x
   * numpy
   * PIL (Python Imaging Library)

## Usage

    - Clone this repository: git clone https://github.com/DevMBInformes/lsb-message-finder.git
    - Install the required packages: pip install numpy pillow
    - Navigate to the cloned repository: cd lsb-message-finder
    - Run the script: python mehod_lsb.py
    - Enter the path and name of the image when prompted. Example: path/to/image.png

## How it works

The script converts the image to a numpy array and iterates through each pixel. It then collects the least significant bit (LSB) from the red, green, blue, and alpha channels of each pixel and concatenates them into a string. This string is then divided into 8-bit chunks, converted from binary to decimal, and then to ASCII characters to form the hidden message.


