import argparse, os, json
from pathlib import Path
from common import dir_path, extract_game_uuid_from_filename


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


def get_game_name_from_filename():
    return bruh


def format_time():
    return bruh


def fix_metadata_for_path():
    return bruh


if __name__ == "__main__":
    args = process_args()
    print(
        f"This script will MODIFY the metadata for all files in {args.album_path}.\n"
        f"Currently, this CANNOT be undone automatically.\n"
        f"Press enter to continue, or stop the script (CTRL+C or equivalent)"
    )
    input()
    for root, dirs, all_files in os.walk(args.album_path):
        for filename in all_files:
            print("file")