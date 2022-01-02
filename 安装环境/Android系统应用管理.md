```
# 无线调试连接Android设备
adb connect <IP地址>:<端口号>

# 查看已连接设备
adb devices

# 列出手机上的应用
adb shell pm list packages

# 安装应用
adb install <apk文件>
# 重新安装该程序，保存数据
adb install -r <apk文件>
# 覆盖高版本应用
adb install -d <apk文件>

# 卸载应用
adb uninstall <应用包名>

# 卸载系统应用（不要卸载MIUI系统应用商店）
adb shell pm uninstall --user 0 <应用包名>

华为应用包名
com.huawei.hifolder  热门推荐（精品推荐）
com.huawei.android.thememanager  主题
com.baidu.input_huawei  百度输入法-华为版
com.huawei.browser  华为浏览器
com.huawei.hwireader/com.huawei.hwread.al  华为阅读
com.huawei.music  华为音乐
com.huawei.himovie  华为视频
com.android.stk  SIM卡应用
```

安装 [Apkpure](https://apkpure.com) 代替 [Google Play Store](https://play.google.com/store) ，收藏安装的应用以同步，与系统应用商店配合管理应用。

MIUI不允许安装多应用，所以安装xapk文件时，先在 设置 - 更多设置 - 开发者选项 中关闭 MIUI优化，安装完成后再打开。
