from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2


ap = argparse.ArgumentParser()

image = cv2.imread("../photo/carie.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis("off")
plt.imshow(image)

image = image.reshape((image.shape[0]*image.shape[1], 3))

clt = KMeans(n_clusters=20)
clt.fit(image)
# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)

# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()