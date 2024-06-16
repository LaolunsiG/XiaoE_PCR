## QX全局配置
- [Quantumult-X](https://github.com/rencuijian/Quantumult-X)
  - Quantumult X策略、规则、脚本使用教程
# QX规则-规则来源：“IOS-Rules”
- 去掉了IP规则，只在最后加入"GEOIP,CN,DIRECT",防止DNS泄露（？），减少不必要的DNS解析
# QX规则匹配顺序
- ▎本地>远程>final
- ▎不开分流匹配优化：按照在配置中的顺序从上到下，域名类规则>IP类规则
- ▎开分流匹配优化：host > host-suffix > host-keyword(wildcard) > geoip = ip-cidr (ip6-cidr)> user-agennt
- ▎远程规则开插入资源：优先级会大于本地规则
  
