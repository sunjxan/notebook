安装nginx

```
sudo apt install nginx
```

查看nginx版本

```
nginx -v

# 启动
sudo service nginx start
# 关闭
sudo service nginx stop
# 重启
sudo service nginx restart
# 重新加载配置
sudo service nginx reload
```

安装好的文件位置：

/usr/sbin/nginx  主程序

/etc/nginx  存放配置文件

/var/log/nginx  存放日志

/var/www/html  默认虚拟主机



**配置文件结构**

```
# 全局块
...

# events块
events {
    ...
}

# http块
http
{
    # http全局块
    ...
    
    # server块
    server
    { 
        # server全局块
        ...
        
        # location块
        location [PATTERN]   
        {
            ...
        }
        location [PATTERN] 
        {
            ...
        }
    }
    server
    {
      ...
    }
    
    # http全局块
    ...
}


1、全局块：配置影响nginx全局的指令。一般有运行nginx服务器的用户组，nginx进程pid存放路径，日志存放路径，配置文件引入，允许生成worker process数等。

2、events块：配置影响nginx服务器或与用户的网络连接。有每个进程的最大连接数，选取哪种事件驱动模型处理连接请求，是否允许同时接受多个网路连接，开启多个网络连接序列化等。

3、http块：可以嵌套多个server，配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置，利用它的反向代理功能提供负载均衡支持。如文件引入，mime-type定义，日志自定义，是否使用sendfile传输文件，连接超时时间，单连接请求数等。

4、server块：配置虚拟主机的相关参数，一个http中可以有多个server。

5、location块：配置请求的路由，以及各种页面的处理情况。

```

具体说明
```

# nginx用户及组:用户 组
# user  nobody;
# 启动进程数量,通常设置成和cpu的数量相等
worker_processes  1;

# 全局错误日志及PID文件
# error_log  logs/error.log;
# error_log  logs/error.log  notice;
# error_log  logs/error.log  info;

# pid        logs/nginx.pid;

# 工作模式及连接数上限
events {
    # 单个后台worker process进程的最大并发链接数
    worker_connections  1024;
}

# 设定http服务器,利用它的反向代理功能提供负载均衡支持
http {
    # 设定mime类型,类型由mime.type文件定义
    include       mime.types;
    # 默认文件类型,默认为text/plain
    default_type  application/octet-stream;

    # 设定日志格式
    # log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    # 指定日志文件的存放路径
    # access_log  logs/access.log  main;

    # sendfile 指令指定 nginx 是否调用 sendfile 函数（zero copy 方式）来输出文件,
    # 对于普通应用,必须设为 on,
    # 如果用来进行下载等应用磁盘IO重负载应用,可设置为 off,
    # 以平衡磁盘与网络I/O处理速度,降低系统的uptime.
    sendfile        on;
    # 此选项允许或禁止使用socke的TCP_CORK的选项,此选项仅在使用sendfile的时候使用
    # tcp_nopush     on;

    # 连接超时时间
    # keepalive_timeout  0;
    keepalive_timeout  65;

    # 开启gzip压缩
    # gzip  on;

    # 设定虚拟主机配置
    server {
        # 监听端口
        listen       80;
        # 绑定域名
        server_name  localhost;

        # charset utf-8;

        # 设定本虚拟主机的访问日志
        # access_log  logs/host.access.log  main;

        # 默认请求
        location / {
            # 根目录
            root   html;
            # 默认页
            index  index.html index.htm;
        }

        # error_page  404              /404.html;

        # 服务器错误页面重定向至/50x.html
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        # location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        # }

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        # location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        # }

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        # location ~ /\.ht {
        #    deny  all;
        # }
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    # server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    # }


    # HTTPS server
    #
    # server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    # }

}
```

