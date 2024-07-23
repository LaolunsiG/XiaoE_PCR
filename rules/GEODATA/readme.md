# GEODATA
> 比较重要吧,不懂事什么东西
- 地理位置相关的数据，通常用于根据地理位置管理网络流量。

**DAT 和 MMDB 文件**
  - 是存储 IP 地址和地理位置信息的数据文件，其中 MMDB 是一种更高效的格式，广泛应用于需要快速查询和精确地理位置信息的场景中。

## 第三方Geodata数据库
- 数据类型-文件格式
### GEOIP-基于 IP 地址的地理位置数据库。主要用于根据 IP 地址的地理位置来路由或限制流量。
#### mmdb
- [Hackl0us-(GeoIP2-CN)-Country](https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb)
  ```
  https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb
  ```
- [NobyDa-geoip-(Private-GeoIP-CN)](https://raw.githubusercontent.com/NobyDa/geoip/release/Private-GeoIP-CN.mmdb)
  ```
  https://raw.githubusercontent.com/NobyDa/geoip/release/Private-GeoIP-CN.mmdb
  ```
- [Loyalsoldier-geoip-(Country-only-cn-private)](https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country-only-cn-private.mmdb)
  ```
  https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country-only-cn-private.mmdb
  ```
#### dat
- [Loyalsoldier-(v2ray-rules-dat)-geoip](https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/geoip.dat)
  ```
   https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/geoip.dat
   ```
### GEOSITE-基于域名的地理位置和类别分类数据库。主要用于根据域名类别来路由或管理流量。
#### dat
- [Loyalsoldier-(v2ray-rules-dat)-geosite](https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/geosite.dat)
  ```
  https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/geosite.dat
  ```
### ASN
- [Loon0x00-GeoLite2-ASN](https://gitlab.com/Loon0x00/loon_data/-/raw/main/geo/GeoLite2-ASN.mmdb)
  ```
  https://gitlab.com/Loon0x00/loon_data/-/raw/main/geo/GeoLite2-ASN.mmdb
  ```
