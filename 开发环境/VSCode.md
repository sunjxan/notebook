1. 安装VS Code；
2. 安装插件“Remote - WSL”；
3. 点击最左下角图标，选择安装的Linux发行版；
4. 打开Windows文件系统下的项目目录；
5. 选择默认Shell：/bin/zsh；
6. 安装（Install on WSL）插件“Python”，“Go”；
7. 修改launch.json文件
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Node",
            "type": "node",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "skipFiles": [
                "<node_internals>/**"
            ]
        },
        {
            "name": "Go",
            "type": "go",
            "request": "launch",
            "program": "${file}"
        }
    ]
}
```

8. 左下角切换anaconda环境的python解释器，即可使用Jupyter notebook：打开ipynb文件或者Ctrl+Shift+P输入 jupyter选择Python: Create New Blank Jupyter Notebook