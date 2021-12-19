import sys
import cv2
from matplotlib import pyplot as plt
from matplotlib import colors
from . import dft

file_name = sys.argv[1]
im = cv2.imread(file_name)

output_image = dft.main(im)


cmap = colors.ListedColormap(
    ["black", "limegreen", "white", "yellow", "steelblue", "magenta", "orangered"]
)
plt.imsave("output.bmp", output_image, cmap=cmap)
print("output.bmp is saved at ./")
