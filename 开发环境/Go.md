```
cd /usr/local
# 下载安装包（https://golang.org/dl/）
sudo wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
# 解压
sudo tar -xvf go1.14.2.linux-amd64.tar.gz

# 设置环境变量，在~/.zshrc追加
export GOROOT="/usr/local/go"
export GOPATH="/home/<user>/.local/lib/go"
export PATH="${GOROOT}/bin:$PATH"

# 生效
source .zshrc

#查看版本
go version
```

