```
cd /usr/local
# 下载安装包（https://nodejs.org/en/download/）
sudo wget https://nodejs.org/dist/v12.16.3/node-v12.16.3-linux-x64.tar.xz
# 解压
sudo tar -xvf node-v12.16.3-linux-x64.tar.xz
sudo mv node-v12.16.3-linux-x64 node

#安装yarn（https://classic.yarnpkg.com/en/docs/install#debian-stable）
# 添加GPG key
curl -fsSL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
# 添加仓库
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt update && sudo apt install yarn

# 设置环境变量，在~/.zshrc追加
export NODE_HOME="/usr/local/node"
export PATH="${NODE_HOME}/bin:$PATH"

# 生效
source ~/.zshrc

# 查看版本
node -v
npm -v
yarn -v
```

