import argparse, os
from common import dir_path, extract_game_uuid_from_filename

if __name__ == "__main__":
    # PARSE ARGS
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "album_path",
        help="The path to the directory containing all of the photos and videos",
        type=dir_path
    )
    args = parser.parse_args()
    # END PARSE ARGS

    game_names = {}
    image_links = {}
    num_games_found = 0

    # walk through all files in every subdirectory (recursively gets every single file)
    for root, dirs, all_files in os.walk(args.album_path):
        for filename in all_files:
            game_uuid = extract_game_uuid_from_filename(filename)
            if game_uuid not in game_names:
                num_games_found += 1
                game_names[game_uuid] = f"Game {num_games_found}"
                image_links[game_uuid] = os.path.join(root, filename)
    # TODO generate JSON file
    print("\n\n".join(
        [
            f"{game_names[uuid]}\n    -->  file:///{link.replace("\\", "/").replace(" ", "%20")}\n"
            for uuid, link in image_links.items()
        ]
    ))
