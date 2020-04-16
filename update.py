# 1. 禁用JS后复制网页内容到Typora
# 2. 附上原网页地址
# 3. 执行本脚本下载图片，更新目录

import os
import shutil
from urllib.request import urlretrieve


def downimage(url, file):
    if url[:4] != 'http':
        shutil.move(url, file)
        print(file, '移动成功')
        return
    if url[:9] == 'http:////':
        url = 'http://' + url[9:]
    elif url[:10] == 'https:////':
        url = 'https://' + url[10:]
    urlretrieve(url, file)
    print(file, '下载成功')

def createfileitem(floor, title, filepath):
    global summary
    if filepath == None:
        summary.append('\t' * floor + '- ' + title + '\n')
        return

    global path
    start = len(path + os.sep)
    summary.append('\t' * floor + '- [' + title + '](' + filepath[start:] + ')\n')

def scandir(dir, floor):
    files = os.listdir(dir)
    for file in files:
        filepath = dir + os.sep + file
        if os.path.isdir(filepath):
            if file[0] == '.' or os.path.isfile(filepath + '.md'):
                continue
            createfileitem(floor, file, None)
            scandir(filepath, floor + 1)
            continue
        if os.path.isfile(filepath) and file[-3:] == '.md':
            createfileitem(floor, file[:-3], filepath)
            downdir = filepath[:-3]
            if os.path.isdir(downdir):
                continue
            else:
                os.mkdir(downdir)
            with open(filepath, 'r', encoding='utf8') as f:
                lines = f.readlines()
            num = 0
            for index, line in enumerate(lines):
                line = line.strip()
                if line[:6] == '![img]':
                    num += 1
                    newfile = file[:-3] + os.sep + str(num) + '.png'
                    lines[index] = '![img](' + newfile + ')\n'
                    downimage(line[7:-1], downdir + os.sep + newfile)
            with open(filepath, 'w', encoding='utf8') as f:
                f.writelines(lines)

path = os.path.dirname(__file__)
readme = path + os.sep + 'README.md'
if os.path.isfile(readme):
    os.remove(readme)

summary = []
scandir(path, 0)
with open(readme, 'w', encoding='utf8') as f:
    f.writelines(summary)