# paranoma python sdk

## 登录

- 导入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.login import login_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 在使用sdk时必须先登录账号

```
    try:        httpProfile = HttpProfile()       
        httpProfile.endpoint = "192.168.31.149:8089"       
        httpProfile.reqTimeout = 30       
        lg = login_client.LoginClient(httpProfile)       
        req = models.CreateLoginRequest()       
        req.username = "admin"       
        req.password = "adminPassword"       
        resp = lg.login(req)       
        return resp   
    except PanSDKException as err:       
        print(err)
```

- 用户登出

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    httpProfile.reqTimeout = 30   
    lg = login_client.LoginClient(httpProfile)   
    resp = lg.logout()   
    print(resp)
except PanSDKException as err:   
    print(err)
```

## 用户管理

- 导入依赖包

```
from panclient.common.exception.pan_sdk_exception
import PanSDKExceptionfrom panclient.user
import user_client, modelsfrom panclient.common.profile.http_profile import HttpProfile
```

- 获取当前用户信息

```
    try:       
        httpProfile = HttpProfile()       
        httpProfile.endpoint = "192.168.31.149:8089"       
        uc = user_client.UserClient(httpProfile)       
        resp = uc.get_user_me()       
        print(resp)   
    except PanSDKException as err:       
        print(err)
```

- 获取用户列表

```
    try: 
        httpProfile = HttpProfile()       
        httpProfile.endpoint = "192.168.31.149:8089"       
        uc = user_client.UserClient(httpProfile)       
        resp = uc.get_user()       
        print(resp)   
    except PanSDKException as err:       
        print(err)

```

- 获取用户角色

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    uc = user_client.UserClient(httpProfile)   
    resp = uc.get_roles()   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 获取用户

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    uc = user_client.UserClient(httpProfile)   
    resp = uc.get_user()   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 删除用户

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    req = models.CreateUserRequest()   
    req.userId = "USER_83c2bdb867c448ed8488bdea5b124c1f"   
    uc = user_client.UserClient(httpProfile)   
    resp = uc.del_user(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 增加用户

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    req = models.CreateUserRequest()   
    req.username = "timmy"   
    req.password = "password"   
    req.emailAddress = "timmy.wang@ebistrategt.com"   
    req.displayname = "timmy"   
    req.roles = ["2", "1"]   
    uc = user_client.UserClient(httpProfile)   
    resp = uc.add_user(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```
## 设置

- 导入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.settings import settings_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 设置时间

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    req = models.CreateSettingTime()   
    req.id = "USER_1"   
    req.query = "60"   
    req.findPath = "120"   
    uc = settings_client.SettingClient(httpProfile)   
    uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"                       uc._panorama_workspace_id="WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.set_time(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

## 数据集

- 导入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.dataset import dataset_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 获取数据集

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    uc = dataset_client.DataSetClient(httpProfile)   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.get_dataset()   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 删除数据集

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    req = models.CreateGetDataset()   
    req.id = "4a7f87df89aa49d9be39393e16f69759"   
    uc = dataset_client.DataSetClient(httpProfile)   
    uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.del_dataset(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 删除数据集数据

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    req = models.CreateGetDataset()   
    req.id = "cac90168b3a5475c98b3f79ce775fbe2"   
    uc = dataset_client.DataSetClient(httpProfile)   
    uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.del_dataset_data(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 增加数据集

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    req = models.CreateDataset()   
    req.displayType = True   
    req.title = "tim_test"   
    req.remark = "tim test"   
    req.rolesId = ["1", "2"]   
    req.schemaIds = ["http://panorama.org#root", "http://panorama.org/longRunningProcess#longRunningProcess"]   
    req.userIds = ["USER_1", "USER_0919d2fccd244e98ad890b79163c4621"]   
    uc = dataset_client.DataSetClient(httpProfile)   
    uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.add_dataset(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

## schema

- 导入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.schema import schema_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 获取schema

```
try:   
    httpProfile = HttpProfile()   
    httpProfile.endpoint = "192.168.31.149:8089"   
    uc = schema_client.SchemaClient(httpProfile)   
    resp = uc.get_schema()   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 修改Schema的concept

```
try:   
    json =
'''{"displayName":"testSchema2","color":"#2685D9","parentConcept":"panorama#lol/testSchema2","glyphIconHref":"img/glyphicons/glyphicons_091_adjust@2x.png","title":"panorama#lol/testSchema2","id":"panorama#lol/testSchema2"}'''   
    req = models.CreateSchemaConcept()   
    req.from_json_string(json_str=json)   
    hp = HttpProfile()   
    hp.endpoint = "192.168.31.149:8089"   
    uc = schema_client.SchemaClient(hp)   
    uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.mod_schema_concept(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 获取所有数据表

```
try:   
    hp = HttpProfile()   
    hp.endpoint = "192.168.31.149:8089"   
    uc = schema_client.SchemaClient(hp)   
    uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.get_all_db_table()   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 设置自动映射

```
try:   
    req = models.CreateAutoMapping()   
    req.id = "ff8081816957333e01695737cb560000"   
    hp = HttpProfile()   
    hp.endpoint = "192.168.31.149:8089"   
    uc = schema_client.SchemaClient(hp)   
    uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"   
    resp = uc.auto_mapping(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

- 创建系统schema

```
try:   
    req = models.CreateSystemSchema()   
    req.dataJson = '''[{"title":"panorama#tim_测试/access","id":"panorama#tim_测试/access","color":"rgb(216,178,137)","glyphIconHref":"resource?id=static/images/icons/Thing.png","displayName":"access","instance":"gogs","dbId":"ff8081816957333e01695737cb560000","table":"access","object":"access","properties":[{"displayName":"id","dataType":"integer","displayExpression":"","entityImage":false,"predicate":"id","object":"id","primaryKey":true,"index":false,"objectOrDefault":"id"}'''   
    req.dataSet = "962db4e18d434a3bac12416a0435384f"   
    hp = HttpProfile()   
    hp.endpoint = "192.168.31.149:8089"   
    uc = schema_client.SchemaClient(hp)   
    resp = uc.create_system_schema(req)   
    print(resp)
except PanSDKException as err:   
    print(err)
```

## 数据导入

- 引入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.importdata import import_client, models
from panclient.common.profile.http_profile import HttpProfile
```

### 数据库导入

#### 获取所有数据库的配置信息
```angular2
def test_get_database_config():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        uc = import_client.ImportClient(hp)
        resp = uc.get_database_config()
        print(resp)
    except PanSDKException as err:
        print(err)
```


#### 保存或更新数据库配置信息

```angular2
def test_save_database_config():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseConfig()
        req.id = "abc123"
        req.dbName = "jira_postgres"
        req.dbRemark = "jira 数据2"
        req.adapter = "PostgreSQL"
        req.host = "192.168.31.226"
        req.port = "5555"
        req.dbInstanceName = "postgres"
        req.dbUser = "postgres"
        req.dbPassword = "abc123"
        req.secondary = "public"
        req.show = True
        req.csvRemote = True
        uc = import_client.ImportClient(hp)
        resp = uc.save_database_config(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```


#### 删除数据库配置信息
```
def test_delete_database_config():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseConfig()
        req.id = "ff8081816ecede6e016ecee0ce4d0001"
        uc = import_client.ImportClient(hp)
        resp = uc.delete_database_config(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

#### 测试连接数据库
```angular2
def test_ping_database_test():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseConfig()
        req.id = "40289f546a5388d0016a5391bbc50000"
        req.dbName = "didi"
        req.dbRemark = "didi_analysis"
        req.adapter = "MySQL"
        req.host = "192.168.31.226"
        req.port = "33066"
        req.dbInstanceName = "didi_analysis"
        req.dbUser = "root"
        req.dbPassword = "aasgzmysql"
        uc = import_client.ImportClient(hp)
        resp = uc.ping_database_test(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```


 #### 获取外部数据库全部的表和表的字段
 ```python
def test_get_out_database_info():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseConfig()
        req.id = "ff8081816ecede6e016ecee0ce4d0001"
        uc = import_client.ImportClient(hp)
        resp = uc.get_out_database_info(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

 #### 获取所有数据库和数据表信息
```python
def test_get_all_database():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_all_database()
        print(resp)
    except PanSDKException as err:
        print(err)
```

 #### 创建Schema,生成默认的映射.
 ```python
def test_generate_schema_map():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseConfig()
        req.id = "40289f546a5388d0016a5391bbc50000"
        uc = import_client.ImportClient(hp)
        resp = uc.generate_schema_map(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```python

#### 根据连接ID获取全部映射
 ```python
def test_get_schema_map():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseSchemaConfig()
        req.connectId = "40289f546a5388d0016a5391bbc50000"
        uc = import_client.ImportClient(hp)
        resp = uc.get_schema_map(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

#### 修改映射关系
 ```python
def test_mod_schema_map():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseSchemaConfig()
        req.rawStr = """
        {
    "entityId": "ff8081816ec4c40d016ec4c67758001f",
    "primaryKey": "id",
    "sortRule": "id",
    "tableName": "list",
    "conceptId": "panorama_dev.gwyn.list",
    "connectId": "40289f546a5388d0016a5391bbc50000",
    "properties": [
      {
        "id": "ff8081816ec4c40d016ec4c677580020",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "fieldName": "entry_id",
        "fieldType": "string",
        "propertyId": "entry_id",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true
      },
      {
        "id": "ff8081816ec4c40d016ec4c677590021",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "fieldName": "g_no",
        "fieldType": "string",
        "propertyId": "g_no",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true
      },
      {
        "id": "ff8081816ec4c40d016ec4c677590022",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "fieldName": "good_co",
        "fieldType": "string",
        "propertyId": "good_co",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true
      },
      {
        "id": "ff8081816ec4c40d016ec4c6775a0023",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "fieldName": "rmb",
        "fieldType": "string",
        "propertyId": "rmb",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true
      },
      {
        "id": "ff8081816ec4c40d016ec4c6775a0024",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "fieldName": "good_name",
        "fieldType": "string",
        "propertyId": "good_name",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true
      },
      {
        "id": "ff8081816ec4c40d016ec4c6775b0025",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "fieldName": "id",
        "fieldType": "string",
        "propertyId": "id",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true
      }
    ],
    "edges": [
      {
        "tcemId": "ff8081816ec4c40d016ec4c6775b0026",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "edgeName": "panorama_dev.gwyn.head",
        "startTable": "list",
        "startField": "entry_id",
        "endTable": "head",
        "endField": "entry_id",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true,
        "id": "ff8081816ec4c40d016ec4c6775b0026"
      },
      {
        "tcemId": "ff8081816ec4c40d016ec4c6775c0027",
        "tcmId": "ff8081816ec4c40d016ec4c67758001f",
        "edgeName": "panorama_dev.gwyn.goods",
        "startTable": "list",
        "startField": "good_co",
        "endTable": "goods",
        "endField": "good_co",
        "createTime": "1970-01-01T12:02:51.352",
        "valid": true,
        "id": "ff8081816ec4c40d016ec4c6775c0027"
      }
    ]
  }
    """
        uc = import_client.ImportClient(hp)
        resp = uc.mod_schema_map(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```
#### 导出schema文件
 ```python
def test_export_schema_map():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.10.113:8186"
        req = models.DatabaseSchemaConfig()
        req.connectId = "40289f546a5388d0016a5391bbc50000"
        uc = import_client.ImportClient(hp)
        resp = uc.export_schema_map(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

#### 导入数据库数据
 ```python
def test_import_database_data():
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.31.195:8186"
        req = models.DatabaseSchemaConfig()
        req.rawStr = """
        {
    "importType": "database",
    "paramMap": {
        "selectedMappingIds": [
            "ff8081816ecaecf8016ecaef006b0028",
            "ff8081816ecaecf8016ecaef018b002f",
            "ff8081816ecaecf8016ecaef02c80032",
            "ff8081816ecaecf8016ecaef04880034",
            "ff8081816ecaecf8016ecaef05a70047"
        ],
        "loadOption": "duplicate"
    }
}
        """
        uc = import_client.ImportClient(hp)
        resp = uc.import_database_data(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

### rdf导入

- 获取rdf映射信息

```
    try:
        req = models.RdfMapping()
        req.dataSet = "cac90168b3a5475c98b3f79ce775fbe2"
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_rdf_mapping(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 获取rdf文件

```
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_rdf_files()
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 获取rdf的Predicate

```
    try:
        req = models.RdfFile()
        req.filePath = "lol3.rdf"
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_rdf_file_predicate(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 开始导入rdf任务

```
    try:
        req = models.RdfFile()
        req.filePath = "lol3.rdf"
        req.dataSet = "cac90168b3a5475c98b3f79ce775fbe2"
        req.mapping = ["http://panorama.org#root", "http://panorama.org/longRunningProcess#longRunningProcess"]
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.import_rdf_start(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

### 使用JMS导入

- 获取jms列表

```
    try:
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_all_jms()
        print(resp)
    except PanSDKException as err:
        print(err)
```

- jms连接测试

```
    try:
        req = models.JmsRequest()
        req.dataset = "cac90168b3a5475c98b3f79ce775fbe2"
        req.datasetSchema = "root,Long Running Process"
        req.id = ""
        req.jmsConsumer = "json"
        req.jmsDrive = ""
        req.jmsName = "tim_test"
        req.jmsPassword = "sss"
        req.jmsQueue = "sss"
        req.jmsRemark = "test"
        req.jmsUrl = "192.168.1.1"
        req.jmsUser = "sss"
        req.jsonHelpMess = helpMess
        schema = models.JmsSchema()
        schema.displayName = "root"
        schema.schemaId = "http://panorama.org#root"
        req.schemaList = [schema]
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.jms_connect_test(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- jms消费者测试

```
    try:
        req = models.JmsRequest()
        req.dataset = "cac90168b3a5475c98b3f79ce775fbe2"
        req.datasetSchema = "root,Long Running Process"
        req.id = ""
        req.jmsConsumer = "json"
        req.jmsDrive = ""
        req.jmsName = "tim_test"
        req.jmsPassword = "sss"
        req.jmsQueue = "sss"
        req.jmsRemark = "test"
        req.jmsUrl = "192.168.1.1"
        req.jmsUser = "sss"
        req.jsonHelpMess = helpMess
        schema = models.JmsSchema()
        schema.displayName = "root"
        schema.schemaId = "http://panorama.org#root"
        req.schemaList = [schema]
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.jms_consumer_test(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 储存jms

```
    try:
        req = models.JmsRequest()
        req.dataset = "cac90168b3a5475c98b3f79ce775fbe2"
        req.datasetSchema = "root,Long Running Process"
        req.id = ""
        req.jmsConsumer = "json"
        req.jmsDrive = ""
        req.jmsName = "tim_test"
        req.jmsPassword = "sss"
        req.jmsQueue = "sss"
        req.jmsRemark = "test"
        req.jmsUrl = "192.168.1.1"
        req.jmsUser = "sss"
        req.jsonHelpMess = helpMess
        schema = models.JmsSchema()
        schema.displayName = "root"
        schema.schemaId = "http://panorama.org#root"
        req.schemaList = [schema]
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.save_jms(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 导入csv

- 上传文件

```
 try:
        req = models.CsvRequest()
        req.filename = "poc_b.csv"
        req.filepath = ".\poc_b.csv"
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8088"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.upload_csv_file(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 上传多个文件

```
    try:
        req = models.CsvRequest()
        req.filename = ["poc_b.csv", "uploadFileNew"]
        req.filepath = [".\poc_b.csv", '.\\uploadFileNew']
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8088"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.upload_multi_csv_file(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 开始导入csv任务

```
        try:
        req = models.CsvJob()
        req.files = ["/home/bot/uploadDoc/poc_b.csv", "/home/bot/uploadDoc/poc_attribute.csv"]
        req.dataSet = "27e5db4727dd429a98a021477e51c819"
        conf_predicate = models.CsvConfig()
        conf_predicate.id = "随便填"
        conf_predicate.fileName = "poc_attribute.csv"
        conf_predicate.fileType = "entity"
        conf_predicate.conceptType = "人员"
        conf_predicate.header = True
        conf_predicate.titleRule = "clt_nbr"
        pre_1 = models.CsvPredicate()
        pre_1.col = "clt_nbr"
        pre_1.predicateName = "id"
        pre_1.type = "string"
        pre_1.dateTimeFormat = "yyyy-MM-dd hh:mm:ss"
        pre_1.title = True
        pre_1.index = False

        pre_2 = models.CsvPredicate()
        pre_2.col = "High_dlq"
        pre_2.predicateName = "dlq"
        pre_2.type = "string"
        pre_2.dateTimeFormat = "yyyy-MM-dd hh:mm:ss"
        pre_2.title = False
        pre_2.index = False

        pre_3 = models.CsvPredicate()
        pre_3.col = "clt_age"
        pre_3.predicateName = "age"
        pre_3.type = "int"
        pre_3.dateTimeFormat = "yyyy-MM-dd hh:mm:ss"
        pre_3.title = False
        pre_3.index = False

        pre_4 = models.CsvPredicate()
        pre_4.col = "CLT_STR_DTE"
        pre_4.predicateName = "createTime"
        pre_4.type = "datetime"
        pre_4.dateTimeFormat = "yyyy/MM/dd"
        pre_4.title = False
        pre_4.index = False
        conf_predicate.predicate = [pre_1, pre_2, pre_3, pre_4]

        conf_edge = models.CsvConfig()
        conf_edge.id = "随便填"
        conf_edge.fileName = "poc_b.csv"
        conf_edge.fileType = "edge"
        conf_edge.header = True
        edge = models.CsvEdge()
        edge.startCsv = "poc_attribute.csv"
        edge.startCsvCol = "clt_nbr"
        edge.startMapping = "clt_nbr1"
        edge.endCsv = "poc_attribute.csv"
        edge.endCsvCol = "clt_nbr"
        edge.endMapping = "clt_nbr2"
        conf_edge.edge = edge
        conf_edge.edgeName = "relationShipB"
        req.config = [conf_edge, conf_predicate]
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8088"
        uc = import_client.ImportClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.start_csv_job(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

## 锦囊

- 引入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.brocade import brocade_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 获取锦囊列表

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        resp = uc.get_brocade_list()
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 获取rawquery列表

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        resp = uc.get_raw_query_list()
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 生成endpoint

```
    try:
        req = models.Brocade()
        req.brocadeId = "939d0f92dcf744daabc0f579cdbe6f2a"
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.generate_endpoint(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 发布API

```
    try:
        req = models.Brocade()
        req.brocadeId = "939d0f92dcf744daabc0f579cdbe6f2a"
        req.deleted = False
        req.endpoint = "/public/api/workflow"
        req.publicState = False
        req.remark = "测试发布为api"
        req.title = "test_api"
        req.uuid = "c36f8ed1e1b34198a2cdd9b63b1dec8a"
        req.verb = "GET"
        req.version = "v1"
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.api_release(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 创建锦囊

```
    try:
        req = models.CreateBrocade()
        content = models.BrocadeContent()
        content.content = "schema{}"
        content.type = "rawQuery"
        req.content = content
        req.params = []
        req.dataSets = []
        req.type = "user"
        req.title = "python_create"
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        #uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        #uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.new_brocade(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 运行raw query

```
    try:
        req = models.BrocadeContent()
        req.content = "schema{}"
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        #uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        #uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.raw_query_exec(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 删除锦囊

```
    try:
        req = models.Brocade()
        req.brocadeId = "5e6cf75661164f02a1ecc6bb1a9ade3e"
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = brocade_client.BrocadeClient(httpProfile)
        #uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        #uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.delete_brocade(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

## 分析

- 引入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.workspace import workspace_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 获取所有产品

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        uc = workspace_client.WorkspaceClient(httpProfile)
        resp = uc.get_all_product()
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 修改产品

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.ProductRequest()
        req.title = "org.panorama.web.product.deck.DeckWorkProduct"
        req.kind = "ff8081816d394604016ddcadafaa02b9"
        req.productId = "test_bigdata_graph_"
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.mod_product(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 创建产品

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.NewProductRequest()
        req.title = "test_bigdata_graph"
        req.data = []
        req.projectId = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        req.type = "deck"
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.create_product(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 删除产品

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.ProductRequest()
        req.productId = "ff8081816d394604016ddcadafaa02b9"
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.del_product(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 获取产品

```
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.ProductRequest()
        req.productId = "ff8081816d394604016dc92196fd00bd"
        req.params = '{"includeVertices":true,"includeEdges":true}'
        req.includeExtended = True
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_product(req)
        print(resp)
    except PanSDKException as err:
        print(err)
  ```
  
  - 删除图的点
  
  ```
      try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.ProductRequest()
        req.productId = "ff8081816d394604016dc92196fd00bd"
        req.params = '{"removeChildren":true,"preventBroadcastToSourceGuid":true}'
        req.vertexIds = ["242f6dee34dc4b6c8986d5022beb21d2"]
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.delete_graph_vertices(req)
        print(resp)
    except PanSDKException as err:
        print(err)
  ```
  
  - 寻找点的联系
  
  ```
      try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.FindRelateRequest()
        req.graphVertexIds = ["1dca4e4d24d84dfebb73bddeaadb7ca8"]
        req.limitEdgeLabel = "panorama#Movies/performance.character"
        req.limitParentConceptId = "panorama#Movies/Performance"
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.find_vertex_related(req)
        print(resp)
    except PanSDKException as err:
        print(err)
  ```
  
  - 获取多个点的信息
  
  ```
      try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.MultipleVertices()
        req.workspaceId = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        req.vertexIds = ["e96f77010b624af6955a900dc036204a",
                         "7ab1ff56527b4e3bb64099501ca2959e",
                         "83a8e073662e4250b9a6fe98b414d72d",
                         "3783ee59cc754ba9b2051d0881d7e2c1",
                         "6af7b5854b824d7a86998a48f252b56d",
                         "1dca4e4d24d84dfebb73bddeaadb7ca8",
                         "242f6dee34dc4b6c8986d5022beb21d2",
                         "684f6fce1adc469b835b46d78d29007e"]
        req.includeAncillary = False
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_vertex_multiple(req)
        print(resp)
    except PanSDKException as err:
        print(err)
  ```
  
  - 图的搜索
  
  ```
      try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "192.168.31.149:8089"
        req = models.SearchRequest()
        req.fromBrocade = True
        si = models.SearchItem()
        si.type = "vertex"
        si.start = []
        si.conceptTypes = ["panorama#Movies/Movie"]
        si.keyword = "*"
        f = models.Filter()
        f.predicate = ">"
        f.propertyId = "panorama#Movies/initial_release_date"
        f.value = "2009-11-26 00:00"
        si.filters = [f]
        req.searchItems = [si]
        uc = workspace_client.WorkspaceClient(httpProfile)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.search(req)
        print(resp)
    except PanSDKException as err:
        print(err)
  ```

## 数据探查

- 引入依赖包

```
from panclient.common.exception.pan_sdk_exception import PanSDKException
from panclient.workflow import workflow_client, models
from panclient.common.profile.http_profile import HttpProfile
```

- 获取图项目列表

```
    try:
        req = models.GraphProduct()
        req.workspaceId = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = workflow_client.WorkflowClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.get_graph_product(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```

- 运行workflow

```
    try:
        req = models.SemSetList()
        ss = models.SemSet()
        ss.id = "ce9e385c-65c6-477c-8067-bd03e0f6defd"
        ss.disabled = False
        ss.info = ""
        ss.label = "流程1"
        ss.type = "tab"

        ss1 = models.SemSet()
        ss1.credentials = {}
        ss1.dataSetId = "fd912ec041064155b19b22e8b9c64fc9"
        ss1.entityClass = "panorama#Movies/Movie"
        ss1.id = "962b27f8.221588"
        ss1.name = "电影"
        ss1.type = "数据集"
        ss1.wires = [["55a388de.8eea58"]]
        ss1.x = 260
        ss1.y = 320
        ss1.z = "ce9e385c-65c6-477c-8067-bd03e0f6defd"

        ss2 = models.SemSet()
        ss2.credentials = {}
        ss2.field = "panorama#Movies/initial_release_date"
        ss2.id = "55a388de.8eea58"
        ss2.name = "2000后"
        ss2.opt = ">"
        ss2.pickType = "prop"
        ss2.type = "筛选过滤"
        ss2.value = "2000-01-01 00:00:00"
        ss2.wires = [["f1048b95.1c10a8"]]
        ss2.x = 410
        ss2.y = 320
        ss2.z = "ce9e385c-65c6-477c-8067-bd03e0f6defd"

        ss3 = models.SemSet()
        ss3.analysis = "python_test"
        ss3.analysisId = "ff8081816d394604016decf90f8202c7"
        ss3.analysisType = "org.panorama.web.product.graph.GraphWorkProduct"
        ss3.credentials = {}
        ss3.graphName = ""
        ss3.id = "f1048b95.1c10a8"
        ss3.name = "2000后拍的电影"
        ss3.oper = "add"
        ss3.type = "推送到分析"
        ss3.wires = []
        ss3.workspaceId = "WORKSPACE_26277eb956f045fb84104a5af015cc73"
        ss3.x = 610
        ss3.y = 340
        ss3.z = "ce9e385c-65c6-477c-8067-bd03e0f6defd"

        req.SemSetList = [ss, ss1, ss2, ss3]
        req.workspaceId = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        hp = HttpProfile()
        hp.endpoint = "192.168.31.149:8089"
        uc = workflow_client.WorkflowClient(hp)
        uc._panorama_source_guid = "8c1186:80eb70:549c37:50ff89"
        uc._panorama_workspace_id = "WORKSPACE_b5feabf58b1f420088dde168e66d1096"
        resp = uc.sem_set(req)
        print(resp)
    except PanSDKException as err:
        print(err)
```
