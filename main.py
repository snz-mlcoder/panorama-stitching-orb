from stitcher import stitch_images
import cv2

# Load input images
img1 = cv2.imread('images/left.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/right.jpg', cv2.IMREAD_COLOR)

# Stitch images
result = stitch_images(img1, img2)

# Show and save result
cv2.imshow("Panorama", result)
cv2.imwrite("panorama_output.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
