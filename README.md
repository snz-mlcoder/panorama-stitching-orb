# Panorama Stitching with OpenCV and ORB

This project demonstrates how to stitch two images together to create a seamless panorama using Python and OpenCV.

We use the ORB (Oriented FAST and Rotated BRIEF) algorithm to detect and describe keypoints, and then align the images using a homography matrix.

---

## ✨ Features

- Uses ORB for fast and license-free keypoint detection and description  
- Employs Brute-Force Matcher with Hamming distance for descriptor matching  
- Applies RANSAC-based homography estimation  
- Handles image alignment with perspective warping  
- Works with images that have slight perspective changes  

---

## 📁 Folder Structure

```
panorama-stitching-orb/
├── images/
│   ├── left.jpg         # First input image
│   └── right.jpg        # Second input image
├── main.py              # Entry point to the script
├── stitcher.py          # Core stitching logic
├── requirements.txt     # Required Python packages
└── README.md            # This file
```

---

## 🚀 How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt

Run the script

python main.py

Notes
ORB is chosen over SIFT/SURF due to its open-source, license-free nature.

You can adjust the min_match_count parameter in stitcher.py for stricter matching.


Example Output
<p align="center"> <img src="panorama_output.jpg" alt="Panorama Output" width="600"/> </p>
