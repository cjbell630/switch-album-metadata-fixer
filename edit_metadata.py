import argparse, os, json
from pathlib import Path
from common import dir_path, extract_game_uuid_from_filename
from datetime import datetime
import pytz
import PIL.Image
import PIL.ExifTags
import mutagen

UUID_NAMES = {}
TIMEZONE = pytz.timezone("UTC")


def load_name_json(path: str):
    global UUID_NAMES
    with open(path, "r") as file:
        UUID_NAMES = json.load(file)


def process_args():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "album_path",
        help="The path to the directory containing all of the photos and videos",
        type=dir_path
    )
    parser.add_argument(
        "data",
        help="The path to the json file containing game names for UUIDs"
    )
    parser.add_argument(
        "-t", "--timezone",
        default="UTC",
        required=False,
        help="Assume images were taken in this timezone."
    )
    return parser.parse_args()


def get_time_from_filename(filename: str) -> datetime:
    """
    Creates a datetime from the timestamp in the provided filename.
    Datetime is tz aware to the timezone provided when running the script

    :param filename: the filename to parse
    :return: timestamp as tz aware datetime
    """
    time_string = filename.split("-")[0]
    cleaned_time_string = time_string[0:-2]
    return TIMEZONE.localize(datetime.strptime(cleaned_time_string, "%Y%m%d%H%M%S"))


def get_game_name_from_filename(filename: str) -> str:
    """
    Extracts the UUID from the provided filename and returns the associated game name
    Pre: the json data is loaded into UUID_NAMES
    :param filename: the filename to extract from
    :return: the game name associated with that file
    """
    uuid = extract_game_uuid_from_filename(filename)
    return UUID_NAMES[uuid]


def format_time(time: datetime) -> str:
    """
    Format time according to EXIF standard:
    https://www.imagekit.com/IK8Help/source/controlreference/imagekitcontrol/file/exif/propertydatetimeoriginal.htm
    :param time: datetime to format
    :return: formatted string
    """
    return time.strftime("%Y:%m:%d %H:%M:%S")

def format_offset(time: datetime) -> str:
    offset_string = time.strftime("%z")
    return f"{offset_string[:3]}:{offset_string[3:]}"


def set_metadata_for_video():
    # TODO
    return


def set_metadata_for_image(full_path: str, exif_dict):
    image = PIL.Image.open(full_path)
    exif = image.getexif()
    for key, value in exif_dict.items():
        exif[key] = value
    image.save(full_path, exif=exif)


def fix_metadata_for_path(filename: str, full_path: str):
    game_name = get_game_name_from_filename(filename)
    timestamp = get_time_from_filename(filename)
    exif_dict = {
        0x9003: format_time(timestamp), # DateTimeOriginal
        0x9011: format_offset(timestamp), # OffsetTimeOriginal
        0x0110: "Nintendo Switch", # Model
        0xa434: game_name # LensModel
    }
    extension = full_path.split(".")[-1]
    match (extension.lower()):
        case "mp4":
            set_metadata_for_video()
        case "jpg":
            set_metadata_for_image(full_path, exif_dict)
        case _:
            raise Exception(f"unknown filetype \"{extension}\" found at: {full_path}")


if __name__ == "__main__":
    args = process_args()
    TIMEZONE = pytz.timezone(args.timezone)
    load_name_json(args.data)
    print(
        f"This script will MODIFY the metadata for all files in {args.album_path}.\n"
        f"Currently, this CANNOT be undone automatically.\n"
        f"Press enter to continue, or stop the script (CTRL+C or equivalent)"
    )
    input()
    for root, dirs, all_files in os.walk(args.album_path):
        for filename in all_files:
            # TODO add loading string
            fix_metadata_for_path(filename, os.path.join(root, filename))
