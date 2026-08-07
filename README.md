# iNg

自用配置、规则与图标资源。

## 图标清单

- [GeneralIcon.json](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/GeneralIcon.json)
- [AirportIcon.json](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/AirportIcon.json)
- [EmbyIcon.json](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/EmbyIcon.json)
- [FlagIcon.json](https://raw.githubusercontent.com/sunfing/iNg/main/Icons/FlagIcon.json)

添加、删除或重命名 `Icons/*Icons` 中的 PNG 文件后，运行：

```powershell
python tools/sync_icon_manifests.py
python tools/sync_icon_manifests.py --check
```

清单只收录 `.png` 文件，目录中的 `null` 占位文件会被忽略。GitHub Actions
会在相关文件发生变化时检查清单是否同步。
