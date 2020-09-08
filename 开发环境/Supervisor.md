```
# 安装supervisor
pip3 install supervisor

# 生成配置文件
echo_supervisord_conf > supervisord.conf
sudo mkdir /etc/supervisor
sudo mv supervisord.conf /etc/supervisor
sudo vim /etc/supervisor/supervisord.conf

# 将
;[inet_http_server]
;port=127.0.0.1:9001
# 改为
[inet_http_server]
port=*:9001

# 将
;[include]
;files = relative/directory/*.ini
# 改为
[include]
files = conf.d/*.ini

# 创建任务配置文件
sudo mkdir /etc/supervisor/conf.d
sudo vim /etc/supervisor/conf.d/test.ini

[program:<任务名>]
command=<命令>
directory=<工作目录>
user=<用户名>
#supervisor启动的时候是否随着同时启动，默认true
autostart=false
#这个选项是子进程启动多少秒之后，此时状态如果是running，则我们认为启动成功了。默认值为1
startsecs=1
#程序异常退出后自动重启
autorestart=true
#启动失败自动重试次数，默认是3
startretries=3
#把stderr重定向到stdout，默认false
redirect_stderr=false
#输出日志文件
stdout_logfile=/tmp/stdout.log
#错误日志文件
stderr_logfile=/tmp/stderr.log
loglevel=info
stopsignal=KILL
stopasgroup=true
killasgroup=true

# 启动
supervisord
# 关闭
supervisorctl shutdown

# 查看所有进程的状态
supervisorctl status
supervisorctl start <任务名>
supervisorctl stop <任务名>
supervisorctl restart <任务名>
# 更新配置文件
supervisorctl update
# 重新启动supervisord
supervisorctl reload

# WebUI  http://localhost:9001
```

