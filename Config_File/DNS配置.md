# DNS配置

**DNS(Domain Name System/域名系统)**-将人们易于记忆的域名（如 www.example.com）转换为计算机能够理解的IP地址（如 192.0.2.1）。这就像是互联网的“电话簿”，帮助浏览器找到你要访问的网站。
  - [Cloudflare](https://www.cloudflare-cn.com/learning/dns/what-is-a-dns-server/)
  - [百度百科](https://baike.baidu.com/item/%E5%9F%9F%E5%90%8D%E7%B3%BB%E7%BB%9F/2251573)

## 推荐的DNS服务器
- 非加密DNS

| 服务提供商 | IP地址 |
| -- | -- |
| 114 DNS | 114.114.114.114 |
| 阿里(Ali)DNS | 223.5.5.5 |
| 腾讯DNS |  119.29.29.29 |
|  字节跳动(火山引擎)DNS|  180.184.1.1 |
| 360DNS | 101.226.4.6 |

- 加密DNS [服务提供商-加密协议-DNS服务器地址]
  - 阿里(Ali)DNS
    - DOH
      - ```
        https://223.5.5.5/dns-query
        ```
    - DOT
      - ```
        dns.alidns.com
        ```

## 感谢
- [dns.iui.im](https://dns.iui.im/#LOG)
- [国内好用的DNS](https://blog.lindexi.com/post/%E5%9B%BD%E5%86%85%E5%A5%BD%E7%94%A8%E7%9A%84-DNS-%E5%88%97%E8%A1%A8.html)
