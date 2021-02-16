import openslide
from openslide import *
from openslide.deepzoom import DeepZoomGenerator
import requests
from PIL import Image
from io import BytesIO
from django.core.files import File
import os


image_file = openslide.OpenSlide(svs_path)
image_dims = image_file.dimensions
thumb_dims = tuple( (600, 600) )
thumb_file = image_file.get_thumbnail(thumb_dims)
thumb_file.save("test_thumbnail.png", "png")