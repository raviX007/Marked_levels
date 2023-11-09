import cv2
import numpy as np

def _preprocess_image(image):
    """Preprocess the input image by converting it to grayscale and detecting edges."""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=30, threshold2=100)

    return edges

def _extract_marked_points(image, edges):
    """Extract the marked points on the stock chart image."""

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    marked_points = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                
                if 0 < cx < image.shape[1] and 0 < cy < image.shape[0]:
                    marked_points.append((cx, cy))

    return marked_points

def extract_marked_levels(image):
    """Extract the marked levels on the stock chart image.

    Args:
        image: A NumPy array representing the stock chart image.

    Returns:
        A list of tuples, with each tuple containing the x and y coordinates of a marked level.
    """

    edges = _preprocess_image(image)
    marked_points = _extract_marked_points(image, edges)

    
    marked_points.sort(key=lambda point: point[1])

    
    marked_levels = []
    for i in range(len(marked_points)):
        if i == 0 or marked_points[i][1] - marked_points[i - 1][1] > 10:
            marked_levels.append([])
        marked_levels[-1].append(marked_points[i])

    
    return marked_levels

def main():
    """Extract the marked levels from the input stock chart images."""

    
    image_1 = cv2.imread("./images/AssignmentImage-1.png")
    image_2 = cv2.imread("./images/AssignmentImage-2.png")

    
    marked_levels_1 = extract_marked_levels(image_1)
    marked_levels_2 = extract_marked_levels(image_2)

    
    print("Marked levels in AssignmentImage-1.png:")
    for level in marked_levels_1:
        for point in level:
            print(point)

    print("Marked levels in AssignmentImage-2.png:")
    for level in marked_levels_2:
        for point in level:
            print(point)

if __name__ == "__main__":
    main()
