#!/usr/bin/env python3

from pydicom import dcmread
from pydicom.encaps import generate_pixel_data_frame

import numpy as np
import PIL
from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

ds = dcmread('dataset/wsi_small.dcm')
#ds = dcmread('dataset/1059_8.dcm')

print()
print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
print()

pat_name = ds.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print(f"Patient's Name....: {display_name}")
print(f"Patient ID........: {ds.PatientID}")
print(f"Modality..........: {ds.Modality}")
print(f"Study Date........: {ds.StudyDate}")
print(f"Image size........: {ds.Rows} x {ds.Columns}")
print(f"Pixel Spacing.....: {ds.SamplesPerPixel}")
print(f"Number of Frame...: {ds.NumberOfFrames}")

print(f"TransferSyntaxUID.: {ds.file_meta.TransferSyntaxUID} ({ds.file_meta.TransferSyntaxUID.name})")

raw_bytes = ds.PixelData

frame_generator = generate_pixel_data_frame(ds.PixelData, ds.NumberOfFrames)

for i in range(0, ds.NumberOfFrames):
    frame = next(frame_generator)
    f = open('dataset/jpeg/f'+str(i)+'.jpg', 'wb')
    f.write(frame)
    f.close()


list_im = ['dataset/jpeg/f20.jpg', 'dataset/jpeg/f21.jpg', 'dataset/jpeg/f22.jpg']
imgs    = [ PIL.Image.open(i) for i in list_im ]

min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb = imgs_comb.filter(FIND_EDGES)

imgs_comb.save( 'dataset/Merged_Image_WSI.jpg' )    

