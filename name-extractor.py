import argparse, os



def extract_game_uuid_from_filename(filename: str) -> str:
    """
    Given a filename (with or without extension), will return the game UUID.
    :param filename: the filename to read from
    :return: the game UUID within that filename
    """
    # TODO
    return ""

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
    parser.add_argument("album_path", help="The path to the directory containing all of the photos and videos", type=dir_path)
    args = parser.parse_args()
    # END PARSE ARGS

    for root, dirs, files in os.walk(args.album_path):
        for filename in files:
            print(filename)
