## 1. 自定义 ODM 对象
[SubjectForm](https://github.com/thcpc/pyodm/blob/master/example/custom_odm_factory/custom/subject_form.py)  
[SubjectItem](https://github.com/thcpc/pyodm/blob/master/example/custom_odm_factory/custom/subject_item.py)

## 2. 定义 ODM 对象的配置的XML文件
[custom.xml](https://github.com/thcpc/pyodm/blob/master/example/custom_odm_factory/custom.xml)
- modulePath:class 的 package 路径
- clazz: class 名
## 3. CdiscSpecificationFactory 加载ODM
[example.py](https://github.com/thcpc/pyodm/blob/master/example/custom_odm_factory/example.py)