[原网页](http://dblab.xmu.edu.cn/blog/2138-2/)
```
cd /usr/local
# 下载安装包（https://maven.apache.org/download.cgi）
sudo wget https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
# 解压
sudo tar -xvf apache-maven-3.6.3-bin.tar.gz
sudo mv apache-maven-3.6.3 maven

# 设置环境变量，在~/.zshrc追加
export MAVEN_HOME="/usr/local/maven"
export PATH="${MAVEN_HOME}/bin:$PATH"

# 生效
source .zshrc

#查看版本
mvn -v

# 更换Maven源到国内镜像，修改 /usr/local/maven/conf/settings.xml中<mirrors>
sudo vim /usr/local/maven/conf/settings.xml

<mirror>
    <id>nexus-aliyun</id>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    <mirrorOf>*</mirrorOf>
</mirror>
```