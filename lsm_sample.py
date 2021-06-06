#!/usr/bin/env python3

from pydicom import dcmread

ds = dcmread('dataset/lsm.dcm')

print()
print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
print()

print(f"Patient ID........: {ds.PatientID}")
print(f"Modality..........: {ds.Modality}")
print(f"Study Date........: {ds.StudyDate}")
print(f"Image size........: {ds.Rows} x {ds.Columns}")
print(f"Pixel Spacing.....: {ds.SamplesPerPixel}")
print(f"TransferSyntaxUID.: {ds.file_meta.TransferSyntaxUID} ({ds.file_meta.TransferSyntaxUID.name})")

print(f"Pixel Array......: {ds.pixel_array}")
arr = ds.pixel_array

# Sample Pre-processing sample, in raw bits  
arr[arr < 10] = 255
ds.PixelData = arr.tobytes()
ds.save_as("dataset/sample_dicom_output_lsm.dcm")