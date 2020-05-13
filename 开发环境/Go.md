```
cd /usr/local/share
# 下载安装包（https://golang.org/dl/）
sudo wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
# 解压
sudo tar -xvf go1.14.2.linux-amd64.tar.gz

# 设置环境变量，在~/.zshrc追加
export PATH="/usr/local/share/go/bin:$PATH"

# 生效
source .zshrc
```

