# 各种代理软件适用规则，不同软件之间大同小异
## 规则集
- RULE-SET
  - 引用规则集合，需配置rule-providers
- DOMAIN-SET
## 域名规则 
- DOMAIN

  - 匹配完整域名

- DOMAIN-SUFFIX

  - 匹配域名后缀

  - 例：google.com匹配www.google.com/mail.google.com和google.com,但不匹配content-google.com

- DOMAIN-KEYWORD

  - 使用域名关键字匹配

- DOMAIN-REGEX（或URL-REGEX）

  - 域名正则表达式匹配

- GEOSITE
  - 匹配 Geosite 内的域名，部分内容参考 v2fly/domain-list-community
## IP规则

- IP-CIDR & IP-CIDR6

  - 匹配 IP 地址范围，IP-CIDR和IP-CIDR6效果是一样的，IP-CIDR6只是一个别名

- IP-SUFFIX

  - 匹配 IP 后缀范围

- IP-ASN

  - 匹配 IP 所属 ASN

- GEOIP

  - 匹配 IP 所属国家代码

- SRC-GEOIP

  - 匹配来源 IP 所属国家代码

- SRC-IP-ASN

  - 匹配来源 IP 所属 ASN

- SRC-IP-CIDR

  - 匹配来源 IP 地址范围

- SRC-IP-SUFFIX

  - 匹配来源 IP 后缀范围

## 端口规则
1.DST-PORT

匹配请求目标端口范围

2.SRC-PORT

匹配请求来源端口范围

3.IN-PORT

匹配入站端口,可用端口范围
## 进程规则
- PROCESS-PATH

  - 使用完整进程路径匹配

- PROCESS-PATH-REGEX

  - 使用进程路径正则表达式匹配

- PROCESS-NAME

  - 使用进程匹配，在Android平台可以匹配包名

4.PROCESS-NAME-REGEX

使用进程名称正则表达式匹配，在Android平台可以匹配包名
## 其他规则

1.IN-TYPE

匹配入站类型

2.IN-USER

匹配入站用户名，支持使用 / 分隔多个用户名

3.IN-NAME

匹配入站名称

- UID

  - 匹配 Linux USER ID

- NETWORK

  - 匹配tcp或者udp

- DSCP

  - 匹配DSCP标记 (仅限 tproxy udp 入站)

## 逻辑规则
- AND & OR & NOT

  - 逻辑规则，需要注意括号的使用

- SUB-RULE

  - 匹配至子规则,需要注意括号的使用
## 兜底规则
- MATCH or Final

  - 匹配所有请求，无需条件

