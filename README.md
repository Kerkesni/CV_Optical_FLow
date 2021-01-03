# CV_Optical_FLow
This Project contains implementations of optical flow algorithms.

## Variations Implemented
1. Dense Optical Flow (Farnebäck - Gunnar method)
2. Lucas-Kanade Sparce Optical flow

## Requirements to run
- [Python](https://www.python.org/downloads/)
- [OpenCV](https://pypi.org/project/opencv-python/)

## Results

### Dense Optical Flow (Vector Visualization)
![Fully Dense](./results/fully_dense.gif)

### Dense Optical Flow (Blob Visualization)
![partially Dense](./results/partial_dense..gif)

**Note** : *Bolob Colors represent direction of the optical flow vectors*

### Lucas-Kanade Sparce Optical Flow
![Sparce](results/sparce.gif)

## References
- Lucas, Bruce D., and Takeo Kanade. "An iterative image registration technique with an application to stereo vision." (1981): 674.
- Farnebäck, Gunnar. "Two-frame motion estimation based on polynomial expansion." Scandinavian conference on Image analysis. Springer, Berlin, Heidelberg, 2003.
