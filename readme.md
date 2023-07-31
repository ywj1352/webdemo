
# 结构

- controller
  - __init__.py 必须
- repository
  - 链接 数据库操作
- service
  - 聚合 repository 和 manager 接口 做聚合操作
- manager 
  - 请求第三方接口
- common 
  - 放一些 工具类
- config
  - 做一些需要配置的操作