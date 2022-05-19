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
git submodule add https://github.com/alanorth/hugo-theme-bootstrap4-blog.git themes/hugo-theme-bootstrap4-blog
```

5. 修改配置：

```
vim config.json

{
   "relativeurls": true,
   "languageCode": "zh-cn",
   "title": "xxx的博客",
   "theme": "hugo-theme-bootstrap4-blog"
}
```

6. 生成网页：

```
hugo -D
```

7. 开启服务：

```
hugo server --bind 127.0.0.1 --baseURL http://127.0.0.1/ --port 8000
```

8. 添加文章，自动更新网站：

```
# 根据模板archetypes/default.md创建新的markdown文件
hugo new posts/hello-world.md
```

