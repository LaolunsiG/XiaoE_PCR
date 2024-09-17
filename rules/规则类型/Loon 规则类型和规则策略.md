# Loon 规则类型和规则策略
## Loon 规则类型
### 规则集
- RULE-SET：匹配规则集内容。规则集的内容需包含规则类型，如"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Apple/Apple.list"。（兼容仅包含IP地址且不带规则类型的规则集）
- DOMAIN-SET：匹配域名集内容。域名集的内容不包含规则类型，如"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Apple/Apple_Domain.list"。

### 单个规则
\# 域名规则
- DOMAIN-SUFFIX：匹配请求域名的后缀。如“DOMAIN-SUFFIX,example.com,DIRECT”可以匹配到“a.example.com、a.b.example.com”。
- DOMAIN-KEYWORD：匹配请求域名的关键词。如“DOMAIN-KEYWORD,exa,DIRECT”可以匹配到“a.example.com、a.b.example.com”。
- DOMAIN：匹配请求的完整域名。如“DOMAIN,www.example.com,DIRECT”只能匹配到“www.example.com”。

\# IP规则
- GEOIP：匹配IP数据库。如“GEOIP,CN,DIRECT”可以匹配到归属地为CN的IP地址。
- IP-CIDR：匹配IPv4或IPv6地址。如“IP-CIDR,192.168.1.0/24,DIRECT”可以匹配到IP段“192.168.1.1～192.168.1.254”。当域名请求遇到IP类规则时，Shadowrocket会向本地DNS服务器发送查询请求，以判断主机IP是否匹配规则。若IP类规则加“no-resolve”(如：IP-CIDR,172.16.0.0/12,DIRECT,no-resolve)，则域名请求将会跳过此规则，不会触发本地DNS查询。
- IP-ASN：匹配IP地址隶属的ASN编号。如"IP-ASN,56040,DIRECT"可以匹配到属于China Mobile Communications Corporation网络的IP地址。

\# 逻辑规则
- AND：逻辑规则，与规则。如“AND,((DOMAIN,www.example.com),(DST-PORT,123)),DIRECT”可以匹配到“www.example.com:123”。
- NOT：逻辑规则，非规则。如“NOT,((DST-PORT,123)),DIRECT”可以匹配到除了“123”端口的其他所有请求。
- OR：逻辑规则，或规则。如“OR,((DST-PORT,123),(DST-PORT,456)),DIRECT”可以匹配到“123”或“456”端口的所有请求。

\# 其他规则
- USER-AGENT：匹配用户代理字符串，支持使用通配符“*”。如“USER-AGENT,MicroMessenger*,DIRECT”可以匹配到“MicroMessenger Client”。
- URL-REGEX：匹配URL正则式。如“URL-REGEX,^https?://.+/item.+,REJECT”可以匹配到“https://www.example.com/item/abc/123”。
- SCRIPT：匹配脚本名称。
- DST-PORT：匹配目标主机名的端口号。如“DST-PORT,443,DIRECT”可以匹配到443目标端口。

\# 兜底规则
- FINAL：兜底策略。如“FINAL,PROXY”表示当其他所有规则都匹配不到时才使用FINAL规则的策略。
  
## Loon 内置规则策略：
### 直连
- DIRECT：直连。连接不经过任何代理服务器。
### 拒绝
- REJECT：拒绝 返回200 响应空的响应体)
- REJECT-IMG：拒绝 返回200和一个 1px GIF 的响应体)
- REJECT-DICT：拒绝 返回200和内容为空的 JSON 的响应体)
- REJECT-ARRY ：拒绝 返回200和一个内容为空的 JSON 数组)
- REJECT-DROP：拒绝 拒绝并丢弃请求，且不会返回任何响应。因为部分程序有着十分暴力的重试逻辑，连接失败后会立刻进行重试，导致请求风暴)
### 代理
- 除此之外，规则策略还可以选择「代理分组」、「订阅名称」、「分组」、「节点」。
