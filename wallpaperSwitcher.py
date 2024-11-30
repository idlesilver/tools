import win32api,win32con,win32gui
import os, sys
import tkinter as tk
from tkinter import filedialog
import mimetypes

# default wallpaper list
default_wallpaper_files = [
    r"C:\Windows\Web\Screen\img100.jpg",
    r"C:\Windows\Web\Screen\img101.jpg",
    r"C:\Windows\Web\Screen\img102.jpg",
    r"C:\Windows\Web\Screen\img103.jpg",
    r"C:\Windows\Web\Screen\img104.jpg",
    r"C:\Windows\Web\Screen\img105.jpg",
]

def get_wallpaper():
    wallpaper_files = []
    # get wallpaper config
    wallpapers_config_path = "wallpapers.txt"
    wallpapers_dir = "wallpapers"
    # wallpaper config file
    if os.path.isfile(wallpapers_config_path):
        try:
            with open(wallpapers_config_path, "r") as file:
                wallpapers = file.readlines()
        except UnicodeDecodeError:
            with open(wallpapers_config_path, "r", encoding="utf-8") as file:
                wallpapers = file.readlines()
        for wallpaper in wallpapers:
            wallpaper = wallpaper.strip()
            if wallpaper and os.path.isfile(wallpaper) and is_valid_image(wallpaper):
                wallpaper_files.append(wallpaper)
        return wallpaper_files
    # wallpaper directory
    elif os.path.isdir(wallpapers_dir):
        for file in os.listdir(wallpapers_dir):
            file_path = os.path.abspath(os.path.join(wallpapers_dir, file))
            if os.path.isfile(file_path) and is_valid_image(file_path):
                wallpaper_files.append(file_path)
        return wallpaper_files
    # default wallpaper list
    else:
        return default_wallpaper_files

def is_valid_image(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and mime_type.startswith('image/'):
        return True
    else:
        return False

def set_wallpaper(image_path):
    set_success = False
    # check path validation
    if not os.path.isfile(image_path) or not is_valid_image(image_path):
        print("Invalid image file path: ", image_path)
        return set_success

    # set wallpaper style
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 壁纸样式：
    # 0: 居中
    # 2: 拉伸
    # 6: 适应
    # 10: 填充
    # 22: 跨区
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "10")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")

    # set wallpaper file
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path,
                                  win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDWININICHANGE)
    set_success = True
    return set_success

def main():
    if len(sys.argv) == 1:
        print("No image file path provided, rotate between given list.")
        print("Default wallpaper list: ", default_wallpaper_files)
        print("config file: wallpapers.txt")
        print("wallpapers directory: wallpapers")
        wallpaper_files = get_wallpaper()
        print(wallpaper_files)
        
        # rotate between given list
        current_wallpaper = win32gui.SystemParametersInfo(win32con.SPI_GETDESKWALLPAPER, 0, 0)
        if current_wallpaper in wallpaper_files:
            cur_idx = wallpaper_files.index(current_wallpaper)
        else:
            cur_idx = -1
        nxt_idx = (cur_idx + 1) % len(wallpaper_files)

        image_path = wallpaper_files[nxt_idx]
        set_wallpaper(image_path)
        return

    elif len(sys.argv) == 2:
        print("Image file path provided.")
        # drag image file to exe
        image_path = sys.argv[1]
        if set_wallpaper(image_path):
            return

    print("No valid image file path provided, open file")
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(title="选择一张图片 select an image",
                                            filetypes=[("图片文件 image files", "*.bmp;*.jpg;*.jpeg;*.png")])
    if image_path:
        set_wallpaper(image_path)
        
if __name__ == "__main__":
    main()