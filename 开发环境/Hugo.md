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

6. 生成网页：

```
hugo -D
```

7. 配置 `nginx` 服务：

```
sudo vim /etc/nginx/conf.d/hugo.conf

server {
    listen 80;
    server_name <IP或域名>;
    location / {
        root /home/<user>/blog/public;
        index index.html;
    }
    error_page 404 /404.html;
}

# 测试配置是否正确
sudo nginx -t

sudo service nginx reload
```

8. 添加文章，并更新网站：

```
# 根据模板archetypes/default.md创建新的markdown文件
hugo new posts/hello-world.md

# 编辑文章内容
vim content/posts/hello-world.md

# 更新网站
hugo -D
```

主题、搜索功能、评论功能、背景音乐、分类、RSS