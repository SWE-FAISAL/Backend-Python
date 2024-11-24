from app import app
from Model.userModel import userModel
from Model.authModel import auth_model
from flask import request, send_file
import os
from datetime import datetime

obj = userModel()
auth = auth_model()

# GET/READ Operation
@app.route('/user/getalluser', methods=["GET"])
def userControllerSignup():
    return obj.getAllUserModel()

# POST/CREATE Operation 
@app.route("/user/add", methods=["POST"])
def add_user():
    return obj.add_user_model(request.form)

@app.route("/user/addmultiple", methods=["POST"])
def add_multiple_users():
    return obj.add_multiple_users_model(request.json)

# Delete Operation 
@app.route("/user/delete/<id>", methods=["DELETE"])
def delete_user(id):
    return obj.delete_user_model(id)

# Update Operation 
@app.route("/user/update", methods=["PUT"])
def update_user():
    return obj.update_user_model(request.form)

# Patch Operation 
@app.route("/user/patch", methods=["PATCH"])
def patch_user():
    return obj.patch_user_model(request.form)


@app.route("/user/page/<pno>/limit/<limit>", methods=["get"])
def pagination(pno, limit):
    return obj.pagination_model(pno, limit)

@app.route("/user/<uid>/avatar/upload", methods=["PATCH"])
def upload_avatar(uid):
    file = request.files['avatar']
    new_filename =  str(datetime.now().timestamp()).replace(".", "") # Generating unique name for the file
    split_filename = file.filename.split(".") # Spliting ORIGINAL filename to seperate extenstion
    ext_pos = len(split_filename)-1 # Canlculating last index of the list got by splitting the filname
    ext = split_filename[ext_pos] # Using last index to get the file extension
    db_path = f"uploads/{new_filename}.{ext}"
    file.save(f"uploads/{new_filename}.{ext}")
    return obj.upload_avatar_model(uid, db_path)

@app.route("/user/avatar/<uid>", methods=["GET"])
def get_avatar(uid):
    data = obj.get_avatar_path_model(uid)
    root_dir = os.path.dirname(app.instance_path)
    return send_file(f"{root_dir}{data['payload'][0]['avatar']}")


@app.route("/user/login")
def user_login():
    auth_data = request.authorization
    return obj.user_login_model(auth_data['username'], auth_data['password'])