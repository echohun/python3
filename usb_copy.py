import os
import time
import shutil


USB = 'D:\\'  # u盘目录
SAVE = 'C:\\Users\Leticia\Desktop\copy'  # 保存目录


def usbcopy():
    shutil.copytree(USB, SAVE)


def main():
    while (1):
        time.sleep(2)  # 休眠时间
        if os.path.exists(USB):
            break
    usbcopy()

main()
