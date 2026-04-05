#!/bin/bash

RAW_TRAINVAL="0-raw/train-val"
PRE_TRAINVAL="1-preprocessed/train-val/images"

python3 ../src/prog_tiff2bmp.py \
  --input-dir $RAW_TRAINVAL \
  --output-dir $PRE_TRAINVAL \
  --names 'Red.bmp' 'Green.bmp' 'Blue.bmp' 'Nir.bmp' 'RedEdge.bmp'


RAW_TEST="0-raw/test"
PRE_TEST="1-preprocessed/test/images"

python3 ../src/prog_tiff2bmp.py \
  --input-dir $RAW_TEST \
  --output-dir $PRE_TEST \
  --names 'Red.bmp' 'Green.bmp' 'Blue.bmp' 'Nir.bmp' 'RedEdge.bmp'

