## Step1. 定义 ODM 配置对象 XML 文件
[mapper.xml](https://github.com/thcpc/pyodm/blob/master/example/database/mappers/mapper.xml) <br>
文件名: 可自定义 <br>
属性说明 <br>
1. 元素名:表明的ODM对象的层级
因为数据库查询的结果，结果是平行的，但 ODM对象为树形结构，为了表述这个树形结构，所以定义通过XML描述结构关系
2. ODMClass: 对应的ODM 对象
3. 其它属性：Key对应 ODM 对象的Attribute， Value 对应的 数据库查询的字段

## Step2. 定义数据库映射对象
[subject_mapper.py](https://github.com/thcpc/pyodm/blob/master/example/database/mappers/subject_mapper.py)

## Step3. 定义数据库源
[subject_data_resource.py](https://github.com/thcpc/pyodm/blob/master/example/database/subject_data_resource.py)

## Step4. 生成 ODM 对象
[main.py](https://github.com/thcpc/pyodm/blob/master/example/database/main.py)