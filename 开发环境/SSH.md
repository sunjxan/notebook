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

# 修改默认端口
sudo vim /etc/ssh/sshd_config
# 删除掉Port 22前面的#，然后下一行输入新的端口号如：Port 10000（最大不能超过65535）

# 登录
ssh -p10000 <user>@<hostname>
```

