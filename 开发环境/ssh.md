```
# 安装 SSH server
sudo apt install openssh-server

# 开启服务并查看
sudo service sshd restart
sudo netstat -anp | grep ssh

# 生成密钥
sudo mkdir ~/.ssh/
cd ~/.ssh/
ssh-keygen -t rsa -C "youremail@example.com"
# 将公钥加入授权
cat ./id_rsa.pub >> ./authorized_keys

# 登录
ssh <当前用户>@localhost
```

