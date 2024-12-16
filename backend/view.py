from flask import Flask, request, render_template, jsonify, make_response
from functools import wraps
import pymysql
from flask_cors import CORS
import jwt
import datetime
from jwt.exceptions import DecodeError, ExpiredSignatureError

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 允许跨域携带 Cookie
SECRET_KEY = '123456'

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
        print(f"数据库连接失败：{e}")
        return None

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email', '')
    password = data.get('password', '')

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, email FROM user u WHERE u.email=%s AND u.password=%s"
            cursor.execute(sql, (email, password))
            result = cursor.fetchone()
            print(result)
            if result:
                payload = {
                    'id': result['id'],  # 用户的唯一标识符
                    'email': result['email'],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # JWT过期时间
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                resp = make_response(jsonify(code=1, message='登录成功', data=result,token=token))
                resp.set_cookie('token', token, httponly=True, secure=False)  # 将token存入cookie
                return resp
            else:
                return jsonify(code=0, message="用户名或密码错误"), 401
    finally:
        connection.close()


@app.route('/user', methods=['POST'])
def user():
    token = request.json['token']
    print(token)
    if not token:
        return jsonify(code=0, message="未登录或会话已过期"), 403
    try:
        # 解析token
        playload = jwt.decode(token, '123456', algorithms=['HS256'])
        # payload将包含在token中编码的数据，例如用户ID
        print(playload)
        user = {'id': playload['id'], 'email': playload['email']}

        return jsonify(code=1, message='获取用户信息成功', data=user), 200
    except DecodeError:
        return jsonify(code=0, message="Token解码失败"), 403
    except ExpiredSignatureError:
        return jsonify(code=0, message="Token已过期"), 403
    except Exception as e:
        print(e)
        # 捕获其他可能的异常
        return jsonify(code=0, message=str(e)), 403

