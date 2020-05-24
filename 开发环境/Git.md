1. Windows安装Git（<https://git-scm.com/downloads>）；

2. Checkout Windows-style,commit Unix-style line endings
在检出文本文件时，Git会将LF转换为CRLF。当提交文本文件时，CRLF将转换为LF。 对于跨平台项目，这是Windows上推荐的设置（“core.autocrlf”设置为“true”）。

在各操作系统下，文本文件所使用的换行符是不一样的。UNIX/Linux 使用的是 0x0A（LF），早期的 Mac OS 使用的是0x0D（CR），后来的 OS X 在更换内核后与 UNIX 保持一致了。但 DOS/Windows 一直使用 0x0D0A（CRLF）作为换行符。Git提供了一个“换行符自动转换”功能。
```
# 提交时CRLF转换为LF，检出时LF转换为CRLF（对于跨平台项目，这是Windows上推荐的设置）
git config --global core.autocrlf true   

# 提交时CRLF转换为LF，检出时不转换（对于跨平台项目，这是Unix上的推荐设置）
git config --global core.autocrlf input   

# 提交检出均不转换
git config --global core.autocrlf false
```

3. 关闭文件模式

```
# 忽略文件权限修改
git config --global core.filemode false
```

4. 设置用户信息

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

5. 安装TortoiseGit和语言包（https://tortoisegit.org/download/）；

6. 创建SSH Key
    在Linux的用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有`id_rsa`和`id_rsa.pub`这两个文件，如果已经有了，可直接跳到下一步。如果没有，打开Shell，创建SSH Key：

  ```
ssh-keygen -t rsa -C "youremail@example.com"
  ```
  你需要把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可，由于这个Key也不是用于军事目的，所以也无需设置密码。如果一切顺利的话，可以在用户主目录里找到`.ssh`目录，里面有`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对，`id_rsa`文件内长字符串是私钥，不能泄露出去，`id_rsa.pub`文件全文是公钥，可以放心地告诉任何人。

  ssh-keygen生成的`key`在TortoiseGit下是不能使用的。因为ssh-keygen生成的密钥采用的是`OpenSSH SSH-2`，而TortoiseGit是通过Pageant进行私钥/公钥验证的，所以想要在TortoiseGit中使用ssh-keygen生成的key就需要通过`PuTTYGen`来进行转格式：

  > 1) 将Linux下的.ssh目录复制到Windows的用户主目录里；

  > 2）运行`PuTTYGen`，在`Conversions`菜单中点击`Import key`，选择`ssh-keygen`生成的私钥文件所在位置，比如`id_rsa`文件；

  > 3）点击`Save private key`按钮，将其保存为`.ppk`文件；

  > 4）打开`Pageant`，点击`Add Key`，选择前一步所保存的`.ppk`文件所在的位置即可。