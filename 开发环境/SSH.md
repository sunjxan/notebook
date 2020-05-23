```
# 安装SSH
sudo apt install ssh

# 开启服务并查看
sudo service ssh start
sudo netstat -anp | grep ssh

# 生成密钥
ssh-keygen -t rsa
# 将公钥加入授权
cd ~/.ssh
cat id_rsa.pub >> authorized_keys

# 登录
ssh <当前用户>@localhost
```

