# 1. 禁用JS后复制网页内容到Typora
# 2. 附上原网页地址
# 3. 执行本脚本下载图片，更新目录

import os
import re
import base64
import shutil
import urllib
from urllib.request import urlretrieve

pattern_split_1 = re.compile('(!\[[^\]]+\]\([^\)]+\))')
pattern_find_1 = re.compile('!\[[^\]]+\]\(([^\)]+)\)')
pattern_split_2 = re.compile('(<img src="[^"]+"[^/>]*/>)')
pattern_find_2 = re.compile('<img src="([^"]+)"[^/>]*/>')

def downimage(url, file):
    downdir = os.path.abspath(os.path.dirname(file))
    if not os.path.isdir(downdir):
        os.mkdir(downdir)
    if url.startswith('http'):
        # 绕过反爬虫机制
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36')]
            urllib.request.install_opener(opener)
            urlretrieve(url, file)
        except:
            print(file, '下载失败！')
        else:
            print(file, '下载成功')
            return True
    elif url.startswith('data:image/png;base64,'):
        try:
            imgdata = base64.b64decode(url[22:])
            with open(file, 'wb') as f:
                f.write(imgdata)
        except:
            print(file, '下载失败！')
        else:
            print(file, '下载成功')
            return True
    else:
        if url[1] == ':':
            url = '/mnt/' + url[0].lower() + url[2:]
            url = url.replace('\\', '/')
        try:
            shutil.move(url, file)
        except:
            print(file, '移动失败！')
        else:
            print(file, '移动成功')
            return True

def createfileitem(floor, title, filepath):
    global summary
    if filepath == None:
        summary.append('\t' * floor + '- ' + title + '\n')
        return

    global path
    start = len(path + '/')
    summary.append('\t' * floor + '- [' + title + '](' + filepath[start:] + ')\n')

def scandir(dir, floor, pattern_split, pattern_find):
    files = os.listdir(dir)
    for file in files:
        filepath = dir + '/' + file
        if os.path.isdir(filepath):
            if file[0] == '.' or file == '__pycache__' or filepath[-7:] == '.assets':
                continue
            createfileitem(floor, file, None)
            scandir(filepath, floor + 1, pattern_split, pattern_find)
            continue
        if os.path.isfile(filepath) and file[-3:] == '.md':
            createfileitem(floor, file[:-3], filepath)
            with open(filepath, 'r', encoding='utf8') as f:
                lines = f.readlines()
            num = 0
            for index, line in enumerate(lines):
                res = pattern_split.split(line)
                len_res = len(res)
                if len_res != 1:
                    for ix in range(len_res):
                        if ix % 2:
                            # res[ix]是图片引入
                            # filename_ori是图片url
                            filename_ori = pattern_find.findall(res[ix])[0]

                            filename = filename_ori
                            if filename_ori.startswith('<'):
                                filename = filename_ori[1:-1]
                            if filename_ori.startswith('http'):
                                if filename_ori.startswith('http:////'):
                                    filename = 'http://' + filename_ori[9:]
                                elif filename_ori.startswith('https:////'):
                                    filename = 'https://' + filename_ori[10:]
                            elif filename_ori.startswith('file'):
                                if filename_ori.startswith('file:///'):
                                    filename = filename_ori[8:]
                                elif filename_ori.startswith('file://'):
                                    filename = filename_ori[7:]
                            
                            prefix = file[:-3] + '.assets'
                            if filename.startswith(prefix):
                                continue
                            filename_path = urllib.parse.urlparse(filename).path
                            rindex = filename_path.rfind('.')
                            suffix = filename_path[rindex:] if rindex != -1 else ''

                            # 确定图片文件新路径
                            while True:
                                num += 1
                                newfile = prefix + '/' + str(num) + suffix
                                newfilepath = dir + '/' + newfile
                                if not os.path.isfile(newfilepath):
                                    break
                            
                            # 切换工作目录获取绝对路径
                            os.chdir(dir)   
                            if downimage(filename, newfilepath):
                                res[ix] = res[ix].replace(filename_ori, newfile)
                    lines[index] = ''.join(res)
            with open(filepath, 'w', encoding='utf8') as f:
                f.writelines(lines)

path = os.path.abspath(os.path.dirname(__file__))
readme = path + '/' + 'README.md'
if os.path.isfile(readme):
    os.remove(readme)

summary = []
scandir(path, 0, pattern_split_1, pattern_find_1)

summary = []
scandir(path, 0, pattern_split_2, pattern_find_2)

with open(readme, 'w', encoding='utf8') as f:
    f.writelines(summary)
