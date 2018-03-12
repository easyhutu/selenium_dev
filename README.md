## selenium_dev

自动化测试持续集成项目

gitblit  http://172.30.18.222

jenkins http://172.30.18.222:9514

## 目录描述


### ddt 插件：
>需将145行
```angular2html
wrapper.__doc__ = func.__doc__.format(*args, **kwargs)
```
修改为
```angular2html
title = re.findall(r'\'title\': \'.+\',',func.__doc__.format(*args, **kwargs))
wrapper.__doc__ = title[0] if title else None
```