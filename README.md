Solution in Theory

The general approximation of the solution can be expressed in following steps:
 First the contour points and the center point of each polygon are located.
 Next for each polygon, the distance (radius) and the angle of each contour point relative to the center is obtained.
 Distances from center of the shape to the contour points are stored and sorted with respect to angles they make with the x axis. The distances are stored in array with their ascending angle order from (pi) to (- pi) like d1, d2, d3, d4 ...
 This array actually represents a distribution of distance measures over ascending angles from (- pi) to (pi). Distance will increase as we move towards the vertices of the polygon and decreases as we move towards middle of the polygon's edges. Becasue the resulted distributions are already sinosoidal waves with the frequency equal to the number of polygon edges, lets say n, thus applying a Discrete Fourier Transform (DFT) to distribution will result in a fourier expression with the biggest coefficient in its n'th term. Therefore the greatest coefficient's term index will represent the polygon's number of edges. 
 
 
 
 Explanation of Control-Flow

This section describes the control-flow of the code by describing the functions in order of execution: There are two seperate code files, first one is "main.py" which is responsible for assigning different colors to different class of polygons and saving the final painted image. Besides these tasks it calls the "main()" function in the other code file, "dft.py", which is the main code snippet doing the most of the job. this section is set to describe the code in the order of execution:

    main(im):
        Gets polygon contours of the polygons.
        Saves the contours as the connected components with attributes:
            label
            centroid
        For each polygon contour:
            takes the centroid.
            Saves the radius of all contour (boundary) points relative to centroid.
            Saves the angle of all contour (boundary) points relative to centroid.
            IF the variation in radius of contour points are negligible then decides the shape as "Circle"
            (NOTE) Circle is checked and now starts to check the other polygons.
            Sorts the radius values with respect to their contour end-point's ascending angle from center.
            This array of sorted radius values are fed to the Real Fast Fourier Transform (rfft) to extract final transformation's terms.
            These terms in complex form are converted from rectangular coordinate to the polar ccoordinate and saved as weights or coefficient values.
            The index of maximum coefficient is extracted and assigned to the value, "n".
            Based on the value of "n", the current polygon under investigation is decided to be classified as a n-edged polygon.


Execution Instructions

    REQUIRES PYTHON>=3.9

    Please extract the package.

    Run make in the directory containing this file to setup a virtual environment and install the module in it.

    Run make activate to activate the environment.

    Inside the environment, run python -m dft my_image.bmp to process an image (avoid using .jpg images, prefer bmp or png). The output will be saved at ./output.bmp.
