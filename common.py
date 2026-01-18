import re, os


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
        raise ValueError('Invalid game UUID')


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
