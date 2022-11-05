# Shoebox

I like to keep my photos organized by year, with each year organized by date + name, e.g. `2022-07-14 Squirrels at the bird feeder`. Easy enough with a photo shoot, but the number of photos in a cloud-synced folder e.g. `Dropbox\Photos` or `Pictures\iCloud Photos` can quickly get out of hand. Who has time to go through all these and sort them into folders?

This Python script helps a little. It will iterate through a folder full of JPGs, create a sub-folder for each one in the `YYYY-MM-DD` format if needed, then move the photo into it. From there, it should be easier to name these and file them away.

This is for Windows only, but I may tweak for MacOS and Linux later on.

## Usage

Update the `WORKDIR` var to the directory containing the photos, e.g.:

```python
WORKDIR = 'Pictures\iCloud Photos'
```

... the script will find your home directory.

Then run the script:

```powershell
PS C:\Users\cbrown\Desktop\shoebox> python3 shoebox.py
```

The script will create a subdirectory for each image it finds with the format YYYY-MM-DD (if needed) for every photo, then move it to that directory. 

[modeline]: # ( vi: set textwidth=78 colorcolumn=80: )
