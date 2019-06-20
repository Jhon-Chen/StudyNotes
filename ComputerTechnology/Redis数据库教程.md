# Redis数据库教程

[TOC]

Redis 是一个高性能的 key-value 数据库。

## nosql介绍

### NoSQL：一类新出现的数据库（not only sql）

* 泛指非关系型的数据库

* 不支持SQL语法

* 存储结构跟传统关系型数据库中的那种关系表完全不同，nosql中存储的数据都是KV形式

* NoSQL的世界中没有一种通用的语言，每种nosql数据库都有自己的api和语法，以及擅长的业务场景

* NoSQL中的产品种类相当多：

* - Mongodb

  * Redis
  * Hbase hadoop
  * Cassandra hadoop

### NoSQL和SQL数据库的比较

* 适用场景不同：sql数据库适用于关系特别复杂的数据查询场景，nosql反之
* “事务”特性的支持：sql对事务的支持非常完善，而nosql基本不支持事务
* 两者在不断的取长补短，呈现融合趋势

#### Redis简介

* Redis是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。从2010年3月15日起，Redis的开发工作由VMware主持。从2013年5月开始，Redis的开发由Pivotal赞助。
* Redis是NoSQL技术阵营中的一员，它通过多种键值数据类型来适应不同场景下的储存需求，借助一些高层级的接口使用其可以胜任，如缓存、队列系统的不同角色。

#### Redis特性

Redis与其他key-value缓存产品有以下三大特点：

1. Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
2. Redis不仅仅支持简单的key-value类型的数据，同时还提供list, set, zset, hash等数据结构的存储。
3. Redis支持数据的备份，即master-slave模式的数据备份。

#### Redis优势

* 性能极高---Redis能读的速度是110000次/s，写的速度是81000次/s。
* 丰富的数据类型---Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets数据类型操作。
* 原子---Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。
* 丰富的特性---Redis还支持 publish/subscribe ，通知，key过期等待特性。

#### Redis应用场景

* 用来做缓存（encache/mmcached）--- redis的所有数据是放在内存中的（内存数据库）
* 可以在某些特定应用场景下替代传统数据库 --- 比如社交类应用
* 在一些大型系统中，巧妙地实现一些特定的功能：session共享、购物车
* 只要你有丰富的想象力，redis可以用在可以给你无限的惊喜... ...

## Redis服务器端和客户端命令

### 服务器端

* CentOS7中：sudo systemctl start redis.service

### 客户端

* 连接redis：redis-cli
* 运行测试命令：ping
* 切换数据库：select [index]

## Redis中的增删改查

### 数据结构

* redis是key-value的数据库，每条数据都是一个键值对
* 键的类型是字符串
* 注意：键不能重复

![_201906172010340fd47.png](https://miao.su/images/2019/06/17/_201906172010340fd47.png)

* 值的类型分为五种：
* 1. 字符串string
  2. 哈希hash
  3. 列表list
  4. 集合set
  5. 有序集合zset

### 数据操作行为

* 保存
* 修改
* 获取
* 删除

## String类型

> 字符串类型是Redis中最为基础的数据存储类型，它在Redis中是二进制安全的，这便意味着该类型可以接受任何格式的数据，如JPEG图像或者Json对象描述信息等。在Redis中字符串类型的Value最多可以容纳的数据长度是512M。

### 保存

如果设置的键不存在则添加，如果设置的键已经存在则修改。

* 设置键值
  `set key value`
* 例1：设置键为name值为itcast的数据
  `set name itcast`
* 设置键值及过期时间，以秒为单位
  `setex key seconds value`
* 例2：设置键为aa值为aa过期时间为3秒的数据
  `setex aa 3 aa`
* 设置多个键值
  `mset key1 value1 key2 value2`
* 例3：这只键为a1值为pthon、键为a2值为java、键为a3值为c
  `mset a1 python a2 java a3 c`
* 追加值
  `append key value`
* 例4：向键为a1中追加值haha
  `append ‘a1’ ‘haha’`

### 获取

* 获取：根据键获取值，如果不存在此键则返回nil
  `get key`
* 例5：获取键a1的值
  `get a1`
* 根据多个键获取多个值
  `mget key1 key2`
* 例6：获取a1，a2，a3的值
  `mget a1 a2 a3`

## 键命令

* 查找键，参数支持正则表达式
  `keys pattern`
* 例1：查看所有键
  `keys *`
* 例2：查看名称中包含a的键
  `keys ‘a*’`
* 判断键是否存在，如果存在返回1，不存在返回0
  `exists key1`
* 例3：判断键a1是否存在
  `exists a1`
* 删除键及对应的值
  `del key1 key2`
* 例5：删除a2
  `del a2`
* 查看有效时间，以秒为单位
  `ttl key`
* 例7：查看键a1的有效时间
  `ttl a1`

## hash类型

> hash用于存储对象、对象的结果为属性、值；值的类型为string

* hash用于存储对象，对象的结构为属性、值
* 值的类型为String

### 增加修改

* 设置单个属性
  `hset key field value`
* 例1：设置键user的属性name为jhonchen
  `hset user name jhonchen`

### 获取

* 获取指定键所有的属性
  `hkeys key`
* 例2：获取键user的所有属性
  `hkeys user`
* 获取一个属性的值
  `hget key field`
* 例3：获取键user属性name的值
  `hget user name`
* 获取多个属性的值
  `hmget key field1 field2`
* 例4：获取键user属性name和age的值
  `hmget user name age`
* 获取键所有属性的值
  `hvals key`
* 例5：获取键user的所有属性的值
  `hvals user`

### 删除

* 删除整个hash键及值，使用del命令
* 删除属性，属性对应的值会被一起删除
  `hdel key field1 filed2`
* 例6：删除键u2的属性age
  `hdel u2 age`

## list类型

> 列表的元素类型为string；按照插入顺序排序

### 增加

* 在左侧插入数据
  `lpush key value1 value2`
* 例1：从键a1的列表左侧加入数据a，b，c
  `lpush a1 a b c`
* 在右侧插入数据
  `rpush key value1 value2`
* 例2：从键b1的列表右侧加入数据0,1
  `rpush b1 0 1`
* 在指定元素的前或后插入新元素
  `linsert key before 或 after 现有元素 新元素`
* 例3：在键a1的列表中元素b前加入3
  `linsert b1 before b 3`

### 获取

* 返回列表里指定范围内的元素
  * start、stop为元素的下标索引
  * 索引从左侧开始，第一个元素为0
  * 索引可以是负数，表示从尾部开始计数，如-1表示最后一个元素
    `lrange key start stop`
  * 例4：获取键为b1的列表所有元素
    `lrange b1 0 -1`

#### 设置指定索引位置的元素值

* 索引从左侧开始，第一个元素为0
* 索引可以是负数，表示尾部开始计数，如-1表示最后一个元素
  `lset key index value`
* 例5：修改键为b1的列表中下标为1的元素值为z
  `lset b1 1 z`

### 删除

* 删除指定元素
  * 将列表中前count次出现的值为value的元素移出
  * count > 0：从前往后移出
  * count < 0：从后往前移出
  * count = 0：移出所有
    `lrem key count value`
* 例6.1：向列表b2中加入元素q，w，q，e，r，t，q，q
  `lpush b2 q w q e r t q q`
* 例6.2：从b2列表右侧开始删除2个b
  `lrem b2 -2 q`
* 例6.3：查看列表b2的所有元素
  `lrange b2 0 -1`

## set类型

> 无序集合；元素为string类型；元素具有唯一性，不重复；没有修改操作

### 增加

* 添加元素
  `sadd key member1 member2`
* 例1：向键b3中添加元素 jhon tina ma
  `sadd key jhon tina ma`

### 获取

* 返回所有的元素
  `smembers key`
* 例2：获取键b3的集合中所有元素
  `smembers b3`

### 删除

* 删除指定元素
  `srem key`
* 例3：删除键b3的集合中元素jhon
  `srem b3 jhon`

## zset类型

> sorted set，有序集合
>
> 元素为string类型
>
> 元素具有唯一性，不重复
>
> 每个元素都会关联一个double类型的score，表示权重，通过权重将元素从小到大排序

### 增加

* 添加
  `zadd key score1 member1 score2 member2`
* 例1：向键b4的集合中添加元素 jhon tina damon anna，权重分别为4,5,6,7
  `zadd b4 4 jhon 6 tina 5 damon 7 anna`

### 获取

> 返回指定范围内的元素
>
> start、stop为元素的下标索引
>
> 索引从左侧开始，第一个元素为0
>
> 索引可以是负数，表示从尾部开始计数，如-1表示最后一个元素
> `zrange key start stop`

* 例2：获取键表b4的集合中所有的元素
  `zrange b4 0 -1`
* 返回score值在min和max之间的成员
  `zrangebyscore key min max`
* 例3：获取键b4的集合中权限值在5和6之间的成员
  `zrangebyscore b4 5 6`
* 返回成员member的score值
  `zscore key member`
* 例4：获取键b4的集合中元素tina的权重
  `zscore b4 tina`

### 删除

* 删除指定元素
  `zrem key member1 member2`
* 例5：删除集合b4中元素damon
  `zrem b4 damon`
* 删除权重在指定范围的元素
  `zremrangebyscore key min max`
* 删除集合b4中权限大于7的元素
  `zremrangeby score key 7`

## 与Python的交互

>  [源码见github仓库]([https://github.com/Jhon-Chen/Code_Practice/tree/master/F_flask/Part7_Redis%E6%95%B0%E6%8D%AE%E5%BA%93](https://github.com/Jhon-Chen/Code_Practice/tree/master/F_flask/Part7_Redis数据库))

## 搭建主从

### 主从概念

* 一个master可以拥有多个slave，一个slave又可以拥有多个slave，如此下去，形成了强大的多级服务器集群架构
* master用来写数据，slave用来读数据，经统计：网站的读写比率是10:1
* 通过主从配置可以实现读写分离
* master和slave都是一个redis实例（redis服务）

![imagebac15.png](https://miao.su/images/2019/06/18/imagebac15.png)

### 主从配置

#### 配置主

* 查看当前主机的ip地址,注意，阿里云查出来的是内网ip
  `ifconfig`
* 修改 etc/redis/redis.config 文件
  `sudo vim redis.conf`
  `bind 47.100.200.127`
* 重启redis服务
  `sudo service redis stop`
  `redis-server redis.conf`

#### 配置从

* 复制 etc/redis/redis.conf 文件
  `sudo cp redis.conf ./slave.conf`
* 修改 redis/slave.conf 文件
  `sudo vim slave.conf`
* 编辑内容
  `bind 47.100.200.127`
  `slaveof 47.100.200.127 6379`
  `port 6378`
* redis服务
  `sudo redis-server slave.conf`
* 查看主从关系
  `redis-cli -h 47.100.200.127 info Replication`

#### 数据操作

* 在master和slave分别执行info命令，查看输出信息 进入主客户端
  `redis-cli -h 47.100.200.127 -p 6379`
* 进入从客户端
  `redis-cli -h 47.100.200.127 -p 6378`
* 在master上写数据
  `set aa aa`
* 在slave上读数据
  `get aa`

## 搭建集群

> 之前我们已经建立主从概念，一主可以多从，如果同时的访问量过大（1000w），主服务器肯定会挂掉，数据服务就挂掉了或者发生自然灾难。
>
> 大公司都会有很多的服务器（华东、华南、华中、华北、西北、西南、东北、台港澳等地区的机房）

### 集群的概念

* 集群是一组相互独立的、通过高速互联网的计算机，它们构成了一个组，并以单一系统的模式加以管理。一个客户与集群互相作用时，集群像是一个独立的服务器。集群配置是用于提高可用性和可所方向。
* 当请求到来，首先由负载均衡服务器处理，把请求转发到另外一台服务器上。

![imagee2693.png](https://miao.su/images/2019/06/20/imagee2693.png)

### Redis集群

* 分类
  * 软件层面
  * 硬件层面

* 软件层面：只有一台电脑，在这一台电脑上启动了多个redis服务

![image96e6d.png](https://miao.su/images/2019/06/20/image96e6d.png)

* 硬件层面：存在多台实体电脑，每台电脑上都启动了一个redis或者多个redis服务

![image2b9b4.png](https://miao.su/images/2019/06/20/image2b9b4.png)

### 搭建集群

* 当前拥有两台主机47.100.200.127、（IP），这里的IP在使用时要改为实际值。

具体略过。