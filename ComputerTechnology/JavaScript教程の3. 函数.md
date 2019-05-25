# <center>JavaScript教程の函数</center>

[TOC]

## 函数

有了函数, 我们就可以将重复的部分写成更有意义的函数调用. 基本上所有的高等语言都支持函数, JavaScript也不例外. JavaScript的函数不仅可以像变量一样使用, 还具有非常强大的抽象能力.

**抽象**

抽象在数学中是非常常见的, 比如一些特殊的符号记法. 而这些抽象记法往往还是可扩展的. 可见, 借助抽象, 我们才能不关心底层的具体计算过程, 而是直接在更高的层次上思考问题. 写计算机程序也是一样, 函数就是最基本的一种抽象.

### 函数的定义和调用

#### 定义函数

在JavaScript中, 定义函数的方式如下:

```javascript
function abs(x){
	if(x > 0){
	return x;
	}else{
	return -x;
	}
}
```

上述`abs()`的函数定义中:

* `function`指出这是一个函数定义;
* `abs`是函数的名称;
* `(x)`括号内列出函数的参数, 多个参数以`,`分隔;
* `{...}`之间的代码是函数体, 可以包含若干语句, 甚至可以没有的语句. 

注意: 函数体内部的语句在执行时, 一旦执行到`return`时, 函数就执行完毕, 并将结果返回. 因此, 函数内部通过条件判断和循环可以实现非常复杂的逻辑.
如果没有`return`语句, 函数执行完毕后也会返回一个结果, 只是结果为`undefined.`
由于JavaScript的函数也是一个对象, 上述定义的`abs()`函数实际上是一个函数对象, 而函数名`abs`可以视为指向该函数的变量. 因此, 第二种定义函数的方法如下:

```javascript
var abs = function(x){
	if(x >= 0){
	 	return x;
	}else{
		return -x;
	}
};
```

在这种方式下, `function(x){...}`是一个匿名函数, 它没有函数名. 但是, 这个匿名函数赋值给了变量`abs`, 所以, 通过变量`abs`就可以调用该函数.
上述两种定义完全等价, 注意第二种方式按照完整语法需要在函数体末尾加一个`;`,表示赋值语句结束

#### 调用函数

调用函数时, 按顺序传入参数即可:

```javascript
abs(10); //返回10
```

由于JavaScript允许传入任意个参数而不影响调用, 因此传入的参数比定义的参数多也没问题, 虽然函数内部并不需要这些参数, 而同时传入的参数少也没有问题:

```javascript
abs(10, 'bilibili'); //返回10
abs();  //返回NaN
```

此时`abs(x)`函数的参数`x`将收到`undefined`, 计算结果为`NaN`.
要避免收到`undefined`, 可以对参数进行检查:

```javascript
function abs(x){
	if (typeof x!=='number'){
		throw 'Not a number'
	}
	if (x>=0){
		return x;
	} else{
		return -x;
	}
}
```

#### arguments

JavaScript还有一个免费赠送的关键字`argument`, 它只在函数内部起作用, 并且永远指向当前函数的调用者传入的所有参数. `argument`类似`Array`但它不是一个`Array`:

```javascript
function foo(x){
	console.log('x = '+ x);  //10
	for (var i=0; i<arguments.length; i++){
		console.log('arg' + i + '=' + arguments[i]);  //10, 20, 30
	}
}
foo(10,20,30)
```

利用`arguments`, 你可以获得调用者传入的所有参数. 也及时说, 即使函数不定义任意参数, 还是可以拿到参数的值:

```javascript
function abs(){
	if(arguments.length === 0){
		return 0;
	}
	var x = arrguments[0];
	return x >= 0 ? x : -x;
}
abs(); //0
abs(10); //10
abs(-9); //9
```

实际上`arguments`最常用于判断传入参数的个数, 你可能会看见这样的写法:

```javascript
//foo(a[, b], c)  接受2~3个参数, b是可选参数, 如果只传入2个参数, b默认为null
function foo(a, b, c){
	if(arguments.length === 2){
		//实际拿到的参数是a和b, c为undefined
		c = b;
		b = null;
	}
	//... ...
}
```

要把中间的参数`b`变为"可选"参数, 就只能通过`arguments`判断, 然后重新调整参数并赋值.

#### rest参数

由于JavaScript函数允许接受任意个参数, 于是我们就不得不用`arguments`来获取所有的参数:

```javascript
function foo(a,b){
	var i, rest = [];
	if(arguments.length > 2){
		for(i = 2; i < arguments.length; i++){
			rest.push(arguments[i]);
		}
	}
	console.log('a = ' + a);
	console.log('b = ' + b);
	console.log(rest);
}
```

为了获取除了已定义参数`a, b`之外的参数, 我们不得不用`arguments`, 并且循环要从索引`2`开始以排除前两个参数, 这种写法很别扭, 只是为了获取额外的`rest`参数, 我们都是用另外一个方法:

````javascript
function foo(a, b, ...rest){
	console.log('a = ' + a);
	console.log('b = ' + b);
	console.log(rest);
}
foo(1, 2, 3, 4, 5);  //结果a=1, b=2, rest=[3, 4, 5]
foo(1);  //结果a=1, b=undefined, rest=[]
````

rest参数只能写在最后, 前面用`...`标识, 从运行结果可知, 传入参数先绑定`a, b`, 多于的参数以数组的形式交给变量`rest`, 所以, 不需要`arguments`我们就获得了全部参数.
如果传入的参数连正常定义的参数都没有填满, 也不要紧, rest参数会接受一个空数组(注意, 并不是undefined)

#### 小心你的`return`语句

前面我们提到了JavaScript引擎有一个在行末自动添加分号的机制, 这可能让你栽在return语句的一个大坑里:

```javascript
function foo(){
	return {name: 'foo'};
}
foo(); //return {name: 'foo'}
```

如果把return语句拆成两行:

```javascript
function foo(){
	return
		{name: 'foo'};
}
foo();  //undefined
```

要小心了, 由于JavaScript引擎在行末自动添加分号的机制, 上面的代码实际上变成了:

```javascript
funciton foo(){
	return;  //自动添加分号, 相当于返回了undefined;
		{name: 'foo'};  //这个语句已经不执行了, 因为return终止了执行
}
```

如果要用分行写, 那就需要将`return`的结果加上`{...}`以表示语句尚未结束.

### 变量作用域与解构赋值

在JavaScript中, 用`var`声明的变量实际上是有作用域的.
如果一个变量在函数体内声明, 则该函数的作用域为整个函数体, 在函数体外不可引用该变量:

```javascript
function foo(){
	var x = 1;
	x = x + 1;
}
x = x + 2; //ReferenceError! 无法在函数体外引用变量x
```

如果两个不同的函数各自声明了同一个变量, 那么该变量只在各自的函数体内起作用. 换句话说, 不同函数内部的同名变量互相独立, 互不影响:

```javascript
function(){
	var x = 1;
	x = x + 1;
}
function bar(){
	var x = 'a';
	x = x + 'b';
}
```

由于JavaScript的函数可以嵌套, 此时, 内部函数可以访问外部函数定义的变量, 反过来则不行:

```javascript
function foo(){
	var x = 1;
	function bar(){
		var y = x + 1; //bar可以访问foo变量x
	}
	var z = y + 1; //ReferenceError! foo不可以访问bar的变量y!
}
```

如果内部函数和外部函数的变量重名, 那内部函数的变量将"屏蔽"外部函数的变量. 这说明了JavaScript的函数在查找变量时从自身函数定义开始, 从"内"向"外"查找.

#### 变量提升

JavaScript的函数定义有个特点, 他会先扫描整个函数体的语言, 把所有声明的变量"提升"到函数顶部:

```javascript
function foo(){
	var x = 'Hello,'+ y;
	console.log(x);
	var y = 'Bob';
}
foo();
```

虽然是`strict`模式, 但是`var x = 'Hello,'+ y;`并不会报错, 原因是变量`y`在稍后声明了. 但是`console.log`显示`Hello,undefined`, 说明变量`y`的值为`undefined`. 这正是因为JavaScript引擎自动提升了y的变量声明, 但是不会提升变量的赋值. 对于上述`foo()`函数, JavaScript引擎看到的代码相当于是:

```javascript
function foo(){
	var y;
	var x = 'Hello,'+ y;
	console.log(x);
	y = 'Bob';
}
foo();
```

由于JavaScript的这一怪异特性, 我们在函数内部定义变量时, 请严格遵守"在函数内部首先声明所有变量"这一规则. 最常见的做法是用一个`var`声明函数内部用到的所有变量:

```javascript
function foo(){
	var
		x = 1,
		y = x + 1,
		z, i;
	for (i = 0; i < 100; i++){
		...
	}
}
```

#### 全局作用域

不在任何函数内定义的变量就具有全局作用域. 实际上, JavaScript默认有一个全局对象`window`, 全局作用域的变量实际上被绑定到`window`的一个属性:

```javascript
var course = 'Learn JavaScript';
alert(course);  //'Learn JavaScript'
alert(window.course); //'Learn JavaScript'
```

因此, 直接访问全局变量`course`和访问`window.course`是完全一样的.
由于函数定义有两种方式, 以变量方式`var foo = function(){}`定义的函数实际上也是一个全局变量, 因此, 顶层函数的定义也被视为一个全局变量, 并绑定到`window`对象:

```javascript
function foo(){
	alert('foo');
}
foo();  //直接调用
window.foo();  //通过window.foo()调用
```

进一步说, 我们每次直接调用的`alert()`函数其实也是`window`的一个变量. 如果把一个函数赋值给`window.alert`会导致`alert`无法正常使用. 这说明JavaScript实际上只有一个全局作用域. 任何变量(函数也视为变量), 如果没有在当前函数作用域中找到, 就会继续往上查找, 最后如果在全局作用域中也没有找到, 就会报`ReferenceError`错误.

名字空间

全局变量会绑定到`window`上, 不同的JavaScript文件如果使用了相同的全局变量, 或者定义了相同名字的顶层函数, 都会造成命名冲突, 而这种错误还很难发现.
减少冲突的一个方法是把自己的所有变量和函数全部绑定到一个全局变量中. 例如:

```javascript
//唯一的全局变量MYAPP
var MYAPP = {};
//其他变量
MYAPP.name = 'myapp';
MYAPP.version = 1.0;
//其他函数
MYAPP.foo = function(){
	return 'foo';
};
```

把自己的代码全部放入唯一的名字空间`MYAPP`中, 会大大减少全局变量冲突的可能. 许多注明的JavaScript库都是这么干的, 比如 jQuery, YUI, underscore等.

#### 局部作用域

由于JavaScript的变量作用域实际上是函数内部, 我们在`for`循环等语句块中无法定义具有局部作用域的变量的:

```javascript
function foo(){
	for(var i = 0; i<100; i++){
		... ...
	}
	i += 100; //仍然可以引用变量 i
}
```

为了解决块级作用域, ES6引入了新的关键字`let`, 用`let`替代`var`可以声明一个块级作用域的变量:

```javascript
function foo(){
	var sum = 0;
	for (let i=0; i<100; i++){
		sum += i;
	}
	i += 1;  //SyntaxError
}
```

#### 常量

由于`var`和`let`声明的是变量, 如果要声明一个常量, 在ES6之前是不行的, 我们通常用全部大写的变量来标识"这是一个变量, 不要修改它的值":

```javascript
var PI = 3.14;
```

ES6标准引入了新的关键字`const`来定义常量, `const`与`let`都具有块级作用域:

```javascript
const PI = 3.14;
PI = 3;  //某些浏览器不能不错, 但是无效果
PI; //3.14
```

#### 解构赋值

从ES6开始, JavaScript引入了解构赋值, 可以同时对一组变量进行赋值.  什么是解构赋值? 我们先看看传统的做法, 如何把一个数组的元素分别赋值给几个变量:

```javascript
var arr = ['hello', 'javascript', 'ES6'];
var x = arr[0];
var y = arr[1];
var z = arr[2];
```

现在, 在ES6中, 可以使用解构赋值, 直接对多个变量同时赋值:

```javascript
// 需要浏览器支持解构赋值
var[x, y, z] = ['hello', 'javascript', 'ES6'];  //x,y,z分别为赋值为数组对应的元素
```

注意: 对数组元素进行解构赋值时, 多个变量要用`[...]`括起来.如果数组本身还有嵌套, 也可以通过下面的形式进行解构赋值, 注意嵌套层次和位置要保持一致:

```javascript
let [x,[y,z]] = ['hello',['javascript','ES6']];
```

解构赋值还可以忽略某些元素:

```javascript
let [,,z] = ['hello', 'javascript', 'ES6'];  //忽略前两个元素, 只对z赋值第三个元素
```

如果需要从第一个对象中取出若干属性, 也可以使用解构赋值, 便于快速获取对象的指定属性:

```javascript
var person = {
	name: '小明',
	age: 20,
	gender: 'male',
	passport: 'G-12345'
	school: 'No.4 middleschool'
};
var {name, age, passport} = person;
```

对一个对象进行解构赋值时, 同样可以直接对嵌套的对象属性进行赋值, 只要保证对应层次是一致的:

```javascript
var person = {
	name: '小明',
	age: 20,
	gender: 'male',
	passport: 'G-12345'
	school: 'No.4 middleschool'
	address: {
		city: 'Beijing',
		street: 'No.1 Road',
		zipcode: '1001'
	}
};
var {name, address:{city,zip}} = person;  //zip是undefined, 因为属性名不对 要注意address不是变量
```

使用解构赋值对对象属性进行赋值时, 如果对应的属性不存在, 变量将被赋值为`undefined`, 这和引用一个不存在的属性获得`undefined`是一致的. 如果要使用的变量名和属性名不一致, 可以使用下面的语法获取:

```htmljavascript
var person = {
	name: '小明',
	age: 20,
	gender: 'male',
	passport: 'G-12345'
	school: 'No.4 middleschool'
};
// 把passport属性赋值给变量id
let {name, passport:id} = person;
// 注意: passport不是变量, 而是为了让变量id获得passport属性
```

解构赋值还可以使用默认值, 这样就避免了不存在的属性返回`undefined`的问题:

```javascript
var person = {
	name: '小明',
	age: 20,
	gender: 'male',
	passport: 'G-12345'
	school: 'No.4 middleschool'
};
// 如果person对象没有single属性, 默认赋值为true
var {name, single=true} =person;
```

有些时候, 如果变量已经被声明了, 再赋值的时候, 正确的写法也会报语法错误:

```javascript
//声明变量
var x,y;
//解构赋值
{x, y} = {name: '小明', x: 100, y: 200};  //语法错误
```

这是因为JavaScript引擎把`{`开头的语句当作了块处理, 于是`=`不再合法.  解决方法是用小括号括起来:

```javascript
({x, y} = {name: '小明', x: 100, y: 200});
```

#### 使用场景

解构赋值在很多时候可以大大简化代码. 例如, 交换两个变量的值就不再需要临时变量:

```javascript
var x = 1, y = 2;
[x, y] = [y, x]
```

快速获取当前页面的域名和路径:

```javascript
var {hostname: domain, pathname: path} = location; 
```

如果一个函数接收一个对象作为参数, 那么, 可以使用解构直接把对象的属性绑定到变量中. 例如, 下面的函数可以快速创建一个`Date`对象:

```javascript
function buildDate({year, month, day, hour=0, minute=0, second=0}){
	return new Date(year + '-' + month + '-' + day + '' + hour + ':' + minute + ':' + second);
}
```

它的方便之处在于传入的对象只需要`year`、`month`和`day`这三个属性:

```javascript
buildDate({year:2017, month:1, day:1});
//Sun Jan 01 2017 00:00:00 GMT+0800(CST)
```

也可以传入`hour`、`minute`和`second`属性:

```javascript
bulidDate({year:2017, month:1, day:1, hour:20, minute:15});
//Sun Jan 01 2017 20:15:00 GMT+0800(CST)
```

使用解构赋值可以减少代码量, 但是, 需要在支持ES6解构赋值特性的现代浏览器才能正常运行.

### 方法

在一个对象中绑定函数, 称为这个对象的方法.
在JavaScript中, 对象的定义时这样的:

```javascript
var xiaoming = {
	name: '小明',
	birth: 1990
};
```

但是如果我们给`xiaoming`绑定一个函数, 就可以做更多的事情:

```javascript
var xiaoming = {
	name: '小明',
	birth: 1990
	age: function(){
		var y = new Date().getFullYear();
		return y - this.birth;
	}
};
xiaoming.age;  //function xiaoming.age()
xiaoming.age();  //今年调用是25 明年调用是26
```

绑定到对象上的函数称为方法, 和普通函数也没什么区别, 但是他在内部使用了一个`this`关键字.
在一个方法内部, `this`是一个特殊的变量, 它始终指向当前对象, 也就是`xiaoming`这个变量. 所以, `this.birth`可以拿到`xiaoming`的`birth`属性.

JavaScript的函数内部如果调用了`this`, 那么这个`this`到底指向谁?
答案是视情况而定.
如果以对象的方式形式调用, 比如`xiaoming.age()`, 该函数的`this`指向被调用的对象, 也就是`xiaoming`, 这就符合我们得预期.
如果单独调用函数,比如`getage()`, 此时, 该函数的`this`指向全局对象, 也就是`window`.
要注意:

```javascript
var fun = xiaoming.age;  //先拿到xiaoming的age函数
fun();  //NaN
```

也是不行的!!! 要保证`this`指向正确, 必须用`obj.xxx()`的形式调用!
由于这是一个巨大的设计错误, 要想纠正可没那么简单. ECMA决定, 在strict模式下让函数的`this`指向`undefined`, 因此, 在strict模式下会得到一个错误:

```javascript
var xiaoming = {
	name: '小明',
	birth: 1900,
	age: function(){
		var y = new Date().getFullYear();
		return y - this.birth;
	}
};
var fn = xiaoming.age;
fn();  //报错undefined
```

这个决定只是让错误即使暴露出来, 并没有解决`this`应该指向的正确位置.
有些时候, 喜欢重构的你把方法重构了一下:

```javascript
var xiaoming = {
	name: '小明',
	birth: 1990,
	age: function(){
		function getAgeFromBirth(){
			var y = new Date().getFullYear();
			return y - this.birth;
		}
		return getAgeFromBirth();
	}
};
xiaoming.age();  //报错undefined
```

结果又报错了! 原因是`this`指针只在`age`方法的函数内指向`xiaoming`, 在函数内部定义的函数, `this`又指向`undefined`了! (非strict模式下, 他会重新指向全局对象`window`!)
修复的办法也不是没有, 我们用一个`that`变量首先捕获`this`:

```javascript
var xiaoming = {
	name: '小明',
	birth: 1990,
	age: function(){
		var that = this;  //在方法内部一开始就捕获this
		function getAgeFromBirth(){
			var y = new Data().getFullYear();
			return y -that.birth;  //用that而不是this
		}
		return getAgeFromBirth();
	}
};
xiaoming.age();  //25
```

用`var that = this;`, 你就可以放心地在方法内部定义其他函数, 而不是把所有语句都堆到一个方法中.

#### apply

虽然在一个独立的函数调用中, 根据是否是strict模式, `this`指向`undefined`或`window`, 不过, 我们还可以控制`this`的指向的.
要指定函数的`this`指向哪一个对象, 可以用函数本身的`apply`方法, 它接收两个参数, 第一个参数就是需要绑定的`this`变量, 第二个参数是`Array`, 表示函数本身的参数.
用`apply`修复`getAge()`调用:

```javascript
function getAge(){
	var y -this.birth;
}
var xiaoming = {
	name: '小明',
	birth: 1990,
	age: getAge
};
xiaoming.age();  //25
getAge.apply(xiaoming, []);  //25, this指向xiaoming, 参数为空
```

另一个与`apply()`类似的方法是`call()`, 唯一的区别是:

* `apply()`把参数打包成`Array`再传入;
* `call()`把参数按顺序传入.

比如调用`Math.max(3, 5, 3)`,分别用`apply()`和`call()`实现如下:

```javascript
Math.max.apply(null,[3,5,4]);  //5
Math.max.call(null,3,5,4);  //5
```

对于普通函数调用, 我们常把`this`绑定为`null`.

#### 装饰器

利用`apply()`, 我们还可以动态的改变函数的行为.
JavaScript的所有对象都是动态的, 即使内置的函数, 我们也可以重新指向新的函数.
现在假定我们想统计一下代码一共调用了多少次`parselnt()`,可以把所有的调用都找出来, 然后手动加上`count += 1`, 不过这样做太傻了. 最佳方案是用我们自己的函数替换掉默认的`parselnt()`:

```javascript
var count = 0;
var oldParselnt = parselnt;  //保留原函数
window.parselnt = function(){
	count += 1;
	return oldParselnt.apply(null, arguments);  //调用原函数
};
```

### 高阶函数

JavaScript的函数其实都纸箱某个变量. 既然变量可以指向函数, 函数的参数能接受变量, 那么一个函数就可以接受另一个函数作为参数, 这种函数就称之为高阶函数.
一个简单地高阶函数:

```javascript
function add(x,y,f){
	return f(x) + f(y);
}
```

#### map/reduce

注: 可以去读一下Google那篇鼎鼎大名的论文"[MapReduce: Simplified Data Processing on Large Clusters](<https://www.cnblogs.com/YaoDD/p/6017397.html>)", 你就能大概明白map/reduce的概念.

##### map

举例说明 比如我们有一个函数$f(x)=x^2$, 要把这个函数作用在一个数组`[1,2,3,4,5,6,7,8,9]`上, 就可以用`map`实现如下:![Snipaste_2019-05-24_17-20-54d9c5a.jpg](https://miao.su/images/2019/05/24/Snipaste_2019-05-24_17-20-54d9c5a.jpg)

由于`map()`方法定义在JavaScript的`Array`中, 我们调用`Array`的`map()`方法, 传入我们自己的函数, 就得到了一个新的`Array`作为结果:

```javascript
function pow(x){
	return x * x;
}
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var results = arr.map(pow);  // [1, 4, 9, 16, 25, 36, 49, 64, 81]
console.log(results);
```

注意: `map()`传入的参数是`pow`, 即函数对象本身.
你可能回想, 不需要`map()`, 写一个循环, 也可以计算出结果:

```javascript
var f = function(x){
	return x * x;
};
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var result = [];
for (var i=0; i<arr.length; i++) {
    result.push(f(arr[i]));
}
```

的确可以, 但是, 从上面的循环代码, 我们无法一眼看明白"把$f(x)$"作用在`Array`的每一个元素并把结果生成一个新的`Array`.
所以, `map()`作为高阶函数, 事实上它把运算规则抽象了, 因此我们可以简化计算任意复杂的函数, 例如把`Array`的所有数字转为字符串:

```javascript
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(String); // ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

仅仅需要一行代码.

##### reduce

再看`reduce`的用法. `Array`的`reduce()`把一个函数作用在这个`Array`的$[x_1,x_2,x_3...]$上, 这个函数必须接受两个参数, `reduce()`把结果继续和序列的下一个元素做累积运算, 其效果就是:

```javascript
[x_1,x_2,x_3...].reduce(f) = f(f(f(x_1,x_2), x_3), x_4)
```

比方说对一个`Array`求和, 就可以用`reduce`实现:

```javascript
var arr = [1, 3, 5, 7, 9];
arr.reduce(function(x, y){
	return x + y;
});  // 25
```

要把`[1, 3, 5, 7, 9]`变换成整数13579, `reduce()`也能派上用场:

```javascript
var arr = [1, 3, 5, 7, 9];
arr.reduce(function(x, y){
	return x * 10 + y;
});  // 13579
```

如果我们继续改进这个例子, 想办法把一个字符串`13579`变成`Array---[1, 3, 5, 7, 9]`, 再利用`reduce()`就可以写出一个把字符串转换为`Number`的函数.

#### filter

filter也是一个常用的操作, 它用于把`Array`的某些元素过滤掉, 然后返回剩下的元素.
和`map()`类似, `Array`的`filter()`也接受一个函数. 和`map()`不同的是, `filter()`把传入的函数依次作用于每个元素, 然后根据返回的值`true`还是`false`决定保留还是丢弃该元素.
例如在一个`Array`中, 删掉偶数, 只保留技术, 可以这么写:

```javascript
var arr = [1, 2, 4, 5, 6, 9, 10, 15];
var r = arr.filter(function(x){
	return x % 2 !== 0;
});
r;  //[1, 5, 9, 15]
```

把一个`Array`中的空字符删掉, 可以这么写:

```javascript
var arr = ['A', 'B', null, undefined, 'C', ''];
var r = arr.filter(function(s){
	return s && s.trim(); // 注意: IE9一下没有trim()方法
});
r;  //['A', 'B', 'C']
```

可见用`filter()`这个高阶函数, 关键在于正确实现一个筛选函数.

#### 回调函数

`filter()`接受的回调函数, 其实可以有多个函数. 通常我们仅使用第一个参数, 表示`Array`的某个元素. 回调函数还可以接收另外两个参数, 表示元素的位置和数组本身:

```javascript
var arr = ['A','B','C'];
var r = arr.filter(function(element, index, self){
	console.log(element);  //一次打印'A','B','c'
	console.log(index);  //依次打印0, 1, 2
	console.log(self);  //self就是变量arr
	return true;
});
```

利用`filter`, 可以巧妙的去除`Array`的重复元素:

```javascript
var 
	r,
	arr = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'strawberry'];
r = arr.filter(function(element, index, self){
	return self.indexOf(element) === index;
});
```

去除重复元素依靠的是`indexOf`总是返回第一个元素的位置, 后续的重复元素位置与`indexOf`返回的位置不相等, 因此被`filter`过滤掉了.

#### sort排序算法

排序也是在程序中经常用到的算法. 无论使用冒泡排序还是快速排序, 排序的核心是比较两个元素的大小. 如果是数字我们可以直接比较, 但如果是字符串或者两个对象呢? 直接比较数学上的大小是没有意义的, 因此, 比较的过程必须通过函数抽象出来. 通常规定, 对于两个元素`x`和`y`, 如果认为`x < y`, 则返回`-1`, 如果认为`x == y`, 则返回`0`, 如果认为`x > y`, 则返回`1`, 这样, 排序算法就不用关心具体的比较过程, 而是根据比较结果直接排序.
JavaScript的`Array`的`sort()`方法就是用于排序的, 但是排序结果可能让你大吃一惊:

```javascript
// 看上去正常的结果:
['Google', 'Apple', 'Microsoft'].sort(); // ['Apple', 'Google', 'Microsoft'];

// apple排在了最后:
['Google', 'apple', 'Microsoft'].sort(); // ['Google', 'Microsoft", 'apple']

// 无法理解的结果:
[10, 20, 1, 2].sort(); // [1, 10, 2, 20]
```

第二个排序把`apple`排在了最后, 是因为字符串根据ASCII码进行排序, 而小写字母`a`的ASCII码在大写字母之后.
为什么第三个排序结果也是错的呢?
这是因为`Array`的`sort()`方法默认把所有元素先转换为String再排序, 结果`10`排在了`2`的前面, 因为字符`1`比字符`2`的ASCII码小.
所以, 如果你不知道`sort()`方法的默认排序规则, 直接对数字排序, 绝对会被坑!!!
幸运的是, `sort()`方法也是一个高阶函数, 它还可以接收一个比较函数来实现自定义的排序.
要按数字大小排序, 我们可以这么写:

```javascript
var arr = [10, 20, 1, 2];
arr.sort(function(x, y){
	if(x < y){
		return -1;
	}
	if(x > f){
		return 1;
	}
	return 0;
});
console.log(arr);  //[1, 2, 10, 20]
```

如果要倒序排序, 我们可以把大的数放在前面
默认情况下, 对字符串排序, 是按照ASCII的大小比较的, 现在, 我们提出排序应该忽略大小写, 不必对现有代码大加改动, 只要我们能定义出忽略大小写的比较算法就可以:

```javascript
var arr = ['Google', 'apple', 'Microsoft'];
arr.sort(function (s1, s2) {
    x1 = s1.toUpperCase();
    x2 = s2.toUpperCase();
    if (x1 < x2) {
        return -1;
    }
    if (x1 > x2) {
        return 1;
    }
    return 0;
}); // ['apple', 'Google', 'Microsoft']
```

忽略大小写来比较两个字符串, 实际上就是先把字符串都变成大写(或者都变成小写), 再比较.
最后友情提示, `sort()`方法会直接对`Array`进行修改, 他返回的结果仍是当前的`Array`

```javascript
var a1 = ['B', 'A', 'C'];
var a2 = a1.sort();
a1; // ['A', 'B', 'C']
a2; // ['A', 'B', 'C']
a1 === a2; // true, a1和a2是同一对象
```

#### Array

对于数组, 除了`map()`、`reduce`、`filter()`、`sort()`这些方法可以传入一个函数之外, `Array`对象还提供了很多非常实用的高阶函数.

##### every

`every()`方法可以判断数组的所有元素是否满足测试条件. 例如, 给定一个包含若干字符串的数组, 判断所有字符串是否满足指定的测试条件:

```javascript
var arr = ['Apple', 'pear', 'orange'];
console.log(arr.every(function(s){
	return s.length > 0;
}));   //true, 因为每个元素都满足s.length > 0;
console.log(arr,every(function(s){
	return s.toLowerCase() === s;
}));   //false,因为不是每个元素全部都是小写
```

##### find

`find()`方法用于查找符合条件的第一个元素, 如果找到了, 返回这个元素, 否则, 返回`undefined`:

```javascript
var arr = ['Apple', 'pear', 'orange'];
console.log(arr.find(function(s){
	return s.toLowerCase() === s;
}));  //'pear' 
console.log(arr.find(function(s){
	return s.toUpperCase() === s;
}));  //undefined
```

##### findIndex

`findIndex()`和`find()`类似, 也是查找符合条件的第一个元素, 不同之处在于`findIndex()`会返回这个元素的索引, 如果没有找到, 返回`-1`:

```javascript
var arr = ['Apple', 'pear', 'orange'];
console.log(arr.findIndex(function (s) {
    return s.toLowerCase() === s;
})); // 1, 因为'pear'的索引是1

console.log(arr.findIndex(function (s) {
    return s.toUpperCase() === s;
})); // -1

```

##### forEach

`forEach()`和`map()`类似，它也把每个元素依次作用于传入的函数，但不会返回新的数组。`forEach()`常用于遍历数组，因此，传入的函数不需要返回值：

```javascript
var arr = ['Apple', 'pear', 'orange'];
arr.forEach(console.log); // 依次打印每个元素
```

#### 闭包

##### 函数作为返回值

高阶函数除了可以接受函数作为参数外, 还可以把函数作为结果值返回.
我们来实现一个对`Array`的求和. 通常情况下, 求和的函数是这样定义的:

```javascript
function sum(arr){
	return arr.reduce(function(x, y){
		return x + y;
	});
}
sum([1, 2, 3, 4, 5]);  //15
```

但是, 如果不需要立即求和, 而是在后面的代码中, 根据需要再计算怎么办? 可以不返回求和的结果, 而是返回求和的函数!

```javascript
function lazy_sum(arr){
	var sum = function(){
		return arr.reduce(function(x, y){
			return x + y;
		});
	}
	return sum;
}
```

当我们调用`lazy_sum()`时, 返回的并不是求和结果, 而是求和函数:

```js
var f = lazy_sum([1, 2, 3, 4, 5]);  //function sum()
```

调用函数`f`时, 才真正计算求和的结果:

```js
f();  //15
```

在这个例子中, 我们在函数`lazy_sum`中定义了函数`sum`, 并且, 内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量, 当`lazy_sum`返回函数`sum`时, 相关参数和变量都保存在返回的函数中, 这种称为`闭包(Closure)`的程序解构拥有极大的威力.
再注意一点: 当我们调用`lazy_sum()`时, 每次调用都会返回一个新的函数, 即使传入相同的参数:

```js
var f1 = lazy_sum([1, 2, 3, 4, 5]);
var f2 = lazy_sum([1, 2, 3, 4, 5]);
f1 === f2;  //false
```

`f1()`和`f2()`的调用结果不影响.

##### 闭包

注意到返回的函数在其定义内部引用了局部变量`arr`, 所以, 当一个函数返回了一个函数后, 其内部的局部变量还被新函数引用, 所以闭包的实现并不容易.
另外需要注意: 返回的函数并没有立即执行, 而是直到调用了`f()`才执行. 现在看一个例子:

````js
function count(){
	var arr = [];
	for (var i = 1; i <= 3; i++){
		arr.push(function(){
			return i * i;
		});
	}
	return arr;
}
var results = count();
var f1 = results[0];
var f2 = results[1];
var f3 = results[2];
````

在上面的例子中, 每次循环, 都创建了一个新的函数, 然后, 把创建的3个函数都添加到一个`Array`中返回了. 你可能认为返回的结果是`1, 4, 9`,但实际的结果是:

```js
f1();  //16
f2();  //16
f3();  //16
```

全部都是16! 原因就在于返回的函数引用了变量`i`, 但它并非立刻执行. 等到3个函数都返回时, 它们所引用的变量`i`已经变成了`4`, 因此最终结果为`16`.
返回闭包时牢记的一点就是: 返回函数不要引用任何循环变量, 或者后续会发生变化的变量.
如果一定要引用循环变量怎么办? 方法是再创建一个函数, 用该函数的参数绑定循环变量到当前的值, 无论该循环变量后续如何更改, 已绑定到函数参数的值不变:

```js
function count(){
	var arr = [];
	for(var i = 1; i <= 3; i++){
		arr.push((function(n){
			return function(){
				return n * n;
			}
		})(i)):
	}
	return arr;
}
var results = count();
var f1 = results[0];  // 1
var f2 = results[1];  // 4
var f3 = results[2];  // 9
```

理论上讲, 创建一个匿名函数并立即执行可以这么写: (由于JavaScript语法解析的问题, 会报错`SyntaxError`, 因此需要用括号把整个函数定义括起来)

```html
(function(x){return x * x}){3};
```

通常, 一个立即执行的匿名函数可以把函数体拆开, 一般这么写:

```js
(function(x){
	return x * x;
})(3);
```

闭包的功能非常强大的功能. 举个栗子:
在面向对象的设计语言里, 比如Java和C++, 要在对象内部封装一个私有变量, 可以用`private`修饰一个成员变量.
在没有`class`机制, 只有函数的语言里, 借助闭包, 同样可以封装一个私有变量. 我们用JavaScript创建一个计数器:

```js
function create_counter(initial){
	var x = initial || 0;
	return {
		inc: function(){
			x += 1;
			return x;
		}
	}
}
```

它用起来像这样

```js
var c1 = create_counter();
c1.inc(); // 1
c1.inc(); // 2
c1.inc(); // 3

var c2 = create_counter(10);
c2.inc(); // 11
c2.inc(); // 12
c2.inc(); // 13
```

在返回的对象中, 实现了一个闭包, 该闭包携带了局部变量`x`, 并且, 从外部代码根本无法访问到变量`x`. 换句话说, 闭包就是携带状态的函数, 并且它的状态可以完全对外隐藏起来.
闭包还可以把多参数的函数变成单参数的函数. 例如, 要计算$x^y$可以用`Math.pow(x,y)`函数, 不过考虑到经常计算$x^2$或$x^3$, 我们可以利用闭包创建新的函数`pow2`和`pow3`:

```javascript
'use strict';

function make_pow(n){
    return function(x){
        return Math.pow(x, n);
    }
}
// 创建两个新函数:
var pow2 = make_pow(2);
var pow3 = make_pow(3);

console.log(pow2(5)); // 25
console.log(pow3(7)); // 343
```

#### 箭头函数

ES6标准新增了一种新的函数: Arrow Function(箭头函数). 如下:

```js
x => x * x
```

相当于:

```js
function(x){
	return x * x
}
```

箭头函数相当于匿名函数, 并且简化了函数定义. 箭头函数有两种格式, 一种像上面的, 只包含了一个表达式, 连`{...}`和`return`都省略掉了. 还有一种可以包含多条语句, 这时候就不能省略`{...}`和`return`:

```js
x => {
	if(x > 0){
		return x * x;
	}
	else{
		return - x * x;
	}
}
```

如果参数不是一个, 就需要用括号`()`括起来:

```js
// 两个参数:
(x, y) => x * x + y * y
// 无参数:
() => 3.14
// 可变参数:
(x, y, ...rest) => {
	var i, sum = x + y;
	for(i = 0; i < rest.length; i++){
		sum += rest[i];
	}
	return sum;
}
```

如果要返回一个对象, 就要注意, 如果是单表达式, 这么写的话会报错:

```js
// SyntaxError:
x => {foo: x}
```

因为和函数体的`{...}`有语法冲突, 所以要改为:

```js
// ok:
x => ({foo: x})
```

##### this

箭头函数看上去是匿名函数的一种简写, 但实际上, 箭头函数和匿名函数有个明显的区别: 箭头函数内部的`this`是词法作用域, 由上下文确定.
回顾前面的例子, 由于JavaScript函数对`this`绑定的错误处理, 下面的例子无法得到预计结果:

```js
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = function () {
            return new Date().getFullYear() - this.birth; // this指向window或undefined
        };
        return fn();
    }
};
```

现在, 箭头函数完全修复了`this`的指向, `this`总是指向词法作用域,也就是外层调用者`obj`:

```js
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
        return fn();
    }
};
obj.getAge(); // 25
```

由于`this`在箭头函数汇总已经按照词法作用域绑定了, 所以, 用`call()`或者`apply()`调用箭头函数时, 无法对`this`进行绑定, 即传入的第一个参数被忽略:

```js
var obj = {
    birth: 1990,
    getAge: function (year) {
        var b = this.birth; // 1990
        var fn = (y) => y - this.birth; // this.birth仍是1990
        return fn.call({birth:2000}, year);  //传入的第一个参数直接被忽略
    }
};
obj.getAge(2015); // 25
```

#### generator

generator(生成器)是ES6标准引入的新的数据类型. 一个generator看上去像一个函数, 但可以返回多次.
generator跟函数很像, 定义如下:

```js
function* foo(x){
	yield x + 1;
	yield x + 2;
	return x + 3;
}
```

generator和函数不同的是, generator由`function*`定义(注意多出的`*`), 并且, 除了`return`运距, 还可以使用`yield`返回多次.
比如使用生成器完成的斐波拉契数列:

```js
function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 0;
    while (n < max) {
        yield a;
        [a, b] = [b, a + b];
        n ++;
    }
    return;
}
```

至二级调用试试:

```js
fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window}
```

直接调用一个生成器和调用函数不一样,`fib(5)`仅仅是创建了一个generator对象, 还没有去执行它.
调用generator对象有两个方法, 一是不断地调用generator对象的`next()`方法:

```js
var f = fib(5);
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: false}
f.next(); // {value: undefined, done: true}
```

`next()`方法会执行generator的代码, 然后, 每次遇到`yield x;`就返回一个对象`{value: x, done: true/false}`, 然后`暂停`. 返回的`value`就是`yield`的返回值, `done`表示这个generator是否已经执行结束了. 如果`done`为`true`, 则`value`就是`return`的返回值.
当执行到`done`为`true`时, 这个generator对象已经全部执行完毕, 不要再继续调用`next()`了. 第二个方法是直接用`for...of`循环迭代generator对象, 这种方式不需要我们自己判断`done`.

```js
use strict'

function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 0;
    while (n < max) {
        yield a;
        [a, b] = [b, a + b];
        n ++;
    }
    return;
}
for (var x of fib(10)) {
    console.log(x); // 依次输出0, 1, 1, 2, 3, ...
}
```

generator和普通函数比, 有什么用?
因为generator可以在执行过程中多次返回, 所以它看上去就像一个可以记住执行状态的函数, 利用这一点, 写一个generator就可以实现需要用面向对象才能实现的功能. 例如, 用一个对象来保存状态, 的这么写:

```js
var fib = {
    a: 0,
    b: 1,
    n: 0,
    max: 5,
    next: function () {
        var
            r = this.a,
            t = this.a + this.b;
        this.a = this.b;
        this.b = t;
        if (this.n < this.max) {
            this.n ++;
            return r;
        } else {
            return undefined;
        }
    }
};
```

用对象的属性来保存状态, 相当的繁琐.
generator还有另外一个巨大的好处, 就是把异步回调代码变成"同步"代码. 这个好处等后面学了AJAX以后才能体会到. 没有generator之前的黑暗时代, 用AJAX时需要这么写:

```js
ajax('http://url-1', data1, function (err, result) {
    if (err) {
        return handle(err);
    }
    ajax('http://url-2', data2, function (err, result) {
        if (err) {
            return handle(err);
        }
        ajax('http://url-3', data3, function (err, result) {
            if (err) {
                return handle(err);
            }
            return success(result);
        });
    });
});
```

回调越多, 可读性越差, 而我们有了generator之后, 可以这么写:

```js
try {
    r1 = yield ajax('http://url-1', data1);
    r2 = yield ajax('http://url-2', data2);
    r3 = yield ajax('http://url-3', data3);
    success(r3);
}
catch (err) {
    handle(err);
}
```

看上去是同步的代码, 实际是异步执行的.

