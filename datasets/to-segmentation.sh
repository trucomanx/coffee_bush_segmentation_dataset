#!/bin/bash


PRE_TRAINVAL_DIR="1-preprocessed/train-val"
SEG_TRAINVAL_DIR="2-segmentation/train-val"

python3 ../src/prog_bmp2npy.py \
  --input-base-dir $PRE_TRAINVAL_DIR \
  --output-base-dir ../output/train \
  --image-names "Red.bmp" "Green.bmp" "Blue.bmp" "Nir.bmp" "RedEdge.bmp" \
  --label-names "bushes.bmp" "map.bmp" \
  --images-dname "images" \
  --labels-dname "labels" \
  --height 128 \
  --width 128 \
  --step 16
