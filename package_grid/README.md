## 热点网格

### 热点网格各表
+ T_GRID_CURRENT_HOT_GROUP 部级热点网格  region_level = 0
+ T_GRID_CURRENT_HOT_GROUP_PROVINCE 省级别热点网格 region_level = 1
+ T_GRID_CURRENT_HOT_GROUP_CITY 城市级别热点网格 region_level = 2
+ T_GRID_CURRENT_HOT_GROUP_COUNTY 区县级别热点网格 region_level = 3
+ T_GRID_CURRENT_HOT_GROUP_REGION 跨区县热点网格 

### 配置文件
+ config/grid.ini
+ [PROPERTY] 参数配置
    properties: lng,lat,gridid,provinceid,cityid,countyid,countyid2 图层参数配置
    filePath: {root_dir}{os.sep}shapefile{os.sep}grid 生成shapefile文件存储位置
+ [LEVEL{0-3}] 图层级别配置
    layerName: grid_level{0-3} 图层名称
    level: {0-3} region_level级别
    tableName: 表名称
+ [SQL]
    ```
      SELECT  
        a.LONGITUDE AS lng,  
        a.LATITUDE AS lat,  
        a.STAND_GRIDID AS gridid,  
        a.PROVINCEID AS provinceid,  
        a.CITYID AS cityid,  
        a.COUNTYID AS countyid,  
        b.COUNTY_ID AS countyid2,  
        a.LONGITUDE_DOWN_LEFT AS minlng,  
        a.LATITUDE_DOWN_LEFT AS minlat,  
        a.LONGITUDE_UP_RIGHT AS maxlng,  
        a.LATITUDE_UP_RIGHT AS maxlat  
      FROM  
        {} a  
      LEFT JOIN   
        T_GRID_CURRENT_HOT_GROUP_REGION b  
      ON  
        a.STAND_GRIDID = b.STAND_GRIDID  
      WHERE  
        a.SELECTED_FLAG = 1;  
    ```

### 查询SQL
1. 部级热点网格
    layerName: grid_level0, grid_level0_gcj
    ```
    SELECT 
      a.LONGITUDE AS lng,
      a.LATITUDE AS lat,
      a.STAND_GRIDID AS gridid,
      a.PROVINCEID AS provinceid,
      a.CITYID AS cityid,
      a.COUNTYID AS countyid,
      b.COUNTY_ID AS countyid2,
      a.LONGITUDE_DOWN_LEFT AS minlng,
      a.LATITUDE_DOWN_LEFT AS minlat,
      a.LONGITUDE_UP_RIGHT AS maxlng,
      a.LATITUDE_UP_RIGHT AS maxlat
    FROM
      T_GRID_CURRENT_HOT_GROUP a
    LEFT JOIN 
      T_GRID_CURRENT_HOT_GROUP_REGION b
    ON
      a.STAND_GRIDID = b.STAND_GRIDID
    WHERE 
      a.SELECTED_FLAG = 1;
    ```
2. 省级热点网格
    layerName: grid_level1, grid_level1_gcj
    ```
    SELECT 
      a.LONGITUDE AS lng,
      a.LATITUDE AS lat,
      a.STAND_GRIDID AS gridid,
      a.PROVINCEID AS provinceid,
      a.CITYID AS cityid,
      a.COUNTYID AS countyid,
      b.COUNTY_ID AS countyid2,
      a.LONGITUDE_DOWN_LEFT AS minlng,
      a.LATITUDE_DOWN_LEFT AS minlat,
      a.LONGITUDE_UP_RIGHT AS maxlng,
      a.LATITUDE_UP_RIGHT AS maxlat
    FROM
      T_GRID_CURRENT_HOT_GROUP_PROVINCE a
    LEFT JOIN 
      T_GRID_CURRENT_HOT_GROUP_REGION b
    ON
      a.STAND_GRIDID = b.STAND_GRIDID
    WHERE 
      a.SELECTED_FLAG = 1;
    ```
3. 市级热点网格
    layerName: grid_level2, grid_level2_gcj
    ```
    SELECT 
      a.LONGITUDE AS lng,
      a.LATITUDE AS lat,
      a.STAND_GRIDID AS gridid,
      a.PROVINCEID AS provinceid,
      a.CITYID AS cityid,
      a.COUNTYID AS countyid,
      b.COUNTY_ID AS countyid2,
      a.LONGITUDE_DOWN_LEFT AS minlng,
      a.LATITUDE_DOWN_LEFT AS minlat,
      a.LONGITUDE_UP_RIGHT AS maxlng,
      a.LATITUDE_UP_RIGHT AS maxlat
    FROM
      T_GRID_CURRENT_HOT_GROUP_CITY a
    LEFT JOIN 
      T_GRID_CURRENT_HOT_GROUP_REGION b
    ON
      a.STAND_GRIDID = b.STAND_GRIDID
    WHERE 
      a.SELECTED_FLAG = 1;
    ```
4. 区县级热点网格
    layerName: grid_level3, grid_level3_gcj
    ```
    SELECT 
      a.LONGITUDE AS lng,
      a.LATITUDE AS lat,
      a.STAND_GRIDID AS gridid,
      a.PROVINCEID AS provinceid,
      a.CITYID AS cityid,
      a.COUNTYID AS countyid,
      b.COUNTY_ID AS countyid2,
      a.LONGITUDE_DOWN_LEFT AS minlng,
      a.LATITUDE_DOWN_LEFT AS minlat,
      a.LONGITUDE_UP_RIGHT AS maxlng,
      a.LATITUDE_UP_RIGHT AS maxlat
    FROM
      T_GRID_CURRENT_HOT_GROUP_COUNTY a
    LEFT JOIN 
      T_GRID_CURRENT_HOT_GROUP_REGION b
    ON
      a.STAND_GRIDID = b.STAND_GRIDID
    WHERE 
      a.SELECTED_FLAG = 1;
    ```
    