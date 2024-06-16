# QX全局配置教程和资源
- [Quantumult-X](https://github.com/rencuijian/Quantumult-X)
  - Quantumult X策略、规则、脚本使用教程
## QX规则
- 去掉了IP规则，只在最后加入"GEOIP,CN,DIRECT",防止DNS泄露（？），减少不必要的DNS解析
- IP规则
  - IP-CIDR
    - IP-CIDR,127.0.0.0/8,policy  
  - IP6-CIDR
    - IP6-CIDR,2620:0:2d0:200::7/32,policy 
  - GEOIP（IP地理位置 (国家代码)）
    - GEOIP,CN,DIRECT 
  - IP-ASN（通过IP自治系统编号）
    - IP-ASN,714
- 域名规则-可以用“DOMAIN”
  - HOST（域名 ）
    - HOST,www.google.com,policy
  - HOST-SUFFIX（域名后缀）
    - HOST-SUFFIX,youtube.com,policy
  - HOST-KEYWORD（域名关键字）
  - HOST-WILDCARD（域名通配符）
- 其他规则
  - USER-AGENT
- 兜底规则（全匹配）
  - final 
### 规则来源
- [IOS-Rules](https://github.com/blackmatrix7/ios_rule_script)
### QX规则匹配顺序
- 本地>远程>final
- 不开分流匹配优化：按照在配置中的顺序从上到下，域名类规则>IP类规则
- 开分流匹配优化：host > host-suffix > host-keyword(wildcard) > geoip = ip-cidr (ip6-cidr)> user-agennt
- 远程规则开插入资源：优先级会大于本地规则

