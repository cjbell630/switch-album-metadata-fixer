# Plan

## Original version: 3 CLI tools

### #3: Apply names

Assumes steps 1/2 have been taken in some correct form and the user has a JSON file with the structure:

```json
{
  "UUID": "Game Name",
  ...
}
```

Takes 2 required CLI args: directory, and json paths.  
Takes 1 optional CLI arg: timezone taken in  
Confirm with the user that the data will be modified in the specified way and it cannot be undone automatically.  
Reiterate over every file in the provided directory.  
Assume the UUID is in the provided JSON file. If not, store it in a list of skips to report to the user later.  
Edit the metadata such that:
TODO

#### Required functions:

- Extract time from filename
- Get game name from UUID
- Get time to apply TODO how to store time in metadata? Is timezone required or can it be omitted?
- Save metadata (image path)

#### Ideas/Enhancements:

- Add a CLI arg to control metadata schema. Likely unnecessary as redundant metada shouldn't be harmful for most photo
  organizing applications.
- Dry run
- Undo feature

## REWRITE: HTML only UI

### Frontend

1. Show homepage with instructions to user.
2. User chooses a folder and presses start
3. The webpage shows UUIDs with 1 image/video as a thumbnail, and the others viewable on a click
4. The user assigns all UUIDs and presses continue
5. Success! Screen

### Backend

#### Endpoints

- Search path for images: takes folder path and returns page with images
- Get image: returns image from absolute path
- Edit data: takes UUID mapping and applies it