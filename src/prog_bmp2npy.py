#!/usr/bin/env python3

import os
import extras
import pandas as pd
import argparse
from tqdm import tqdm

def generate_dataset(   input_base_dir,
                        output_base_dir,
                        image_names,
                        label_names,
                        images_dname,
                        labels_dname,
                        height,
                        width,
                        step
                    ):
    input_images_dir = os.path.join(input_base_dir, images_dname)
    input_labels_dir = os.path.join(input_base_dir, labels_dname)

    for i, dname in enumerate(tqdm(os.listdir(input_images_dir), desc="Processing TIFFs")):
        frel_img_list, frel_lbl_list = extras.generate(
            output_base_dir,
            input_images_dir,
            input_labels_dir,
            dname,
            image_names,
            label_names,
            images_dname,
            labels_dname,
            separate=True,
            height=height,
            width=width,
            step=step
        )
        
        if i == 0:
            dataframes = []
            N = len(frel_lbl_list)
            
            for n in range(N):
                df = pd.DataFrame({'images': frel_img_list, 'labels': frel_lbl_list[n]})
                dataframes.append([df])

        else:
            for n in range(N):
                df = pd.DataFrame({'images': frel_img_list, 'labels': frel_lbl_list[n]})
                dataframes[n].append(df)

    for n in range(N):
        df = pd.concat(dataframes[n], ignore_index=True)
        base, ext = os.path.splitext(label_names[n])
        df.to_csv(os.path.join(output_base_dir, base + '.csv'), index=False)


def main():
    parser = argparse.ArgumentParser(description="Generate dataset from preprocessed images")

    parser.add_argument("--input-base-dir", required=True)
    parser.add_argument("--output-base-dir", required=True)

    parser.add_argument(
        "--image-names",
        nargs="+",
        default=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp']
    )

    parser.add_argument(
        "--label-names",
        nargs="+",
        default=['bushes.bmp','map.bmp']
    )

    parser.add_argument("--images-dname", default="images")
    parser.add_argument("--labels-dname", default="labels")

    parser.add_argument("--height", type=int, default=128)
    parser.add_argument("--width", type=int, default=128)
    parser.add_argument("--step", type=int, default=16)

    args = parser.parse_args()

    generate_dataset(
        input_base_dir=args.input_base_dir,
        output_base_dir=args.output_base_dir,
        image_names=args.image_names,
        label_names=args.label_names,
        images_dname=args.images_dname,
        labels_dname=args.labels_dname,
        height=args.height,
        width=args.width,
        step=args.step
    )


if __name__ == "__main__":
    main()


'''
generate_dataset(   input_base_dir='../input/1-preprocessed/train',
                    output_base_dir='../output/train',
                    image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp'],
                    label_names=['bushes.bmp','map.bmp'],
                    images_dname='images',
                    labels_dname='labels',
                    height=128,
                    width=128,
                    step=16
                    )
'''


'''
python3 ../src/prog_bmp2npy.py \
  --input-base-dir ../input/1-preprocessed/train \
  --output-base-dir ../output/train \
  --image-names Red.bmp Green.bmp Blue.bmp Nir.bmp RedEdge.bmp \
  --label-names bushes.bmp map.bmp \
  --images-dname images \
  --labels-dname labels \
  --height 128 \
  --width 128 \
  --step 16
'''
