# Flask-Web-Base
简述：具有基本工程结构和模板样式的工程模板

##### 工程说明：
```
---app
    |-- main
          |-- __init__.py
          |-- views.py
    |-- static
          |-- loader
                |-- loader.css
          |-- pace
                |-- pace.min.js
                |-- pace_flash.css
          |-- pjax
                |-- application.js
                |-- jquery.pjax.min.js
          |-- cichar_css.css
          |-- favicon.ico
    |-- templates
          |-- index
                |-- index.html
          |-- base.html
          |-- content.html
          |-- file.html
          |-- footer.html
          |-- header.html
    |-- __init__.py
    |-- pjax.py
---config.py
---manage.py
```
##### APP：     
* main为在APP中注册的蓝图，其中包括index路由  
       
* static为静态文件夹：  
  * 其中loader为一份页面加载元素动画  
  * pace是开源的页面加载进度条插件  
  * pjax是开源的用于局部页面加载的插件  
  * cichar_css.css中定义了基本的导航栏和页脚  
  * 同时摘取了bootstrap中的栅格式系统。  
 
* templates为模板文件夹，file.html为样式及js文件引入模板，base.html定义了header,content,footer三部分的划分。
  * 其中header从header.html中加载  
  * footer从footer.html中加载  
  * content从路由中传递的模板加载，例如：  
  * index.html从content.html中继承对content的页面划分，index路由的主体内容在Index.html中完成。  
  * conteng.html只提供基本的content区域划分。 

* __init__.py:  
  * app的初始化  

* pjax.py:  
  * 提供pjax函数供路由使用  
  
       
##### APP配置：config.py  
       对APP的配置
       
##### APP启动入口：manage.py  
       启动APP
       
