# Multi-Scale Image Processing with Gaussian and Laplacian Filters

This project implements a multi-resolution and multi-scale image analysis pipeline using Gaussian, Laplacian, and Laplacian of Gaussian (LoG) filtering techniques in Python with OpenCV.

## Features

- **Image Reduction & Expansion**  
  Functions to downsample and upsample images using Gaussian blurring and interpolation.

- **Multi-Resolution Pyramid**  
  Constructs an image pyramid by iteratively applying Gaussian blur and downsampling. Useful for analyzing features at different spatial resolutions.

- **Multi-Scale Pyramid**  
  Applies Gaussian blur multiple times without changing image size to simulate scale-space representation.

- **Laplacian Filtering**  
  Highlights edges and fine details by applying the Laplacian operator across different scales.

- **Laplacian Approximation**  
  Two methods:
  - **Resolution-based**: Difference between successive downsampled images.
  - **Scale-based**: Difference between successive blurred images at constant resolution.

## Dependencies

- Python 3.x  
- OpenCV  
- NumPy

```bash
pip install opencv-python numpy
