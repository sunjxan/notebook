```
# 安装SSH
sudo apt install ssh

sudo vim /etc/ssh/sshd_config
# 修改默认端口：Port 10000（最大不能超过65535）
# 设置可以用密码登录：PasswordAuthentication yes

# 开启服务并查看
sudo service ssh start
sudo netstat -anp | grep ssh

# 登录
ssh -p10000 <user>@<hostname>
```

#### 密钥登录
本地生成的一对秘钥，私钥（~/.ssh/id_rsa）和公钥（~/.ssh/id_rsa.pub）
公钥（~/.ssh/id_rsa.pub）应该保存在远程服务端的已认证的秘钥文件（~/.ssh/authorized_keys）内

连接过程：

1. 本地向远程服务端发起连接；

2. 服务端随机生成一个字符串发送给发起登录的本地端；

3. 本地对该字符串使用私钥（~/.ssh/id_rsa）加密发送给服务端；

4. 服务端使用已认证的秘钥文件（~/.ssh/authorized_keys）内的公钥一一尝试对字符串进行解密；

5. 服务端对比解密后的字符串和第一次发送给客户端未加密的字符串，若一致则判断该公钥对应账户登录成功；

```
# 生成密钥
ssh-keygen -t rsa

# 将公钥加入授权
cd ~/.ssh
cat id_rsa.pub >> authorized_keys
```

