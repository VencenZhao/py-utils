## python小工具

### dependencies 项目依赖
+ python3 [python3.7.3](https://www.python.org/downloads/)
+ GDAL [python地理数据处理环境搭建](https://blog.csdn.net/shaxiaozilove/article/details/78975386)
+ PyMySQL `pip install PyMySQl`
+ numpy `pip install numpy`
+ requests `pip install requests`

### config 配置文件
+ database.ini 数据库链接配置
+ grid.ini 热点网格图层配置

### log 日志文件

### package_block 小网格图层生成工具

### package_coor 坐标转换工具
+ `from package_coor.CoorUtils import CoorUtils`
+ `coor = CoorUtils`
+ `lngAndLat = coor.wgs84_to_gcj02(lng, lat)`
+ 参考 > `package_test/test_coor.py`

### package_db 连接MySQL数据库工具
+ `from package_db.DBUtils import DBUtils`
  + host = 'xxx.xxx.xxx.xxx'
  + username = 'root'
  + password = 'root'
  + port = 3306
  + db = 'DATABASE'
  + conn = DBUtils(host, username, password, port, db);
  + sql = 'select * from tableName;'
  + result = conn.select(sql)
  + print(result)

### package_file 文件操作工具
+ `from package_file.FileUtils import FileUtils`
+ `fileUtils = FileUtils()`
+ `fileUtils.createFile(filePath)`

### package_gdal 图层生成工具
+ `from package_gdal.GDALUtils import GDALUtils`
  + gd = GDALUtils(['lng', 'lat', 'stand_gridid', 'provinceid', 'cityid', 'countyid', 'countyid2'], 0, './', 'polygonWithMinMaxLayer', isGCJ = False)
  + gd.initShapeFile()
  + gd.initShapeFileProperties(result)

### package_grid 热点网格生成工具


### package_highvalue 高值区生成工具(TODO)


### package_log 日志工具


### package_poi 兴趣点生成工具(TODO)


### package_test 测试脚本
+ **test_coor.py** 坐标转换测试
+ **test_gdal.py** 图层生成工具测试
+ **test_gridLayer.py** 热点网格图层生成测试
+ **test_log.py** 日志工具测试
+ **test_mysql.py** 数据库连接及图层生成工具测试
+ **test_package.py** 引入python package测试


### shapefile shapefile存放位置
+ **grid** 热点网格图层
+ **highvalue** 高值区图层 (TODO)
+ **poi** 兴趣点图层 (TODO)# py-utils
