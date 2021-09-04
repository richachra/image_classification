import urllib.request
from pycocotools.coco import COCO
import os
import numpy as np
import cv2 as cv

#dataDir = #eg-r'C:\Users\nikhil\Desktop\Richa-Docs\579-Intelligent system\PRJ\coco\annotations'
classes = ['street']#['stop sign', 'bus','car','person','traffic light']
#parent_dir = r"C:\Users\nikhil\Desktop\Richa-Docs\579-Intelligent system\PRJ\coco-dataset"
#img_dir = #eg- r'C:\Users\nikhil\Desktop\Richa-Docs\579-Intelligent system\PRJ\coco\images\train2017\train2017'


def img_fromurl(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)  # 'Load it as it is'
    return img

def annotate_crop(class_cat, images, coco,arg):
    # print(class_cat,parent_dir)
    path = os.path.join(arg.parent_loc, class_cat)

    if not os.path.isdir(path):
        os.mkdir(path)
    for i in images:
        catIds = coco.getCatIds(catNms=class_cat)
        annIds = coco.getAnnIds(imgIds=i['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        im = os.path.join(arg.train_data, i['file_name'])
        src_image = cv.imread(im)
        if src_image is None:
            src_image = img_fromurl(i['coco_url'])
        for ind, ann in enumerate(anns):
            bound_box = ann['bbox']
            y1 = int(bound_box[1])
            y2 = int(bound_box[1] + bound_box[3])
            x1 = int(bound_box[0])
            x2 = int(bound_box[0] + bound_box[2])
            # print(x1,x2,y1,y2)
            crop_image = src_image[y1:y2, x1:x2]
            if crop_image is not None:
                # dst_img = cv.resize(src=crop_image, dsize=(img_height, img_width))
                new_img = i['file_name'].split('.')[0] + '_' + str(ind) + '.jpg'
                dst_path = os.path.join(path, new_img)
                cv.imwrite(dst_path, crop_image)

def filter_dataset(arg, mode: str):

    # Annotation file
    annFile = arg.annotation_data + '/instances_{}2017.json'.format(mode)
    coco = COCO(annFile)

    for cl in classes:
        print(cl)
        images = []
        catIds = coco.getCatIds(catNms=cl)
        imgIds = coco.getImgIds(catIds=catIds)
        print(imgIds, catIds, cl)
        # quit()
        images += coco.loadImgs(imgIds)
        annotate_crop(cl, images, coco,arg)

def coco_download(arg):
    filter_dataset( arg,mode='train')