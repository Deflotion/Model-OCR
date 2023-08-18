
pelat-mobil-indonesia - v3 2023-07-20 1:06pm
==============================

This dataset was exported via roboflow.com on August 15, 2023 at 3:04 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2465 images.
Plate are annotated in Tensorflow Object Detection format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -10 and +10 degrees
* Random brigthness adjustment of between -50 and +50 percent
* Random Gaussian blur of between 0 and 2.5 pixels
* Salt and pepper noise was applied to 10 percent of pixels


