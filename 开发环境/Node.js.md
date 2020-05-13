```
cd /usr/local/share
# 下载安装包（https://nodejs.org/en/download/）
sudo wget https://nodejs.org/dist/v12.16.3/node-v12.16.3-linux-x64.tar.xz
# 解压
sudo tar -xvf node-v12.16.3-linux-x64.tar.xz
sudo mv node-v12.16.3-linux-x64 node

#安装yarn（https://classic.yarnpkg.com/en/docs/install#debian-stable）
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn

# 设置环境变量，在~/.zshrc追加
export PATH="/usr/local/share/node/bin:$PATH"

# 生效
source .zshrc

# 更换源到国内镜像
npm config set registry https://registry.npm.taobao.org
yarn config set registry https://registry.npm.taobao.org
```

