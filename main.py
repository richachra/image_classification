import argparse
import coco_data_download


def main(arg) -> None:
    if arg.download_data:
        coco_data_download.coco_download(arg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--download_data", help="download data from coco")
    parser.add_argument("--train_data",help="save location for train data from coco")
    parser.add_argument("--annotation_data", help="location to extract annotation file from your machine")
    parser.add_argument("--parent_loc", help="Nahi pata")
    args = parser.parse_args()

    main(args)

#--download_data True --annotation_data C:\Users\nikhil\Desktop\Richa-Docs\579-Intelligent system\PRJ\coco\annotations --train_data C:\Users\nikhil\Desktop\Richa-Docs\579-Intelligent system\PRJ\coco\annotations --parent_loc C:\Users\nikhil\Desktop\Richa-Docs\579-Intelligent system\PRJ\coco-dataset
