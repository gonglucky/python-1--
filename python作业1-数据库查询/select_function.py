import pymysql.cursors

'''
    condition_str:查询条件
    *field:选取列的元组，默认为*
    **config:数据库配置和选取的表名
    return: 数据库连接 conn,是否连接成功 connected,sql语句 sql
'''


def select(*field, condition_str=None, **config):
    if type(field) is not tuple:
        print('错误: 查询列名参数不是元组类型！')

    if type(config) is not dict:
        print('错误: 访问信息参数不是字典类型！')
    else:
        for key in ['host', 'port', 'user', 'pw', 'db']:
            if key not in config.keys():
                print('错误: 访问信息参数字典缺少 %s' % key)
        if 'charset' not in config.keys():
            config['charset'] = 'utf8'
    try:
        conn = pymysql.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            passwd=config['pw'],
            db=config['db'],
            charset=config['charset'],
            cursorclass=pymysql.cursors.DictCursor)
        connected = True
    except pymysql.Error as e:
        print('数据库连接失败:', end='')

    sql = 'SELECT '
    field_num = len(field)
    if field_num == 0:
        sql = sql + "*"
    else:
        for index, item in enumerate(field):
            sql = sql + str(item) + ','
        sql = sql[:-1]

    sql = sql + ' FROM '
    tables = config['table']

    tables_num = len(tables)
    if tables_num == 0:
        print("错误: table参数缺少table")
    else:
        for item in tables:
            sql = sql + str(item) + ','
        sql = sql[:-1]

    sql = sql + ' WHERE ' + str(condition_str)
    return conn, connected, sql
