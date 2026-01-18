import argparse, os, json
from pathlib import Path
from common import dir_path, extract_game_uuid_from_filename

if __name__ == "__main__":
    # PARSE ARGS
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "album_path",
        help="The path to the directory containing all of the photos and videos",
        type=dir_path
    )
    # TODO add arg for output file path
    # TODO add arg for input file path (master list)
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
                image_links[game_uuid] = Path(os.path.join(root, filename)).as_uri()

    # Output json file with UUID and names
    with open("game_names.json", "w+") as outfile:
        json.dump(game_names, outfile, indent=4)
        # TODO maybe add warning about overwriting file

    # Print game numbers and file links
    print("\n\n".join(
        [
            f"{game_names[uuid]}\n    -->  {link}\n"
            for uuid, link in image_links.items()
        ]
    ))
