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
## 数据用例方面
目前用例数据保存在mongodb中，具体配置需要在framework/page_data.py 中定义模型和获取方式
一个典型的登录用例如下：
```angular2html
{ 
    "_id" : ObjectId("5a9e0851d9c4dc32e46552cd"), 
    "username" : "xxx", 
    "password" : "xxx", 
    "assert_type" : "equal", 
    "assert_data" : "【万店掌】手机巡店系统_远程巡店_视频巡店_客流统计_客流分析_客流计数_会员识别_连锁店监控", 
    "title" : "错误高管用户名登录--zqq", 
    "is_run" : false
}
```
### web driver
驱动强烈建议使用selenium grid 远程调用管理，方便持续集成

### 其他
如有兴趣共同学习探讨，邮件： 1711621009@qq.com ~
