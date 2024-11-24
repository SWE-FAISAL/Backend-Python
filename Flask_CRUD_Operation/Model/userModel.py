import mysql.connector
from Config.config import dbconfig
import json
from flask import make_response
import jwt
from datetime import datetime, timedelta


class userModel():
    def __init__(self):
        # DBMS CONNECTION
        try:
         self.connection = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
         self.connection.autocommit=True
         self.cursor = self.connection.cursor(dictionary=True)
         print('connecting to database sucessfully')
        except:
            print("Error in connecting to database")
    
    # GET/READ Operation
    def getAllUserModel(self):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        if len(result)>0:
            return {"payload":result}
            # return make_response({"payload":result},200)
        else:
            return "No Data Found"
        
    # POST/Create Operation 
    def add_user_model(self, data):
        self.cursor.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    def add_multiple_users_model(self, data):
        # Generating query for multiple inserts
        qry = "INSERT INTO users(name, email, phone, roleid, password) VALUES "
        for userdata in data:
            qry += f" ('{userdata['name']}', '{userdata['email']}', '{userdata['phone']}', {userdata['roleid']},'{userdata['password']}'),"
        finalqry = qry.rstrip(",")
        self.cur.execute(finalqry)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    # Delete Operation 
    def delete_user_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)
        
    # Update Operation 
    def update_user_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    # Patch Operation     
    def patch_user_model(self, data):
        qry = "UPDATE users SET "
        for key in data:
            if key!='id':
                qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {data['id']}"
        self.cursor.execute(qry)
        if self.cursor.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)


    def pagination_model(self, pno, limit):
        pno = int(pno)
        limit = int(limit)
        start = (pno*limit)-limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cursor.execute(qry)
        result = self.cursor.fetchall()
        if len(result)>0:
            return make_response({"page":pno, "per_page":limit,"this_page":len(result), "payload":result})
        else:
            return make_response({"message":"No Data Found"}, 204)


    def upload_avatar_model(self, uid, db_path):
        self.cur.execute(f"UPDATE users SET avatar='{db_path}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"FILE_UPLOADED_SUCCESSFULLY", "path":db_path},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)


    def get_avatar_path_model(self, uid):
        self.cur.execute(f"SELECT avatar FROM users WHERE id={uid}")
        result = self.cur.fetchall()
        if len(result)>0:
            print(type(result))
            return {"payload":result}
        else:
            return "No Data Found"  


    def user_login_model(self, username, password):
        self.cursor.execute(f"SELECT id, roleid, avatar, email, name, phone from users WHERE email='{username}' and password='{password}'")
        result = self.cursor.fetchall()
        if len(result)==1:
            exptime = datetime.now() + timedelta(minutes=15)
            exp_epoc_time = exptime.timestamp()
            data = {
                "payload":result[0],
                "exp":int(exp_epoc_time)
            }
            print(int(exp_epoc_time))
            jwt_token = jwt.encode(data, "Sagar@123", algorithm="HS256")
            return make_response({"token":jwt_token}, 200)
        else:
            return make_response({"message":"NO SUCH USER"}, 204)    