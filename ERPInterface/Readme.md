# 接口自动化框架

设计模式

​	UI自动化框架：PO，Page object

表现层：元素，链接

操作层：对元素和链接的一些操作

业务层：case 测试用例

python+pytest+requests+PO   描述不准确  ，因为是把页面当做是一个对象，但是接口准确来讲没有页面的概念，所有不能叫做PO模式

**但是，PO模式的思想是可以在接口自动化中来使用的**

## 分层：借鉴的PO模式的思想

### 表现层：静态

​	接口路径；请求方式；参数

### 操作层

​	发起请求；请求这个接口；requests

### 业务层

​	不同的接口操作组合可以形成不同的测试用例

## 框架介绍

​	**Case：存放测试用例的位置**

​	Config：存放配置文件的位置

​	Data：存放数据文件的位置 文件可以使xlsx或者xls或者csv

​	**Interface：类似与UI自动化框架里面的Page，存放接口的类**

​	Report：存放测试报告文件的位置

​	**Utils：存放工具类的位置**

​		Cfg.py：读取数据库配置文件

​		Database.py：对pymysql进行的二次封装，实现查询数据和执行SQL的方法

​		Encryption.py：实现框架内所有需要用到的加密方法，目前只有md5加密

​		GetCodeImg.py：实现获取登录页面需要的图片验证码

​		**GetKeywords.py**：对python中的**jsonpath**的库进行二次封装，**用来提取接口的返回值**

​		OperationData.py：对pandas进行的二次封装，封装了用来读取数据文件的方法

​		**SendMethod.py**：对requests进行的二次封装，封装了发起请求的方法

​		TimeFormat.py：封装对时间格式的处理

