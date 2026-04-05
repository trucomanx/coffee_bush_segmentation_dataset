#!/bin/bash

RAW_TRAIN_VAL="0-raw/train-val"
PRE_TRAIN_VAL="1-preprocessed/train-val/images_delete"

python3 ../src/prog_tiff2bmp.py \
  --input-dir $RAW_TRAIN_VAL \
  --output-dir $PRE_TRAIN_VAL \
  --names 'Red.bmp' 'Green.bmp' 'Blue.bmp' 'Nir.bmp' 'RedEdge.bmp'
