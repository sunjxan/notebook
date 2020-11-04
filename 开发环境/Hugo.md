1. 在 https://github.com/gohugoio/hugo/releases 下载hugo的Linux-64bit最新版本tar包：

```
cd /usr/local
sudo wget https://github.com/gohugoio/hugo/releases/download/v0.78.0/hugo_0.78.0_Linux-64bit.tar.gz
```

2. 解压，配置：

```
sudo tar -xvf hugo_0.78.0_Linux-64bit.tar.gz
sudo mv hugo sbin
sudo rm -f README.md LICENSE
hugo version
```

3. 建立网站：

```
cd ~
hugo new site blog -f=json
```

4. 添加主题：

```
cd blog
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
```

5. 修改配置：

```
vim config.json

{
   "relativeurls": true,
   "languageCode": "zh-cn",
   "title": "xxx的博客",
   "theme": "ananke"
}
```

6. 启动服务，监视并自动生成静态文件，并配置 `supervisord`：

```
sudo vim /etc/supervisor/conf.d/hugo.ini

[program:hugo]
command=hugo -D -w
directory=/home/<user>/blog
#supervisor启动的时候是否随着同时启动，默认true
autostart=true
#这个选项是子进程启动多少秒之后，此时状态如果是running，则我们认为启动成功了。默认值为1
startsecs=1
#程序异常退出后自动重启
autorestart=true
#启动失败自动重试次数，默认是3
startretries=3
#把stderr重定向到stdout，默认false
redirect_stderr=false
#输出日志文件
stdout_logfile=/tmp/hugo-stdout.log
#错误日志文件
stderr_logfile=/tmp/hugo-stderr.log
loglevel=info
stopsignal=KILL
stopasgroup=true
killasgroup=true

supervisorctl reload
```

7. 配置 `nginx` 反向代理：

```
sudo vim /etc/nginx/conf.d/hugo.conf

server {
    listen 80;
    server_name <IP或域名>;
    error_page 404 /404.html;
    root /home/<user>/blog/public;
}

sudo service nginx reload
```

8. 添加文章，然后刷新主页：

```
hugo new posts/hello-world.md
vim content/posts/hello-world.md
```

