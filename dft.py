from collections import Counter
import time
import cmath
import cv2
import numpy as np


def get_contours(arr):
    inner_mat: np.ndarray = arr[1:-1, 1:-1]
    borders_ = np.zeros_like(inner_mat)
    borders = arr.copy()
    trimmed_bottom, trimmed_top, trimmed_left, trimmed_right = (
        arr[:-2, 1:-1],
        arr[2:, 1:-1],
        arr[1:-1, 0:-2],
        arr[1:-1, 2:],
    )
    for trimmed_array in (trimmed_bottom, trimmed_top, trimmed_left, trimmed_right):
        borders_ += (inner_mat == 1) * (trimmed_array == 0)

    borders[1:-1, 1:-1] = (borders_.astype(np.bool8)).astype(np.int8)
    return borders


def main(im):
    mat: np.ndarray = (im[:, :, 0] == 255).astype(np.int8)

    borders = get_contours(mat)
    comps = cv2.connectedComponentsWithStats(borders, 8, cv2.CV_32S)
    comps_2 = cv2.connectedComponentsWithStats(mat, 8, cv2.CV_32S)

    numLabels, labels, stats, centroids = comps
    numLabels_, labels_, stats_, centroids_ = comps_2

    # 0th term is the center of the all clusters
    # we ignore it

    # centroids of mat is better than that of contours

    started_at = time.perf_counter()
    results: list[int] = []
    output_image = np.zeros_like(labels_).astype(np.uint8)

    for L in range(1, numLabels):

        p_center = centroids[L]  # center of the Lth detected shape
        mask = labels == L

        boundary_points = np.transpose(
            mask.nonzero()
        )  # array([[391, 668], [391, 669],...])

        # We need distance of each point from the center as well as that point's angle.
        # But first, let's move them about the origin by moving the center to the origin
        boundary_points = boundary_points - p_center[::-1]
        boundary_points = boundary_points.T[0] + boundary_points.T[1] * 1j

        R = np.abs(boundary_points)
        O = np.angle(boundary_points)  # phase, ie theta. Values range from -pi to pi

        if max(R) - min(R) < 2:
            # circles have minimal variance in R
            output_image += (labels_ == L).astype(np.uint8)
            results.append(1)
            continue

        # Sort distances wrt theta values
        phase_indices = O.argsort()
        sorted_R = R[phase_indices]

        rfft_terms = np.fft.rfft(sorted_R)
        rfft_terms[:3] = 0
        # if we have a polygon with n-edges, rfft_terms[n] should have the largest magnitude

        rfft_weigths = [cmath.polar(z)[0] for z in rfft_terms[:10]]
        n = rfft_weigths.index(max(rfft_weigths))

        output_image += (labels_ == L).astype(np.uint8) * (n)
        results.append(n)

    print(Counter(results))
    print("elapsed: " + str(time.perf_counter() - started_at))
    return output_image