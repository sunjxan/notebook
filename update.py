# 1. 禁用JS后复制网页内容到Typora
# 2. 附上原网页地址
# 3. 执行本脚本下载图片，更新目录

import os
import re
import base64
import shutil
import urllib
from urllib.request import urlretrieve

pasplit = re.compile('(!\[[^\]]+\]\([^\)]+\))')
pafind = re.compile('!\[([^\]]+)\]\(([^\s\)]+)(\s[\'\"]([^\s\'\"]+)[\'\"])?\)')


def downimage(url, file):
    downdir = os.path.abspath(os.path.dirname(file))
    if not os.path.isdir(downdir):
        os.mkdir(downdir)
    if url[:4] == 'http':
        if url[:9] == 'http:////':
            url = 'http://' + url[9:]
        elif url[:10] == 'https:////':
            url = 'https://' + url[10:]
        # 绕过反爬虫机制
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36')]
        urllib.request.install_opener(opener)
        urlretrieve(url, file)
        print(file, '下载成功')
    elif url[:22] == 'data:image/png;base64,':
        imgdata = base64.b64decode(url[22:])
        with open(file, 'wb') as f:
            f.write(imgdata)
        print(file, '下载成功')
    else:
        shutil.move(url, file)
        print(file, '移动成功')


def createfileitem(floor, title, filepath):
    global summary
    if filepath == None:
        summary.append('\t' * floor + '- ' + title + '\n')
        return

    global path
    start = len(path + '/')
    summary.append(
        '\t' * floor + '- [' + title + '](' + filepath[start:] + ')\n')


def scandir(dir, floor):
    os.chdir(dir)
    files = os.listdir(dir)
    for file in files:
        filepath = dir + '/' + file
        if os.path.isdir(filepath):
            if file[0] == '.' or os.path.isfile(filepath + '.md'):
                continue
            createfileitem(floor, file, None)
            scandir(filepath, floor + 1)
            continue
        if os.path.isfile(filepath) and file[-3:] == '.md':
            createfileitem(floor, file[:-3], filepath)
            with open(filepath, 'r', encoding='utf8') as f:
                lines = f.readlines()
            num = 0
            for index, line in enumerate(lines):
                res = pasplit.split(line)
                if len(res) != 1:
                    for ix in range(len(res)):
                        if ix % 2:
                            while True:
                                num += 1
                                newfile = file[:-3] + \
                                    '.assets/' + str(num) + '.png'
                                newfilepath = dir + '/' + newfile
                                if not os.path.isfile(newfilepath):
                                    break
                            tmp = pafind.findall(res[ix])[0]
                            if os.path.dirname(os.path.abspath(tmp[1])) == os.path.dirname(os.path.abspath(newfilepath)):
                                num -= 1
                                continue
                            if tmp[3]:
                                res[ix] = '![' + tmp[0] + \
                                    '](' + newfile + ' "' + tmp[3] + '")'
                            else:
                                res[ix] = '![' + tmp[0] + \
                                    '](' + newfile + ')'
                            downimage(tmp[1], newfilepath)
                    lines[index] = ''.join(res)
            with open(filepath, 'w', encoding='utf8') as f:
                f.writelines(lines)


path = os.path.abspath(os.path.dirname(__file__))
readme = path + '/' + 'README.md'
if os.path.isfile(readme):
    os.remove(readme)

summary = []
scandir(path, 0)
with open(readme, 'w', encoding='utf8') as f:
    f.writelines(summary)
