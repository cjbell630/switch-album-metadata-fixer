# Switch Album Metadata Fixer

Edits the EXIF data of photos from the Switch gallery to preserve information encoded in the filename (timezone, game)
such that it can be viewed in a photo manager such as Immich or Google Photos.

If your photo manager does not seem to accept the resulting metadata, feel free to modify the script to add additional
metadata and submit a pull request!

## DISCLAIMER

Technically speaking, the scripts work. But I'm not very proud of it and I'd like to rewrite it in a better language,
with easier to understand code, and a full web-based GUI. But for now, this script serves my purpose. Hopefully it will
for you too! :)

## Usage

### 1. Setup

Download the source code from the [latest release](https://github.com/cjbell630/switch-album-metadata-fixer/releases/latest) and unzip/untar it.

Navigate to the unzipped project directory and run `pip install -r requirements.txt`, or install manually.  
Make sure you have `exiftool` installed on your system.

### 2. Extract UUIDs

Run the following command, where `<target_directory>` is the location of your Switch gallery. (any folder structure will
work)

`python extract_uuids.py <target_directory>`

This will generate `game_images.json` and `game_names.json`.

### 3. Assign names to UUIDs

This can be done by hand (modifying the JSON file directly), using the GUI, or both.

#### Web GUI

Run the following, with `game_images.json` and `game_names.json` in the same directory as `edit_metadata.py`:

`python set_names_gui.py`

Click the link in the output or navigate to http://localhost:8000/ in your browser.  
Replace "Game 1" etc. with the game depicted in the corresponding screenshot.

> NOTE! Many images will likely not load, and some will be unhelpful to determining the game.  
> I plan to rewrite this whole project someday, but for now, please fill in the missing info by hand (see next
> section).

Click "Save" at the bottom, and note the location of the downloaded `game_names.json`.

#### Assigning by hand

Modify `game_names.json`, replacing all "Game 1" etc with the game name associated with that UUID.  
The easiest way to determine this is to navigate to your Switch album directory and search the UUID. All screenshots and
videos that appear were taken in the same software, according to the Switch system.

### 4. Edit the EXIF data

Run the following command. `<modified_json_file>` is the JSON file you created/modified in step 2 (`game_names.json` in
most cases).

> NOTE! The Switch does not store timezone information in screenshots.  
> Optionally add the `-t <timezone>` flag at the end to set the timezone the screenshots were taken in.  
> (IANA Canonical; use [this](https://www.simplemaplab.com/tools/time-zone-finder) site if you're unsure.  
> Type in your city and copy the text below "IANA name" at the bottom. It should have a "/" in it.)

`python edit_metadata.py <target_directory> <modified_json_file>`

Read the warning and press Enter to continue.

Screenshots shouldn't take much time, but videos can take around 1-2 seconds each to process, so be prepared to wait!