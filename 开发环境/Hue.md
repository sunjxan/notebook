[原网页](<http://dblab.xmu.edu.cn/blog/1892/>)

```
# 确保git,python,java,maven,node,mysql,hadoop,hive的安装
# 安装依赖库和依赖工具
sudo apt install aptitude
sudo aptitude install ant gcc g++ make python2.7-dev libffi-dev libkrb5-dev libmysqlclient-dev libsasl2-dev libsasl2-modules-gssapi-mit libsqlite3-dev libssl-dev libxml2-dev libxslt-dev libldap2-dev libgmp3-dev

# 安装
cd /usr/local
# 下载安装包（https://docs.gethue.com/releases/）
sudo wget https://cdn.gethue.com/downloads/hue-4.7.0.tgz
# 解压
sudo tar -xvf hue-4.7.0.tgz
sudo mv hue-4.7.0 hue

# 因为在hue中很多操作需要文件所有者权限，所以需要更改hue目录所有者
sudo chown -R <user>:<user> /usr/local/hue

# 编译
cd hue
make apps

# 设置环境变量，在~/.zshrc追加
export HUE_HOME="/usr/local/hue"
export PATH="${HUE_HOME}/build/env/bin:$PATH"
# 生效
source ~/.zshrc

# 查看版本
hue version

# 启动服务（http://localhost:8000），创建账号
hue runserver
```


