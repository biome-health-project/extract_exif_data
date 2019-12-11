import PIL.Image
import PIL.ExifTags
import os
import sys
import pandas as pd

df = pd.read_csv("nepal_original_filepaths_working_filepaths.csv")
#allfiles = df.new_file_structure
allfiles = df.filepath

#Change this to the location where you want the text file with the exif data to go
sys.stdout = open(os.path.join('D:/Fiona/Biome_Health_Project/exif_output/nepal_exif_out.txt'), "w")

# Pick out which exif data you're interested in
keys = ['Make', 'Model', 'DateTime','DateTimeDigitized','LightSource', 'Flash']

###saves filepath rather than information extracted from it####

for image in allfiles:
  try:
    img = PIL.Image.open(image)
  except OSError as e:
    print('Bad file ' + image)   #If a file is corrupt we are unable to get exif data from it, in this case it will print "Bad file" in the output
  exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
  }
  keys_out = [str(exif.get(key)) for key in keys]
  filepath = str(image)
  print(filepath + ', ' + ', '.join(keys_out)) 
