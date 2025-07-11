import cv2 as cv
import numpy as np

# -------------------------- Part 1 --------------------------------

image  = cv.imread('Einstein.jpg')
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()


def reduce(I: np.ndarray = image):
    (width, height) = I.shape[0:2]
    center_coords = (int(height) // 2 , int(width) //2)
    I = np.array(I)
    blurred_image = cv.GaussianBlur(I, (7,7), 0)

    reduced_image = np.array(cv.resize(blurred_image, center_coords, interpolation=cv.INTER_AREA))
    return reduced_image



def expand(I: np.ndarray = image):
    (width, height) = I.shape[0:2]
    doubled_size = (int(height) * 2 , int(width) * 2)

    expanded_image = np.array(cv.resize(I, doubled_size, interpolation=cv.INTER_LINEAR))
    return expanded_image


# ---------------------- PART 1 -----------------------------
def multiResolutionPyramid(I: np.ndarray = image, n: int = 4):
    I = np.array(I)

    pyramid = [None] * n
    pyramid[0] = I

    for i in range(1,n):
        downsized_image = reduce(pyramid[i-1])
        pyramid[i] = downsized_image

    return pyramid



for i, level_image in enumerate(multiResolutionPyramid(image)):
    cv.imshow(f'Level {i}', level_image)

cv.waitKey(0)
cv.destroyAllWindows()


# ---------------------- PART 2 -----------------------------
def multiScalePyramid(I: np.ndarray = image, n: int = 4):
    I = np.array(I)

    pyramid = [None] * n
    pyramid[0] = I
    blurred_image = cv.GaussianBlur(I, (7,7), 0)
    pyramid[1] = blurred_image
    for i in range(1,n):
        blurred_image = cv.GaussianBlur(blurred_image, (7,7), 0)
        pyramid[i] = blurred_image

    return pyramid

for i, level_image in enumerate(multiScalePyramid(image)):
    cv.imshow(f'Level {i}', level_image)

cv.waitKey(0)
cv.destroyAllWindows()


# ---------------------- PART 3 -----------------------------
def LaplacePyramid(I:np.ndarray = multiResolutionPyramid, n: int = 4):
    laplacian_pyramid = []
    
    for i in range(1, n + 1):
        laplacian_image = cv.Laplacian(I,-1)
        j = i-1
        while j > 0:
            laplacian_image = cv.Laplacian(laplacian_image,-1)
            j = j-1
        laplacian_pyramid.append(laplacian_image)

    return laplacian_pyramid


for i, level_image in enumerate(LaplacePyramid(image)):
    cv.imshow(f'Level {i}', level_image)

cv.waitKey(0)
cv.destroyAllWindows()



# ---------------------- PART 4 -----------------------------
def laplacianApproximation_res(I:np.ndarray, n: int = 4):

    gaussian_pyramid_images = multiResolutionPyramid(I, n)

    laplacian_layers = []

    resize_width = I.shape[0]
    resize_height = I.shape[1]

    for i in range(0, n-1):

        resize_width = gaussian_pyramid_images[i].shape[0]
        resize_height = gaussian_pyramid_images[i].shape[1]

        laplacian_image = gaussian_pyramid_images[i] - cv.resize(gaussian_pyramid_images[i + 1], (resize_height, resize_width))

        laplacian_layers.append(laplacian_image)

    return laplacian_layers


for i, level_image in enumerate(laplacianApproximation_res(image)):
    cv.imshow(f'Level {i}', level_image)

cv.waitKey(0)
cv.destroyAllWindows()



# ---------------------- PART 5 -----------------------------
def laplacianApproximation(I:np.ndarray, n: int = 4):

    gaussian_pyramid_images = multiScalePyramid(I, n)

    laplacian_layers = []
    for i in range(0, n-1):

        laplacian_image = gaussian_pyramid_images[i] - gaussian_pyramid_images[i + 1]

        laplacian_layers.append(laplacian_image)


    return laplacian_layers


for i, level_image in enumerate(laplacianApproximation(image)):
    cv.imshow(f'Level {i}', level_image)

cv.waitKey(0)
cv.destroyAllWindows()


    
