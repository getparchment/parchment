import os
import shutil

def cp_folders(src, dst, symlinks=False, ignore=None):
    dir_list = os.listdir(src)
    for item in dir_list:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s,d, symlinks, ignore)


def delete_file_folder(src):
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            if item == 'CNAME':
                pass
            elif item == '.git':
                pass
            else:
                itemsrc = os.path.join(src, item)
                delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))
