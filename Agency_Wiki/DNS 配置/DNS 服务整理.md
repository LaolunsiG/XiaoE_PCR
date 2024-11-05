# DNS 服务整理

## 国内 DNS 服务
|     |                 |
| --- | --------------- |
|     | 182.254.118.118 |

| 服务提供商      | DNS 类型 | 服务1                                                                                                                           | 服务2                                                                 |
| ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 阿里(Ali)DNS | UDP    | 223.5.5.5                                                                                                                     | 233.6.6.6                                                           |
|            | DOH    | https://223.5.5.5/dns-query<br>https://dns.alidns.com/dns-query                                                               | https://223.6.6.6/dns-query                                         |
|            | DOT    |                                                                                                                               | tls://dns.alidns.com:853                                            |
| 腾讯DNS      | UDP    | 119.29.29.29 <br>119.28.28.28                                                                                                 | 182.254.116.116<br>182.254.118.118                                  |
|            | DOH    | https://doh.pub/dns-query<br>https://1.12.12.12/dns-query<br>https://120.53.53.53/dns-query <br>https://sm2.doh.pub/dns-query |                                                                     |
|            | DOT    |                                                                                                                               | tls://dot.pub:853<br>tls://1.12.12.12:853<br>tls://120.53.53.53:853 |

## 国外 DNS 服务
### 国内可以直连使用的 DNS 服务


| 服务提供商      | DNS 类型 | 服务1                                                                                 | 服务2                                       | 服务3                                |     |
| ---------- | ------ | ----------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------- | --- |
| 台湾Quad 101 | UDP    | 101.101.101.101                                                                     | 101.102.103.104                           |                                    |     |
|            | DOH    | https://dns.twnic.tw/dns-query - 不可用                                                |                                           |                                    |     |
| Google     | udp    | 8.8.8.8                                                                             | 8.8.4.4                                   |                                    |     |
|            | DOH    | https://dns.google/dns-query - 不可用                                                  |                                           | https://dns64.dns.google/dns-query |     |
|            | DOT    |                                                                                     | tls://8.8.4.4:853<br>tls://dns.google:853 |                                    |     |
|            | DOQ    |                                                                                     |                                           |                                    |     |
| Cloudflare | UDP    | 1.1.1.1                                                                             | 1.0.0.1                                   |                                    |     |
|            | DOH    | - https://1.1.1.1/dns-query<br>- https://cloudflare-dns.com/dns-query               | - https://1.0.0.1/dns-query               |                                    |     |
|            | DOT    | tls://one.one.one.one:853 - 不可用<br>tls://1dot1dot1dot1.cloudflare-dns.com:853 - 不可用 |                                           |                                    |     |
| 其他私人服务     | DOH    | https://doh.apad.pro/dns-query - 不可用                                                |                                           |                                    |     |
 

