# Wallpaper Switcher

<img src="assets/folderRotate.gif" width="100%"/>

## Intro
I love using cartoon images as my wallpapers. However, it can sometimes be awkward to show them in front of your audience during an academic presentation. Therefore, I made this little tool to save the day. It can help you quickly switch the wallpaper and switch back later.

>[!caution] 
> - **Only supports Windows**
> - **Always back up your current wallpaper before using this tool**

## Installation
### Download portable exe
- check the [lateset release](https://github.com/idlesilver/wallpaperSwitcher/releases/latest) for the `wallpaperSwitcher.exe`

### Build from source
- Install python environment. Google it if you don't have one.
- install pywin32 package with `pip install pywin32`
- install pyinstaller package with `pip install pyinstaller`
- Clone repo, or download and decompression [source zip](https://github.com/idlesilver/wallpaperSwitcher/releases/download/v1.0/wallpaperSwitcher.zip)
- Enter the decompression folder and compile the exe file by `pyinstaller --onefile --noconsole --icon=wallpaper.ico .\setWallpaper.py`
  - You can modify the icon and scripts as you like
  - The exe file should be in `dist` folder, you can move it to any where as you like

## Usage
1. Double-click to switch between the wallpapers in the list. The wallpaper list can be defined by
   1. An image path list in `wallpaper.txt` 
   2. images in the folder named wallpapers
   3. image paths defined in `default_wallpaper_files` in the script
2. Drag an image to set it as your wallpaper
3. Drag any non-image-type file to it to manually select a wallpaper

>[!tip] 
>`wallpaper.txt` and `wallpapers` folder should be in the same location as the executable file or the Python script.

## More demos
### Rotate images in list
<img src="assets/listRotate.gif" width="100%"/>

### Rotate images in folder
<img src="assets/folderRotate.gif" width="100%"/>

### Drag image files
<img src="assets/dragImage.gif" width="100%"/>

### Drag non-image files to trigger image select
<img src="assets/dragNonimage.gif" width="100%"/>

### Rotate images in default list
<img src="assets/defaultRotate.gif" width="100%"/>

