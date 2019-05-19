# 前端入门



[TOC]





## html和css入门

### 1.HTML文件基本结构

```html
<!DOCTYPE html> //文档申明
<html lang="en">
<head> //头
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title> //标题
</head>
<body> //体
    
</body>
</html>
```

[返回目录](#前端入门)

### 2.常用标签概览

```html
<!DOCTYPE html>  //首行 文档声明
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title> //网页的名称
</head>
<body>
    <h1>标题标签  块元素</h1> 
    <div>  //布局标签 里面可放任意元素 块元素特性
        <br> //换行标签 
        <img src="图片地址" alt="加载失败显示内容"> //图片标签 内联元素特性
    </div>
    <p>  //段落标签 块元素特性
        <span>文字特殊标记</span> //特殊文字标记标签 内联元素特性
        <a href+"链接地址">显示链接的文字(蓝色 下划线)</a> //超链接标签 内联元素特性
    </p>
    <!--这是注释标签  还有字符实体   &nbsp空格   "<"&lt  ">"&gt-->
</body>
</html>
```

[返回目录](#前端入门)

### 3.文字格式标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <b>加粗</b> //以下都是内联元素特性 不换行
    <i>倾斜</i>
    <u>下划线</u>
    <s>删除线</s>
    <br> <!--或者也可以写成一下形式-->
    <strong>加粗</strong>
    <em>倾斜</em>
    <ins>下划线</ins>
    <del>删除线</del>
</body>
</html>
```

[返回目录](#前端入门)

### 4.图片标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <img src="/home/Desktop/gakki.jpg" alt="gakki最美~" title="点我点我">
    <!--html的标签内 用键值对x="y"表示标签属性 一个标签可以添加多个属性 各个属性之间用空格隔开-->
	<!--alt="如果图片读取失败 则显示这个文本"-->
    <!--title="鼠标悬停在图片上时会显示这里的备注信息"-->    
</body>
</html>
```

[返回目录](#前端入门)

### 5.超链接标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <a href="http://www.baidu.com">百度</a>
    <!--href="链接地址 以http协议开头"-->
    <a href="01-demo.html" target="_blank">本地跳转</a>
    <!--target有 
		1."_self"默认用新页面替换当前页面
		2."_blank"打开一个新的标签页
		3."framename"在指定的iframe窗口中打开链接-->
    <a href="#">假链接 点了也没用</a>
    <a href="http://www.bilibili.com"><img src="gakki.jpg" alt="ruin"></a>
    <!--可以利用标签嵌套 使一个图片拥有超链接功能 即点击图片跳转-->
    
</body>
</html>
```

[返回目录](#前端入门)

### 6.页面布局初体验

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!--布局先分行 再分列-->
    <div>
        <div>
        	先把行分好<h1>
            标题
            </h1><a href="xxx">超链接</a>                
        </div>
    </div>
    <p>
        这是一个段落,可以放入一大段的文字
    </p>
</body>
</html>
```

[返回目录](#前端入门)

### 7.css书写方式

Cascading Style sheets  层叠样式表  CSS专门负责html文档内的表现形式  通过选择器将样式和页面属性关联 
引入方式有一下三种：

```html
<!DOCTYPE html> <!--嵌入式  电商首页可能会用-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title> <!--写在head中-->
    <style type="text/css"> /*text/css表示纯文本的css形式 这个书写可有可无*/
        h1{color:red;font-size:100px;font-family:"宋体"；}
    </style>
</head>
<body>
    <h1>
        我设计的标题
    </h1>
</body>
</html>
```

```html
<!DOCTYPE html> <!--外链式  工作中最常用的用法--> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="mystyle.css"> 
    <!--rel="html与css文件的关系" href="css文件的地址" -->
</head>
<body>
    <p>
        用css装饰的段落文字
    </p>
</body>
</html>
```

```html
<!DOCTYPE html> <!--行内式  基本不用-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div style="color:blue;heiget:100px;width:200px;background:red;">
        <!--要给哪一块加表现形式 就在标签中加style-->
        这是一个行内式的css测试块
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 8.常用的文字控制属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        p{
            color:blue;  /*文字颜色*/
            font-weight:bold;  /*是否加粗*/
            font-style:italic;  /*是否倾斜*/
            font-size:20px;  /*字号*/
            font-family:"宋体";  /*字体*/
            line-height:20px;  /*行高*/
            text-decoration:underline;  /*文字下划线*/
            text-indent:2em;  /*首行缩进 em为一个字符的大小*/
          }
        h1{font-wight:normal;}
        a{
            text-decoration:normal;
        }
    </style>
</head>
<body>
    <p>
        这是一个段落
    </p>
    <h1>
        标题
    </h1>
    <a>这是一个超链接</a>
</body>
</html>
```

[返回目录](#前端入门)

### 9.基本布局属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{
            width:300px;
            height:200px;
            background:green;
        }
    </style>
</head>
<body>
    <div>
        布局的基本属性是 宽 高 背景色
    </div>
</body>
</html>
```

[返回目录](#前端入门)

## html和css进阶

### 1.选择器

```html
<!DOCTYPE html>  <!--类选择器-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        .aa{
            color:green;
        }
        .bb{
            color:red;
        }
    </style>
</head>
<body>
    <div class='aa'>
        这是aa类的展示
    </div>
    <p class="bb">
        这是bb类的展示
    </p>
</body>
</html>
```

```html
<!DOCTYPE html>  <!--并集选择器-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div,p,h1{
            color:red;
        }
    </style>
</head>
<body>
    <div>
        红色
    </div>
    <p>
        也是红色
    </p>
    <h1>
        还是红色
    </h1>
</body>
</html>
```



```html
<!DOCTYPE html> <!--层级选择器-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        /*注意中间有一个空格 就是层级选择器*/
        ul .aa{
            color:red;
        }
    </style>
</head>
<body>
    <ul>
        <li class="aa">ul li</li>
    </ul>
</body>
</html>
```

```html
<!DOCTYPE html> <!--id选择器-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
    	/*注意:一个id选择器一个页面只能使用一次*/
        /*实际上并不是用id选择器写css样式  而是通过id选择器查找标签做数据交互*/
        #aa{
            color:green;
        }
    </style>
</head>
<body>
    <div id="aa">
        11111
    </div>
</body>
</html>
```

```html
<!DOCTYPE html> <!--伪类选择器-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        a{color:red;}
        a:hover{color:green}
        /*一共有四种 1.a:link{}链接颜色 2.a:visited{}点击后 3.a:hover{}悬停 4.a:active{}点按时*/
    </style>
</head>
<body>
    <!--伪类就是状态  以冒号开头-->
    <a href="#">点我点我!</a>
</body>
</html>
```

[返回目录](#前端入门)

### 2.列表

一般应用在布局中的新闻标题列表和文章标题列表以及菜单

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        ul{list-style:none; /*去掉列表样式和项目符号*/}
    </style>
</head>
<body>
    <!--经验:一般前端开发 网站的导航会使用ul标签写代码-->
    <!--列表:用于整体的大标签 嵌套表示某一项的小标签-->
    <ul>
        <!--无序:ul嵌套li ul是无序列表整体 li时某一项-->
        <!--前面没有序号-->
        <li>新闻1</li>
        <li>新闻2</li>
        <li>新闻3</li>
    </ul>
    <ol>
        <!--有序:ol嵌套li ol是整体标签 li是某一项-->
        <!--前面有序号-->
        <li>标题1</li>
        <li>标题2</li>
        <li>标题3</li>
    </ol>
    <dl>
        <!--项目:dl嵌套dt和dd  dl是整体标签 dt是项目标题 dd是项目的描述信息-->
        <dt>项目名</dt>
        <dd>项目描述</dd>
    </dl>
</body>
</html>
```

[返回目录](#前端入门)

### 3.表格

```html
<!DOCTYPE html>  <!--我感觉这辈子都用不到这个极其落后的玩意儿了-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        table{border:1px red solid;
        /*border(一个key对应多个值):粗细 颜色 线条种类(solid是实线)*/
        border-collapse:collapse;
        /*合并表格边框线*/}
    </style>
</head>
<body>
    <!-- 国内2005年互联网行业改革：网站改版从表格布局改成div布局 -->
    <!-- 表格：浏览器读取完整个表格再显示页面 -->
    <!-- div：读取一行显示一行 -->
    <!-- 结构：table嵌套tr，tr嵌套td；table是整个表格，tr是行，td是单元格 -->
    <!-- th:表头 -->
    <!-- cellspacing:拉开单元格之间的距离 -->
    <!-- cellpadding :拉开内容和td边缘之间的距离 -->
    <table cellspacing="50" cellpadding="20">
        <tr>
            <th>1</th>
            <th colspan="2">2</th>            
        </tr>
        <tr>
            <td>1</td>
            <td rowspan="2">2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>1</td>            
            <td>3</td>
        </tr>
    </table>
</body>
</html>
```

[返回目录](#前端入门)

### 4.表单

用于搜索不同类型的用户输入

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        textarea{resize:none;outline:none;/*默认焦点框为蓝色*/}
        /*定义多行文本输入框*/
    </style>
</head>
<body>
    <form action="提交地址" method="post">
    <!--form标签 定义整体的表单区域 action表单数据提交地址 method提交方法-->
        <!--input标签定义通用的表单元素-->
        <input type="text" value="默认值"> <!--单行文本框--><br>
        <input type="password"> <!--输入密码-->
        <input type="radio" name="favorite food" id="apple"><lable for="apple">苹果</lable> <!--radio单选框-->
        <input type="radio" name="favorite food" id="banana"><lable for="banana">香蕉</lable> <!--lable用于扩大触发区域 for后的数值应该与id一样-->
        <input type="file"> <!--上传文件-->
        <textarea>这是多行文本域</textarea>
        <select> <!--下拉菜单 配合option食用更佳-->
            <option>嫁</option>
            <option>不嫁</option>
            <option>丁克</option>
        </select>
        <input type="checkbox" checked>娶 <!--多选框-->
        <input type="submit" value="注册"> <!--提交按钮-->
        <input type="button" value="普通按钮"> <!--普通按钮-->
        <botton>还可以直接用标签创建</botton>
        <input type="reset"> <!--重置按钮-->
    </form>
</body>
</html>
```

[返回目录](#前端入门)

### 5.css盒子模型

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{
            width:300px;
            height:200px;
            background:#ccc;
            border:10px solid red;
            padding:20px; /*内边距 是内容与盒子边缘的距离*/
            box-sizing:border-box; /*启用盒子内减模式 css3.0的新功能*/
            margin:50px; /*外边距 盒子外面的距离 拉开两个盒子之间的距离*/
        }
    </style>
</head>
<body>
    <div>
        lalala~
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 6.文字居中

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{width:300px; height:200px; background:red;
        	text-align:center; /*文字垂直居中 设置行高属性等于自身高度属性*/
            line-height:200px; }
        p{
            line-height:100px;
        }
    </style>
</head>
<body>
    <div>
        文字
    </div>
    <p>
        6666666666666666666666666666666666666666666666666666666666666666666
    </p>
</body>
</html>
```

[返回目录](#前端入门)

### 7.版心居中

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{width:1000px; height:200px; background:#ccc;
        margin: 0 auto;} /*网页有效内容的 标签 居中(并不是标签内的文字)*/
    </style>
</head>
<body>
    <div>
        996
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 8.显示隐藏

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{
            width:100px; height:100px; background:green;
            visibility:hidden; /*占位*/
            /*还可以使用 display:none;(不占位)  display:block(占位)*/
        }
    </style>
</head>
<body>
    <div>
        亲
    </div>
    <h1>
        这是一个标题
    </h1>
</body>
</html>
```

[返回目录](#前端入门)

### 9.溢出

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{width:100px;height:100px;background:#ccc;overflow:auto;}
        /*hidden隐藏 auto有滚动条 scroll总有滚动条 visible默认值会显示出框*/
    </style>
</head>
<body>
    <div>
        其实还是可以的嘛~其实还是可以的嘛~其实还是可以的嘛~
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 10.浮动

浮动的框可以向左或向右移动  直到它的外边缘碰到包含框或另一个浮动框的边框为止  由于浮动框不在文档的普通流中  所以文档的普通流中的块框表现得就像浮动框不存在一样

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        .box{width:100px;height:100px;background:red;
        float:right;}
    </style>
</head>
<body>
    <div class="box">
        这是一个浮动块
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 11.定位

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        .box1{border:1px solid red;left:100px;right:200px;
        position:relative;} /*相对定位 以父级做参照*/
        .box2{border:1px solid green;left:100px;right:200px;
        position:absolute;} /*绝对定位 脱离文档流 以父级参照 会移出屏幕*/
        .box3{border:1px solid blue;left:100px;right:200px;
        position:fixed;} /*固定定位 脱离文档流 相对浏览器位置固定*/
    </style>
</head>
<body>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <div class="box1"><img src="xxx.jpj"></div>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <div class="box2"><img src="xxx.jpj"></div>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <div class="box3"><img src="xxx.jpj"></div>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
    <p>666666666666666666666666666666666666666666666666666666666666666</p>
</body>
</html>
```

[返回目录](#前端入门)

### 12.iframe

可以在页面中打开一个局部窗口 嵌入另一个页面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        iframe{width:1200px; height:800px;}
    </style>
</head>
<body>
    <a href="http://www.baidu.com" target="myframe">百度</a>
    <a href="http://www.taobao.com" target="myframe">淘宝</a>
    <iframe src="gakki.html" name="myframe"></iframe>
    <!--打开新的页面 嵌入在iframe中-->
</body>
</html>
```

[返回目录](#前端入门)

## JavaScript初步

JavaScript是运行在浏览器端的语言 主要解决前端与用户的交互问题  HTML 中的脚本必须位于 `<script> </script>` 标签之间     脚本可被放置在 HTML 页面的 `<body>  <head> `部分中

### 1. 获取html元素并替换

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="box"> <!--这里并不是id选择器 只是起了一个别名 下边好取元素-->
        divdivdiv
    </div>
</body>
</html>
<script> document.getElementById('box').innerHTML = 'javascript'</script>
<!--document.getElementById('xxx')获取htmlxx标签中的元素-->
<!--innerHTML = XXX 可以在获取之后向其中写入xxx从而改变html元素里的内容-->
```

[返回目录](#前端入门)

### 2. 入口函数

js取元素的操作并不能放在html定义这个元素的上方 因为系统是顺序执行的 这样这个脚本并不能生效 所以我们只有把js脚本写在代码的最下方或者使用一个入口函数

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	window.onload = function(){
            document.getElementById('box').innerHTML = 'javascript'
        } /*用function(){} 把整个脚本封装成一个函数window.onload
        他会等到html文档的元素加载完成再执行这个脚本*/
    </script>
</head>
<body>
    <div id="box">
        divdivdiv
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 3.利用脚本控制CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    window.onload = function(){
        document.getElementById('box').style.color = 'red'
        document.getElementById('box').style.background = "#ccc"
        document.getElementById('box').style.fontSize = "60px"
    } /*获取元素之后 .style.属性='xxx' 就能够控制html元素的属性*/
        /*注意 HTML里属性用'-'连接的 在js里需改成小驼峰写法*/
        /*class属性改成className*/
    </script>
</head>
<body>
    <div id="box">
        脚本控制的文字
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 4.变量

可以把获取到的元素赋给一个变量 然后通过变量名.innerHTML可以控制html元素的属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    window.onload = function(){
        var oBox = document.getElementById('box') /*var表示赋值给一个变量*/
        alert(typeof(oBox)) /*获取oBox的变量类型*/
        oBox.innerHTML = '<p>js变量</p>' /*最终输出的是这个*/
    }
    </script>
</head>
<body>
    <div class='box'>
        js变量控制的元素
    </div>
</body>
</html>
```

[返回目录](#前端入门)

### 5.数据类型

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script> 
    	var num1 = 1.1  // number数字型
    	var num2 = '1' // string字符串
        var bool = true // boolean布尔型
        // undefined 未定义 出错时会显示这个类型
        var 0 = null // object对象型 空对象和有数据的对象
        alter(typeof(0))
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 6.函数

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	alert(num) // 变量不支持预解析
        var num=1
        fnAlert() //函数支持预解析
        function fnAlert(){alter('自定义函数的弹窗')}
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 7.条件判断

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
    	var times =10
        if(time <= 6){alter('what you want do')}
        else if(times <= 7){alter('just go')}
        else{alter('have no choose')}
        /*与&&  或&&  非!*/
    </style>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 8.事件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    window.onload = function(){
        var oBtn1 = document.getElementById('btn1')
        var oBtn2 = document.getElementById('btn2')
        var oBtn3 = document.getElementById('btn3')
        // function(){} 匿名函数
        oBtn1.onclick = function(){alert('点击成功')}
        oBtn2.onmouseover = function(){alert('鼠标划过')}
        oBtn3.onmouseout = function(){alert('鼠标离开')}
        //事件语法 变量名.事件属性(类型) = 匿名函数
    }
    </script>
</head>
<body>
    <botton id="btn1">单击</botton>
    <botton id="btn2">鼠标划过</botton>
    <botton id="btn3">鼠标离开</botton>
</body>
</html>
```

[返回目录](#前端入门)

### 9.等号问题

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	var num1 = 1
        var str = '1'
        alert(num1 === str)
        // '==' 只判断数据数值
        // '==='判断数值+数据类型
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 10.循环

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	for(var i=0;i<3;i++){alter('for')} //类似c语言的写法
        /* var i=0; while(i<3){alter('while') i++}*/
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 11.数组

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	var arr2 = [10, 20, 30, 40, 'abc', 20, 40, 10]
        alert(ar2) //显示整个数组
        arr2.push('jop') // 结尾添加数据
        arr2.pop() //弹出结尾元素
        // arr2.splice(位置下标,删除的数据的个数,添加的数据)
        // arr2.splice(3) 删除这个位置(3)之后的所有
        // arr2.join('分隔符号')
        // arr2.indexOf(数据) 返回下标
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 12.数组去重

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	var arr = [10, 20, 30, 20, 10, 50, 30, 40]
        var newArr = []
        for(var i=0;i<arr.length;i++){
            if(arr.indexOf(arr[i] == i)){
                newArr.push(arr[i])
            }
        }
        alert(newArr)
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 13.数组写入页面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    window.onload = function(){
        var oMyul = document.getElementById('myul')
        var arr = ['复仇者联盟4','大侦探皮卡丘','一只狗的使命','何以为家']
        var str = ''
        for(var i=0;i<arr.length;i++){str += '<li>'+arr[i]+'</li>'}
        oMyul.innerHTML = str
    } //以后以这种循环取数据的方法会非常的常用!!!
    </script>
</head>
<body>
    <ul id="myul">
        
    </ul>
</body>
</html>
```

[返回目录](#前端入门)

### 14.字符串操作方法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    var str1 = '1.9'/*parseInt()转换成数值型  parseFloat()保留小数*/
    var str2 = 'abcdefg' /*substring(开始下标,结束下标) 切割字符串(不包含结束位)*/
    // 变量名.split('分隔符')  元素间以分隔符隔开成数组
    var str3 = ''
    </script>
</head>
<body>
    
</body>
</html>
```

[返回目录](#前端入门)

### 15.调bug

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    	window.onload = function(){
        var oBtn = document.getElementById('btn')
        oBtn.onclick = function(){
            console.log(1)
            oBtn.innerHTML = 'okk'
        }
        document.title = 'you know'
    }
    </script>
</head>
<body>
    <button id="btn">
        按钮
    </button>
</body>
</html>
```

[返回目录](#前端入门)

### 16.定时器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script>
    window.onload = function(){
        var oBtn1 = document.getElementById('btn1')
        var oBtn2 = document.getElementById('btn2')
        var oBtn3 = document.getElementById('btn3')
        var oTimer = null //定时器就是对象型数据类型
        /*单次 setTimeout()  多次setInterval()  这两个函数的两个参数相同*/
        /*参数1-命令-匿名函数形式/函数名形式  参数2-延迟时间(毫秒)*/
        oBtn1.onclick = function(){
            setTimeout(function(){
                alert('单次')
            }, 2000)
        }
        oBtn2.onclick = function(){
            oTimer = setInterval(aa, 2000)
        }
        oBtn3.onclick = function(){
            clearInterval(oTimer)
            oTimer = null
        }
        function aa(){
            alert('多次')
        }
    }
    </script>
</head>
<body>
    <botton id="btn1">单次定时器</botton>
    <botton id="btn2">多次循环定时器</botton>
    <botton id="btn3">停止多次循环定时器</botton>
</body>
</html>
```

[返回目录](#前端入门)

### 17.标签移动原理

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        div{
            width:200px; height:150px; background:green; position:absolute;
            left:0; top:0;
        }
    </style>
    <script>
    window.onload = function(){
        var oBox = document.getElementById('box')
        var num = 0  //num就是left的值 下面的脚本会将num传值给left元素
        var speed = 3
        setInterval(fnMove, 30) //设置多次定时器 每次移动一定的距离
        function fnMove(){
            num += speed
            if(num>600){
                speed = -3
            }
            if(num<0){
                speed = 3
            }
            oBox.style.left = num + 'px'
        }
    }
    </script>
</head>
<body>
    <div id="box">
        
    </div>
</body>
</html>
```

[返回目录](#前端入门)

