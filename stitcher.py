import cv2
import numpy as np

def stitch_images(img1, img2, min_match_count=10):
    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    # Use BFMatcher with Hamming distance
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    # Sort matches by distance (best matches first)
    matches = sorted(matches, key=lambda x: x.distance)

    if len(matches) > min_match_count:
        # Extract location of good matches
        src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # Compute Homography
        M, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

        # Warp img2 to img1 using Homography
        result = warp_images(img1, img2, M)
        return result
    else:
        print(f"Not enough matches are found - {len(matches)}/{min_match_count}")
        return img1

def warp_images(img1, img2, H):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    # Corners of the second image
    points_img2 = np.float32([[0,0], [0,h2], [w2,h2], [w2,0]]).reshape(-1,1,2)
    points_img2_transformed = cv2.perspectiveTransform(points_img2, H)

    # Corners of the first image
    points_img1 = np.float32([[0,0], [0,h1], [w1,h1], [w1,0]]).reshape(-1,1,2)

    # Combine all points to get final canvas size
    all_points = np.concatenate((points_img1, points_img2_transformed), axis=0)
    [xmin, ymin] = np.int32(all_points.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(all_points.max(axis=0).ravel() + 0.5)

    translation_dist = [-xmin, -ymin]
    H_translation = np.array([[1, 0, translation_dist[0]],
                              [0, 1, translation_dist[1]],
                              [0, 0, 1]])

    output_img = cv2.warpPerspective(img2, H_translation.dot(H), (xmax - xmin, ymax - ymin))
    output_img[translation_dist[1]:h1+translation_dist[1], translation_dist[0]:w1+translation_dist[0]] = img1

    return output_img
