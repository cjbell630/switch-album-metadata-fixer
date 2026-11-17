import argparse, os, json
from pathlib import Path
from common import dir_path, extract_game_uuid_from_filename

UUID_NAMES = {}

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
    return parser.parse_args()


def get_time_from_filename():
    return bruh


def get_game_name_from_filename(filename: str) -> str:
    uuid = extract_game_uuid_from_filename(filename)
    return UUID_NAMES[uuid]


def format_time():
    return bruh

def set_metadata_for_video():
    return

def set_metadata_for_image():
    return

def fix_metadata_for_path(filename: str, full_path: str):
    print(full_path)
    game_name = get_game_name_from_filename(filename)
    # TODO get info from filename
    # TODO handle based on extension
    extension = full_path.split(".")[-1]
    match (extension.lower()):
        case "mp4":
            set_metadata_for_video()
        case "jpg":
            set_metadata_for_image()
        case _:
            raise Exception(f"unknown filetype \"{extension}\" found at: {full_path}")


if __name__ == "__main__":
    args = process_args()
    load_name_json(args.data)
    print(
        f"This script will MODIFY the metadata for all files in {args.album_path}.\n"
        f"Currently, this CANNOT be undone automatically.\n"
        f"Press enter to continue, or stop the script (CTRL+C or equivalent)"
    )
    input()
    for root, dirs, all_files in os.walk(args.album_path):
        for filename in all_files:
            fix_metadata_for_path(filename, os.path.join(root, filename))