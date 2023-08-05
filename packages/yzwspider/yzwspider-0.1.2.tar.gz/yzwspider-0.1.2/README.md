# yzw
scrapy爬取研招网专业信息(末尾有度盘全部数据)

含有考试范围、专业等，可输出到Excel或MySQL。

数据大概这个样子，获得数据之后我们就能方便地进行筛选了。

![图1](https://github.com/Hthing/yzw/blob/master/img/excel.png) 

## 安装：  
```
pip install yzwspider
```



## 运行环境：
python3.7以上（使用了新版argparse模块）

## 数据格式：

建表语句存于yzwspider/yzw/settings.py中， 爬取时会自动建表（数据库要提前建立）。

```mysql
CREATE TABLE `major` (
  `id` char(21) PRIMARY KEY, # id 为爬取页面的id参数+考试范围序号
  `招生单位` varchar(40) NOT NULL,
  `院校特性` varchar(10) DEFAULT NULL,
  `院系所` varchar(40) DEFAULT NULL,
  `专业` varchar(40) DEFAULT NULL,
  `研究方向` TINYTEXT DEFAULT NULL,
  `学习方式` varchar(30) DEFAULT NULL,
  `拟招生人数` varchar(40) DEFAULT NULL,
  `业务课一` varchar(40) DEFAULT NULL,
  `业务课二` varchar(40) DEFAULT NULL,
  `外语` varchar(40) DEFAULT NULL,
  `政治` varchar(40) DEFAULT NULL,
  `所在地` varchar(30) DEFAULT NULL,
  `指导老师` TINYTEXT DEFAULT NULL,
  `专业代码` varchar(10) DEFAULT NULL,
  `门类` varchar(20) DEFAULT NULL,
  `一级学科` varchar(40) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8
```



## 使用方法

​	

### 2. 运行

 1. 安装好第三方库。

 2. 根据yzw.sql创建数据表（若输出至Excel则不用）

 3. 修改schools.ini文件

 4. 在项目根目录执行

    ```
    python ./yzw/start.py
    ```

附上最终数据

链接：https://pan.baidu.com/s/1T-ejrTdqMTodA1T2DWU9Dg 
提取码：xt3e

## 爬取页面

​	爬取的页面如下，另外每行数据的id由页面的id以及考试范围顺序组成

​	![图2](https://github.com/Hthing/yzw/blob/master/img/page.png)

