# <center>Flask框架</center>

[TOC]

## Web表单

Web表单是HTML页面中负责数据采集的部件。表单由三个部分组成：表单标签、表单域、表单按钮。表单允许用户输入数据，负责HTML页面的数据采集，通过表单将用户输入的数据提交给服务器。

在Flask中，为了处理Web表单，我们可以使用`Flask-WTF`扩展，它封装了`WTForms`，并且它由验证表单数据的功能。

原有的表单写法：

```html
<form method="post">
    <label>表单标签</label><input type="输入类型" name="名称" placeholder="占位文本"><br>
    <label>表单标签</label><input type="输入类型" name="名称" placeholder="占位文本"><br>
</form>
```

WTF表单的写法：

配置参数，关闭 CSRF 校验：

```python
app.config['WTF_CSRF_ENABLED'] = False
```

先定义一个表单类，文本字段、密码字段、提交按钮：

```python
class RegisterForm(FlaskForm):
    名称1 = StringField('xxx1'， validators=[InputRequired('yyy1')], render_kw={'placeholder': '占位文字1'})
    名称2 = PasswordField('xxx2'， validators=[InputRequired('yyy2')], render_kw={'placeholder': '占位文字2'})
    名称3 = 字段对象('xxx3'， validators=[InputRequired('yyy3')], 验证请求, render_kw={'placeholder': '占位文字3'})
```

创建路由，创建类实例：

```python
def register_wtf():
    regiser_form = RegisterForm()
```

执行注册逻辑：

```python
if register_form.validate_on_submit():
    pass
	return success
else:
    if request.method == 'POST':
        flash('参数错误')
return render_template('xxx.html')
```

取到表单中提交的参数：

```python
username = request.form.get('username')
# 或者
username = register_form.username.data
```

模板中的WTF写法：

```jinja2
<form method="post">
	{{ form.名称1.label}}{{ form.名称1 }}<br>
	{{ form.名称1.label}}{{ form.名称1 }}<br>
</form>
```



### WTForms支持的HTML标准字段

| 字段对象           | 说明                                      |
| :----------------- | :---------------------------------------- |
| StringField        | 文本字段                                  |
| TextAreaField      | 多行文本字段                              |
| PasswordField      | 密码文本字段                              |
| HiddenField        | 隐藏文件字段                              |
| DateField          | 文本字段，值为 datetime.date 文本格式     |
| DateTimeField      | 文本字段，值为 datetime.datetime 文本格式 |
| IntegerField       | 文本字段，值为整数                        |
| DecimalField       | 文本字段，值为decimal.Decimal             |
| FloatField         | 文本字段，值为浮点数                      |
| BooleanField       | 复选框，值为True 和 False                 |
| RadioField         | 一组单选框                                |
| SelectField        | 下拉列表                                  |
| SelectMutipleField | 下拉列表，可选择多个值                    |
| FileField          | 文件上传字段                              |
| SubmitField        | 表单提交按钮                              |
| FormField          | 把表单作为字段嵌入另一个表单              |
| FieldList          | 一组指定类型的字段                        |

### WTForms常用验证函数

| 验证函数     | 说明                                     |
| :----------- | :--------------------------------------- |
| DataRequired | 确保字段中有数据                         |
| EqualTo      | 比较两个字段的值，常用于比较两次密码输入 |
| Length       | 验证输入的字符串长度                     |
| NumberRange  | 验证输入的值在数字范围内                 |
| URL          | 验证URL                                  |
| AnyOf        | 验证输入值在可选列表中                   |
| NoneOf       | 验证输入值不在可选列表中                 |

使用 Flask-WTF 需要配置参数 SECRET_KEY。

CSRF_ENABLED是为了CSRF（跨站请求伪造）保护。 SECRET_KEY用来生成加密令牌，当CSRF激活的时候，该设置会根据设置的密匙生成加密令牌。

## CSRF

* `CSRF`全拼为`Cross Site Request Forgery`，译为跨站请求伪造。
* `CSRF`指攻击者盗用了你的身份，以你的名义发送恶意请求

### CSRF示意图

![Snipaste_2019-06-02_16-20-42f0817.jpg](https://miao.su/images/2019/06/02/Snipaste_2019-06-02_16-20-42f0817.jpg)

### 防止 CSRF 攻击

#### 步骤

1. 在客户端向后端请求界面数据的时候，后端会往响应中的 cookie 中设置 csrf_token 的值
2. 在 Form 表单中添加一个隐藏的的字段，值也是 csrf_token
3. 在用户点击提交的时候，会带上这两个值向后台发起请求
4. 后端接受到请求，以会以下几件事件：
   - 从 cookie中取出 csrf_token
   - 从 表单数据中取出来隐藏的 csrf_token 的值
   - 进行对比
5. 如果比较之后两值一样，那么代表是正常的请求，如果没取到或者比较不一样，代表不是正常的请求，不执行下一步操作

#### 代码演示

添加生成csrf_token的函数：

```python
def generate_csrf():
	return bytes.decode(base64.b64encode(os.urandom(48)))
```

渲染模板时传入此函数：

```python
csrf_token(取的名字) = generate_csrf()
```

在对应的表单中加上隐藏的csrf块：

```html
<form method="post">
    <input type="hidden" name="csrf_token" value="{{csrf_token（取的名字）}}">
    ... ...
</form>
```

在cookie中也加上这个csrf值：

```python
response.set_cookie('csrf_token', csrf_token)
```

取出表单和cookie中csrf的值做校验，校验成功再继续操作：

```python
form_csrf_token = request.form.get('csrf_token')  # 取表单
cookie_csrf_token = request.cookies.get('csrf_token', '')  # 取cookie 
```



## ORM

- **ORM** 全拼`Object-Relation Mapping`.
- 中文意为 **对象-关系映射**.
- 主要实现模型对象到关系数据库数据的映射.

### ORM图解

![Snipaste_2019-06-02_20-51-0297091.jpg](https://miao.su/images/2019/06/02/Snipaste_2019-06-02_20-51-0297091.jpg)

### 优点 

- 只需要面向对象编程, 不需要面向数据库编写代码.
  - 对数据库的操作都转化成对类属性和方法的操作.
  - 不用编写各种数据库的`sql语句`.
- 实现了数据模型与数据库的解耦, 屏蔽了不同数据库操作上的差异.
  - 不在关注用的是`mysql`、`oracle`...等.
  - 通过简单的配置就可以轻松更换数据库, 而不需要修改代码.

### 缺点 

- 相比较直接使用SQL语句操作数据库,有性能损失.
- 根据对象的操作转换成SQL语句,根据查询的结果转化成对象, 在映射过程中有性能损失.



## Flask-SQLAlchemy安装及设置

- SQLALchemy 实际上是对数据库的抽象，让开发者不用直接和 SQL 语句打交道，而是通过 Python 对象来操作数据库，在舍弃一些性能开销的同时，换来的是开发效率的较大提升
- SQLAlchemy是一个关系型数据库框架，它提供了高层的 ORM 和底层的原生数据库的操作。flask-sqlalchemy 是一个简化了 SQLAlchemy 操作的flask扩展。
- [文档地址](http://docs.jinkan.org/docs/flask-sqlalchemy)

 安装模块：

```bash
sudo pip install flask-sqlalchemy
sudo pip install flask-mysql
```

导入模块并配置数据库对象(关闭数据库追踪)：

```python
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@localhost:port/database_name"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
```

初始化数据库对象：

```python
db = SQLAlchemy(app)
```

创建一个类以准备创建表：

```python
class 表名xxx(db.Model):
    __tablename__ = "表别名"
    字段名 = db.Column(db.Interger字段类型, 约束)
```

### 其他配置

| 名字                      | 备注                                                         |
| :------------------------ | :----------------------------------------------------------- |
| SQLALCHEMY_DATABASE_URI   | 用于连接的数据库 URI 。例如:sqlite:////tmp/test.dbmysql://username:password@server/db |
| SQLALCHEMY_BINDS          | 一个映射 binds 到连接 URI 的字典。更多 binds 的信息见[*用 Binds 操作多个数据库*](http://docs.jinkan.org/docs/flask-sqlalchemy/binds.html#binds)。 |
| SQLALCHEMY_ECHO           | 如果设置为Ture， SQLAlchemy 会记录所有 发给 stderr 的语句，这对调试有用。(打印sql语句) |
| SQLALCHEMY_RECORD_QUERIES | 可以用于显式地禁用或启用查询记录。查询记录 在调试或测试模式自动启用。更多信息见get_debug_queries()。 |
| SQLALCHEMY_NATIVE_UNICODE | 可以用于显式禁用原生 unicode 支持。当使用 不合适的指定无编码的数据库默认值时，这对于 一些数据库适配器是必须的（比如 Ubuntu 上 某些版本的 PostgreSQL ）。 |
| SQLALCHEMY_POOL_SIZE      | 数据库连接池的大小。默认是引擎默认值（通常 是 5 ）           |
| SQLALCHEMY_POOL_TIMEOUT   | 设定连接池的连接超时时间。默认是 10 。                       |
| SQLALCHEMY_POOL_RECYCLE   | 多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL ， Flask-SQLALchemy 自动设定 这个值为 2 小时。 |

### 连接其他数据库

完整连接 URI 列表请跳转到 SQLAlchemy 下面的文档 ([Supported Databases](http://www.sqlalchemy.org/docs/core/engines.html)) 。这里给出一些 常见的连接字符串。

- Postgres:

```python
postgresql://scott:tiger@localhost/mydatabase
```

- MySQL:

```pyhton
mysql://scott:tiger@localhost/mydatabase
```

- Oracle:

```pyhton
- oracle://scott:tiger@127.0.0.1:1521/sidname
```

- SQLite （注意开头的四个斜线）:

```python
sqlite:////absolute/path/to/foo.db
```

### 常用的SQLAlchemy字段类型

| 类型名       | python中类型      | 说明                                                |
| :----------- | :---------------- | :-------------------------------------------------- |
| Integer      | int               | 普通整数，一般是32位                                |
| SmallInteger | int               | 取值范围小的整数，一般是16位                        |
| BigInteger   | int或long         | 不限制精度的整数                                    |
| Float        | float             | 浮点数                                              |
| Numeric      | decimal.Decimal   | 普通整数，一般是32位                                |
| String       | str               | 变长字符串                                          |
| Text         | str               | 变长字符串，对较长或不限长度的字符串做了优化        |
| Unicode      | unicode           | 变长Unicode字符串                                   |
| UnicodeText  | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool              | 布尔值                                              |
| Date         | datetime.date     | 时间                                                |
| Time         | datetime.datetime | 日期和时间                                          |
| LargeBinary  | str               | 二进制文件                                          |

### 常用的SQLAlchemy列选项

| 选项名      | 说明                                              |
| :---------- | :------------------------------------------------ |
| primary_key | 如果为True，代表表的主键                          |
| unique      | 如果为True，代表这列不允许出现重复的值            |
| index       | 如果为True，为这列创建索引，提高查询效率          |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值 |
| default     | 为这列定义默认值                                  |

### 常用的SQLAlchemy关系选项

| 选项名         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| backref        | 在关系的另一模型中添加反向引用                               |
| primary join   | 明确指定两个模型之间使用的联结条件                           |
| uselist        | 如果为False，不使用列表，而使用标量值                        |
| order_by       | 指定关系中记录的排序方式                                     |
| secondary      | 指定多对多关系中关系表的名字                                 |
| secondary join | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件 |

### 模型之前的关联

#### 一对多

```python
class Role(db.Model):
    ...
    #关键代码
    us = db.relationship('User', backref='role', lazy='dynamic')
    ...

class User(db.Model):
    ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

- 其中realtionship描述了Role和User的关系。在此文中，第一个参数为对应参照的类"User"
- 第二个参数backref为类User申明新属性的方法
- 第三个参数lazy决定了什么时候SQLALchemy从数据库中加载数据
  - 如果设置为子查询方式(subquery)，则会在加载完Role对象后，就立即加载与其关联的对象，这样会让总查询数量减少，但如果返回的条目数量很多，就会比较慢
    - 设置为 subquery 的话，role.users 返回所有数据列表
  - 另外,也可以设置为动态方式(dynamic)，这样关联对象会在被使用的时候再进行加载，并且在返回前进行过滤，如果返回的对象数很多，或者未来会变得很多，那最好采用这种方式
    - 设置为 dynamic 的话，role.users 返回查询对象，并没有做真正的查询，可以利用查询对象做其他逻辑，比如：先排序再返回结果

#### 多对多

```python
registrations = db.Table('registrations',  
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')),  
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))  
)  
class Course(db.Model):
    ...
class Student(db.Model):
    ...
    courses = db.relationship('Course',secondary=registrations,  
                                    backref='students',  
                                    lazy='dynamic')
```

### 常用的SQLAlchemy查询过滤器

| 过滤器      | 说明                                             |
| :---------- | :----------------------------------------------- |
| filter()    | 把过滤器添加到原查询上，返回一个新查询           |
| filter_by() | 把等值过滤器添加到原查询上，返回一个新查询       |
| limit       | 使用指定的值限定原查询返回的结果                 |
| offset()    | 偏移原查询返回的结果，返回一个新查询             |
| order_by()  | 根据指定条件对原查询结果进行排序，返回一个新查询 |
| group_by()  | 根据指定条件对原查询结果进行分组，返回一个新查询 |

### 常用的SQLAlchemy查询执行器

| 方法           | 说明                                         |
| :------------- | :------------------------------------------- |
| all()          | 以列表形式返回查询的所有结果                 |
| first()        | 返回查询的第一个结果，如果未查到，返回None   |
| first_or_404() | 返回查询的第一个结果，如果未查到，返回404    |
| get()          | 返回指定主键对应的行，如不存在，返回None     |
| get_or_404()   | 返回指定主键对应的行，如不存在，返回404      |
| count()        | 返回查询结果的数量                           |
| paginate()     | 返回一个Paginate对象，它包含指定范围内的结果 |

### 创建表：

```python
db.create_all()
```

### 删除表

```python
db.drop_all()
```

### 插入一条数据

```pyhton
ro1 = Role(name='admin')
db.session.add(ro1)
db.session.commit()
#再次插入一条数据
ro2 = Role(name='user')
db.session.add(ro2)
db.session.commit()
```

### 一次插入多条数据

```python
us1 = User(name='wang',email='wang@163.com',password='123456',role_id=ro1.id)
us2 = User(name='zhang',email='zhang@189.com',password='201512',role_id=ro2.id)
us3 = User(name='chen',email='chen@126.com',password='987654',role_id=ro2.id)
us4 = User(name='zhou',email='zhou@163.com',password='456789',role_id=ro1.id)
us5 = User(name='tang',email='tang@itheima.com',password='158104',role_id=ro2.id)
us6 = User(name='wu',email='wu@gmail.com',password='5623514',role_id=ro2.id)
us7 = User(name='qian',email='qian@gmail.com',password='1543567',role_id=ro1.id)
us8 = User(name='liu',email='liu@itheima.com',password='867322',role_id=ro1.id)
us9 = User(name='li',email='li@163.com',password='4526342',role_id=ro2.id)
us10 = User(name='sun',email='sun@163.com',password='235523',role_id=ro2.id)
db.session.add_all([us1,us2,us3,us4,us5,us6,us7,us8,us9,us10])
db.session.commit()
```

### 查询:filter_by精确查询

返回名字等于wang的所有人

```python
User.query.filter_by(name='wang').all()
```

### first()返回查询到的第一个对象

```python
User.query.first()
```

### all()返回查询到的所有对象

```python
User.query.all()
```

### filter模糊查询，返回名字结尾字符为g的所有数据。

```python
User.query.filter(User.name.endswith('g')).all()
```

### get():参数为主键，如果主键不存在没有返回内容

```python
User.query.get()
```

### 逻辑非，返回名字不等于wang的所有数据

```python
User.query.filter(User.name!='wang').all()
```

### not_ 相当于取反

```python
from sqlalchemy import not_
User.query.filter(not_(User.name=='chen')).all()
```

### 逻辑与，需要导入and，返回and()条件满足的所有数据

```python
from sqlalchemy import and_
User.query.filter(and_(User.name!='wang',User.email.endswith('163.com'))).all()
```

### 逻辑或，需要导入or_

```python
from sqlalchemy import or_
User.query.filter(or_(User.name!='wang',User.email.endswith('163.com'))).all()
```

### 查询数据后删除

```python
user = User.query.first()
db.session.delete(user)
db.session.commit()
User.query.all()
```

### 更新数据

```python
user = User.query.first()
user.name = 'dong'
db.session.commit()
User.query.first()
```

### 关联查询示例：

> 角色和用户的关系是一对多的关系，一个角色可以有多个用户，一个用户只能属于一个角色。

- 查询角色的所有用户

```python
#查询roles表id为1的角色
ro1 = Role.query.get(1)
#查询该角色的所有用户
ro1.us.all()
```

- 查询用户所属角色

```python
#查询users表id为3的用户
us1 = User.query.get(3)
#查询用户属于什么角色
us1.role
```

## 综合案例-图书管理

- WTF表单
- 数据库操作
- 一对多关系演练

### 定义模型

模型表示程序使用的数据实体，在Flask-SQLAlchemy中，模型一般是Python类，继承自db.Model，db是SQLAlchemy类的实例，代表程序使用的数据库。

类中的属性对应数据库表中的列。id为主键，是由Flask-SQLAlchemy管理。db.Column类构造函数的第一个参数是数据库列和模型属性类型。

> 注：如果没有在创建数据库的时候指定编码的话，向数据库中插入中文后，会报错，那么需要修改数据库的编码集:

```python
alter database 数据库名 character set utf8
```

如下示例，配置数据库：

```python
app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://jhonchen:password@localhost:3306/booktest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```



定义了两个模型类，作者和书名。

```python
class Author(db.Model):
    # 作者模型　"一"
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义属性,以便作者模型可以直接通过该属性访问其"多"的一方的数据
    # backref使其可以反过来获取"一"这一方的信息
    books = db.relationship('Book', backref='author')
    

class Book(db.Model):
    # 书本模型  "多"
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # "一"的一方的"id"作为外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))
```

创建表并添加测试数据：

```python
# 创建表
db.drop_all()
db.create_all()
# 添加数据
au1 = Author(name='老王')
au2 = Author(name='老尹')
au3 = Author(name='老刘')
# 把数据提交给用户会话
db.session.add_all([au1, au2, au3])
# 提交会话
db.session.commit()
bk1 = Book(name='老王回忆录', author_id=au1.id)
bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
bk3 = Book(name='如何才能让自己更帅', author_id=au2.id)
bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
# 把数据提交给用户会话
db.session.add_all([bk1, bk2, bk3, bk4, bk5])
# 提交会话
db.session.commit()
```

到这里基本界面显示和数据库导入完成。

