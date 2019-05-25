# <center> JavaScript教程 </center>

[TOC]

## JavaScript

JavaScript是世界上最流行的脚本语言，所有网页和基于HTML5的app应用，交互逻辑都是由JavaScript驱动的。简单的说JavaScript是一种运行在浏览器中的解释型编程语言。

## JavaScript简介

### JavaScript历史

要了解JavaScript，我们首先要回顾一下JavaScript的诞生。在上个世纪的1995年，当时的网景公司正凭借其Navigator浏
览器成为Web时代开启时最著名的第一代互联网公司。
由于网景公司希望能在静态HTML页面上添加一些动态效果，于是叫Brendan Eich这哥们在两周之内设计出了JavaScript语言。你没看错，这哥们只用了10天时间。
为什么起名叫JavaScript？原因是当时Java语言非常红火，所以网景公司希望借Java的名气来推广，但事实上JavaScript除了语法上有点像Java，其他部分基本上没啥关系。

### ECMAScript

因为网景开发了JavaScript，一年后微软又模仿JavaScript开发了JScript，为了让JavaScript成为全球标准，几个公司联合ECMA（European Computer Manufacturers Association）组织定制了JavaScript语言的标准，被称为ECMAScript标准。所以简单说来就是，ECMAScript是一种语言标准，而JavaScript是网景公司对ECMAScript标准的一种实现。
那为什么不直接把JavaScript定为标准呢？因为JavaScript是网景的注册商标。
不过大多数时候，我们还是用JavaScript这个词。如果你遇到ECMAScript这个词，简单把它替换为JavaScript就行了。

### JavaScript版本

JavaScript语言是在10天时间内设计出来的，虽然语言的设计者水平非常NB，但谁也架不住“时间紧，任务重”，所以，JavaScript有很多设计缺陷，我们后面会慢慢讲到。
此外，由于JavaScript的标准——ECMAScript在不断发展，最新版ECMAScript 6标准（简称ES6）已经在2015年6月正式发布了，所以，讲到JavaScript的版本，实际上就是说它实现了ECMAScript标准的哪个版本。
由于浏览器在发布时就确定了JavaScript的版本，加上很多用户还在使用IE6这种古老的浏览器，这就导致你在写JavaScript的时候，要照顾一下老用户，不能一上来就用最新的ES6标准写，否则，老用户的浏览器是无法运行新版本的JavaScript代码的。
不过，JavaScript的核心语法并没有多大变化。我们的教程会先讲JavaScript最核心的用法，然后，针对ES6讲解新增特性。

## 快速入门

JavaScript代码可以直接嵌在网页的任何地方，不过通常我们都把JavaScript代码放到`<head>`中：

```html
<html>
<head>
  <script>
    alert('Hello, world');
  </script>
</head>
<body>
  ...
</body>
</html>
```

由`<script>...</script>`包含的代码就是JavaScript代码, 他将直接被浏览器执行.
第二种方法是把JavaScript代码放到一个单独的`.js`文件中, 然后在HTML中通过`<script src="..."></script>`引入这个文件:

```html
<html>
    <head>
        <script src="/static/js/abc.js"></script>
    </head>
    <body>
        ...
    </body>
</html>
```

这样, `/static/js/abc.js`就会被执行.
把JavaScript代码放入一个单独的`.js`文件中更有利于维护代码, 并且多个页面可以各自引用一份`.js`文件.

#### 如何编写JavaScript

可以用任意文本编辑器来编写JavaScript代码,这里简单推荐几个:
Visual Studio Code/  Sublime Text/  Notepad++
注意: 不可以用Word或者记事本编写JavaScript或者HTML!

#### 如何运行JavaScript

要让浏览器运行一个JavaScript, 必须先有一个HTML页面, 在HTML页面中引入JavaScript, 然后, 让浏览器加载该页面, 就可以执行JavaScript代码

#### 调试

首先, 请下载一个Chrome浏览器. 安装之后随便打开一个网页, 然后点击菜单的"查看(View)"-"开发者(Developer)"-"开发者工具(Developer Tools)", 浏览器窗口就会一分为二,如下: ![Snipaste_2019-05-22_11-30-326ee1f.png](https://miao.su/images/2019/05/22/Snipaste_2019-05-22_11-30-326ee1f.png)

先点击"控制台(Console)", 在这个面板里可以直接输入JavaScript代码, 按回车执行.
要查看一个变量的内容, 在Console中输入`console.log(a)`, 回车后显示的值就是变量的内容.

### 基本语法

#### 语法

JavaScript的语法和Java类似, 每个语句以`;`结束, 语句块用`{...}`. 但是, JavaScript并不强制要求在每个语句的结尾加`;`,浏览器中负责执行JavaScript代码的引擎会自动补上`;`.
例如, 下面的代码就是一段完整的赋值语句:

```html
var x = 1;
```

语句块是一组语句的集合:

```html
if(2 > 1){
	x = 1;
	y = 2;
	z = 3;
}
```

注意花括号内的语句应该有缩进. 缩进不是JavaScript语法必须的, 但是缩进有利于我们理解代码.
当然`{...}`还可以嵌套形成层级结构, JavaScript本身对嵌套的层级并没有限制, 但是过多的嵌套无疑会增加代码的阅读难度. 遇到这种情况需要把部分代码抽出来, 作为函数来调用, 这样可以大大增加代码的可读性.

#### 注释

以`//`开头直到行末的字符被视为注释, 注释是给开发人员看的, JavaScript引擎会自动忽略.
另一种注释是用`/*...*/`把多行的字符包起来, 把一大块看作是注释:

```html
//这是一行注释
alert('done!') //这也是一行注释
/*这会是很多行
注释*/
```

注意: JavaScript严格区分大小写!

### 数据类型和变量

#### 数据类型

计算机程序的实质是处理各种数据, 远不止于数值, 还有文本、图形、音频、视频、网页等各种数据, 不同的数据自然也需要定义不同的数据类型, 在JavaScript中定义了以下几种数据类型:

##### Number

JavaScript不区分整数和浮点数, 同一用Number表示, 以下都是合法的Number类型:

```html
123; //整数
0.1234; //浮点数
1.235e3;  //科学计数法
-99; //负数
NaN; //NaN表示not a number, 当无法计算结果时用NaN表示
Infinity; //无限大, 当数值超过了JavaScript的Number能表示的最大值时, 就表示为无限大
```

计算机使用二进制, 所以有时用十六进制表示整数比较方便, 十六进制用0x前缀和0-9, a-f表示
Number可以直接做四则运算, 规则和数学一致

##### 字符串

字符串是以单引号或者双引号括起来的任意文本

##### 布尔值

布尔值和布尔代数完全一致,只有`ture`和`false`两个数值.
`&&`是且, `||`是或, `!`是非

##### 比较运算符

JavaScript允许对任意数据类型做比较:

```html
false == 0; //true
false === 0; //false
```

要特别注意相等运算符`==`. 和`===`:
第一种`==`比较, 他会自动转换数据类型再比较, 很多时候会得到非常诡异的结果;
第二种`===`比较,他不会自动转换数据类型, 如果数据类型不一致, 返回`false`, 如果一致再比较.
故我们只使用`===`方式比较!
另外就是`NaN`这个特殊的Number与其他所有值都相等, 包括自己:

```html
NaN === NaN; //false
```

唯一能够判断`NaN`的方法是通过`isNaN()`函数:

```html
isNaN(NaN); //true
```

最后要注意浮点数的比较:

```html
1/3 === (1 - 2/3); //false
```

这并不是JavaScript的设计缺陷, 浮点数在运算过程中会产生误差, 因为计算机无法精确表示无限循环小数. 要比较两个浮点数是否相等, 只能计算他们之差的绝对值, 看是否小于某个阈值:

```html
Math.abs(1/3 - (1 - 2/3)) < 0.00000001; //true
```

##### null和undefined

`null`表示一个"空"的值, 它和`0`以及空字符串`' '`不同, `0`是一个数值, `' '`表示长度为0的字符串, 而`null`表示空.
`undefined`表示值未定义. 事实证明, 这两者的区别并不大, 大多数情况下我们都用`null`. `undefined`仅仅在判断函数参数是否传递的情况下有用.

##### 数组

数组是一组按顺序排列的集合 集合的每个值称为元素. JavaScript的数组可以包括任意数据类型, 例如:

```html
[1, 2, 3.14, 'Hello', null, true]
```

数组用`[]`表示, 元素间用`,`分隔, 另一种创建数组的方法是通过`Array()`函数实现:

```html
new Array(1, 2, 3); //创建数组
```

然而, 出于代码的可读性考虑, 强烈建议直接使用`[]`!
数组的元素可以通过索引来访问. 索引起始值为`0`.

##### 对象

JavaScript的对象是由一组由键-值组成的无序集合, 例如:

```html
var person = {
	name:'Bob',
	age:20,
	tags:['js','web','mobile'],
	city:'Beijing',
	hasCar:true,
	zipcode:null
};
```

JavaScript对象的键都是字符串类型, 值可以是任意数据. 上述的`person`对象一共定义了6个键值对, 其中每个键又称为对象的属性.
要获取一个对象的属性, 我们用`对象变量.属性名`的方法:

```html
person.name; //'Bob'
person.zipcodel; //null
```

##### 变量

变量不仅可以是数字, 还可以是任意数据类型.
变量在JavaScript中就是用一个变量名表示, 变量名是大小写英文、数字、`$`和`_`的组合, 且不能用数字开头. 变量名也不能是JavaScript的关键字:

```html
var a; //申明了变量a, 此时a的值为undefined
var $b = 1; //申明了变量$b, 同时给$b赋值, 此时$b的值为1
var s_007 = '007'; //s_007是一个字符串
var Answer = true; //Answer是一个布尔值true
var t = null; //t的值是null
```

在JavaScript中, 使用等号`=`对变量进行赋值. 可以把任意数据类型赋值给变量, 同一个变量可以反复赋值, 而且可以是不同类型的赋值. 但是注意只能使用`var`声明一次. 

这种变量本身类型不固定的语言称之为动态语言, 与之对应的是静态语言. 静态语言在定义变量时必须指定变量类型, 如果赋值的时候类型不匹配就会报错(如Java和C).
注意: 请不要把赋值的`=`和数学的`=`等价!
要显示变量的内容, 可以用`console.log(x)`, 打开Chrome的控制台就可以看见结果. 使用`console.log()`而不是`alert()`的好处是可以避免烦人的弹窗.

#### strict模式

为了避免不使用`var`申明全局变量的问题, ECMA在后续的规范中推出了strict模式, 启用strict模式的方法是在JavaScript代码的第一行加上:

```html
'use strict';
```

这是一个字符串, 不支持strict模式的浏览器会把它当做一个字符串处理,支持的浏览器会启动strict模式.

#### 字符串

如果字符串内包含`'`或者`"`,可以使用转义字符`\`来标识, 比如:

```html
'I\'m \"OK\"!';
```

转义字符`\`可以转义很多字符, 比如`\n`表示换行, `\t`表示制表符, 字符`\`本身也要转义,所以`\\`表示的字符就是`\`.

##### 多行字符串

由于多行字符串用`\n`写起来比较费事儿, 所以最新的ES6标准新增了一种多行字符串的表示方法, 用反引号`*...*`表示:

```html
`这是一个
多行
字符串`;
```

注意: 单引号在键盘在ESC的下方, 数字键1的左边

##### 模板字符串

要把多个字符串连接起来, 可以用`+`连接:

```html
var name = '小明';
var age = 20;
var message = '你好,' + name + ',你今年' + age + '岁了!';
alert(message);
```

如果有很多变量需要连接, 用`+`号就比较麻烦. ES6新增了一种模板字符串, 表示方法和上面的多行字符串一样, 但是它会自动替换字符串中的变量:

```html
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`; //用反引号
alert(message);
```

##### 操作字符串

字符串常见的操作如下:

```html
var s = 'Hello, world!';
s.length;  //13
```

要获取字符串某个指定位置的字符, 使用类似Array的下标操作, 索引从0开始:

```html
var s = 'Hello, world!';
s[0]; //H
s[6]; // ''
s[13]; //undefined 超出范围不会报错,但一律返回undefined
```

注意: 字符串是不可变的, 如果对字符串的某个索引赋值, 不会有任何的错误, 但是也没有任何的效果.

###### toUpperCase

`toUpperCase()`把一个字符串全部变成大写:

```html
var s = 'Hello';
s.toUpperCase();  //返回'HELLO'
```

###### toLowerCase

`toLowerCase()`把一个字符串全部变成小写:

```html
var s = 'Hello';
var lower = s.toLowerCase();
lower; //'hello'
```

###### indexOf

`indexOf()`会搜索指定字符串出现的位置:

```html
var s = 'Hello';
s.indexOf('l');  //返回2
s.indexOf('p');  //没有找到返回-1
```

###### substring

`substring()`返回指定索引区间的子串:

```html
var s = 'Hello, world';
s.substring(0,5); //从索引0到5(不包括5), 返回'Hello'
s.substring(7);  //从索引7开始到结尾, 返回'world'
```

#### 数组

JavaScript的`Array`可以包含任意数据类型, 并通过索引来访问每个元素.
要取得`Array`的长度, 直接访问`length`属性:

```
var arr = [1, 2, 3.14, 'Hello', null, true];
arr.length;  //6
```

注意: 直接给`Array`的`length`赋值会导致`Array`大小的变化:

```html
var arr = [1, 2, 3, undefined, undefined, undefined];
arr.length; //3
arr.length = 6;
arr;  //arr变成[1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr;  //arr变成[1, 2]
```

`Array`可以通过索引把对应的元素修改为新的值, 因此, 对`Array`的索引进行赋值会直接修改这个`Array`, 与此同时, 如果通过索引赋值时, 索引超过了范围, 通样会引起`Array`大小的变化:

```html
var arr = [1, 2, 3];
arr[5] = 'x';
arr;  //arr变为[1, 2, 3, undefined, undefined, 'x']
```

大多数其他编程语言不允许直接修改数组的大小, 越界访问索引会报错. 然而, JavaScript的`Array`却不会有任何的错误. 在编写代码时, 不建议直接修改`Array`的大小, 访问索引要确保索引不会越界.

##### indexOf

与String类相似,`Array`也可以通过`indexOf()`来搜索一个指定元素的位置:

```html
var arr = [10, 20, '30', 'xyz'];
arr.indexOf(10);  //元素10的索引为0
arr.index(30); //元素30没有找到, 返回-1
arr.index('30');  //元素'30'的索引为2
```

注意: 30和'30'是不同的元素

##### slice

`slice()`就是对于String的`substring()`版本, 它截取`Array`的部分元素, 然后返回一个新的`Array`:

```html
var arr = ['A', 'B', 'C', 'D', 'E'];
arr.slice(0,3); // ['A', 'B', 'C']
arr.slice(3);  //['D', "E"]
```

注意:  不包括结束索引
如果不给`slice()`传递任何参数, 他就会从头到尾截取所有元素, 利用这一点我们可以很轻松的赋值一个`Array`:

```html
var arr = ['A', 'B', 'C', 'D', 'E'];
var aCopy = arr.slice();
aCopy === arr; //false
```

##### push和pop

`push()`和`Array`的末尾添加若干元素, `pop()`则把`Array`的最后一个元素删除掉:

```html
var arr = [1, 2];
arr.push('A','B'); //返回Array新的长度:4
arr.pop();  //pop()返回'B' 空数组pop不会报错而是返回undefined
```

##### unshift和shift

如果要往`Array`的头部添加元素, 使用`unshift()`方法, `shift()`方法则把`Array`的第一个元素删掉:

```html
var arr = [1, 2];
arr.unshift('A', 'B');  //返回Array新的长度:4
arr.shift();  //'A'  空数组一样返回undefined
```

##### sort

`sort()`可以对当前`Array`进行排序, 他会直接修改当前`Array`的元素位置, 直接调用是, 按照默认顺序排序:

```html
var arr = ['b', 'c', 'a'];
arr.sort();
arr;  //['a', 'b', 'c']
```

##### reverse

`reverse()`把整个`Array`的元素翻转:

```html
var arr = [1, 2, 5];
arr.reverse();
arr;  //[5, 2, 1]
```

##### splice

`splice()`方法是修改`Array`的"万能方法", 它可以从指定的索引驾驶删除若干元素, 然后再从该位置添加若干元素:

```html
var arr = [1, 2, 3, 4, 5];
arr.aplice(2, 3, 'ok', 'yes')
arr;  //[1, 2, 'ok', 'yes']
```

##### concat

`concat()`方法把当前的`Array`和另一个`Array`连接起来, 返回一个新的`Array`:

```html
var arr = [1, 2, 3];
var arr2 = [1, 3, 2];
var arr_add = arr.concat(arr2);
arr_add;  //[1, 2, 3, 1, 3, 2]
```

注意: `concat()`方法并没有修改当前的`Array`, 而是返回了一个新的`Array`.
实际上, `concat()`方法可以接受任意个元素和`Array`,并且自动把`Array`拆开, 然后全部添加到新的`Array`里:

```html
var arr = [1, 2, 3];
arr.concat(1, 2, [1, 2]); //[1, 2, 3, 1, 2, 1, 2]
```

##### join

`join()`方法是一个非常实用的方法, 它把当前`Array`的每个元素都用指定的字符串连接起来, 然后返回连接返回后的字符串:

```html
var arr = [1, 2, 3, 4, 5];
arr.join('-');  // '1-2-3-4-5'
```

如果`Array`的元素不是字符串, 将自动转换为字符串后再连接

#### 多维数组

如果数组的某个元素又是一个`Array`, 则可以形成多维数组, 例如:

```html
var arr = [[1, 2],[3, 4, 5],'-'];
```

#### 对象

JavaScript的对象是一种无序的集合数据类型, 它由若干键值对组成.
JavaScript用一个`{...}`表示一个对象, 键值对以`xxx:xxx`形式申明, 用`,`隔开. 
注意: 最后一个键值对不需要在末尾加`,`
访问对象属性是通过`.`操作符来完成的, 但这要求属性名必须是一个有效的变量名. 如果属性名包含特殊字符, 就必须用`''`括起来:

```html
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
xiaoming.name; // '小明'
xiaoming.birth; // 1990
var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};
xiaohong['middle-school']; // 'No.1 Middle School'
xiaohong['name']; // '小红'
xiaohong.name; // '小红'
```

`xiaohong`的属性名`middle-school`不是一个有效的变量, 就需要用`''`括起来. 访问这个属性也无法使用`.`操作符, 必须用`['xxx']`来访问.
实际上, JavaScript对象的所有属性都是字符串, 不过属性对应的值可以使任意数据类型.  如果访问了一个不存在的属性会返回`undefined`.
由于JavaScript的对象是动态类型, 你可以自由地给一个对象添加或删除属性:

```html
var xiaoming = {
name: '小明'
};
xiaoming.age;  //undefined
xiaoming.age = 18;  //新增一个age属性
delete xiaoming.age;  //删除age属性
xiaoming.age;  //underfined
delete xiaoming.school;  //删除不存在的属性不会报错
```

如果我们要检测`xiaoming`是否拥有某一属性, 可以用`in`操作符:

```html
var xiaoming = {
	name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
'name' in xiaomming;  //true
'grade' in xiaoming;  //false
```

不过要小心, 如果`in`判断一个属性存在, 这个属性不一定是`xiaoming`的, 也有可能是继承得到的. 如果要判断一个属性是否是其自由地, 可以用`hasOwnProperty()`方法:

```html
var xiaoming = {
name: '小明'
};
xiaoming.hasOwnPorperty('name');  //true
xiaoming.hasOwnPorperty('toString');  //false
```

#### 条件判断

JavaScript使用`if(){...}else{...}`来进行条件判断. 其中`else`语句是可选的. 如果只包含一条语句, name就可以省略`{...}`.

```html
var age = 20;
if (age >= 18)
	alert('adult');
else
	alert('teenager');
```

省略`{...}`的危险在于, 如果后来想增添一些语句, 却忘了写`{}`, 就改变了`if...else...`的语义.
所以我们建议永远都要加上`{...}`.

##### 多条件判断

如果还有更细致地判断条件, 可使用多个`if...else..`语句组合:

```html
var age = 3;
if(age >= 18){
	alert('adult');
}else if(age >= 6){
	alert('teenager');
}else{
	alert('kid');
}
```

上述多个`if...else...`的组合实际上相当于两层`if...else...`, 但是我们通常把`else if`连写在一起以增加代码的可读性. 这里的`else`略掉了`{}`是没有问题的, 因为它只包含了一个`if`语句.
注意: `if...else...`语句的执行特点是二选一, 在多个`if...else...`语句中, 如果某个条件成立, 则后续就不在继续判断了.

#### 循环

JavaScript的循环有两种, 一种是`for`循环, 通过初识条件, 结束条件和递增条件来循环执行语句块:

```html
var x = 0;
var i;
for (i=1; i<=1000; i++){
	x = x + i;
}
```

`for`循环最常用的地方是利用索引遍历数组:

```html
var arr = [1, 2, 3];
var i, x;
for(i=0; i<arr.length; i++){
	x = arr[i];
	console.log(x);
}
```

`for`循环的三个条件都是可以省略的, 如果没有退出循环的判断条件, 就必须使用`break`语句退出循环, 否则就是死循环.

##### for...in

`for`循环的一个变体是`for...in`循环,  它可以把一个对象所有的属性一次循环列出来:

```html
var o = {
	name:'Jack',
	age:20,
	city:'Beijing'
};
for(var key in o){
	console.log(key);  //'name', 'age', 'city'
}
```

要过滤掉对象继承的属性, 用`hasOwnProperty()`来实现.
由于`Array`也是对象, 而它的每个元素的索引被视为对象的属性, 因此, `for...in`循环可以直接循环出`Array`的索引:

```html
var a = [2, 3, 5];
for(var i in a){
console.log(i);  //'0','1','2'
console.log(a[i]);  //'2', '3','5'
}
```

注意: `for...in`对`Array`的循环得到的是`String`而不是`Number`.

##### while

`for`循环在已知循环的初始和结束条件时非常有用, 而上述忽略了条件的`for`循环容易让人看不清循环的逻辑, 此时用`while`循环更佳.
`while`循环只有一个判断条件, 条件满足, 就不断循环, 条件不满足则退出循环.

```html
var x = 0;
var n = 99;
while (n > 0) {
    x = x + n;
    n = n - 2;
}
x; // 2500
```

##### do...while

最后一种循环是`do{...}while()`循环, 它和`while`循环的唯一区别在于, 不是每一次循环开始的时候判断条件, 而是在每次循环完成的时候判断条件

```html
var n = 0;
do {
    n = n + 1;
} while (n < 100);
n; // 100
```

小结: 循环是让计算机做重复任务的有效方法, 有些时候, 如果代码写的有问题, 会让程序陷入"死循环", 也就是永远循环下去. JavaScript的死循环会让浏览器无法正常显示网页或者执行当前页面的逻辑, 有的浏览器会直接秒退, 因此要特别注意死循环的问题.
在编写循环代码时, 务必要小心编写初识条件和判断条件, 尤其是边界值.

#### Map和Set

JavaScript的默认对象表示方式`{}`可以视为表的语言中的`Map`或`Dictionary`的数据结构, 即一组键值对.
但是JavaScript的对象有个小问题, 就是键必须是字符串. 但实际上Number或者其他数据类型作为键也是非常合理的.
为了解决这个问题,就引入了`Map`这个新的数据类型.

##### Map

`Map`是一组键值对的结构, 具有极快的查找速度. 初始化`Map`需要一个二维数组, 或者直接初始化一个空`Map`.

```html
var m = new Map();
m.set('A',1);  //存入一个新键值对
m.set('B',2);
m.get('A');  //1
m.delete('A');  //删除key 'A'
m.get('A');  //返回undefined
```

由于一个key只能对应一个value, 所以多次给一个key放入value, 后面的值会把前面的冲掉.

##### Set

`Set`和`Map`类似, 也是一组key的集合, 但不存储value. 由于key不能重复, 所以在`Set`中, 没有重复的key.
要创建一个`Set`, 需要提供一个`Array`作为输入, 或者直接创建一个空`Set`:

```html
var s1 = new Set();  //空Set
var s2 = new Set([1, 2, 3]);  //含1,2,3
```

重复的元素在`Set`中会自动被过滤:

```html
var s = new Set([1,2,3,3,'3']);
s; //Set{1,2,3,'3'}
```

通过`add(key)`方法可以添加元素到`Set`中, 可以重复添加, 但是不会有效果:

```html
s.add(4);
s; // Set {1, 2, 3, 4}
s.add(4);
s; // 仍然是 Set {1, 2, 3, 4}
```

通过`delete(key)`方法可以删除元素:

```html
var s = new Set([1, 2, 3]);
s; // Set {1, 2, 3}
s.delete(3);
s; // Set {1, 2}
```

#### iterable

遍历`Array`可以采用下标循环, 遍历`Map`和`Set`就无法使用下标. 为了统一集合类型, ES6标准引入了新的`iterable`类型. `Array`, `Map`, `Set`, 都属于`iterable`类型.
具有`iterable`类型的集合可以通过新的`for...of`循环来遍历.
用`for..of`循环遍历集合:

```html
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    console.log(x);
}
for (var x of s) { // 遍历Set
    console.log(x);
}
for (var x of m) { // 遍历Map
    console.log(x[0] + '=' + x[1]);
```

你可能会有疑问`for..in`和`for...of`的区别.

`for ... in`循环由于历史遗留问题，它遍历的实际上是对象的属性名称。一个`Array`数组实际上也是一个对象，它的每个元素的索引被视为一个属性。

当我们手动给`Array`对象添加了额外的属性后，`for ... in`循环将带来意想不到的意外效果：

```html
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    console.log(x); // '0', '1', '2', 'name'
}
```

`for ... in`循环将把`name`包括在内，但`Array`的`length`属性却不包括在内。
`for ... of`循环则完全修复了这些问题，它只循环集合本身的元素：

```
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
```

这就是为什么要引入新的`for ... of`循环。
然而，更好的方式是直接使用`iterable`内置的`forEach`方法，它接收一个函数，每次迭代就自动回调该函数。以`Array`为例：

```html
'use strict'; var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});
```

`Set`与`Array`类似，但`Set`没有索引，因此回调函数的前两个参数都是元素本身：

```
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    console.log(element);
});
```

`Map`的回调函数参数依次为`value`、`key`和`map`本身：

```
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    console.log(value);
});
```

如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们。例如，只需要获得`Array`的`element`：

```
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    console.log(element);
});
```

