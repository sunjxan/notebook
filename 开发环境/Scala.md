[原网页](http://dblab.xmu.edu.cn/blog/2080-2/)
```
cd /usr/local
# 下载安装包（https://www.scala-lang.org/download/）
sudo wget https://downloads.lightbend.com/scala/2.13.2/scala-2.13.2.tgz
# 解压
sudo tar -xvf scala-2.13.2.tgz
sudo mv scala-2.13.2 scala

# 设置环境变量，在~/.zshrc追加
export SCALA_HOME="/usr/local/scala"
export PATH="${SCALA_HOME}/bin:$PATH"

# 生效
source .zshrc

#查看版本
scala --version
```