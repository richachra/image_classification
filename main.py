import argparse
import coco_data_download


def main(arg) -> None:
    if arg.download_data:
        coco_data_download.coco_download()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--download_data", help="download data from coco")
    args = parser.parse_args()

    main(args)
