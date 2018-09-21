import sys
import argparse
import cv2,glob
import numpy as np
from PIL import Image, ImageFont, ImageDraw
if __name__ == '__main__':

    try:

        annotation_path = 'train.txt'
        parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
        '''
        Command line options
        '''
        parser.add_argument(
            '--annotation', type=str,
            help='path to annotation file, default train.txt'
        )
        FLAGS = parser.parse_args()

        if "annotation" in FLAGS:
            annotation_path = FLAGS.annotation


        with open(annotation_path) as f:
            lines = f.readlines()
        for line in lines:
            data = line.split()
            image = Image.open(data[0])
            box = np.array([np.array(list(map(int,box.split(',')))) for box in data[1:]])

            draw = ImageDraw.Draw(image)
            for b in box:
                print(b)
                left,top,right,bottom,class_id = list(b)
                print(left)
                draw.rectangle([left,top,right,bottom])

            image = np.asarray(image)
            #PILはBGR,cv2はRGBで、色がおかしくなるので修正
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imshow("result", image)
            key = cv2.waitKey(0)
            # ESCで終了
            if key==27:
                print("exit")
                cv2.destroyAllWindows()
                break
    except KeyboardInterrupt:
        print("exit")
