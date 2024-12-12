from flask import Flask,request,render_template,session,redirect,url_for,jsonify
from datetime import datetime
import pymysql
from models import User
app = Flask(__name__)

config = {
    'host': 'localhost',
    'user': 'lxc',
    'password': '123456',
    'db': 'test_user',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    try:
        connection = pymysql.connect(**config)
        print("数据库链接成功")
        return connection
    except pymysql.MySQLError as e:
        print("数据库连接失败：{e}")
        return None
    return connection

@app.route('/',methods = ['GET','POST'])
def hello_world():
    result = []
    if request.method == 'POST':
        input_text = request.form.get('inputText', '')
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # 执行一个查询
                sql = "SELECT * FROM emp2022150152 where empno={0}".format(input_text)
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
    user = User(name = "lxc",email = "lxc@jb.com")
    return render_template('index.html',user = user,result=result)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.json
        email = data.get('email', '')
        password = data.get('password', '')
        print(email,password)
        try:
            connection = get_db_connection()
            with connection.cursor() as cursor:
            # 执行一个查询
                sql = "SELECT id,email,password  FROM user where email='{0}' and password='{1}'".format(email,password)
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
                if result:
                    return jsonify(code=1, msg="登录成功", data=result),200
                else:
                    return jsonify(code=0, msg="用户名或密码错误", data=result), 401
        finally:
            connection.close()
    return render_template('login.html')


@app.route("/blog")
def blog():
    return 'Welcome to my blog!'

@app.route("/blog/<int:blog_id>")
def show_blog(blog_id):
    return render_template('blog_detail.html', blog_id=blog_id )

@app.route('/blog/list')
def bolg_lost():
    page = request.args.get('page',1,int)
    return f'Blog List Page {page}'

@app.route('/child')
def extend_child():
    return render_template('child.html')

@app.route('/static')
def static_demo():
    return render_template('static_demo.html')