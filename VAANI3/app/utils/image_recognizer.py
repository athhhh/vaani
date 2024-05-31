import cv2

def image_recognition(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Perform image recognition using OpenCV or other libraries
    # ...

    # Return the description
    description = 'This is a sample image description.'
    return description