# Marked_levels
This Python application analyzes stock chart images and extracts marked levels, representing significant points such as highs, lows, support, resistance, or any other annotations.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functionalities](#functionalities)

## Requirements
- Python 3.x
- OpenCV
- Pillow (PIL)


Install the required libraries using:

```bash
pip install opencv-python-headless pillow pytesseract
```

## Installation
1. Clone the repository:

```bash
git clone https://github.com/ravix007/Marked_levels.git
cd Marked_levels
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the main script:

```bash
python main.py
```

This will analyze the stock chart images provided in the "AssignmentImage-1.png" and "AssignmentImage-2.png" files and print the extracted marked levels.


## Functionalities
The main functionality of the application is in the `main.py` file. The code is structured as follows:

- `_preprocess_image`: Preprocesses the input image by converting it to grayscale and detecting edges.
- `_extract_marked_points`: Extracts the marked points on the stock chart image using contours.
- `extract_marked_levels`: Extracts the marked levels from the stock chart image by ordering and grouping the marked points.

### Example Usage:

```python
import cv2


image = cv2.imread("AssignmentImage-1.png")


marked_levels = extract_marked_levels(image)

for level in marked_levels:
    for point in level:
        print(point)
```

