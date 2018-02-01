import glob, os
from keras.preprocessing.image import ImageDataGenerator
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True, help="path to the image folder for augmentation")
ap.add_argument("-c", "--counts", required=True, help="how many you want to create for an image.")
ap.add_argument("-o", "--output", required=True, help="path for the output images.")
args = vars(ap.parse_args())

datagen = ImageDataGenerator(
    rotation_range=35,
    width_shift_range=0.15,
    height_shift_range=0.15,
    shear_range=0.15,
    zoom_range=0.25,
    horizontal_flip=True,
    vertical_flip = True,
    fill_mode="nearest")


for file in os.listdir(args["folder"]):
    filename, file_extension = os.path.splitext(file)
    print(filename, file_extension)
    filecount = 0

    if(file_extension==".jpg" or file_extension==".png"):
        i = 0
        print("process ...#{} {}".format(i, filename))
        img = cv2.imread(args["folder"]+"/"+file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # (samples counts, channels, height, width)
        img = img.reshape((1,) + img.shape)
        for batch in datagen.flow(img, batch_size=1, save_to_dir=args["output"], \
                save_prefix=filename+"_"+str(i), save_format="jpg"):
            i += 1
            print("counts:{}  i:{}  True:{}".format(args["counts"], i , i>int(args["counts"])))

            if(i>int(args["counts"])):
                print("------------------------->")
                break

        filecount += 1
