# 代理软件配置文件示例
> !! 注意不要将 **"[MITM]"配置** 的证书分享给他人-[什么是 MITM](https://zh.m.wikipedia.org/wiki/%E4%B8%AD%E9%97%B4%E4%BA%BA%E6%94%BB%E5%87%BB)
- 这些是示例配置文件，请不要直接使用，自己修改配置文件后使用，我的配置不一定适合你，所以自己配置一个配置文件才是最好的选择。

！！在配置之前先了解代理工具的工作流程，以防出现，配置之后，还不如不配置的情况发生。

## 模块化部分配置
1. [DNS配置](https://github.com/LaolunsiG/XiaoE_PCR/blob/main/Config_File/DNS%E9%85%8D%E7%BD%AE.md)
2. 节点配置
   - [节点的正则表达式](https://github.com/LaolunsiG/XiaoE_PCR/blob/main/%E6%B5%8B%E9%80%9F%E9%93%BE%E6%8E%A5%E5%9C%B0%E5%9D%80.md)
   - [节点的测速链接](https://github.com/LaolunsiG/XiaoE_PCR/blob/main/%E6%B5%8B%E9%80%9F%E9%93%BE%E6%8E%A5%E5%9C%B0%E5%9D%80.md)

## 各个软件的配置文件所用的配置文件格式
- [INI](https://blog.csdn.net/a123441/article/details/90668032)-CSDN

| 软件 | 配置文件格式 | {单行}注释符号 |
| -- | :--: | :--: |
| Sing-Box | json  |  |
| Clash_Old  | yaml & json | # |
| Clash_Meta  | yaml & json | # |
| Stash | yaml | # |
| Surfboard | yaml | |
| Surge | INI | # |  
| Loon | INI | # | 
| Shadowrocket | INI | # | 
| LanceX | INI | # | 
| Quantumult_X | INI | # | 

 
## Clash_Old
### Clash_Wiki(知识库)
- [Clash_Old](https://clash.wiki/)
### Clash_Config(配置文件)
- [Clash_for_Android_Sub-Test.yml](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Clash_Old/Clash_for_Android_Sub-Test.yml)
- [XiaoE_CFA_Test.yml](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Clash_Old/XiaoE_CFA_Test.yml)

## Clash_Meta
### Clash_Meta_Wiki(知识库)
- [Clash_Meta](https://wiki.metacubex.one/)
### Clash_Meta_Config(配置文件)
- [Clash_Meta_Old](https://raw.githubusercontent.com/LaolunsiG/XiaoE-PCR/main/Config_File/Clash_Meta/Clash_Meta_Old.yaml)
- [Clash_Meta_New](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Clash_Meta/XiaoE_Clash_Meta.yaml)

## LanceX
### LanceX_Wiki(知识库)
### LanceX_Config(配置文件)
- [XiaoE_LanceX](https://raw.githubusercontent.com/LaolunsiG/XiaoE-PCR/main/Config_File/LanceX/XiaoE%E7%9A%84LanceX%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.conf)

## Loon
### Loon_Wiki(知识库)
- [KeLee8-Loon_tutorial](https://github.com/KeLee8/Loon-tutorial)-KeLee8
- [Loon0x00](https://github.com/Loon0x00/LoonManual/tree/master)-官方
### Loon_Config(配置文件)
- [XiaoE_Loon](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Loon/XiaoE_Loon.conf)

## Quantumult_X
### Quantumult_X_Wiki(知识库)
- [Quantumult X 不完全教程](https://www.notion.so/kopshawn/Quantumult-X-1d32ddc6e61c4892ad2ec5ea47f00917)-Quantumult X 不完全教程
- [Quantumult X Wiki Book](https://qx.atlucky.me/)-Lucky,整点猫咪和INAISI
### Quantumult_X_Config(配置文件)
- [XiaoE_Quantumult_X](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Quantumult_X/XiaoE_Quantumult_X.yaml)

## Shadowrocket
### Stash_Wiki(知识库)
- [Shadowrocket](https://github.com/wlxuf/Shadowrocket)
### Shadowrocket(配置文件)
- [XiaoE_Shadowrocket](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Shadowrocket/XiaoE_Shadowrocket.conf)
  - **此配置文件需要自己配置订阅节点**

## Stash
### Stash_Wiki(知识库)
- [Stash_Wiki](https://stash.wiki/)
### Stash_Config(配置文件)
- [XiaoE_Stash](https://raw.githubusercontent.com/LaolunsiG/XiaoE_PCR/main/Config_File/Stash/XiaoE_Stash.yaml)

## 感谢以下配置
- Clash/Clash_Meta
  - [Lucky配置](https://raw.githubusercontent.com/As-Lucky/Lucky/main/Lucky-ClashVerge.yaml)
  - [可莉示例配置](https://gitlab.com/lodepuly/vpn_tool/-/tree/master/Tool/Clash/Config)
  - [Clash莫离配置](https://github.com/Moli-X/Resources/raw/main/Clash/Clash.yml)
  - [whatshub.top](https://whatshub.top/config/stash-auto.yaml)
- Loon
  - [Copyright配置](https://github.com/SANYIMOE/Quan_Shado_Conf)
  - [Loon 精简配置](https://raw.githubusercontent.com/HoCooo/Loon/main/LoonLite.conf)
  - [懒人配置](https://raw.githubusercontent.com/wlxuf/Shadowrocket/main/lazy_group.conf)
  - [可莉配置-进阶配置](https://gitlab.com/lodepuly/vpn_tool/-/raw/master/Tool/Loon/Config/zh-CN/Loon_Sample_Configuration_By_iKeLee.conf)
- Shadowrocket
  - [Lucky-Shadowrocket配置](https://raw.githubusercontent.com/As-Lucky/Lucky/main/Lucky-Shadowrocket.conf)
  - [whatshub.top-懒人配置](https://whatshub.top/config/shadowrocket_basic.conf) 
- Stash
  - [Infatuation-Fei配置](https://raw.githubusercontent.com/Infatuation-Fei/rule/main/Stash/%E9%85%8D%E7%BD%AE%E6%A8%A1%E6%9D%BF/Config%20for%20Stash.yaml)
  - Lucky/Repcz配置
    - [Stash_lite](https://raw.githubusercontent.com/Repcz/Tool/X/Stash/Stash_lite.yaml)
    - [Stash](https://raw.githubusercontent.com/Repcz/Tool/X/Stash/Stash.yaml)
  - [Stash可莉配置](https://github.com/Moli-X/Resources/raw/main/Clash/Clash.yml)
  - [懒人配置](https://whatshub.top/config/stash-auto.yaml)
  - [Coldvvater配置](https://raw.githubusercontent.com/Coldvvater/Mononoke/master/Stash/Config/Evolve.yaml)
  - [jnlaoshu配置](https://raw.githubusercontent.com/jnlaoshu/MySelf/main/Stash/Config.yaml)


