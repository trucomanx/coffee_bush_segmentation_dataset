#!/bin/bash

python3 ../src/prog_tiff2bmp.py \
  --input-dir "0-raw/train-val" \
  --output-dir "1-preprocessed/train-val/images_delete" \
  --names 'Red.bmp' 'Green.bmp' 'Blue.bmp' 'Nir.bmp' 'RedEdge.bmp'
