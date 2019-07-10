# Django教程

[TOC]

## Django介绍

### 简介

Django，使用Python语言编写的开源Web开发框架，并遵循MVC设计。

Django的主要目的是**简便、快速的开发数据库驱动的网站**。它强调代码复用，多个组件可以很方便的以“插件”形式服务于整个框架，Django有许多功能强大的第三方插件，你甚至可以很方便的开发出自己的工具包。这使得Django具有很强的可扩展性。它还强调快速开发和DRY（DoNotRepeatYourself）原则。

### 特点

1. 重量级框架
   对比Flask框架，Django原生提供了众多的功能组件，让开发更简便快速。
   * 提供项目工程管理的自动化脚本工具
   * 数据库OR支持（对象关系映射，英语：Object Relational Mapping）
   * 模板
   * 表单
   * Admin管理站点
   * 文件管理
   * 认证权限
   * session机制
   * 缓存

2. MVT模式
   有一种程序设计模式叫MVC，其核心思想是分工、解耦，让不同的代码块之间降低耦合，增强代码的可扩展性和可移植性，实现向后兼容。
   * M的全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理
   * V全拼为View，与MVC中的C功能，接受请求，进行业务处理，返回应答
   * T的全拼为Template，与MVC中V功能相同，赋值封装构造要返回的html

## 工程搭建

### 环境安装

1. 创建虚拟环境
   `mkvirtualenv django_demo -p python`

2. 安装Django
   `pip install django==1.11.11`

3. 复习虚拟环境和pip的命令

   ```shell
   # 虚拟环境
   mkvirtualenv name # 创建虚拟环境 name
   rmvirtualenv name # 删除虚拟环境 name
   workon name # 进入虚拟环境 name、查看所有虚拟环境
   deactivate # 退出虚拟环境
   
   # pip命令
   pip list # 查看已安装的依赖包
   pip freeze # 冻结当前环境的依赖包创建工程
   ```

### 创建工程

在使用Flask框架时，项目工程目录的组织与创建是需要我们自己手动创建完成的。
在Django中，项目工程目录可以借助django提供的命令帮助我们创建。

1. 创建
   创建工程的命令：
   `django-admin startproject 工程名称`
   在这里我们创建一个*demo*项目

2. 工程目录说明
   查看创建的工程目录，结构如下：

   ![image5bf92.png](https://miao.su/images/2019/06/21/image5bf92.png)

   * settings.py 是项目的整体配置文件
   * urls.py 是项目的URL配置文件
   * wsgi.py 是项目与WSGI兼容的Web服务器入口
   * manage.py 是项目管理文件，通过它管理项目

3. 运行开发服务器
   在开发阶段，为了能够快速预览到开发的效果，django提供了一个纯python编写的轻量级web服务器，仅在开发阶段使用。
   运行服务器命令如下：

   ```python
   python manage.py runserver ip:port
   ```

   可以不写IP和端口，默认IP是127.0.0.1，端口是8000。

   在浏览器输入网址“47.100.200.127:8000”就可以看到效果。

   * django默认工作在调试Debug模式下，如果增加、修改、删除文件，服务器会自动重启。
   * ctrl+c 可以停止服务器

### 创建子应用

在web应用中，通常有一些业务功能模块是在不同的项目中都可以复用的，故在开发中通常将工程拆分为不同的子功能模块，各功能模块间可以保持相对的独立，在其他工程项目中需要用到某个特定的功能模块时，可以将该模块代码整体复制过去，达到复用的目的。

在Flask中也有类似子功能应用模块的概念，即蓝图Blueprint。
**Django的视图编写是放在子应用中的。**

1. 创建
   在Django中，创建子应用模块目录仍然可以通过命令来操作，即：
   `python manage.py startapp 子应用名`
   *manage.py*为上述创建工程时自动生成的管理文件。
   我们在刚刚创建的*demo*工程中，创建一个用户*Users*子应用模块。
2. 子应用目录说明
   查看此时的工程目录，结构如下：
   ![imageb2f0d.png](https://miao.su/images/2019/06/21/imageb2f0d.png)

* admin.py 文件跟网站的后台管理站点配置相关
* apps.py 文件用于配置当前子应用的相关信息
* migrations 目录用于存放数据库迁移历史文件
* models.py 文件用户保存数据库模型类
* tests.py 文件用于开发测试用例，编写单元测试
* views.py 文件用于编写Web应用视图

3. 注册安装子应用
   创建出来的子应用目录文件虽然被放到了工程中，但是Django工程并不能立即直接使用该子应用，需要注册安装之后才能够使用。

   在工程配置文件setting.py 中，*INSTALLED_APPS*项保存了工程中已经安装的子应用，初识工程汇总的*INSTALL_APP*文件如下：
   ![image12e82.png](https://miao.su/images/2019/06/21/image12e82.png)

   **注册安装一个子应用的方法，即使将子应用的配置信息文件apps.py中的Config类添加到INSTALL_APPS列表中。**
   例如将刚刚创建的Users子应用添加到工程中。添加后如下：

   ![image489db.png](https://miao.su/images/2019/06/21/image489db.png)

### 创建视图

同Flask框架一样，Django也用视图来编写Web应用的业务逻辑。
Django的视图是定义了在子应用的views.py中的。

1. 创建
   打开刚刚创建的Users模块，在views.py中编写视图代码。

   ```python
     1 from django.shortcuts import render
     2 from django.http import HttpResponse
     3 
     4 # Create your views here.
     5 
     6 def index(request):
     7     """视图：
     8     request：用于接收请求request对象
     9     return：响应对象"""                                         
    10     
    11     return HttpResponse('Hello World!')
   ```

   ​	说明：

   * 视图函数的第一个传入参数必须定义，用于接收Django构造的包含了请求数据的*HttpRequest*对象，通常名为*request*。
   * 视图函数的返回值必须为一个响应对象，不能像Flask一样直接返回一个字符串，可以将要返回的字符串数据放到一个*HttpResponse*对象中。

2. 定义路由URL

   1. 在子应用中新建一个urls.py文件用于保存该应用的路由。

   2. 在Users/urls.py文件中定义路由信息

      ```
        1 from django.conf.urls import url
        2 from . import views
        3 
        	# urlpatterns是被django自动识别的路由列表变量
        4 urlpatterns = [
        	# 每个路由信息都需要使用url函数来构造
        5     # url(路径，视图) 使用正则表达式的方式    
        6     url(r'^index/$', views.index ),
        7]
      ```

   3. 在工程总路由demo/urls.py中添加子应用的路由数据

      ```python
       16 # 使用include函数
       17 from django.conf.urls import url, include
       18 from django.contrib import admin
       19 
       20 urlpatterns = [
       21     # Django默认包含的
       22     url(r'^admin/', admin.site.urls),
       23     # 要添加的
       24     url(r'^Users/', include('Users.urls') )
       25     # url(r'^index/$', Users.views.index)                       
       26 ]
      ```

      * 使用include来将子应用users里的全部路由包含进工程路由中；
      * *r‘Users/’*决定了Users子应用的所有路由都以/Users/开头，如我们刚定义的视图index，其最终的完整访问路径为/Users/index/。

      *include*函数除了可以传递字符串之外，也可以直接传递应用的urls模块。如：

      ```python
      from django.conf.urls import url, include
      from django.contrib import admin
      import Users.urls  # 先导入应用的urls模块
      
      urlpatterns = [
          url(r'^admin/', admin.site.urls),
          # url(r'^Users/', include('Users.Urls')),
          url(r'^Users/', include(users.urls)),  # 添加应用的路由
      ]
      ```

   4. 启动运行
      重新启动Django程序

      ```python
      python manage.py runserver 0.0.0.0:8000
      ```

   
   

## 配置、静态文件与路由

1. BASE_DIR
   `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
   当前工程的根目录，Django会依此来定位工程内的相关文件，我们也可以使用该参数来构造文件路径。
2. DEBUG
   调试模式，创建工程后初始值为*True*，即默认工作在调试模式下。作用：
   * 修改代码文件，程序自动启动
   * Django程序出现异常时，向前端显示详细的错误追踪信息，而在非调试模式下，仅返回Server Error(500)
     **注意：**部署线上运行的Django不要运行在调试模式下，记得修改DEBUG=False

3. 本地语言和时区
   Django支持本地化处理，即显示语言与时区支持本地化。
   本地化是将显示语言、时间等使用本地的习惯，这里的本地化就是进行中国化，中国大陆地区使用**简体中文**，时区使用**亚洲/上海**时区，注意这里不使用北京时区表示。
   初始化的工程默认语言和时区为英语和UTC标准时区。

   ```python
   112 # 本地化设置成中文
   113 LANGUAGE_CODE = 'zh-hans'
   114 
   115 # 错误时会有时区显示，另外也会自动转换时区时间
   116 TIME_ZONE = 'Asia/Shanghai'
   ```

### 静态文件

​	项目中的CSS，图片、js都是静态文件。一般会将静态文件放到一个单独的目录中，以方便管理。在html页面中调	用时，也需要制定静态文件的路径，Django中提供了一种解析的方式配置静态文件路径。静态文件可以放在项目根	目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管	理。

​	为了提供静态文件，需要配置两个参数：

* STATICFILES_DIRS 存放查找静态文件的目录 
* STATIC_URL 访问静态文件的URL前缀

#### 示例

1. 在项目根目录下创建static_files目录来保存静态文件

2. 在 *demo/settings.py* 中修改静态文件的两个参数为：

   ```python
   128 STATIC_URL = '/static/'
   129 # 为了解耦合我们不把这个写死 而是使用字符串拼接的方式
   130 STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
   ```

3. 此时在static_files添加的任何静态文件都可以使用网站 **/static/文件在static_files中的路径** 来访问了
   	例如，我们在向static_files目录中添加一个index.html文件，在浏览器中就可以使用 `47.100.200.127:8000/static/index.html` 来访问。
      	或者，我们在static_files目录中添加一个子目录和文件 goods/detail.html，在浏览器中就可以使用`47.100.200.127:8000/static/goods/detail.html`来访问

**注意：**

Django仅在调试模式下（DEBUG=True）能对外提供静态文件。

当DEBUG=False工作在生成模式时，Django不再对外提供静态文件，需要是用collectstatic命令来收集静态文件并提交由其他静态文件服务器来提供。

### 路由说明

![imageb1c5c.png](https://miao.su/images/2019/06/22/imageb1c5c.png)

#### 路由定义位置

Django的主要路由信息定义在工程同名目录下的urls.py文件中，该文件是Django解析路由入口。

每个子应用为了保持相对独立，可以在各个子应用中定义属于自己的urls.py文件来保存该应用的路由。然后用主路由文件包含各应用的子路由数据。

除了上述方式外，也可将工程的全部路由信息都定义在主路由文件中，子应用不再设置urls.py。如：

```python
 17 from django.conf.urls import url 
 18 from django.contrib import admin
 19 import Users.views              
 20                                 
 21                                 
 22 urlpatterns = [                 
 23     # Django默认包含的          
 24     url(r'^admin/', admin.site.urls),
 25     # 要添加的 使用正则表达式匹配
 26     url(r'^Users/index/$', Users.views.index)                                    
 27     # url(r'^index/$', Users.views.index)
 28 ]
```

#### 路由解析顺序

Django在接受到一个请求时，从主路由文件中的 *urlpatterns* 列表中以由上至下的顺序查找对应路由规则，如果发现规则为 *include* 包含，则再进入被包含的 *urls* 中的 *urlpatterns* 列表由上至下进行查询。

值得关注的是**由上至下**的顺序，有可能会使上面的路由屏蔽掉下面的路由，带来非预期的结果。例如：

​	主目录 *urls.py*

```python
 16 # 使用include函数               
 17 from django.conf.urls import url, include 
 18 from django.contrib import admin 
 19 
 20 urlpatterns = [
 21     # Django默认包含的
 22     url(r'^admin/', admin.site.urls),
 23     # 要添加的 使用正则表达式匹配
 24     url(r'^Users/index/$', include('Users.urls'))                                
 25     # url(r'^index/$', Users.views.index)
 26 ]
```

​	子应用目录 *urls.py*

```python
  1 from django.conf.urls import url 
  2 from . import views
  3 
  4 urlpatterns = [
  5     # url(路径，视图) 使用正则表达式的方式    
  6     # url(r'^index/$', views.index ),
  7     # 路由解析的顺序是由上至下，有可能上面的路由会屏蔽下面的路由
  8     url(r'^say',views.say),
  9     url(r'^sayhello', views.sayhello),                                         
 10 ]
```

即使访问 *sayhello* 路径，预期应该进入 *sayhello* 视图执行，但实际优先查找了 *say* 路由规则也与 *sayhello* 路由路径匹配，会屏蔽掉下面的路由。

#### 路由命名和reverse反解析（逆向）

1. 路由命名
   在定义路由的时候，可以为路由命名，方便查找特定视图的具体路径信息。
   
   1. 在使用include函数定义路由时，可以使用namespace参数定义路由的命名空间，如：
   
      ```python
      url(r'^Users/index/$', include('Users.urls', namespace='Users')), 
      ```
   
      命名空间表示，凡是Users.urls中定义的路由，均属于namespace指明的Users名下。
   
   2. 在定义普通路由时，可以使用name参数指明路由的名字，如：
   
      ```python
        4 urlpatterns = [
        5     # url(路径，视图) 使用正则表达式的方式    
        6     url(r'^index/$', views.index, name='index'),
        7     # 路由解析的顺序是由上至下，有可能上面的路由会屏蔽下面的路由
        8     url(r'^say',views.say, name='say'),
        9     # url(r'^sayhello', views.sayhello),                               
       10 ]
      ```
   
   3. reverse反解析
      使用reverse函数，可以根据路由名称，返回具体的路径，如：
   
      ```python
        1 from django.shortcuts import render
        2 from django.http import HttpResponse
        3 # 注意导包的路径
        4 from django.core.urlresolvers import reverse 
        5 
        6 # Create your views here.
        7 
        8 def index(request):
        9     """视图：
       10     request：用于接收请求request对象
       11     return：响应对象"""
       12     
       13     return HttpResponse('Hello World!')
       14 
       15 def say(request):
       16     url = reverse("Users:index")
       17     # 返回 /Users/index 
       18     print(url)
       19 
       20     return HttpResponse("say page")
       21 
       22 def sayhello(request):
       23     return HttpResponse("say hello page")
      ```
   
      * 对于未指明namespace的，reverse（路由name）
      * 对于指明namespace的，reverse（命名空间namespace：路由name）
   
   4. 路径结尾斜线 / 的说明
      Django中定义路由时，通常以斜线/结尾，其好处是用户访问不以斜线/结尾的相同路径时，Django会把用户重定向到以斜线/结尾的路径上，而不会返回404不存在。如：
   
      ```python
      urlpatterns = [
      	url(r'^index/$', views.index, name='index'),
      ]
      ```
   
      用户访问 index 或者 index/ 网址，均能访问到 index 视图。
      **说明：**
      虽然路由结尾带/能够带来上述的好处，但是却违背了HTTP中URL表示资源位置路径的设计理念。是否结尾带/以所属公司定义风格为准。

### App应用配置

在每个应用目录中都包含了apps.py文件，用于保存该应用的相关信息。
在创建应用时，Django会向apps.py文件中写入一个该应用的配置类，如：

```python
  1 from django.apps import AppConfig
  2
  4 class UsersConfig(AppConfig):
  5     name = 'Users' 
```

我们将此类添加到工程 settings.py 的 INSTALLED_APPS 列表中，表名注册安装具备此配置属性的应用。

* AppConfig.name 属性表示这个配置类是加载到哪个应用的，每个配置类必须包含此属性，默认自动生成。

* AppConfig.verbose_name 属性用于设置该应用的直观可读的名字，此名字在Django提供的Admin管理站点中会显示，如：

  ```python
    1 from django.apps import AppConfig
    2 
    4 class UsersConfig(AppConfig):
    5     name = 'Users'
    6     verbose_name = '用户管理' 
  ```

## 请求与响应

### 请求

回想一下，利用HTTP协议向服务器传参有几种途径？

* 提取URL的特定部分，如 /weather/beijing/2018，可以在服务器端的路由中用正则表达式获取
* 查询字符串（query string），形如 key1=value1 & key2=value2
* 请求体（body）中发送的数据，比如表单数据、json、xml
* 在http报头的头（head）中

1. URL路径参数
   在定义路由URL时，可以使用正则表达式提取参数的方法从URL中获取请求参数，Django会将提取的参数直接传递到视图的传入参数中。

   * 未命名参数按名字传递，如：

     ```python
     url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
     
     def weather(request, city, year):
         print('city=%s' % city)
         print('year=%s' % year)
         return HttpResponse('OK')
     ```

   * 命名参数按名字传递，如：

     ```python
     url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
     ```

#### Django中的QueryDict对象

定义在 django.http.QueryDict 中
HttpRequest 对象的属性GET、POST都是QueryDict类型的对象
与python字典不同，QueryDict 类型的对象用来处理同一个键带有多个值的情况

* 方法 get()：根据键获取值
  如果一个键同时拥有多个值将获取**最后一个值**
  如果键不存在则返回None值，可以设置默认值进行后续处理

  ```python
  dict.get('键', 默认值)
  可简写为
  dict['键']
  ```

* 方法 getlist()：根据键获取值，值以列表返回，可以获取指定键的所有值
  如果键不存在则返回空列表[ ]，可以设置默认值进行后续处理

  ```python
  dict.getlist('键', 默认值)
  ```

#### 查询字符串 Query String

获取请求路径中的查询字符串参数（形如 ?k1=v1&k2=v2），可以通过 request.GET 属性获取，返回QueryDict对象。

```python
 31 def qs(request):
 32     a = request.GET.get('a')
 33     b = request.GET.get('b')
 34     alist = request.GET.getlist('a')
 35     print(a)
 36     print(b)
 37     print(alist)
 38     return HttpResponse('OK')
```

**重要：**查询字符串不区分请求形式，即驾驶客户端进行POST方式的请求，依然可以通过request.GET获取请求中的查询字符串数据。

#### 请求体

请求体数据格式不固定，可以是表单类型字符串，可以是JSON字符串，可以是XML字符串，应区别对待。
可以发送请求体数据的请求方式有POST、PUT、PATCH、DELETE。

*Django默认开启了CSRF防护*，会对上述请求方式进行CSRF防护验证，在测试时可以关闭CSRF防护机制，方法为在 settings.py 文件中注释掉CSRF中间件，如：
![imagecabf6.png](https://miao.su/images/2019/06/22/imagecabf6.png)

#### 表单类型 Form Data

前端发送的表单类型的请求体数据，可以通过 request.POST 属性获取，返回 QueryDict对象。

```python
def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')
```

**重要：**只要请求体的数据是表单类型，无论是哪种请求方式（POST、PUT、PATCH、DELETE），都是使用request.POST来获取请求体的表单数据。

#### 非表单类型 Non-Form Data

非表单类型的请求数据，Django无法自动解析，可以通过**request.boby**属性获取最原始的请求体数据，自己按照请求体格式（JSON、XML）进行解析。**request.body返回bytes类型**。
例如要获取请求体中的如下JSON数据：

```python
{"a": 1, "b": 2}
```

可以进行如下方法操作：

```python
import json

def get_body_json():
	json_str = request.body
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')
```

#### 请求头

可以通过**request.META**属性获取请求头headers中的数据，**request.META为字典类型**。

常见的请求头有：

* `CONTENT_LENGTH`——The length of the request body (as a string).

* `CONTENT_TYPE`——The MIME type of the request body.

* `HTTP_ACCEPT`——Acceptable content types for the response.

* `HTTP_ACCEPT_ENCODING`——Acceptable encoding for the response.

* `HTTP_ACCEPT_LANGUAGE`——Acceptable languages for the response.

* `HTTP_HOST`——The HTTP Host header sent by the client.

* `HTTP_REFERER`——The referring page, if any.

* `HTTP_USER_AGENT`——The client’s user-agent string.

* `QUERY_STRING`——The query string, as a single (unparsed) string.

* `REMOTE_ADDR`——The IP address of the client.

* `REMOTE_HOST`——The hostname of the client.

* `REMOTE_USER`——The user authenticated by the Web server, if any.

* `REMOTE_METHOD`——A string such as “GET” or “POST”

* `SERVER_NAME`——The hostname of the server.

* `SERVER_PORT`——The port of the server(as a string).
  具体使用如下：

  ```python
  def get_headers(request):
  	print(request.META['CONTENT_TYPE'])
      return HttpResponse('OK')
  ```

其他常用 HttpRequest 对象属性

* method：一个字符串，表示请求使用的HTTP方法，常用值包括：‘GET’、‘POST’
* user：请求的用户对象
* path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分
* encoding：一个字符串，表示提交的数据的编码方式
  * 如果为None则表示使用浏览器的默认设置，一般为 utf-8
  * 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
* FILES：一个类似于字典的对象，包含所有的上传文件

### 响应

视图在接受请求并处理后，必须返回HTTPResponse对象或子对象。HTTPResponse对象由Django创建，HTTPResponse对象由开发人员创建。

#### HttpResponse

可以使用**django.http.HttpResponse**来构造响应对象。

```python
Response(content=响应体， content_type=响应体数据结构, status=状态码)
```

也可以通过HttpResponse对象属性来设置响应体、响应体数据类型、状态码：

* content：表示返回的内容
* status_code：返回的HTTP响应状态码
* content_type：指定返回数据的MIME类型

响应头可以直接将HTTPResponse对象当做字典进行响应头键值对的设置：

```python
response = Response()
# 自定义响应头jhon，值为tina
response['jhon'] = ['tina'] 
```

示例：

```python
 55 def demo_view(request):
 56     return HttpResponse('jhon tina', status=400)
 57     # 或者                                                                    
 58     response = HttpResponse('jhon tina')
 59     response.status_code = 400
 60     response['jhon'] = 'tina'
 61     return response 
```

#### HTTPResponse子类

Django提供了一系列HTTPResponse的子类，可以快速设置状态码：

* HttpResponseRedirct 301
* HttpResponsePermanentRedirect 302
* HttpResponseNotModified 304
* HttpResponseBadRequest 400
* HttpResponseNotFound 404
* HttpResponseForbidden 403
* HttpResponseNotAllowed 405
* HttpResponseGone 410
* HttpResponseServerError 500

#### JsonResponse

若要返回json数据，可以使用JsonResponse来构造响应对象，作用：

* 帮助我们将数据转换为json字符串
* 设置响应头**Content-Type**为**application/json**

```python
11 from django.http import JsonResponse
65 def demo_view2(request):
66     return JsonResponse({'city': 'beijing', 'subject': 'python'}) 
```

#### redirect重定向

若要使用重定向，可以通过 ` from django.shortcut import redirect`导入

```python
 69 def demo_view3(request):
 70     return redirect('http://47.100.200.127')
```

## Cookie

Cookie，有时也用其复数形式Cookies，指某些网站为了辨别用户的身份、进行session跟踪而存储在用户本地终端上的数据（通常经过加密）。Cookie最早是网景公司的前雇员Lou Montulli在1993年3月发明的。

Cookie是有服务器端生成，发送给User-Agent（一般是浏览器），浏览器会将Cookie的key/value保存到某个目录下的文本文件内，下次请求同一个网站时就发送该Cookie给服务器（前提是浏览器设置为启动Cookie）。Cookie名称和值可以由服务器端开发自己的定义，这样服务器可以知道该用户是否是合法用户以及是否需要重新登录等。服务器可以利用Cookies包含信息的任意性来筛选并经常性维护这些信息，以判断在HTTP传输中的状态。Cookie最典型记住用户名。

Cookie是存储在浏览器中的一段纯文本信息，建议不要存储敏感信息如密码，因为电脑上的浏览器可能被其他人使用。

### Cookie的特点

* Cookie以键值对的格式进行信息的存储
* Cookie基于域名安全，不同域名的Cookie是不能互相访问的
* 当浏览器请求某网站时，会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器

### 设置Cookie

可以通过**HttpResponse**对象中的**set_cookie**方法来设置Cookie。

```python
 60     response = HttpResponse('jhon tina')
 61     response.set_cookie('name', value='Tina_M', max_age=6000)
```

* max_age 单位为秒，默认为None。如果是临时Cookie，可将 max_age 设置为None

### 读取Cookie

可以通过HTTPRequest对象的COOKIES属性来读取本次请求携带的Cookie值。**request.COOKIES为字典类型**。

```python
 66 def demo_view2(request):
 67     cookie1 = request.COOKIES.get('name')
 68     print(cookie1)                                                              
 69     return JsonResponse({'city': 'beijing', 'subject': 'python'})
```

## Session

### 启用session

*Django项目默认启动Session*
可以在 setting.py 文件中查看，如下：
![image8b2fb.png](https://miao.su/images/2019/06/23/image8b2fb.png)

如需禁用session，将上图中的session中间件注释掉即可。

### 存储方式

在setting.py文件中，可以设置session数据的存储方式，可以保存在数据库、本地缓存等。

#### 数据库

存储在数据库中，如下设置可以写，也可以不写，这是**默认存储方式**。

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
```

如果存储在数据库中，需要项 INSTALLED_APPS 中安装 session 应用。
![image08a0a.png](https://miao.su/images/2019/06/23/image08a0a.png)

#### 本地缓存

存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快。

```python
SESSION_ENGINE = 'django.contrib.session.backends.cache'
```

#### 混合存储

优先从本机内存中存取，如果没有则从数据库中存取。

```python
SESSION_ENGINE = 'django.contrib.session.backends.cached_db'
```

#### Redis

在Redis中保存session，需要引入第三方扩展，我们可以使用**django-rendis**来解决。

1. 安装扩展

   ```python
   pip install django-redis
   ```

2. 配置
   在setting.py文件中做如下配置：

   ```python
   133 CACHES = {
   134     "default": {
   135         "BACKEND": "django_redis.cache.RedisCache",
   136         "LOCATION": "redis://47.100.200.127:6379/1",
   137         "OPTIONS": {
   138             "CLIENT_CLASS": "django_redis.client.DefaultClient",
   139         }
   140     }
   141 }
   142 
   143 SESSION_ENGINE = "django.contrib.sessions.backends.cache"
   144 SESSOPM_CACHE_ALIAS = "default"  
   ```

3. session操作
   通过HttpRequest对象的session属性进行会话的读写操作。

   1. 以键值对的格式写session

      ```python
      request.session['键'] = 值
      ```

   2. 根据键读取值

      ```python
      request.session.get('键'，默认值)
      ```

   3. 清楚所有session数据，在存储中删除值部分

      ```python
      request.session.clear()
      ```

   4. 清楚session数据，在存储中删除session的整条数据

      ```python
      request.session.flush()
      ```

   5. 删除session中的指定键及值，在存储中只删除某个键及对应的值

      ```python
      del request.session['键']
      ```

   6. 设置session的有效值

      ```python
      request.session.set_expiry(value)
      ```

      * 如果value是一个整数，session将在value秒没有活动后过期
      * 如果value为0，那么用户session的cookie将在用户的浏览器关闭后过期
      * 如果value为None，那么session有效期将采用系统默认值，**默认为两周**，可以通过在settings.py中设置**SESSION_COOKIE_AGE**来设置全局默认值

      

## 类视图和中间件

### 类视图

#### 类视图引入

以函数的方式定义的视图叫做**函数视图**，函数视图便于理解。但是遇到一个视图对应的路径提供了多种不同HTTP请求方式的支持，便需要在一个函数中编写不同的业务逻辑，代码可读性与复用性不佳。

```python
 79 def register(request):
 80     """处理注册信息"""
 81     # 获取请求方法，判断是GET/POST请求
 82     if request.method == 'GET':
 83         # 处理GET请求，返回注册页面
 84         return render(request, 'register.html')
 85     else:
 86         # 处理POST请求，实现注册逻辑
 87         return HttpResponse('这里实现注册逻辑')  
```

在Django中也可以使用类来定义一个视图，称为**类视图**。
使用类视图可以将视图对应的不同的请求方式以类中的不同方法来区别定义。如下：

```python
 93 class RegisterView(View):
 94     """类视图，处理注册"""
 95        
 96     def get(self, request):
 97         """处理GET请求，返回注册页面"""
 98         return render(request, 'register.html')
 99        
100     def post(self, request):
101         """处理POST请求，实现注册逻辑"""
102         return HttpResponse('这里实现注册逻辑') 
```

类视图的好处：

* 代码的可读性好
* 类视图相对于函数视图有更高的**复用性**，如果其他地方需要用到某个类视图的某个特定逻辑，直接继承该类视图即可

#### 类视图的使用

定义类视图需要继承自Django提供的父类**View**，可使用`from django.views.generic import View`导入，定义方式上面已经展示过了。
*配置路由时，使用类视图的`as_view()`方法来添加*

```python
 19     # 类视图：注册
 20     url(r'^register/$', views.RegisterView.as_view(), name='register'),    
```

#### 类视图原理

```python
 @classonlymethod
    def as_view(cls, **initkwargs):
        """
        Main entry point for a request-response process.
        """
        ...省略代码...

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            # 调用dispatch方法，按照不同请求方式调用不同请求方法
            return self.dispatch(request, *args, **kwargs)

        ...省略代码...

        # 返回真正的函数视图
        return view


    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```

#### 类视图使用装饰器

为类视图添加装饰器，可以使用三种方法、

为了理解方便，我们先来定义一个**为函数视图准备的装饰器**（在设计装饰器时基本都以函数视图作为考虑的被装饰对象），及一个要被装饰的类视图。

```python
104 def my_decorator(func):
105     def wrapper(request, *args, **kwargs):
106         print('自定义装饰器被调用了')
107         print('请求路径%s' % request.path)
108         return func(request, *args, **kwargs)
109     return wrapper
110 
111 
112 class DemoView(View):
113     def get(self, request):
114         print('get方法')
115         return HttpResponse('OK')
116 
117     def post(self, request):
118         print('post方法')
119         return HttpResponse('OK')   
```

#### 在URL配置中装饰

```python
22     url(r'^demo/$', views.my_decorator(views.DemoView.as_view())),  
```

此种方式最简单，但因装饰行为被放置到了url配置中，单看视图的时候无法知道此视图还被添加了装饰器，不利于代码的完整性，不建议使用。

**此种方式会为类视图中的所有请求方法都加上装饰器行为。**（因为是在视图入口处，分发请求方式前）

#### 在类视图中装饰

在类视图中使用为函数视图准备的装饰器时，不能直接添加装饰器，需要使用**method_decorator**将其转换为适用于类视图方法的装饰器。

```python
	views.py
122 # 为特定请求方法添加装饰器
123 class DemoView2(View):
124 
125     @method_decorator(my_decorator)
126     def get(selt, request):
127         print('get方法')
128         return HttpResponse('OK')
129 
130     def post(self, request):                                         
131         print('post方法')
132         return HttpResponse('OK')
	
	urls.py
 23     url(r'^demo4/$', views.DemoView2.as_view()),
```

method_decorator 装饰器还支持使用name参数指明被装饰的方法

```python
135 # 使用name参数指明被装饰的方法
136 @method_decorator(my_decorator, name='post')                         
137 class DemoView3(View):
138     def get(self, request):
139         print('get就是这样')
140         return HttpResponse('OK')
141 
142     def post(self, request):
143         print('post不是你想要的')
144         return HttpResponse('OK')
```

*那么，为什么我们需要使用method_decorator???*
为函数视图准备的装饰器，其被调用时，第一个参数用于接收response对象

```python
def my_decorate(func):
    def wrapper(request, *args, **kwargs):  # 第一个参数request对象
        ...代码省略...
        return func(request, *args, **kwargs)
    return wrapper
```

而类视图中请求方法被调用时，传入的第一个参数不是request对象，而是self视图对象本身，第二个位置参数才是request对象。

```python
class DemoView(View):
    def dispatch(self, request, *args, **kwargs):
        ...代码省略...

    def get(self, request):
        ...代码省略...
```

所以如果直接将用于函数视图的装饰器装饰类视图方法，会导致参数传递出现问题。
*method_decorator的作用是为函数视图装饰器补充第一个self参数，以适配类视图的方法。*
如果将装饰器本身改为可以适配类视图方法的，类似如下，则无需再使用method_decorator。

```python
def my_decorator(func):
    def wrapper(self, request, *args, **kwargs):  # 此处增加了self
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(self, request, *args, **kwargs)  # 此处增加了self
    return wrapper
```

#### 构造Mixin扩展类

使用面向对象多继承的特性。

```python
147 class MyDecoratorMixin(object):
    	# 注意，这里不要写错
148     @classmethod
149     def as_view(cls, *args, **kwargs):
150         view = super().as_view(*args, **kwargs)
151         view = my_decorator(view)
152         return view
153 
154 class DemoView4(MyDecoratorMixin, View):                             
155     def get(self, request):
156         print('get, 你想知道什么')
157         return HttpResponse('OK')
158 
159     def post(self, request):
160         print('post, 我想你需要平稳')
161         return HttpResponse('OK')
```

使用Mixin扩展类，也会为类视图的所有请求方法都添加装饰行为。

### 中间件

Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或者输出。中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性。
我们可以使用中间件在Django处理视图的不同阶段对输入或输出进行干预。

#### 中间件的定义方法

定义一个中间件工厂函数，然后返回一个可以被调用的中间件。中间件工厂函数需要接受一个可以调用的get_response对象。返回的中间件也是一个可以被调用的对象，并且像视图一样需要接收一个request对象参数，返回一个response对象。

```python
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用。
        return response
    return middleware
```



例如，在Users应用中新建一个middleware.py文件：

```python
  2 def my_middleware(get_response):
  3     print('init 被调用')
  4 
  5     def middleware(request):
  6         print('before request 被调用')
  7         response = get_response(request)
  8         print('after response 被调用')
  9         return response
 10     
 11     return middleware 
```

定义好中间件之后，需要在setting.py文件中添加注册中间件:
![imagef1d15.png](https://miao.su/images/2019/06/23/imagef1d15.png)

定义一个视图进行测试：

```python
	views.py:
164 def exm_view(request):
165     print('view 视图被调用')
166     return HttpResponse('OK') 

	urls.py:
 26     url(r'^exm/$', views.exm_view),
```

*注意：Django运行在调试模式下，中间件init部分有可能被调用两次。*

#### 多个中间件的执行顺序

* 在请求视图被处理**前**，中间件**由上至下**依次执行
* 在请求视图被处理**后**，中间件**由下至上**一次执行
  ![image8a4da.png](https://miao.su/images/2019/06/23/image8a4da.png)

示例：
定义两个中间件

```python
  2 def my_middleware(get_response):
  3     print('init 被调用')
  4 
  5     def middleware(request):
  6         print('before request 被调用')
  7         response = get_response(request)
  8         print('after response 被调用')
  9         return response
 10 
 11     return middleware 
 12 
 13 
 14 def my_middleware2(get_response):
 15     print('init2 被调用')
 16 
 17     def middleware(request):
 18         print('before request2 被调用')
 19         response = get_response(request)
 20         print('after response2 被调用')                              
 21         return response
 22    
 23     return middleware 
```

注册添加两个中间件：
![imagea1d01.png](https://miao.su/images/2019/06/23/imagea1d01.png)

执行结果：
![image8fbf2.png](https://miao.su/images/2019/06/23/image8fbf2.png)



## 数据库

### ORM框架

O是object，也就是**类对象**的意思；R是relation，也就是**关系**；M是mapping，也就是**映射**。所以ORM就是关系数据库中**数据表**的意思。在ORM框架中，它会帮我们把类和数据表进行了一个映射，可以让我们*通过类和类对象就能够操作它所对应的表格中的数据*。ORM框架还有一个功能，它可以*根据我们设计的类自动帮我们生成数据库中的表格*，省去了我们自己建表的过程。

Django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作。

使用Django进行数据库开发的步骤如下：

1. 配置数据库连接信息
2. 在models.py中定义模型类
3. 迁移
4. 通过类和对象完成数据的增删改查

### ORM作用

![image16916.png](https://miao.su/images/2019/06/23/image16916.png)

### 配置

在settings.py中保存了数据库的连接配置信息，Django默认初识配置使用**sqlite**数据库。

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

1. 使用**Mysql**数据库首先需要安装驱动程序

   ```shell
   pip install PyMsSQL
   ```

2. 在Django的工程同名子目录的__ init__.py 文件中添加如下语句：

   ```python
     1 from pymysql import install_as_MySQLdb 
     2 
     3 install_as_MySQLdb()
   ```

   作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。

3. 修改**DATABASES**配置信息

   ```python
    80 DATABASES = {
    81     'default': {
    82         'ENGINE': 'django.db.backends.mysql',
    83         'NAME': 'django_demo',
    84         'USER': 'jhonchen',
    85         'HOST': '47.100.200.127',
    86         'PASSWORD': '**********',
    87         'PORT': 3306
    88                                                       
    89     }
    90 }
   ```

4. 在Mysql中创建数据库

   ```mysql
   create database django_demo default charset=utf8;
   ```

#### 定义模型类

* 模型类被定义在`应用/models.py`文件中
* 模型类必须继承自Model类，位于包 django.db.models中

#### 例子

1. 定义
   创建应用booktest，在model.py 文件中定义模型类。

   ```python
   from django.db import models                                                 
     2 
     3 # Create your models here.
     4 
     5 # 定义图书模型类BookInfo
     6 class BookInfo(models.Model):
     7     btitle = models.CharField(max_length=20, verbose_name='名称')
     8     bpub_data = models.DateField(verbose_name='发布日期')
     9     bread = models.IntegerField(default=0, verbose_name='阅读量')
    10     bcomment = models.IntegerField(default=0, verbose_name='评论量')
    11     is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    12 
    13 
    14     class Meta:
    15         # 指明数据库表名
    16         db_table = 'tb_books'
    17         # 在admin站点中显示的名称
    18         verbose_name = '图书'
    19         # 显示的复数名称
    20         verbose_name_plural = verbose_name
    21 
    22     def __str__(self):
    23         """定义每个数据对象的显示信息"""
    24         return self.btitle
    25 
    26 
    27 # 定义影响模型类HeroInfo
    28 class HeroInfo(models.Model):
    29     GENDER_CHOICES = (
    30         (0, 'male'),
    31         (1, 'female')
    32     )
    33     hname = models.CharField(max_length=20, verbose_name='姓名')
    34     hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, ver
    35     hcomment = models.CharField(max_length=200, null=True, verbose_name='描述
    36     hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_nam
    37     is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    38 
    39 
    40     class Meta:
    41         db.table = 'tb_heros'
    42         verbose_name = '英雄'
    43         verbose_name_plural = verbose_name
    44 
    45     def __str__(self):
    46         return self.hname 
   ```

   * 数据库表名
     模型类如果没有指明表名，Djang默认以**小写app应用名——小写模型类名**为数据库表名
     可通过**db_table**指明数据库表名

   * 关于主键
     Django会为表创建自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后Django不会再创建自动增长的主键列。
     默认创建的主键列属性为id，可以使用pk代替，pk的全拼为primary key

   * 属性命名限制
     *不能是python的保留关键字*
     *不允许使用连续的下划线*
     *定义属性时需要指定字段类型，通过字段类型的参数指定选项，语法如下：*

     ```python
     属性=models.字段类型(选项)
     ```

   * 字段类型

     | 类型             | 说明                                                         |
     | ---------------- | ------------------------------------------------------------ |
     | AutoField        | 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性 |
     | BooleanField     | 布尔字段，值为True或False                                    |
     | NullBooleanField | 支持Null、True、False三种值                                  |
     | CharField        | 字符串，参数max_length表示最大字符个数                       |
     | TextField        | 大文本字段，一般超过4000个字符时使用                         |
     | IntegerField     | 整数                                                         |
     | DecimalField     | 十进制浮点数，参数max_digits表示总位数，参数decimal_places表示小数位数 |
     | FloatField       | 浮点数                                                       |
     | DateField        | 日期，参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于最后一次修改的时间戳，它总是使用当前的日期，默认为False。 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为False。 这两个参数是互相排斥的，组合将会发生错误。 |
     | TimeField        | 时间，参数同DateField                                        |
     | DateTimeField    | 日期时间，参数同DateField                                    |
     | FileField        | 上传文件字段                                                 |
     | ImageField       | 继承与FileField，对上传的内容进行校验，确保是有效的图片      |

   * 选项

     | 选项        | 说明                                                         |
     | ----------- | ------------------------------------------------------------ |
     | null        | 如果为True，表示运行为空，默认为False                        |
     | blank       | 如果为True，则该字段允许为空，默认值是False                  |
     | db.column   | 字段的名称，如果未指定，则使用属性的名称                     |
     | db.index    | 若值True，则该字段允许为空白，默认值是False                  |
     | default     | 默认                                                         |
     | primary_key | 若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用 |
     | unique      | 如果为True，这个字段在表中必须有唯一值，默认值是False        |

     **null是数据库范畴的概念，blank是表单验证范畴的**

   * 外键
     在设置外键时，需要通过**on_delete**选项指明主表删除数据时，对于外键引用表数据如果处理，在django.db.models中包含了可选常量：

     * CASCADE 级联，删除主表数据时连通一起删除外键表中的数据

     * PROTECT 保护，通过抛出ProtectError异常，来阻止删除主表中被外键应用的数据

     * SET_NULL 设置为NULL，仅在该字段null=True允许为null时使用

     * SET_DEFAULT 设置为默认值，仅在该字段设置了默认值时可用

     * SET() 设置为特定值或者调用特定方法，如

       ```python
        51 def get_sentinel_user():
        52     return get_user_model().object.get_or_create(username='delete')[0]
        53 
        54 
        55 class MyModel(models.Model):
        56     user = models.ForeignKey(
        57         settings.AUTH_USER_MODEL,
        58         on_delete=models.SET(get_sentinel_user),
        59     ) 
       ```

       * DO_NOTHING 不做任何操作，如果数据库前置指明级联性，此选项会抛出IntegrityError异常

### 迁移

将模型类同步到数据库中。

1. 生成迁移文件

   ```shell
   python manage.py makemigrations
   ```

   ![image3792e.png](https://miao.su/images/2019/06/24/image3792e.png)

2. 同步到数据库中

   ```python
   python manage.py migrate
   ```

   ![imagef771e.png](https://miao.su/images/2019/06/24/imagef771e.png)

### 添加测试数据

```mysql
mysql> insert into tb_books(btitle,bpub_data,bread,bcomment,is_delete) values
    -> ('射雕英雄传','1980-5-1',12,34,0),
    -> ('天龙八部','1986-7-24',36,40,0),
    -> ('笑傲江湖','1995-12-24',20,80,0),
    -> ('雪山飞狐','1987-11-11',58,24,0);
```

```mysql
mysql> insert into tb_heros(hname,hgender,hbook_id,hcomment,is_delete) values
    -> ('郭靖',1,1,'降龙十八掌',0),
    -> ('黄蓉',0,1,'打狗棍法',0),
    -> ('黄药师',1,1,'弹指神通',0),
    -> ('欧阳锋',1,1,'蛤蟆功',0),
    -> ('梅超风',0,1,'九阴白骨爪',0),
    -> ('乔峰',1,2,'降龙十八掌',0),
    -> ('段誉',1,2,'六脉神剑',0),
    -> ('虚竹',1,2,'天山六阳掌',0),
    -> ('王语嫣',0,2,'神仙姐姐',0),
    -> ('令狐冲',1,3,'独孤九剑',0),
    -> ('任盈盈',0,3,'弹琴',0),
    -> ('岳不群',1,3,'华山剑法',0),
    -> ('东方不败',0,3,'葵花宝典',0),
    -> ('胡斐',1,4,'胡家刀法',0),
    -> ('苗若兰',0,4,'黄衣',0),
    -> ('程灵素',0,4,'医术',0),
    -> ('袁紫衣',0,4,'六合拳',0);
```

### 演示工具使用

#### shell工具

Django的manage工具提供了**shell**命令，帮助我们配置好当前工程的运行环境（如连接好数据库等），以便可以直接在终端中执行测试python语句。
通过如下命令进入shell：（不就是ipython么）

```shell
python manage.py shell
```

![image8f0c4.png](https://miao.su/images/2019/06/24/image8f0c4.png)

导入两个模型类，以便后续使用：

```python
from Users.models import BookInfo, HeroInfo
```



#### 查看MySQL数据库日志

查看mysql数据库日志可以查看对数据库的操作纪录。mysql日志文件默认没有产生，需要做如下配置：

```shell
sudo vim /etc/my.cnf
```

![imagec5e53.png](https://miao.su/images/2019/06/24/imagec5e53.png)

修改之后重启mysql服务，然后使用如下命令打开mysql日志文件：

```shell
tail -f /var/log/mysql/mysql.log  # 可以实时查看数据库的日志内容
```



### 数据库的增删改查

#### 增加

增加数据有两种方法：

1. **save**
   通过创建模型类对象，执行对象的save()方法保存到数据库中。

   ```shell
   >>> from datetime import date
   >>> book = BookInfo(
       btitle='西游记',
       bpub_data=date(1988,1,1),
       bread=10,
       bcomment=10
   )
   >>> book.save()
   >>> hero = HeroInfo(
       hname='孙悟空',
       hgender=0,
       hbook=book
   )
   >>> hero.save()
   >>> hero2 = HeroInfo(
       hname='猪八戒',
       hgender=0,
       hbook_id=book.id
   )
   >>> hero2.save()
   ```

2. **create**
   通过`模型类.objects.create()`保存

   ```shell
   >>> hero2.save()
   >>> HeroInfo.objects.create(
   ... hname='沙悟净',
   ... hgender=0,
   ... hbook=book)
   <HeroInfo: 沙悟净>
   ```

#### 查询

1. 基本查询
   **get**查询单一结果，如果不存在会抛出**模型类.DoesNotExist**异常。
   **all**查询多个结果。
   **count**查询结果数量。

```shell
>>> BookInfo.objects.all()
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>, <BookInfo: 西游记>]>
>>> book = BookInfo.objects.get(btitle='西游记')
>>> book.id
5
>>> BookInfo.objects.get(id=3)
<BookInfo: 笑傲江湖>
>>> BookInfo.objects.get(id=100)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/jhonchen/.virtualenvs/django_py3/lib/python3.5/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/jhonchen/.virtualenvs/django_py3/lib/python3.5/site-packages/django/db/models/query.py", line 380, in get
    self.model._meta.object_name
Users.models.DoesNotExist: BookInfo matching query does not exist.
>>> BookInfo.objects.count()
5
```

2. 过滤查询
   实现SQL中的where功能，包括

   * **filter**过滤出多个结果
   * **exclude**排除掉符合条件剩下的结果
   * **get**过滤单一结果

   对于过滤条件的使用，上述三个方法相同，故仅以**filter**进行讲解。
   过滤条件的表达语法如下：

   ```shell
   属性名称_比较运算符=值
   # 属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线
   ```

   1. 相等
      **exact：表示判等**

      ```shell
      >>> BookInfo.objects.filter(id__exact=1)
      <QuerySet [<BookInfo: 射雕英雄传>]>
      ```

   2. 模糊查询
      **contains：包含与否**

      *注：如果要包含%，不需要转义直接写即可*

      ```shell
      >>> BookInfo.objects.filter(btitle__contains='传')
      <QuerySet [<BookInfo: 射雕英雄传>]>
      ```

      **startswith、endswith：以指定值开头或结尾**

      ```shell
      >>> BookInfo.objects.filter(btitle__endswith='部')
      <QuerySet [<BookInfo: 天龙八部>]>
      ```

      *注：以上运算符都区分大小写，在这些运算符前加上 i 表示不区分大小写，如 iexact、icontains、istartswith*

   3. 空查询
      **isnull：是否为null**

      ```shell
      >>> BookInfo.objects.filter(btitle__isnull=False)
      <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>, <BookInfo: 西游记>]>
      ```

   4. 范围查询
      **in：是否包含在范围内**

      ```shell
      >>> BookInfo.objects.filter(id__in=[1,3,5])
      <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 笑傲江湖>, <BookInfo: 西游记>]>
      ```

   5. 比较查询

      * **gt**大于（greater than）
      * **gte**大于等于（greater than equal）
      * **lt**小于（less than）
      * **lte**小于等于（less than equal）

      ```shell
      >>> BookInfo.objects.filter(id__lt=3)
      <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
      ```

      *不等于的运算符，使用exclude()过滤器*

      ```shell
      >>> BookInfo.objects.exclude(id=3)
      <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>, <BookInfo: 西游记>]>
      ```

   6. 日期查询
      **year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算**

      ```shell
      >>> BookInfo.objects.filter(bpub_data__year=1980)
      <QuerySet [<BookInfo: 射雕英雄传>]>
      >>> BookInfo.objects.filter(bpub_data__gt=date(1990,1,1))
      <QuerySet [<BookInfo: 笑傲江湖>]>
      ```

   7. F对象
      之前的查询都是对象的属性与常量的比较，两个属性怎么比较呢？我们可以使用定义在 `django.db.models`中的F对象。
      语法如下：

      ```shell
      F(属性名)
      ```

      ```shell
      >>> BookInfo.objects.filter(bread__gte=F('bcomment'))
      <QuerySet [<BookInfo: 雪山飞狐>, <BookInfo: 西游记>]>
      ```

      可以在F对象上使用算数运算。

      ```shell
      >>> BookInfo.objects.filter(bread__gt=F('bcomment') * 2)
      <QuerySet [<BookInfo: 雪山飞狐>]>
      ```

   8. Q对象
      **多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字**。

      ```shell
      >>> BookInfo.objects.filter(bread__gt=20,id__lt=3)
      <QuerySet [<BookInfo: 天龙八部>]>
      ```

      或者

      ```shell
      >>> BookInfo.objects.filter(bread__gt=20).filter(id__lt=3)
      <QuerySet [<BookInfo: 天龙八部>]>
      ```

      **如果需要实现逻辑或or的查询，需要使用Q( )对象结合 | 运算符**，Q对象被定义在django.db.models中。
      语法如下：

      ```shell 
      Q(属性名__运算符=值)
      ```

      ```shell
      >>> BookInfo.objects.filter(Q(bread__gt=20))
      <QuerySet [<BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
      ```

      Q对象可以使用 &、| 连接，&表示逻辑与，| 表示逻辑或。

      ```shell
      >>> BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
      <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
      ```

      Q对象前可以使用~操作符，表示非not

      ```shell
      >>> BookInfo.objects.filter(~Q(pk=3))
      <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>, <BookInfo: 西游记>]>
      ```

   9. 聚合函数

      使用aggregate( )过滤器调用聚合函数。聚合函数包括：**Avg**平均、**Count**数量、**Max**最大、**Min**最小、**Sum**求和，被定义在django.db.models中。

      ```shell
      >>> from django.db.models import Sum
      >>> BookInfo.objects.aggregate(Sum('bread'))
      {'bread__sum': 136}
      ```

      *注意：aggregate的返回值是一个字典类型*，格式如下：

      ```shell
      {'属性名__聚合类小写'：值}
      如：{'bread__sum':3}
      ```

      使用count时一般不使用aggregate( )过滤器

      ```shell
      >>> BookInfo.objects.count()
      5
      ```

      *注意：count函数的返回值是一个数字*

### 排序

使用**order_by**对结果进行排序

```shell
>>> BookInfo.objects.all().order_by('bread')
<QuerySet [<BookInfo: 西游记>, <BookInfo: 射雕英雄传>, <BookInfo: 笑傲江湖>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>

>>> BookInfo.objects.all().order_by('-bread')
<QuerySet [<BookInfo: 雪山飞狐>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 射雕英雄传>, <BookInfo: 西游记>]>
```



### 关联查询

由一到多的访问语法：
一对一的模型类对象.多对一的模型类名_set.all( )：

```shell
b = BookInfo.objects.get(id=1)
b.heroinfo_set.all()
<QuerySet [<HeroInfo: 郭靖>, <HeroInfo: 黄蓉>, <HeroInfo: 黄药师>, <HeroInfo: 欧阳锋>, <HeroInfo: 梅超风>]>
```

由多到一的访问语法：
多对一的模型类对象.多对一的模型类中的关系类属性名：

```shell
>>> h = HeroInfo.objects.get(id=1)
>>> h.hbook
<BookInfo: 射雕英雄传>
```

访问一对多的模型类关联对象的id语法：
多对一的模型类对象.关联属性_id:

```python
>>> h = HeroInfo.objects.get(id=1)
>>> h.id
```



### 关联过滤查询

*由多模型类条件查询一模型类数据*

```shell
关联模型类名小写__属性名__条件运算符=值
```

*注意：如果没有“__运算符‘部分，表示等于*

```python
>>> BookInfo.objects.filter(heroinfo__hname='孙悟空')
<QuerySet [<BookInfo: 西游记>]>

>>> BookInfo.objects.filter(heroinfo__hcomment__contains='八')
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
```

*由一模型类条件查询多模型类数据*

```shell
一模型类关联属性名__一模型类属性名__条件运算符=值
```

*注意：如果没有“__运算符”部分，表示等于*

```python
>>> HeroInfo.objects.filter(hbook__btitle='天龙八部')
<QuerySet [<HeroInfo: 乔峰>, <HeroInfo: 段誉>, <HeroInfo: 虚竹>, <HeroInfo: 王语嫣>]>

>>> HeroInfo.objects.filter(hbook__bread__gt=30)
<QuerySet [<HeroInfo: 乔峰>, <HeroInfo: 段誉>, <HeroInfo: 虚竹>, <HeroInfo: 王语嫣>, <HeroInfo: 胡斐>, <HeroInfo: 苗若兰>, <HeroInfo: 程灵素>, <HeroInfo: 袁紫衣>]>
```



### 修改

修改更新有两种方法

1. save
   *修改模型类对象的属性，然后执行save( )方法*

   ```python
   >>> hero = HeroInfo.objects.get(hname='猪八戒')
   >>> hero.hname = '猪悟能'
   >>> hero.save()
   ```

2. update
   *使用模型类.objects.filter().update()*，会返回受影响的行数

   ```python
   >>> HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')
   1
   ```

### 删除

*删除有两种方法*

1. 模型类对象delete

   ```python
   >>> hero = HeroInfo.objects.get(id=13)
   >>> hero.delete()
   (1, {'Users.HeroInfo': 1})
   ```

2. 模型类.objects.filter().delete()

   ```python
   >>> HeroInfo.objects.filter(id=14).delete()
   (1, {'Users.HeroInfo': 1})
   ```



### 查询集 QuerySet

#### 概念

Django的ORM中存在查询集的概念。
查询集，也称查询结果集、QuerySet，表示从数据库中获取的对象集合。
当调用如下过滤器方法时，Django会返回查询集（而不是简单的列表）：

* all()：返回所有数据
* filter()：返回满足条件的数据
* exclude()：返回满足条件之外的数据
* order_by()：对结果进行排序

对查询集可以再次调用过滤器进行过滤，如：

```python
>>> BookInfo.objects.filter(bread__gt=30).order_by('bpub_data')
<QuerySet [<BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
```

也就意味着查询集可以含有零个、一个或者多个过滤器。过滤器基于所给的参数限制查询的结果。
**从SQL的角度讲，查询集与select语句等价，过滤器像where、limit、order_by子句**。
判断某一个查询集中是否有数据：

* exists()：判断查询集中是否有数据，如果有则返回True，没有则返回False。

#### 两大特性

##### 惰性执行

创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用。
例如，当执行如下语句时，并未进行数据库查询，只是创建了一个查询集qs：

```python
>>> qs= BookInfo.objects.all()
```

继续执行遍历操作后，才真正的进行了数据库的查询:

```python
for book in qs:
	print(book.btitile)
```

##### 缓存

使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。
**情况一**：如下是两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载。

```python
>>> [book.id for book in BookInfo.objects.all()]
[1, 2, 3, 4, 5]
>>> [book.id for book in BookInfo.objects.all()]
[1, 2, 3, 4, 5]
```

**情况二**：经过存储后，可以重用查询集，第二次使用缓存中的数据

```python
>>> qs = BookInfo.objects.all()
>>> [book.id for book in qs]
[1, 2, 3, 4, 5]
>>> [book.id for book in qs]
[1, 2, 3, 4, 5]
```

##### 限制查询集

可以对查询集进行去下标或切片操作，等同于sql中的limit和offset子句。

*注意：不支持负数索引。*

**对查询集进行切片后返回一个新的查询集，不会立即执行查询**
如果获取一个对象，直接使用`[0]`，等同于`[0:1].get()`，但是如果没有数据，`[0]`引发IndexError异常，`[0:1].get()`如果没有数据引发DoesNotExist异常。

```python
>>> qs = BookInfo.objects.all()[0:2]
>>> qs
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
```

### 管理器Manager

管理器是Django的模型进行数据库操作的接口，Django应用的每个模型类都拥有至少一个管理器。

我们在通过模型类的**objects**属性提供的方法操作数据库时，即是在使用一个管理器对象**objects**。当没有为模型类定义管理器时，Django会为每个模型类生成一个名为objects的管理器，它是**models.Manager**类的对象。

#### 自定义管理器 

我们可以自定义管理器，并应用到我们的模型类上。
*注意：一旦为模型类指明自定义的过滤器后，Django不再生成默认的管理对象objects*
自定义管理器类主要用于两种情况：

1. 修改原始查询集，重写all()方法

   * 打开Users/models.py文件，定义类BookInfoManager

   ```python
    62 # 图书管理器
    63 class BookInfoManager(models.Manager):
    64     def all(self):
    65         # 默认查询未删除的图书信息
    66         # 调用父类的成员语法为：super().方法名
    67         return super().filter(is_delete=False)  
   ```

   * 在模型类BookInfo中定义管理器

     ![image4dd6b.png](https://miao.su/images/2019/06/25/image4dd6b.png)

   * 使用方法

     ```pyhton
     BookInfo.books.all()
     ```

     ![imagecaa80.png](https://miao.su/images/2019/06/25/imagecaa80.png)

2. 在管理器类中补充定义新的方法

   * 打开Users/models.py文件，定义方法create。

     ```python
       8 class BookInfoManager(models.Manager):
       9     def all(self):
      10         # 默认查询未删除的图书信息
      11         # 调用父类的成员语法为：super().方法名
      12         return super().filter(is_delete=False)
      13     def create_book(self, title, pub_data):
      14         # 创建模型类对象self.model可以获得模型类
      15         book = self.model()
      16         book.btitle = title 
      17         book.bpub_data = pub_data
      18         book.bread = 0
      19         book.bcomment = 0
      20         book,is_delete = False
      21         # 将数据插入进数据表
      22         book.save()
      23         return book
     ```

     为模型类BookInfo定义管理器books语法如下：

     ![image4dd6b.png](https://miao.su/images/2019/06/25/image4dd6b.png)

     调用语法如下：

     ![image38cc0.png](https://miao.su/images/2019/06/25/image38cc0.png)

     

## 模板

### 模板使用

#### 配置

在工程中创建模板目录*templates*
在*settings.py*配置文件中修改**TEMPLATES**配置项的DIRS值。
![image12244.png](https://miao.su/images/2019/06/25/image12244.png)

### 定义模板

在templates目录中新建一个模板文件，如index.html

```html
  1 <!DOCTYPE html>
  2 <html lang="en">
  3 <head>
  4     <meta charset="UTF-8">
  5     <meta name="viewport" content="width=device-width, initial-scal
  6     <meta http-equiv="X-UA-Compatible" content="ie=edge">
  7     <title>模板</title>
  8 </head>
  9 <body>
 10     <div>这是一个模板文件</div>                                 	    <h2>{{city}}</h2>   
 11 </body>
 12 </html>
```



### 渲染模板

调用模块分为三个步骤：

1. 找到模板
2. 定义上下文
3. 渲染模板

例如，定义一个视图：
Django提供了一个函数render可以简写上述代码：
`render(request对象, 模板文件路径, 模板数据字典)`

```python
  5 from django.shortcuts import render 
    
 30 #或者这样子简写
 31 def index(request):
 32     context = {'city': '北京'}
 33     return render(request, 'index.html', context)
```

### 模板语法

#### 模板变量

变量名必须由字母、数字、下划线（不能以下划线开头）和点组成。
语法如下：

```python
{{ 变量 }}
```

模板变量可以使python的内建类型，也可以是对象。

```html
html模板：
  1 <!DOCTYPE html>
  2 <html lang="en">
  3 <head>
  4     <meta charset="UTF-8">
  5     <meta name="viewport" content="width=device-width, initial-scal
  6     <meta http-equiv="X-UA-Compatible" content="ie=edge">
  7     <title>模板</title>
  8 </head>
  9 <body>
 10     <div>这是一个模板文件</div>
 11     <h2>{{city}}</h2>
 12     <h4>{{adict}}</h4>
 13     注意字典的取值方法
 14     <h4>{{adict.name}}</h4>
 15     <h4>{{alist}}</h4>
 16     注意列表的取值方法
 17     <h5>{{alist.0}}</h5>
 18 </body>                                                            
 19 </html>
```

```python
views.py:
 29 #或者这样子简写
 30 def index(request):
 31     context = {'city': '北京',
 32                'adict':{
 33                    'name': '西游记',
 34                    'author': '吴承恩'
 35                }
 36                 'alist': [1, 2, 3, 4, 5]
 37             }
 38     return render(request, 'index.html', context)
```

#### 模板语句

1. for 循环：

   ```jinja2
   {% for item in 列表 %}
   循环逻辑
   {{ forloop.counter }} 表示当前是第几次循环，从1开始
   {% empty %} 列表为空或不存在时执行此逻辑
   {% endfor %}
   ```

2. if 条件

   ```jinja2
   {% if ... %}
   逻辑1
   {% elif ... %}
   逻辑2
   {% else %}
   逻辑3
   {% endif %}
   ```

   比较运算符如下：

   `==、!=、<、>、<=、>=`

   布尔运算符如下：
   `and、or、not`

   *注意：运算符左右两侧不能紧挨变量或常量，必须由空格*

   ```jinja2 
   {% if a == 1 %}  # 正确
   {% if a==1 %}  # 错误
   ```

### 过滤器

语法如下：

* 使用管道符号 `|`来应该过滤器，用于进行计算、转换操作，可以使用在变量、标签中。

* 如果过滤器需要参数，则可以使用`:`传递参数。

  ```jinja2
  变量|过滤器：参数
  ```

列举几个如下：

* safe：禁用转义，告诉模板这个变量是安全的，可以解释执行

* length：长度，返回字符串包含字符的个数，或列表、元组、字典的元素个数

* default：默认值，如果变量不存在时则返回默认值

  ```jinja2
  data|default:‘默认值’
  ```

* date：日期，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：

  - Y表示年，格式为4位，y表示两位的年。
  - m表示月，格式为01,02,12等。
  - d表示日, 格式为01,02等。
  - j表示日，格式为1,2等。
  - H表示时，24进制，h表示12进制的时。
  - i表示分，为0-59。
  - s表示秒，为0-59。

  ```jinja2
  value|date:"Y年m月j日	H时i分s秒"
  ```

### 注释

1. 单行注释语法如下：

   ```jinja2
   {# ... #}
   ```

2. 多行注释使用comment标签，语法如下：

   ```jinja2
   {% comment %}
   ...
   {% endcomment %}
   ```

### 模板继承

模板继承和类的继承含义是一样的， 主要是为了提高代码的重用，减轻开发人员的工作量。

#### 父模板

如果发现在多个模板中某些内容相同，那就应该吧这段内容定义到父模板中。
标签block：用于在父模板中预留区域，留给子模板填充差异性的内容，名字不能相同。为了更好的可读性，建议给endblock标签写上名字，这个名字与对应的block名字相同。父模板中也可以使用上下文传递过来的数据。

```jinja2
{% block 名称 %}
预留区域，可以编写内容，也可以没有默认内容
{% endblock 名称 %}
```

#### 子模板

标签extends：继承，写在子模板文件的第一行

```jinja2
{% extend "父模板路径" %}
```

子模板不用填充父模板中的所有预留区域，如果子模板没有填充，则使用父模板定义的默认值。
例如，填充父模板中指定名称的预留区域。

```jinja2
{% block 名称 %}
实际填充内容
{{ block.super }} 用于获取父模板中block的内容
{% endblock 名称 %}
```



## 表单

> Django提供对表单处理的支持，可以简化并自动化大部分的表单处理工作

### 定义表单类

表单系统的核心部分是Django的Form类。Django的数据库模型描述一个对象的逻辑结构、行为以及展现给我们的方式，与此类似，Form类描述一个表单并决定它如何工作和展现。

假如我们想再网页汇总创建一个表单，用来获取用户想保存的图书信息，可能类似的html表单如下：

```html
  1 <!DOCTYPE html>
  2 <html lang="en">
  3 <head>
  4     <meta charset="UTF-8">
  5     <meta name="viewport" content="width=device-width, initial-scal
  6     <meta http-equiv="X-UA-Compatible" content="ie=edge">
  7     <title>表单举例</title>
  8 </head>
  9 <body>
 10     <form action="" method="post">
 11         <input type="text" name="title">
 12         <input type="date" name="pub_date">
 13         <input type="submit">
 14     </form>                                                        
 15 </body>
 16 </html>
```

我们可以几次来创建一个Form类来描述这个表单。
新建一个**forms.py**文件，编写Form类。

```python
  1 #!/usr/bin/env python
  2 # coding=utf-8
  3 
  4 from django import forms
  5 
  6 class BookForm(forms.Form):
  7     title = forms.CharField(label="书名", required=True, max_length
  8     pub_date = forms.DateField(label="出版日期", required=True) 
```

视图中使用表单类

```python
 16 from .forms import BookForm

 20 class BookView(View):
 21     def get(self, request):
 22         form = BookForm()
 23         return render(request, 'form.html', {'form': form})
 24 
 25     def post(self, request):
 26         form = BookForm(request.POST)
 27         if form.is_valid()： # 验证表单数据
 28             print(form.cleaned_data)  # 获取验证后的表单数据
 29 
 30             return HttpResponse("OK")
 31         else:
 32             return render(request, 'form.html', {'form': form})
```

* form.is_valid() 验证表单数据的合法性
* form.cleaned_data 验证通过的表单数据：

### 模板中使用表单类

```html
  1 <!DOCTYPE html>
  2 <html lang="en">
  3 <head>
  4     <meta charset="UTF-8">
  5     <meta name="viewport" content="width=device-width, initial-scal
  6     <meta http-equiv="X-UA-Compatible" content="ie=edge">
  7     <title>表单举例</title>
  8 </head>
  9 <body>
 10     <form action="" method="post">
 11 
 12         <input type="text" name="title">
 13         <input type="date" name="pub_date">
 14 
 15         {% csrf_token %}
 16         {{ form   }}
 17                                                                    
 18         <input type="submit">
 19     
 20     </form>
 21 </body>
 22 </html>
```

* csrf_token 用于添加CSRF防护字段
* form 快速渲染表单字段的方法

### 模型类表单

如果表单中的数据与模型类对应，可以通过继承*forms.ModelForm*更快速的创建表单 。

```python
class BooForm(forms.ModelForm):
	class Meta:
		model = BookInfo
		fields = ('btitle', 'bpub_date')
```



## Admin站点

### 使用Admin站点

假设我们要设计一个新闻网站，我们需要编写展示给用户的页面，网页上展示的新闻信息是从哪里来的呢？**是从数据库中查找到新闻的信息，然后把它展示在页面上**。但是我们的网站上的新闻每天都要更新，这就意味着对数据库的增、删、改、查操作，name我们需要每天写sql语句操作数据库么？如果这样的话，是不是非常繁琐，所以我们可以设计一个页面，通过对这个页面的操作来实现对新闻数据库的增删改查操作。那么问题来了，老板说 我们需要再建立一个新的网站，是不是还要设计一个页面来实现对新网站数据库的增删改查操作，这样子的页面就会具有很大的重复性，那么有没有一种方法能够让我们很快的生成管理数据库表的页面呢？**有！那就是我们下面要说的Django的后台管理**。Django能够根据定义的模型类自动地生成管理页面。

使用Django的管理模块，需要按照如下步骤操作：

1. 管理界面本地化
2. 创建管理员
3. 注册模型类
4. 自定义管理页面

### 管理界面本地化

在`settings.py`中设置语言和时区 

```python
116 # 本地化设置成中文
117 LANGUAGE_CODE = 'zh-hans'
118 
119 # 错误时会有时区显示，另外也会自动转换时区时间
120 TIME_ZONE = 'Asia/Shanghai'
```



### 创建超级管理员

创建管理员的命令如下，按提示输入用户名、邮箱、密码。

```python
python manager.py createsuperuser
```

打开浏览器，在地址栏输入一下地址后，输入用户、密码登陆：

```shell
http://47.100.200.127:8000/admin/
```

![image2676c.png](https://miao.su/images/2019/06/25/image2676c.png)

![image1283f.png](https://miao.su/images/2019/06/25/image1283f.png)

### 注册模型类

登陆后台管理后，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，并进行增删改查的操作。

打开Users/admin.py 文件，编写如下代码：![imageeebf1.png](https://miao.su/images/2019/06/25/imageeebf1.png)

到浏览器中刷新页面，可以看到模型类BookInfo和HeroInfo的管理了。
[![image35685.md.png](https://miao.su/images/2019/06/25/image35685.md.png)](https://miao.su/image/TfaS7)

点击类名称“BookInfo”（图书）可以进入列表页，默认只有一列。

[![imagef3b5a.md.png](https://miao.su/images/2019/06/25/imagef3b5a.md.png)](https://miao.su/image/Tfen5)

在列表页中点击“增加”可以进入增加页，Django会根据模型类的不同生成不同的表单控件，按提示填写表单内容后点击“保存”，完成数据创建，创建成功返回列表页。
![image1cc49.png](https://miao.su/images/2019/06/25/image1cc49.png)

在列表页点击某个元素可进入修改页，按照提示进行内容的修改，修改成功后进入列表页。在修改页点击“删除”可以删除一项。
![image9f7e7.png](https://miao.su/images/2019/06/25/image9f7e7.png)

### 定义与使用Admin管理类

Django提供的Admin站点的展示效果可以通过自定义**ModelAdmin**类来进行控制。

定义管理类需要继承自**admin.ModelAdmin**类，如下

```python
from django.contrib import admin

class BookInfoAdmin(admin.ModelAdmin):
    pass
```

使用管理类有两种方式：

- 注册参数

  ```python
  admin.site.register(BookInfo,BookInfoAdmin)
  ```

- 装饰器

  ```python
  @admin.register(BookInfo)
  class BookInfoAdmin(admin.ModelAdmin):
      pass
  ```

### 调整列表页展示

1. **页大小**
   每页中显示多少条数据，默认为每页显示100条数据，属性如下：

   ```python
   list_per_page=100
   ```

   打开Users/admin.py文件，注释掉BookInfo的注册：

   ![image7389d.png](https://miao.su/images/2019/06/26/image7389d.png)

   打开Users/admin.py文件，注册BookInfo：

   ```python
    85 @admin.register(BookInfo)
    86 class BookInfoAdmin(admin.ModelAdmin):
    87     list_per_page = 2 
   ```

   效果如下：
   ![image09952.png](https://miao.su/images/2019/06/26/image09952.png)

2. **操作选项的位置**
   顶部显示的属性，设置为True在顶部显示，设置为False不再顶部显示，默认为True

   ```python
    88     actions_on_top = True
   ```

   底部显示的属性，设置为True在底部显示i，设置为False不再底部显示，默认为False

   ```python
    89     action_on_bottom = True
   ```

   效果如下：
   ![image15214.png](https://miao.su/images/2019/06/26/image15214.png)

3. **列表中的列**
   属性如下：

   ```python
   list_display = [模型字段1， 模型字段2]
   ```

   例如：

   ```python
    85 @admin.register(BookInfo)
    86 class BookInfoAdmin(admin.ModelAdmin):
    87     list_per_page = 2
    88     actions_on_top = True
    89     actions_on_bottom = True
    90     list_display = ['id', 'btitle'] 
   ```

   效果如下：

   ![imagea9391.png](https://miao.su/images/2019/06/26/imagea9391.png)

4. **将方法作为列**
   列可以是模型字段，还可以是模型方法，要求方法有返回值。
   **通过设置short_description属性，可以设置在admin站点中显示的列名**
   在Users/models.py中把BookInfo类修改如下：

   ```python
   def pub_date(self):
   	return self.bpub_data.strftime("%Y年%m月%d日")
   # 设置方法字段在admin中显示的标题
   pub_date.short_description = '发布日期'
   ```

   修改admin.py文件中的BookInfoAdmin类修改如下：

   ```python
    90 @admin.register(BookInfo)
    91 class BookInfoAdmin(admin.ModelAdmin):
    92     list_per_page = 2
    93     actions_on_top = True
    94     actions_on_bottom = True
    95     list_display = ['id', 'btitle', 'pub_date']
   ```

   效果如下：
   ![imagecaf5a.png](https://miao.su/images/2019/06/26/imagecaf5a.png)

   方法列是不能排序的，如果需要排序需要为方法指定排序依据。

5. **关联对象**
   无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员

   * 打开Users/models.py文件，修改HeroInfo类如下：

     ```python
      58 class HeroInfo(models.Model):
     	pass
      69     def read(self):
      70         return self.hbook.bread
      71     read.short_description = '图书阅读量'
     ```

   * 打开Users/admin.py文件，修改HeroInfoAdmin类如下：

     ```python
      17 @admin.register(HeroInfo)
      18 class HeroInfoAdmin(admin.ModelAdmin):
      19     pass
      20 
      21     list_display = ['id', 'hname', 'hbook', 'read'] 
     ```

   * 效果如下：
     ![image260fd.png](https://miao.su/images/2019/06/26/image260fd.png)

6. **右侧栏过滤器**
   属性如下，只能接受字段，会将对应字段的值列出来，用于快速过滤。一般用于有重复值的字段。

   ```python
   list_filter=[]
   ```

   * 打开Users/admin.py文件，修改HeroInfoAdmin类如下：

     ```python
      17 @admin.register(HeroInfo)
      18 class HeroInfoAdmin(admin.ModelAdmin):
      19     list_filter = ['hbook', 'hgender']                                   
      20                    
      21     list_display = ['id', 'hname', 'hbook', 'read']
     ```

   * 效果如图：
     ![image2aae3.png](https://miao.su/images/2019/06/26/image2aae3.png)

7. **搜索框**
   属性如下，用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。

   ```python
   search_fields=[]
   ```

   * 打开Users/admin.py文件，修改HeroInfoAdmin类如下：

     ```python
      17 @admin.register(HeroInfo)
      18 class HeroInfoAdmin(admin.ModelAdmin):
      19     list_filter = ['hbook', 'hgender']
      20     search_fields = ['hname']                                            
      21                      
      22     list_display = ['id', 'hname', 'hbook', 'read']
     ```

   * 效果如下：
     ![imageb93a3.png](https://miao.su/images/2019/06/26/imageb93a3.png)

### 调整编辑页展示

1. **显示字段**
   属性如下：

   ```python
   fields=[]
   ```

   * 点击某行ID的链接，可以转到修改页面，默认效果如下图：
     ![image19e88.png](https://miao.su/images/2019/06/26/image19e88.png)

   * 打开Users/admin.py文件，修改BookInfoAdmin类如下：

     ```python
       9 @admin.register(BookInfo)
      10 class BookInfoAdmin(admin.ModelAdmin):
      11     list_per_page = 2
      12     actions_on_top = True
      13     actions_on_bottom = True
      14     list_display = ['id', 'btitle', 'pub_date']
      15     fields = ['btitle', 'bpub_data']
     ```

   * 修改效果如下：
     ![imageb2639.png](https://miao.su/images/2019/06/26/imageb2639.png)

2. **分组显示**
   属性如下：

   ```python
   fieldset = (
   	('组1标题'， {'fields': ('字段1', '字段2')}),
   	('组2标题'， {'fields': ('字段3', '字段4')}),
   )
   ```

   * 打开Users/admin.py文件，修改BookInfoAdmin类如下：

     ```python
       9 @admin.register(BookInfo)
      10 class BookInfoAdmin(admin.ModelAdmin):
      11     list_per_page = 2
      12     actions_on_top = True
      13     actions_on_bottom = True
      14     list_display = ['id', 'btitle', 'pub_date']
      15     # fields = ['btitle', 'bpub_data']
      16     fieldsets = (
      17         ('基本', {'fields': ['btitle', 'bpub_data']}),                   
      18         ('高级', {'fields': ['bread', 'bcomment'], 
      19                   'classes': ('collapse',)})  # 是否折叠显示
     ```

   * 效果如下：
     ![imageca42a.png](https://miao.su/images/2019/06/26/imageca42a.png)

3. **关联对象**
   在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格、块两种。

   * 类型`InlineModelAdmin`：表示在模型的编辑页面嵌入关联模型的编辑
   * 子类`TabularInline`：以表格的形式嵌入
   * 子类`StackedInline`：以块的形式嵌入

   打开Users.admin.py文件，创建HeroInfoStackInline类：

   ```python
     9 class HeroInfoStackInline(admin.StackedInline):
    10     model = HeroInfo # 要编辑的对象
    11     extra = 1 # 附加编辑的数量
    12 
    13 
    14 @admin.register(BookInfo)
    15 class BookInfoAdmin(admin.ModelAdmin):
    	pass
    26     inlines = [HeroInfoStackInline]
   ```

   效果如下：
   ![imaged353b.png](https://miao.su/images/2019/06/26/imaged353b.png)

   还可以用表格的形式嵌入：

   * 打开Users/admin.py文件，创建HeroInfoTabularInline类：

     ```python
      13 class HeroInfoTabularInline(admin.TabularInline):
      14     model = HeroInfo
      15     extra = 1
      16 
      18 @admin.register(BookInfo)
      19 class BookInfoAdmin(admin.ModelAdmin):
      	 	pass
      31     inlines = [HeroInfoTabularInline]
     ```

     效果如下：
     ![imagee45d4.png](https://miao.su/images/2019/06/26/imagee45d4.png)

### 调整站点信息

Admin站点的名称信息也是可以自定义的。未调整前如下图：
![image6796e.png](https://miao.su/images/2019/06/26/image6796e.png)

* admin.site.site_header 设置网站页头
* admin.site.site_title 设置页面标题
* admin.site_title 设置首页标语

在Users/admin.py文件中添加以下信息：

```python
  8 admin.site.site_title = 'my first Django project'
  9 admin.site.site_header = 'Django_test_pro'
 10 admin.site.index_title = 'Welcome' 
```

效果如下：
![imageb4f60.png](https://miao.su/images/2019/06/26/imageb4f60.png)

### 上传图片

Django有提供文件系统支持，在Admin站点汇总可以轻松上传图片。
使用Admin站点保存图片，需要安装Python的图片操作包：

```shell
pip install Pillow
```

* 配置
  默认情况下，Django会将上传的图片保存在本地服务器上，需要配置保存路径。我们可以将上传的文件保存在静态文件目录中，如我们之前设置的static_files目录中在settings.py文件中添加如下上传保存目录信息：

  ```python
  MEDIA_ROOT = os.path.join(BASE_DIR, "static_files/medis")
  ```

* 为模板类添加 ImageField 字段
  我们为之前的BookInfo模型类添加一个ImageField

  ```python
  37     image = models.ImageField(upload_to = 'booktest', verbose_name = '图片', null = True)
  ```

  upload_to 选项指明该字段的图片保存在MEDIA_ROOT目录中的哪个子目录
  进行数据库迁移操作：

  ```shell
  python manage.py makemigrations
  python manage.py migrate
  ```

  然后在admin.py文件中添加这个元素块：
  ![imagedb8df.png](https://miao.su/images/2019/06/26/imagedb8df.png)

#### 使用Admin站点上传图片

进入Admin站点的图书管理页面，选择一个图书，能发现多出来一个上传图片的字段。
![image75ac8.png](https://miao.su/images/2019/06/26/image75ac8.png)

选择一张图片并保存后，图片会保存在`static_files/media/Users/`目录下。
在数据库中，我们能够看到image字段被设置为图片的路径。
![image8ad2b.png](https://miao.su/images/2019/06/26/image8ad2b.png)



# Django REST framework教程

我们从分析现状流行的前后端分离Web应用模式说起，然后介绍如何设计REST API，通过使用Django来实现一个REST API为例，明确后端开发REST API要做的最核心工作，然后介绍Django REST framework能帮助我们简化开发REST API的工作。

## Web应用模式

在开发Web应用中，有两个应用模式：

* 前后端不分离
* 前后端分离

### 前后端不分离

![image741aa.png](https://miao.su/images/2019/06/26/image741aa.png)

在前后端不分离的应用模式中，前端页面看到的效果都是由后端控制的，由后端渲染页面或重定向，也就是后端需要控制前端的展示，前端后端的耦合度很高。

这种应用模式比较适合纯网页应用，但是后端对接App时，App可能并不需要后端返回一个HTML网页，而仅仅是数据本身，所以后端原本返回网页的接口不再适用于前端App应用，为了对接App后端还需要再开发一套接口。

### 前后端分离

![ååç«¯åç¦»](file:///D:/python/Django%E6%A1%86%E6%9E%B6/01%E6%A1%86%E6%9E%B6-6%E5%A4%A9/06-DRF%E6%A1%86%E6%9E%B6-%E7%AC%AC06%E5%A4%A9/1-%E6%95%99%E5%AD%A6%E8%B5%84%E6%96%99/DjangoRESTframework%E8%AF%BE%E4%BB%B6/DjangoRESTframework/images/indepent_frontend_backend.png)

在前后端分离的应用模式中，后端仅返回前端所需数据，不再渲染HTML页面，不再控制前端的效果。至于前端用户看到什么效果，从后端请求的数据如何加载到前段中，都由前端自己决定，网页有网页的处理方式，App有App的处理方式，但无论哪种前端，所需的数据都相同，后端仅需开发一套逻辑对外提供数据即可。

在前后端分离的应用模式中，前端与后端的耦合度很低。

在前后端分离的应用模式中，我们通常将后端开发的每一个视图都称为一个**接口**，或者**API**，前端通过访问接口来对数据进行增删改查。

### 认识RESTful

**在前后端分离的应用模式里，后端API接口如何定义**

例如对于后端数据库中保存了商品的信息，前端可能需要对商品数据进行增删改查，那相应的每个操作后端都需要提供一个对于的API接口：

1. POST/add-goods 增加商品
2. POST/delete-goods 删除商品
3. POST/update-goods 修改商品
4. GET/get-goods 查询商品信息

对于接口的请求方式与路径，每个后端开发人员可能都有自己的定义方式，风格迥异。
是否存在一种同一的定义方式，被广大开发人员接受认可的方式呢？

这就是被普遍采用的PAI的RESTful设计风格。

#### 起源

REST这个词，是 `Roy Thomas Fielding`在他2000年的博士论文中提出的。
Fielding是一个非常重要的人，他是HTTP协议（1.0版和1.1版）的主要设计者、Apache服务器软件的作者之一、Apache基金会的第一任主席。所以，他的这篇论文一经发表，就引起了关注，并且立即对互联网开发产生了深远的影响。

#### 名称

Fielding将他理解的互联网软件的架构原则，定名为REST，即`Representational States Transfer`的缩写。维基百科称其为`具象状态传输`，国内大部份人理解为`表现层状态转化`。

`RESTful`是一种**开发理念**。维基百科说：**REST是设计风格而不是标准**。REST描述的是在网络中client和server的一种交互形式；REST本身不实用，实用的是如何设计`RESTful API`（REST风格的网络接口），一种万维网软件架构风格。

我们先来具体看下RESTful风格的url，比如我要查询商品的信息，那么：

> 非REST的url：http://.../queryGoods?id=1001&type=t01
>
> REST的url：http://.../t01/goods/1001

可以看出REST的特点：**URL简洁，将参数通过url传到服务器**，而传统的url比较繁杂，而且现实汇总浏览器的地址栏会拼接一大串字符，相比你们都见过吧。但是采用REST的风格就会好很多，现在很多的网站已经采用这种风格了，这也是潮流的方向。典型的就是url的短话转换。

**那么，到底什么是RESTful架构：如果一个架构符合REST原则，就称它为RESTful架构**

要理解RESTful架构，理解Representation Station Transfer这三个单词的意思。

* **具象的**，就是指表现层，要表现得对象也就是资源，什么资源呢？网站的资源共享的东西，客户端（浏览器）访问web服务器，所获取的就叫资源。比如html、txt、json、图片、视频等等。
* **表现**，比如，文本可以用txt格式表现，也可以用HTML格式、XML格式、JSON格式表现，甚至可以采用二进制格式；图片可以用JPG格式表现，也可以用PNG格式表现。
  浏览器通过URL确定一个资源，但是如何确定它的具体表现形式呢？应该在HTTP请求的头信息中用Accept和Content-Type字段指定，这两个字段才是对 *表现层* 的描述。 
* **状态转换**，就是客户端和服务器互动的一个过程，在这个过程中，势必涉及到数据和状态的变化，这种变化叫做状态转换。
  互联网通信协议HTTP协议，客户端访问必然使用HTTP协议，**如果客户端想要操作服务器，必须通过某种手段，让服务器发生状态转化（State Transfer）**。
  HTTP协议实际上含有4个表示操作方式的动词，分别是`GET、POST、PUT、DELETE`他们分别是对应四种操作，`GET`用于获取资源，`PUT`用于更新资源，`DELETE`用于删除资源。`GET`和`POST`是表单提交的两种基本方式，比较常见，而`PUT`和`DELETE`不太常用。
  而且HTTP协议是一种无状态协议，这样就必须把所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器发生状态转化。
* *总结*：
  * 每一个URL代表一种资源
  * 客户端和服务器之间，传递这种资源的某种表现层
  * 客户端通过四个HTTP动词，对服务器端资源进行操作，实现“表现层状态转化”

### RESTful设计方法

#### 域名

应该尽量将API部署在专用域名之下：

```python
https://api.example.com
```

如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下：

```python
https://example.org/api/
```

#### 版本（Version）

应该讲API的版本号放入URL：

```python
http://www.example.com/app/1.0/foo
http://www.example.com/app/1.1/foo
http://www.example.com/app/2.0/foo
```

另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便直观。Github就是采用了这种做法。

因为不同的版本，可以理解为用一种资源的不同表现形式，所以应该采用用一个URL。版本号可以在HTTP请求头信息的Accept字段中进行区分：

```python
Accept: vnd.example-com.foo+json; version=1.0
Accept: vnd.example-com.foo+json; version=1.1
Accept: vnd.example-com.foo+json; version=2.0
```

#### 路径

路径有称“终点”（endpoint），表示API的具体网址，每个网址代表一种资源（resource）。

1. 资源作为网址，只能有名词，不能有动词，而且所用的名词往往与数据库的表名对应。
   举例来说，下面是一个不好的例子：

   ```python
   /getProducts
   /listOrders
   /retreiveClientByOrder?orderId=1
   ```

2. API中的名词应该使用负数。无论资资源或者所有资源。
   举例来说，获取产品的API可以这样定义：

   ```python
   获取单个产品：http://127.0.0.1:8080/AppName/rest/products/1
   获取所有产品: http://127.0.0.1:8080/AppName/rest/products
   ```

#### HTTP动词

对于资源的具体操作类型，由HTTP动词表示。
常用的HTTP动词有下面四个（括号里是对应的SQL命令）。

* GET（SELECT）：从服务器取出一种资源（一项或多项）。
* POST（CREATE）：在服务器新建一个资源。
* PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
* DELETE（DELETE）：从服务器删除资源。

还有三个不常用的HTTP动词。

* PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）
* HEAD：获取资源的元数据
* OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的

下面是一些例子：

```html
GET /zoos：列出所有动物园
POST /zoos：新建一个动物园（上传文件）
GET /zoos/ID：获取某个指定动物园的信息
PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
DELETE /zoos/ID：删除某个动物园
GET /zoos/ID/animals：列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
```

#### 过滤信息（Filter）

如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。
下面是一些常见的参数：

```html
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
?animal_type_id=1：指定筛选条件
```

参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复。比如`GET/zoos/ID/animals`与`GET/animals?zoo_id=ID`的含义是相同的。

#### 状态码（Status Codes）

服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的HTTP动词）。

```markdown
200 OK - [GET]：服务器成功返回用户请求的数据
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。
```

#### 错误处理（Error handling）

如果状态码是4xx，服务器就应该向用户返回出错信息。一般来说，返回的信息中将error作为键名，出错信息作为键值即可。

```jinja2
{
	error: "Invalid API key"
}
```

#### 返回结果

针对不同的操作，服务器向用户返回的结果应该符合以下规范。

```markdown
GET /collection：返回资源对象的列表（数组）
GET /collection/resource：返回单个资源对象
POST /collection：返回新生成的资源对象
PUT /collection/resource：返回完整的资源对象
PATCH /collection/resource：返回完整的资源对象
DELETE /collection/resource：返回一个空文档
```

#### 超媒体（Hypermedia API）

RESTful API最好做到Hypermedia（即返回结果中提供链接，连向其他API方法），使其用户不查文档，也知道下一步应该做什么。

比如Github的API设计就是这种设计，访问`api.github.com`会得到一个所有可用API的列表。

```python
{
"current_user_url": "https://api.github.com/user",
"authorizations_url": "https://api.github.com/authorizations",
// ...
}
```

从上面可以看到，如果想获取当前用户的信息，应该去访问`api.github,com/user`，然后就得到了下面结果。

```python
{
  "message": "Requires authentication",
  "documentation_url": "https://developer.github.com/v3"
}
```

上面代码表示，服务器给出了提示信息，以及文档的网址。

#### 其他

服务器返回的数据格式，应该尽量使用JSON，避免使用XML。

### 使用Django开发REST接口

我们一Django框架中使用的图书英雄案例来写一套支持图书数据只能删改查的REST API接口，来理解REST API的开发。

在次案例中，前后端均可发送JSON格式数据。

```python
 # views.py
 19 class BooksAPIView(View):
 20     """查询所有图书、增加图书"""
 21     def get(self, request):
 22         """查询所有图书，路由：GET /books/"""
 23         queryset = BookInfo.objects.all()
 24         book_list = []
 25         for book in queryset:
 26             book_list.append({
 27                 'id': book.id,
 28                 'btitle': book.btitle,
 29                 'bpub_date': book.bpub_data,
 30                 'bread': book.bread,
 31                 'bcomment': book.bcomment,
 32                 'image': book.image.url if book.image else ''
 33             })
  34         return JsonResponse(book_list, safe=False)
 35 
 36     def post(self, request):
 37         """新增图书，路由：POST /books/"""
 38         json_bytes = request.body
 39         json_str = json_bytes.decode()
 40         book_dict = json.loads(json_str)
 41         # 此处详细的校验参数省略 使用object 则不能自定义管理器
 42         book = BookInfo.objects.create(
 43             btitle = book_dict.get('btitle'),
 44             bpub_data = datetime.strptime(book_dict.get('bpub_data'), '%Y
 45         )
 46         return JsonResponse({
 47             'id': book.id,
 48             'btitle': book.title,
 49             'bpub_data': book.bpub_data,
 50             'bread': book.bread,
 51             'bcomment': book.bcomment,
 52             'image': book.image.url if book.image else ''
 53         }, status = 201)
 54 
 55 
 56 class BookAPIView(View):
 57     def get(self, request, pk):
 58         """获取单个图书信息，路由：GET /books/<pk>"""
 59         try:
 60             book - BookInfo.objects.get(pk = pk)
 61         except BookInfo.DoesNotExist:
 62             return HttpResponse(status=404)
 63 
 64         return JsonResponse({
 65             'id': book.id,
 66             'btitle': book.btitle,
 67             'bpub_data': book.bpub_data,
 68             'bread': book.bread,
 69             'bcomment': book.bcomment,
 70             'image': book.image.url if book.image else ''
 71         })
  72 
 73     def put(self, request, pk):
 74         """修改图书信息，路由：PUT /books/<pk>"""
 75         try:
 76             book = BookInfo.objects.get(pk=pk)
 77         except BookInfo.DoesNotExist:
 78             return HttpResponse(status=404)
 79 
 80         json_bytes = request.body
 81         json_str = json_bytes.decode()
 82         book_dict = json.loads(json_str)
 83         # 此处详细校验参数省略
 84         book.btitle = book.dict.get('btitle')
 85         book.bpub_data = datetime.strptime(book_dict.get('bpub_data'), '%
 86         book.save()
 87         return JsonResponse({
 88             'id': book.id,
 89             'btitle': book.btitle,
 90             'bpub_data': book.bpub_data,
 91             'bread': book.bread,
 92             'bcomment': book.bcomment,
 93             'image': book.image.url if book.image else ''
 94         }) 
  96 
 97     def delete(self, request, pk):
 98         """删除图书，路由：DELETE /books/<pk>"""
 99         try:
100             book = BookInfo.objects.get(pk=pk)
101         except BookInfo.DoesNotExist:
102             return HttpResponse(status=404)
103 
104         book.delete()
105         return HttpResponse(status=204)
```

```python
# urls.py
 28     url(r'^books/$', views.BooksAPIView.as_view()),
 29     url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()), 
```



### 明确REST接口开发的核心任务

分析一下上节的案例，可以发现，在开发REST API接口时，视图中做的最主要的三件事：

* 将请求的数据（如JSON格式）转换为模型类
* 操作数据库
* 将模型类对象转换为响应的数据（如JSON）

#### 序列化Serialization

*维基百科* 中对序列化的定义：
**序列化**在计算机科学的资料处理中，是指将数据结构或物件状态转换为可取格式（例如存成档案，存于缓存，或经由网络中传送），以留待后续在相同或另一台计算机环境中，能恢复原先状态的过程。依照序列化格式重新获取字节的结果时，可以利用它来产生与原始物件相同语义的副本。对于许多物件，像是使用大量参照的复杂物件，这种序列化重建的过程并不容易。面对对象中的物件序列化，并不概括之前原始物件所关联的函式。这种过程也称为物件编组（marshalling）。从一系列字节提取数据结构的反向操作，是反序列化（也称为解编组，deserialization，unmarshalling）。

**序列化**在计算机科学中通常有一下定义：

在数据储存与传送的部分是指将一个对象存储至一个存储媒介，例如档案或是记忆体缓冲等，或者透过网络传送资料时进行编码的过程，可以是字节或是XML等格式。而字节的或XML编码格式可以还原完全相等的对象。这程序被应用在不同应用程序之间传送对象，以及服务器将对象储存到档案或数据库。相反的过程又称为反序列化。

简而言之，我们可以将**序列化**理解为：

**将程序中的一个数据结构类型转换为其他格式（字典、JSON、XML等），例如将Django中的模型类对象转换为JSON字符串，这个转换过程我们称为序列化。**
如：

```python
queryset = BookInfo.objects.all()
book_list = []
# 序列化
for book in queryset:
	book_list.append({
		'id': book.id,
		'btitle': book.btitle,
		'bpub_data': book.pub_data,
		'bread': book.bread,
		'bcomment': book.bcomment,
		'image': book.image.url if book.image else ''
	})
return JsonResponse(book_list, safe=False)
```

**反之，将其他格式（字典、JSON、XML等）转换为程序中的数据，例如将JSON字符串转换为Django中的模型类对象，这个过程我们称为反序列化。**
如：

```python
json_bytes = request.body
json_str = json_bytes.decode()
# 反序列化
book_dict = json.loads(json_str)
book = BookInfo.objects.create(
	btitle = book_dict.get('btitle'),
	bpub_data = datetime.strptime(book_dict.get('bpub_data', '%Y-%m-%d').date())
)
```

我们可以看到，**在开发REST API时，视图中药频繁的进行序列化和反序列化的编写**

*总结*：
在开发REST API 接口时，我们在视图中需要做的最核心的事是：

* 将数据库数据序列化为前端所需要的格式，并返回
* 将前端发送的数据反序列化为模型类对象，并保存在数据库中

## Django REST framework 简介

1. 在序列化与反序列化时，虽然操作的数据不尽相同，但是执行的过程却是相似的，也就是说这部分代码是可以重复编写的。

2. 在开发REST API的视图中，虽然每个视图具体操作的数据不同，但增、删、改、查的实现流程基本套路化，所以这部分代码也是可以复用简化编写的：

   * **增**：校验请求数据，执行反序列化过程，保存数据库，将保存的对象序列化并返回
   * **删**：判断要删除的数据是否存在，执行数据库删除
   * **改**：判断要修改的数据是否存在，校验请求的数据，执行反序列化过程，保存数据库，将保存的对象序列化并返回
   * **查**：查询数据库，将数据序列化并返回

   **Django REST framework 可以帮助我们简化上述两部分的代码编写，大大提高REST API的开发速度**

### 认识Django REST frameworkj

Django REST framework 框架时一个用于构建Web API的强大而又灵活的工具。
通常简称为DRF框架 或 REST framework。
DRF框架是建立在Django框架基础之上，由Tom Christie大牛二次开发的开源项目。

#### 特点

* 提供了定义序列化器Serializer的方法，可以快速根据Django ORM或者其他库自动序列化/反序列化
* 提供了丰富的类视图、Mixin扩展类，简化视图的编写
* 丰富的定制层级：函数视图、类视图、视图集合到自动生成API，满足各种需求
* 多种身份认证和权限认证方式的支持
* 内置了限流系统
* 直观的API web界面
* 可扩展性，插件丰富

## DRF工程搭建

### 环境安装与配置

DRF需要以下依赖：

* Python
* Django

**DRF是以Django扩展应用的方式提供的，所以我们可以直接利用已有的Django环境而无需重新创建。（若没有Django环境，需先创建Django环境。）**

1. 安装DRF

   ```shell
   pip install djangorestframework
   ```

2. 添加rest_framework应用
   我们利用在Django框架学习汇总创建的demo工程，在**setting.py**的**INSTALL_APPS**中添加‘rest_framework’，就可以进行DRF开发了。

   ```python
   INSTALL_APPS = [
   	...
   	'rest_framework'
   ]
   ```

### 见识DRF的魅力

仍以在学习Django框架时使用的图书英雄为案例，使用Django REST framework快速实现图书的REST API。

1. 创建序列化器
   在Users应用中新建serializers.py用于保存该应用的序列化器。
   创建一个BookInfoSerializer用于序列化与反序列化。

   ```python
     3 class BookInfoSerializer(serializers.ModelSerializer):
     4     """图书数据序列化器"""
     5     class Meta:
     6         model = BookInfo
     7         fields = '__all__' 
   ```

   * **model** 指明该序列化器处理的数据字段从模型类BookInfo参考生成
   * **fields** 指明该序列化器包含模型类中的哪些字段，`__all__`指明包含所有字段
   
2. 编写视图
   在Users应用的views.py中创建视图BookInfoViewSet，这是一个视图集合。

   ```python
   from rest_framework.viewsets import ModelViewSet
   from .serializers import BookInfoSerializer
   from .models import BookInfo
   
   class BookInfoViewSet(ModelViewSet):
   	queryset = BookInfo.objects.all()
   	serializer_class = BookInfoSerializer
   ```

   * **queryset** 指明该视图集在查询数据时使用的查询集
   * **serializer_class**  指明该视图在进行序列化或反序列化时使用的序列化器

3. 定义路由
   在Users应用的urls.py中定义路由信息：

   ```python
   from . import views
   from rest_framework.routers import DefaultRouter
   urlpatterns = [
   	...
   ]
   
   router = DefaultRouter() # 可以处理视图的路由器
   router.register(r'books', views.BookInfoViewSet) # 向路由器中注册视图集
   
   urlpatterns += router.urls # 将路由器中的所有路由信息追加到Django路由列表中
   ```

4. 运行测试
   运行当前程序（与运行Django一样），在浏览器汇总输入网址47.100.200.127:8000/Users，可以看到DRF提供的API Web浏览页面：
   ![image3c2fd.png](https://miao.su/images/2019/06/27/image3c2fd.png)

   点击链接47.100.200.127:8000/Users/books/ 可以访问获取所有数据的接口，如下：

   ![imagef3f72.png](https://miao.su/images/2019/06/27/imagef3f72.png)

   ![imageb1117.png](https://miao.su/images/2019/06/27/imageb1117.png)

   在浏览器输入 47.100.200.127:8000/books/1/  可以访问**获取单一图书信息的接口**（id为1的图书）：

   ![image2d5a5.png](https://miao.su/images/2019/06/27/image2d5a5.png)

   

### Serializer序列化器

#### 定义Serializer

1. 定义方法
   Django REST framewrok中的Serializer使用类来定义，须继承自rest_framework.serializer.Serializer。
   例如，我们已经有了一个数据库模型类BookInfo

   ```
   class BookInfo(models.Model)：
   	btitle = models.CharField(max_length=20, verbose_name='名称')
   	bpub_data = models.DataFiedld(verbose_name='发布日期', null=True)
   	bread = models.IntergeField(default=0, verbose_name='阅读量')
   	bcomment = models.IntergerField(default=0, verbose_name='评论量')
   ```

   我们想为这个模型类提供一个序列化器，可以定义如下：
   
   ```python
     7 class BookInfoSerializer(serializers.Serializer):
     8     """图书数据序列化器"""
     9     id= serializers.IntegerField(label='ID', read_only=True)
    10     btitle = serializers.CharField(label='名称', max_length=20)
    11     bpub_date = serializers.DateField(label='发布日期', required=False)
    12     bread = serializers.IntegerField(label='阅读量', required=False)
    13     bcomment = serializers.IntegerField(label='评论量', required=False)
    14     image = serializers.ImageField(label='图片', required=False)
   ```
   
   *注意：serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义*。serializer是独立于数据库之外的存在。
   
2. 字段与选项

   **常用字段类型**：

   | 字段                    | 字段构造方式                                                 |
   | ----------------------- | ------------------------------------------------------------ |
   | **BooleanField**        | BooleanField()                                               |
   | **NullBooleanField**    | NullBooleanField()                                           |
   | **CharField**           | CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True) |
   | **EmailField**          | EmailField(max_length=None, min_length=None, allow_blank=False) |
   | **RegexField**          | RegexField(regex, max_length=None, min_length=None, allow_blank=False) |
   | **SlugField**           | SlugField(max*length=50, min_length=None, allow_blank=False) 正则字段，验证正则模式 [a-zA-Z0-9*-]+ |
   | **URLField**            | URLField(max_length=200, min_length=None, allow_blank=False) |
   | **UUIDField**           | UUIDField(format='hex_verbose')  format:  1) `'hex_verbose'` 如`"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"`  2） `'hex'` 如 `"5ce0e9a55ffa654bcee01238041fb31a"`  3）`'int'` - 如: `"123456789012312313134124512351145145114"`  4）`'urn'` 如: `"urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` |
   | **IPAddressField**      | IPAddressField(protocol='both', unpack_ipv4=False, **options) |
   | **IntegerField**        | IntegerField(max_value=None, min_value=None)                 |
   | **FloatField**          | FloatField(max_value=None, min_value=None)                   |
   | **DecimalField**        | DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None) max_digits: 最多位数 decimal_palces: 小数点位置 |
   | **DateTimeField**       | DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None) |
   | **DateField**           | DateField(format=api_settings.DATE_FORMAT, input_formats=None) |
   | **TimeField**           | TimeField(format=api_settings.TIME_FORMAT, input_formats=None) |
   | **DurationField**       | DurationField()                                              |
   | **ChoiceField**         | ChoiceField(choices) choices与Django的用法相同               |
   | **MultipleChoiceField** | MultipleChoiceField(choices)                                 |
   | **FileField**           | FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
   | **ImageField**          | ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
   | **ListField**           | ListField(child=, min_length=None, max_length=None)          |
   | **DictField**           | DictField(child=)                                            |

   **选项参数：**

   | 参数名称            | 作用             |
   | ------------------- | ---------------- |
   | **max_length**      | 最大长度         |
   | **min_lenght**      | 最小长度         |
   | **allow_blank**     | 是否允许为空     |
   | **trim_whitespace** | 是否截断空白字符 |
   | **max_value**       | 最小值           |
   | **min_value**       | 最大值           |

   #### 通用参数：

   | 参数名称           | 说明                                          |
   | ------------------ | --------------------------------------------- |
   | **read_only**      | 表明该字段仅用于序列化输出，默认False         |
   | **write_only**     | 表明该字段仅用于反序列化输入，默认False       |
   | **required**       | 表明该字段在反序列化时必须输入，默认True      |
   | **default**        | 反序列化时使用的默认值                        |
   | **allow_null**     | 表明该字段是否允许传入None，默认False         |
   | **validators**     | 该字段使用的验证器                            |
   | **error_messages** | 包含错误编号与错误信息的字典                  |
   | **label**          | 用于HTML展示API页面时，显示的字段名称         |
   | **help_text**      | 用于HTML展示API页面时，显示的字段帮助提示信息 |

3. 创建Serializer对象
   定义好Serializer类后，就可以创建Serializer对象了。
   Serializer的构造方法：

   ```python
   Serializer(instance=None, data=empty, **kwarg)
   ```

   说明：

   1. 用于序列化时，将模型类对象传入**instance**参数

   2. 用于反序列化时，将要被反序列化的数据传入**data**参数

   3. 除了instance和data参数外，在构造Serializer对象，还可以通过**context**参数额外添加数据，如

      ```python
      serializer = AccontSerializer(account, context={'request': request})
      ```

      *通过context参数附加的数据，可以通过Serializer对象的context属性获取*

### 序列化使用

我们在Shell中学习序列化器的使用：

```shell
python manage.py shell
```

1. **基本使用**

   * 先查询出一个图书对象

     ```shell
     >>> from Users.models import BookInfo
     >>> book = BookInfo.objects.get(id=2)
     ```

   * 构造序列化器对象

     ```shell
     >>> from Users.serializers import BookInfoSerializer
     >>> serializer = BookInfoSerializer(book)
     ```

   * 获取序列化数据
     通过data属性可以获取序列化后的数据

     ```shell
     >>> serializer.data
     {'bcomment': 40, 'id': 2, 'image': None, 'btitle': '天龙八部', 'bread': 36}
     ```

   * 如果要序列化的是包含多条数据的查询集QuerySet，可以通过添加**many=True**参数补充说明

     ```shell
     >>> book_qs = BookInfo.objects.all()
     >>> serializer = BookInfoSerializer(book_qs, many=True)
     >>> serializer.data
     [OrderedDict([('id', 1), ('btitle', '射雕英雄传'), ('bread', 12), ('bcomment', 34), ('image', None)]), OrderedDict([('id', 2), ('btitle', '天龙八部'), ('bread', 36), ('bcomment', 40), ('image', None)]), OrderedDict([('id', 3), ('btitle', '笑傲江湖'), ('bread', 20), ('bcomment', 80), ('image', None)]), OrderedDict([('id', 4), ('btitle', '雪山飞狐'), ('bread', 58), ('bcomment', 24), ('image', None)]), OrderedDict([('id', 5), ('btitle', '西游记'), ('bread', 10), ('bcomment', 10), ('image', None)]), OrderedDict([('id', 6), ('btitle', '秋雨'), ('bread', 0), ('bcomment', 0), ('image', None)]), OrderedDict([('id', 7), ('btitle', '红楼梦'), ('bread', 0), ('bcomment', 0), ('image', 'Users/Snipaste_2019-05-23_19-20-13.jpg')])]
     ```

2. **关联对象嵌套序列化**
   如果需要序列化的数据中包含有其他关联对象，则对关联对象数据的序列化需要指明。
   例如，在定义英雄数据的序列化器时，外键hbook（即所属的图书）字段如何序列化？
   我们先定义 *HeroInfoSerializer* 除外键字段外的其他部分：

   ```python
    23     id = serializers.IntegerField(label='ID', read_only=True)
    24     hname = serializers.CharField(label='名字', max_length=20)
    25     hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别'， required=False)
    26     hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
   ```

   对于关联字段可以采用以下形式

   1. *PrimaryKeyRelatedField*
      此字段将被序列化为关联对象的主键

      ```shell
      hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
      或
      hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
      ```

      指明字段时需要包含**read_only=True**或者**queryset**参数：

      * 包含read_only=True参数时，该字段将不能用作反序列化使用
      * 包含queryset参数时，将被用作反序列化时参数校验使用

      ```shell
      >>> from Users.serializers import HeroInfoSerializer
      >>> from Users.models import HeroInfo
      >>> hero = HeroInfo.objects.get(id=6)
      >>> serializer = HeroInfoSerializer(hero)
      >>> serializer.data
      {'hname': '乔峰', 'hbook': 2, 'hgender': 1, 'hcomment': '降龙十八掌', 'id': 6}
      ```

   2. *StringRelateField*
      此字段将被序列化为关联对象的字符串表示方式（即__str__方法的返回值）

      ```shell
      hbook = serializers.StringRelatedField(label='图书')
      ```

      使用效果：

      ```shell
      {'id': 6, 'hname': '乔峰', 'hgender': 1, 'hcomment': '降龙十八掌', 'hbook': '天龙八部'}
      ```

   3. *HyperlinkedRelatedField*
      此字段将被序列化为获取关联对象数据的接口连接

      ```python
      hbook = serializers.HyperlinkedRelatedField(label='图书', read_only=True, view_name='books-detail')
      ```

      必须指明 view_name 参数，以便DRF根据视图名称寻找路由，进而拼接成完整URL。
      使用效果：

      ```shell
      {'id': 6, 'hname': '乔峰', 'hgender': 1, 'hcomment': '降龙十八掌', 'hbook': 'http://127.0.0.1:8000/books/2/'}
      ```

      我们暂时还没有定义视图，此方式不再演示。

   4. *SlugRelateField*
      此字段将序列化为关键对象的指定字段数据

      ```python
      hbook = serializers.SlugRelatedField(label='图书', read_only=True, slug_field='bpub_data')
      ```

      slug_field指明使用关键对象的哪个字段，使用效果：

      ```shell
      {'id': 6, 'hname': '乔峰', 'hgender': 1, 'hcomment': '降龙十八掌', 'hbook': datetime.date(1986, 7, 24)}
      ```

   5. 使用关联对象的序列化器

      ```shell
      hbook = BookInfoSerializer()
      ```

      使用效果

      ```shell
      {'id': 6, 'hname': '乔峰', 'hgender': 1, 'hcomment': '降龙十八掌', 'hbook': OrderedDict([('id', 2), ('btitle', '天龙八部')te', '1986-07-24'), ('bread', 36), ('bcomment', 40), ('image', None)])}
      ```

   6. 重写 *to \_representation* 方法
      序列化器的每个字段实际都会由该字段类型的 *to_representation* 方法决定格式的，可以通过重写该方法来决定格式。
      *注意，to_representations 方法不仅局限在控制关联对象格式上，适用于各个序列器字段类型* 。
      自定义一个新的关联字段：

      ```python
       33 class BookRelateField(serializers.RelatedField):
       34     """自定义用于处理图书的字段"""
       35     def to_presentation(self, value):
       36         return 'Book: %d %s' % (value.id, Value.btitle) 
      ```

      指明hbook为BookRelatedField类型：

      ```shell
      hbook = BookRelateField(read_only=True)
      ```

      使用效果

      ```shell
      {'id': 6, 'hname': '乔峰', 'hgender': 1, 'hcomment': '降龙十八掌', 'hbook': 'Book: 2 天龙八部'}
      
      ```

3. mang参数
   如果关联的对象数据不是只有一个，而是包含多个数据，如想序列化图示BookInfo数据，每个BookInfo对象关联的英雄HeroInfo对可能有多个，此时关联字段类型的指明仍可使用上述几种方式，只是在声明关联字段时，多补充一个mang=True参数即可。
   此处仅拿PrimaryKeyRelateField类型来举例，其他相同，在BookInfoSerilizer中添加关联字段

   ```python
   class BookInfoSerializer(serializers.Serializer):
       """图书数据序列化器"""
       id = serializers.IntegerField(label='ID', read_only=True)
       btitle = serializers.CharField(label='名称', max_length=20)
       bpub_date = serializers.DateField(label='发布日期', required=False)
       bread = serializers.IntegerField(label='阅读量', required=False)
       bcomment = serializers.IntegerField(label='评论量', required=False)
       image = serializers.ImageField(label='图片', required=False)
       heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增
   ```

   使用效果：

   ```shell
   from Users.serializers import BookInfoSerializer
   from Users.models import BookInfo
   book = BookInfo.objects.get(id=2)
   serializer = BookInfoSerializer(book)
   serializer.data
   # {'id': 2, 'btitle': '天龙八部', 'bpub_date': '1986-07-24', 'bread': 36, 'bcomment': 40, 'image': None, 'heroinfo_set': [6,8, 9]}
   ```

### 反序列化使用

#### 验证

使用序列化器进行反序列化时，需要对数据进行验证后，才能获取验证成功的数据或保存成模型类对象。在获取反序列化的数据前，必须调用**is_valid( )**方法进行验证，验证成功返回True，否则返回False。
验证失败，可以通过序列化器对象的**errors**属性获取错误信息，返回字典，包含字段和字段的控制的错误。如果是非字段错误，可以通过修改REST framework配置中的**NON_FIELD_ERRORS_KEY**来控制错误字典中的键名。
验证成功，可以通过序列化器对象的**validated_data**属性获取数据。
在定义序列化器时，指明每个字段的序列化类型和选项参数，本身就是一种验证行为。
如我们前面定义过的BookInfoSerializer：

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
```

通过构造序列化器对象，并将要反序列化的数据传递给data构造参数，进而进行验证

```shell
from Users.serializers import BookInfoSerializer
data = {'bpub_date': 123}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # 返回False
serializer.errors
# {'btitle': [ErrorDetail(string='This field is required.', code='required')], 'bpub_date': [ErrorDetail(string='Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]].', code='invalid')]}
serializer.validated_data  # {}

data = {'btitle': 'python'}
serializer = BookInfoSerializer(data=data)
serializer.is_valid()  # True
serializer.errors  # {}
serializer.validated_data  #  OrderedDict([('btitle', 'python')])
```

*is_valid()* 方法还可以在验证失败时抛出异常*serializers.ValidationError* ，可以通过传递**raise_exception=True**参数开启，REST framework接收到此异常，会向前端返回HTTP 400 BadRequest响应。

```shell
# Return a 400 response if the data was invalid.
serializer.is_valid(raise_exception=True)
```

如果觉得这些还不够，需要再补充定义验证行为，可以使用以下三种方法：

1. *validate_<field_name>*
   对`<field_name>`字段进行验证，如：

   ```python
     8 class BookInfoSerializer(serializers.Serializer):
     9     """图书数据序列化器"""
    	...
    18     def validate_btitle(self, value):
    19         if 'django' not in value.lower():
    20             raise serializers.ValidationError('图书不是关于Django的')
    21         return value
   ```

   测试：

   ```shell
   from Users.serializers import BookInfoSerializer
   data = {'btitle': 'python'}
   serializer = BookInfoSerializer(data=data)
   serializer.is_valid()  # False   
   serializer.errors
   #  {'btitle': [ErrorDetail(string='图书不是关于Django的', code='invalid')]}
   ```

2. *validate*
   在序列化器中需要同时对多个字段进行比较验证时，可以定义validate方法来验证，如：

   ```python
    23     def validate(self, attrs):
    24         bread = attrs['bread']
    25         bcomment = attrs['bcomment']
    26         if bread < bcomment:
    27             raise serializers.ValidationError('阅读量小于评论量')
    28         return attrs
   ```

   测试：

   ```shell
   >>> from Users.serializers import BookInfoSerializer
   >>> data = {'btitle': 'about django', 'bread': 10, 'bcomment': 20}
   >>> s = BookInfoSerializer(data=data)
   >>> s.is_valid()
   False
   >>> s.errors
   {'non_field_errors': [ErrorDetail(string='阅读量小于评论量', code='invalid')]}
   ```

3. *validators*
   在字段中添加 *validators* 选项参数，也可以补充验证行为，如：

   ```python
     7 def about_django(value):
     8     if 'django' not in value.lower():
     9         raise serializers.ValidationError('不是Django')                               
    10                          
    11                           
    13 class BookInfoSerializer(serializers.Serializer):
   	...
   ```

   测试：

   ```shell
   >>> from Users.serializers import BookInfoSerializer
   >>> data = {'btitle': 'python'}
   >>> serializer = BookInfoSerializer(data=data)
   >>> serializer.is_valid()
   False
   >>> serializer.errors
   {'btitle': [ErrorDetail(string='图书不是关于Django的', code='invalid')]}
   ```

   REST framework提供的validators：

   * UniqueValidator
     单字段唯一，如

   ```python
   from rest_framework.validators import UniqueValidator
   slug = SlugField(
   	max_length=100,
   	validators=[UniqueValidator(queryset=BlogPost.objects.all())]
   )
   ```

   * UniqueTogetherValidation
     联合唯一，如：

     ```python
     from rest_framework.validators import UniqueTogetherValidator
     
     class ExampleSerializer(serializers.Serializer):
     	# ...
     	class Meta:
     		validators = [
     			UniqueTogetherValidator(
     				queryset=ToDoItem.objects.all(),
     				fields=('list', 'position')
     			)
     		]
     ```

#### 保存

如果在验证成功后，想要基于validated_data完成数据对象的创建，可以通过create()和update()两个方法来实现。

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    ...

    def create(self, validated_data):
        """新建"""
        return BookInfo(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_data = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        return instance
```

如果需要在返回数据对象的时候，也将数据保存到数据库中，则可以进行如下修改

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    ...

    def create(self, validated_data):
        """新建"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_data = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance
```

实现了上述两个方法后，在反序列化数据的时候，就可以通过save() 方法返回一个数据对象实例了：

```python
book = serializer.save()
```

如果创建序列化器对象的时候，没有传递instance实例，则调用save()方法的时候，create()被调用，相反，如果传递了instance实例，则调用save()方法的时候，update()被调用。
测试：

```shell
>>> from Users.serializers import BookInfoSerializer
>>> data = {'btitle': '封神演义'}
>>> serializer = BookInfoSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.save()
<BookInfo: 封神演义>

>>> from Users.serializers import BookInfoSerializer
>>> from Users.models import BookInfo
>>> book = BookInfo.objects.get(id=2)
>>> data = {'btitle': '倚天'}
>>> serializer = BookInfoSerializer(book, data=data)
>>> serializer.is_valid()
True
>>> serializer.save()
<BookInfo: 倚天>
>>> book.btitle
'倚天'
```

**两点说明：**

1. 在对序列化器进行save( )保存时，可以额外传递数据，这些数据可以在create( )和update( )中的validated_data参数获取到：

   ```shell
   serializer.save(owner=request.user)
   ```

2. 默认序列化器必须传递所有required的字段，否则会抛出验证异常。但是我们可以使用partial参数来允许部分字段更新：

   ```shell
   # Update `comment` with partial data
   serializer = CommentSerializer(comment, data={'content': u'foo bar'}, partial=True)
   ```

### 模型类序列化器ModelSerializer

如果我们想要使用序列化器对应的是Django的模型类，DRF为我们提供了ModelSerializer模型类序列化器来帮助我们快速创建一个Serializer类。
ModelSerializer与常规的Serializer相同，但提供了：

* 基于模型类自动生成一系列的字段
* 基于模型类自动为Serializer生成validators，比如unique_together
* 包含默认的create()和update()的实现

#### 定义

比如我们创建一个BookInfoSerializer

```python
class BookInfoSerializer(serializers.ModelSerializer):
	"""图书数据序列化器"""
	class Meta:
		model = BookInfo
		fields = '__all__'
```

* model 指明参照哪个模型类
* fields 指明为模型类的哪些字段生成

我们可以在`shell`中查看自动生成的BookInfoSerializer的具体实现：

```shell
>>> from Users.serializers import BookInfoSerializer
>>> serializer = BookInfoSerializer()
>>> serializer
BookInfoSerializer():
    id = IntegerField(label='ID', read_only=True)
    btitle = CharField(label='名称', max_length=20)
    bpub_date = DateField(label='发布日期', required=False)
    bread = IntegerField(label='阅读量', required=False)
    bcomment = IntegerField(label='评论量', required=False)
    image = ImageField(label='图片', required=False)
    heroinfo_set = PrimaryKeyRelatedField(many=True, read_only=True)
```



#### 指定字段

1. 使用fields来明确字段，`__all__`表名包含所有字段，也可以写明具体哪些字段，如：

   ```python
   class BookInfoSerializer(serializers.ModelSerializer):
   	"""图书数据序列化器"""
   	class Meta:
   		model = BookInfo
   		field = ('id', 'btitle', 'bpub_data')
   ```

2. 使用`exclude`可以明确排除掉哪些字段

   ```python
   class BookInfoSerializer(serializers.ModelSerializer):
       """图书数据序列化器"""
       class Meta:
           model = BookInfo
           exclude = ('image',)
   ```

3. 默认`ModelSerializer`使用主键作为关联字段，但是我们可以使用`depth`来简单的生成嵌套表示，`depth`应该是正式，表名嵌套的层级数量。如：

   ```python
   class HeroInfoSerializer2(serializers.ModelSerializer):
   	class Meta:
   		model = HeroInfo
   		field = '__all__'
   		depth = 1
   ```

   形成的序列化器如下：

   ```shell
   HeroInfoSerializer():
       id = IntegerField(label='ID', read_only=True)
       hname = CharField(label='名称', max_length=20)
       hgender = ChoiceField(choices=((0, 'male'), (1, 'female')), label='性别', required=False, validators=[<django.core.valators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
       hcomment = CharField(allow_null=True, label='描述信息', max_length=200, required=False)
       hbook = NestedSerializer(read_only=True):
           id = IntegerField(label='ID', read_only=True)
           btitle = CharField(label='名称', max_length=20)
           bpub_date = DateField(allow_null=True, label='发布日期', required=False)
           bread = IntegerField(label='阅读量', max_value=2147483647, min_value=-2147483648, required=False)
           bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=-2147483648, required=False)
   ```

4. 显示指明字段

   ```python
   class HeroInfoSerializer(serializers.ModelSerializer):
   	hbook = BookInfoSerializer
   	class Meta:
   		model = HeroInfo
   		fields = ('id': 'hname', 'hgender', 'hcomment', 'hbook')
   ```

5. 指明只读字段
   可以通过`read_only_fields`指明只读字段，即仅用于序列化输出的手段

   ```python
   class BookInfoSerializer(serializers.ModelSerializer):
   	"""图书数据序列化器"""
   	class Meta:
           model = BookInfo
           fields = ('id', 'btitle', 'bpub_data', 'bread', 'bcomment')
           read_only_field = ('id', 'bread', 'bcomment')
   ```

#### 添加额外参数

我们可以使用`extra_kwargs`参数为`ModelSerializer`添加或修改原有的选项参数

```shell
class BookInfoSerializer(serializers.ModelSerializer):
	"""图书数据序列化器"""
	class Meta:
		model = BookInfo
		fields = ('id', 'btitle', 'bpub_data', 'bread', 'bcomment')
		extra_kwargs = {
			'bread': {'min_value': 0, 'required': True},
			'bcomment': {'max_value': 0, 'required': True},
		}
```

## 视图

### Request与Response

#### Resquest

REST framework 传入视图的request对象不再是Django默认的HTTPRequest对象，而是REST framework提供的扩展类HTTPRequest类的`Request`类的对象。

REST framework 提供了`Parse`解析器，在接受到请求后会自动根据`Content_Type`指明的请求数据类型（如JSON、表单等）将请求数据进行parse解析，解析为类字典对象保存到Request对象中。

**Request对象的数据是自动根据前端发送数据的格式进行解析之后的结果**。

无论前端发送的哪种格式的数据，我们都可以以统一的方式读取数据。

**常用属性**

1. *data*
   `request.data`返回解析之后的请求体数据。类似于Django中标准的`request.POST`和`request.FILES`属性，但是提供如下特性：
   * 包含了解析之后的文件和非文件数据
   * 包含了对POST、PUT、PATCH请求方式解析后的数据
   * 利用了REST framework的parsers解析器，不仅支持表单类型数据，也支持JSON数据
2. *.query_params*
   `request.query_params`与Django标准的`request.GET`相同，只是更换了更正确的名称而已。

#### Response

`rest_framework.response.Response`
REST framework提供了一个响应类`Response`，使用该类构造响应对象时，响应的具体数据内容会被转换（render渲染）成符合前端需求的类型。

REST framework提供了`Renderer`渲染器，用来根据请求头中的`Accpt`（接受数据类型声明）来自动转换响应数据到对应格式。如果前端请求中未进行Accept声明，则会采用默认方式处理响应数据，我们可以通过配置来修改默认响应格式。

```python
REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': ( # 默认响应渲染类
    	'rest_framework.renderers.JSONRenderer', # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer', # 浏览API渲染器
    )
}
```

**构造方式**

```shell
Response(data, status=None, template_name=None, headers=None, content_type=None)
```

`data`数据不要是render处理之后的数据，只需传递python的内建类型数据即可，REST framework会使用`renderer`渲染器处理`data`。

`data`不能是复杂结构的数据，如Django的模型类对象，对于这样的数据我们可以用`Serializer`序列化器序列化处理后（转为了Python字典类型）再传递给`data`参数。
参数类型：

* `data`：为响应追捕的序列化处理后的数据
* `status`：状态码，默认200
* `template_name`：模块名称，如果使用`HTMLRenderer`时需指明；
* `headers`：用于存放响应头信息的字典
* `content_type`：响应数据的Content-Type，通常此参数无需传递，REST framework会根据前端所需类型数据来设置该参数。

**常用属性**

1. `.data`
   传给response对象的序列化后，但尚未render处理的数据
2. `.status_code`
   状态码的数字
3. `.content`
   经过render处理后的响应数据

#### 状态码

为了方便设置状态码，REST framework在`rest_frmaework.status`模块中提供了常用状态码常量。

1. 信息告知——1xx

   ```python
   HTTP_100_CONTINUE
   HTTP_101_SWITCHING_PROTOCOLS
   ```

2. 成功——2xx

   ```pyhton
   HTTP_200_OK
   HTTP_201_CREATED
   HTTP_202_ACCEPTED
   HTTP_203_NON_AUTHORITATIVE_INFORMATION
   HTTP_204_NO_CONTENT
   HTTP_205_RESET_CONTENT
   HTTP_206_PARTIAL_CONTENT
   HTTP_207_MULTI_STATUS
   ```

3. 重定向——3xx

   ```python
   HTTP_300_MULTIPLE_CHOICES
   HTTP_301_MOVED_PERMANENTLY
   HTTP_302_FOUND
   HTTP_303_SEE_OTHER
   HTTP_304_NOT_MODIFIED
   HTTP_305_USE_PROXY
   HTTP_306_RESERVED
   HTTP_307_TEMPORARY_REDIRECT
   ```

4. 客户端错误——4xx

   ```pyhton
   HTTP_400_BAD_REQUEST
   HTTP_401_UNAUTHORIZED
   HTTP_402_PAYMENT_REQUIRED
   HTTP_403_FORBIDDEN
   HTTP_404_NOT_FOUND
   HTTP_405_METHOD_NOT_ALLOWED
   HTTP_406_NOT_ACCEPTABLE
   HTTP_407_PROXY_AUTHENTICATION_REQUIRED
   HTTP_408_REQUEST_TIMEOUT
   HTTP_409_CONFLICT
   HTTP_410_GONE
   HTTP_411_LENGTH_REQUIRED
   HTTP_412_PRECONDITION_FAILED
   HTTP_413_REQUEST_ENTITY_TOO_LARGE
   HTTP_414_REQUEST_URI_TOO_LONG
   HTTP_415_UNSUPPORTED_MEDIA_TYPE
   HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
   HTTP_417_EXPECTATION_FAILED
   HTTP_422_UNPROCESSABLE_ENTITY
   HTTP_423_LOCKED
   HTTP_424_FAILED_DEPENDENCY
   HTTP_428_PRECONDITION_REQUIRED
   HTTP_429_TOO_MANY_REQUESTS
   HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
   HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
   ```

5. 服务器——5xx

   ```python
   HTTP_500_INTERNAL_SERVER_ERROR
   HTTP_501_NOT_IMPLEMENTED
   HTTP_502_BAD_GATEWAY
   HTTP_503_SERVICE_UNAVAILABLE
   HTTP_504_GATEWAY_TIMEOUT
   HTTP_505_HTTP_VERSION_NOT_SUPPORTED
   HTTP_507_INSUFFICIENT_STORAGE
   HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
   ```

### 视图概览

REST framework 提供了众多的通用视图基类与扩展，以简化视图的编写。
视图的继承关系：
![imageafa78.png](https://miao.su/images/2019/06/29/imageafa78.png)

视图的方法和属性：
![_0ad7b.png](https://miao.su/images/2019/06/29/_0ad7b.png)

### 视图说明

#### 两个基类

1.**APIView**
`rest_framework.views.APIView`

`APIView`是REST framework提供的所有视图的基类，继承自Django的`View`父类。
`APIView`与`View`的不同之处在于：

* 传入到视图方法中的是REST framework的`Request`对象，而不是Django的`HttpRequest`对象；
* 视图方法可以返回REST framework的`Response`对象，视图会响应数据设置（render）符合前端要求的格式；
* 任何`APIException`异常都会被捕获到，冰球处理成合适的响应信息；
* 在进行dispatch()分发前，会对请求进行身份认证、权限检查、流量控制。

##### 支持定义的属性：

- **authentication_classes** 列表或元祖，身份认证类
- **permissoin_classes** 列表或元祖，权限检查类
- **throttle_classes** 列表或元祖，流量控制类

在`APIView`中仍以常规的类视图定义方法来实现get() 、post() 或者其他请求方式的方法。

举例：

```python
from rest_framework.views import APIView
from rest_framework.response import Response

# url(r'^books/$', views.BookListView.as_view()),
class BookListView(APIView):
    def get(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)
```

