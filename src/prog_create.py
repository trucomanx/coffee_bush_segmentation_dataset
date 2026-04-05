#!/usr/bin/python

import os
import extras
import pandas as pd

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
    input_images_dir=os.path.join(input_base_dir,images_dname)
    input_labels_dir=os.path.join(input_base_dir,labels_dname)


    for i, dname in enumerate(os.listdir(input_images_dir)):
        frel_img_list,frel_lbl_list = extras.generate(  output_base_dir,
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
                                                        );
        
        if i==0:
            dataframes = [];
            N=len(frel_lbl_list);
            
            for n in range(N):
                df=pd.DataFrame({'images': frel_img_list, 'labels': frel_lbl_list[n]});
                dataframes.append([df])

        else:
            for n in range(N):
                df=pd.DataFrame({'images': frel_img_list, 'labels': frel_lbl_list[n]});
                dataframes[n].append(df);

    for n in range(N):
        df = pd.concat(dataframes[n], ignore_index=True)
        base,ext = os.path.splitext(label_names[n]);
        df.to_csv(os.path.join(output_base_dir,base+'.csv'), index=False)



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
