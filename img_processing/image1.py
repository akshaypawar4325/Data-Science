from skimage import data
camera=data.camera()
print("Type of the camera",type(camera))
print("Shape of the camera",camera.shape)
print("size of the camera",camera.size)
print("Minimus value in camera",camera.min())
print("Maximum value in camera",camera.max())
print("Minimum value of the camera",camera.mean())
