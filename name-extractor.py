import argparse, os, re


def extract_game_uuid_from_filename(filename: str) -> str:
    """
    Given a filename (with or without extension), will return the game UUID.

    Test cases:
        ARMS
        2017091212162800-5175A9E8354E328724729A6641D0F22F.jpg
        2017091213472700-5175A9E8354E328724729A6641D0F22F.jpg
        2017092918372900-5175A9E8354E328724729A6641D0F22F.jpg

        BOTW
        2017122520595000-F1C11A22FAEE3B82F21B330E1B786A39.jpg

        MARIO ODYSSEY
        2017102900230700-8AEDFF741E2D23FBED39474178692DAF.mp4

    :param filename: the filename to read from
    :return: the game UUID within that filename
    """
    UUID_REGEX = r".*-([A-Z\d]*)"
    if match := re.search(UUID_REGEX, filename, re.IGNORECASE):
        return match.group(1)
    else:
        raise argparse.ArgumentTypeError("Invalid game UUID")


def dir_path(string):
    """
    https://stackoverflow.com/a/51212150
    :param string:
    :return:
    """
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


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
    # TODO generate simple HTML page with clickable file links
    # TODO generate JSON file
    # Alternatively write js code and make the HTML page export the json file instead of making the user modify it themselves
    print("\n\n".join([f"{game_names[uuid]}: \"{link}\"\n" for uuid, link in image_links.items()]))
