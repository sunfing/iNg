# iNg

iNg 是一个自用网络配置、分流规则与配套静态资源仓库，主要整理
Clash/Mihomo、Surge 配置，以及可独立引用的规则和图标资源。

更新频道：[i_chl](https://t.me/i_chl)

## 仓库内容

| 目录 | 内容 |
| --- | --- |
| [`Config/`](Config/) | Clash/Mihomo 与 Surge 配置模板 |
| [`Rules/`](Rules/) | 可独立引用的分流规则，提供不同客户端所需格式 |
| [`Icons/`](Icons/) | 机场、通用、旗帜等 PNG 图标及 JSON 清单 |
| [`Monitor/`](Monitor/) | 监控展示等场景使用的静态图片 |

## 配置

- [Clash/Mihomo 配置](https://raw.githubusercontent.com/sunfing/iNg/main/Config/ConfigForClash)：包含远程代理集、DNS、流量嗅探、TUN、策略组与远程规则集。
- [Surge 配置](https://raw.githubusercontent.com/sunfing/iNg/main/Config/ConfigForSurge)：包含通用设置、策略组、分流规则与 URL Rewrite。

配置按 AI 服务、流媒体、社交、下载、开发平台、云服务、游戏平台和地区节点等场景进行分组。两份配置均包含较完整的行内注释，使用前请先阅读对应说明，并根据自己的客户端版本和网络环境调整。

## 规则

- [AIGC `.yaml`](https://raw.githubusercontent.com/sunfing/iNg/main/Rules/AIGC/A_AIGC.yaml)：供 Clash/Mihomo `rule-providers` 使用的 classical YAML 规则集。
- [AIGC `.list`](https://raw.githubusercontent.com/sunfing/iNg/main/Rules/AIGC/A_AIGC.list)：供 Surge `RULE-SET` 使用的文本规则集。

两种格式维护同一组 AIGC 服务域名，并分别被仓库中的 Clash/Mihomo 与 Surge 配置引用。

## 图标

- [Airport Icon](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/AirportIcon.json)
- [General Icon](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/GeneralIcon.json)
- [Flag Icon](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/FlagIcon.json)
- [Emby Icon](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/EmbyIcon.json)（预留清单）

图标清单使用统一的 `name`、`description` 和 `icons` 结构。单个图片的 Raw 地址格式为：

```text
https://raw.githubusercontent.com/sunfing/iNg/main/Icons/<目录>/<文件名>.png
```

## 使用注意

- 本仓库按个人需求维护，配置不是开箱即用的节点订阅；请填写自己的订阅地址并检查策略组。
- YAML 对缩进敏感；修改 Clash/Mihomo 配置后，请先完成 YAML 解析和客户端配置检查。
- 配置依赖部分远程规则与静态资源，上游地址变化或网络不可达可能影响更新。
- 公开分享或提交修改前，请检查并移除订阅链接、控制器/API 口令及其他私有参数。

## License

仓库原创内容遵循 [MIT License](LICENSE)。第三方素材遵循各自的授权声明；旗帜素材许可见
[`Icons/FlagIcons/LICENSE.lipis-flag-icons.txt`](Icons/FlagIcons/LICENSE.lipis-flag-icons.txt)。
