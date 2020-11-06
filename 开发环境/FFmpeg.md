```
sudo apt install ffmpeg

ffmpeg -version

# 转换编码格式
ffmpeg -i input.mp4 -c:v libx265 output.mp4

# 转换容器格式
ffmpeg -i input.mp4 -c copy output.webm

# 从视频中提取音频
ffmpeg -i input.mp4 -vn -c:a copy output.aac

# 给视频添加音频
ffmpeg -i input.aac -i input.mp4 output.mp4
```

