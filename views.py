from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from . import db
import json
import os
from werkzeug.utils import secure_filename
import cv2
from .utilities import AES 
from .utilities import DES_single, md5
# from .utilities import RSA 
from .utilities import SHA2 as sha
#from .utilities import DiffieHellman as  DH
from .utilities import compareHashes 

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/3des', methods=['GET', 'POST'])
@login_required
def DES_3():
    if request.method == 'POST':
        file = request.files['file']
        key = request.form.get('key')
        method = request.form.get('method')
        fileName = secure_filename(file.filename)
        file.save(os.path.join('./website/static/files/', fileName))
        filePath = './website/static/files/' + fileName
        if method == "encrypt":
            encryptedFile = "../static/files/" + DES_single.encrypt(filePath, key)
            return render_template("download.html", user=current_user, title = "Triple DES Encryption", content = encryptedFile, file = list(encryptedFile.split("/"))[-1], message = "File encrypted successfully!!")
        else:
            decryptedFile = "../static/files/" + DES_single.decrypt(filePath, key)
            return render_template("download.html", user=current_user, title = "Triple DES Decryption", content = decryptedFile,file = list(decryptedFile.split("/"))[-1], message = "File decrypted successfully!!")
        
    return render_template("Triple DES encode.html", user=current_user)

@views.route('/compareHashes', methods=['GET', 'POST'])
@login_required
def compare():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        fileName1 = secure_filename(file1.filename)
        file1.save(os.path.join('./website/static/files/', fileName1))
        filePath1 = './website/static/files/' + fileName1
        fileName2 = secure_filename(file2.filename)
        file2.save(os.path.join('./website/static/files/', fileName2))
        filePath2 = './website/static/files/' + fileName2
        message = compareHashes.compareHashes(filePath1,filePath2)
        return render_template("compare_hashes.html", user=current_user, message = message)
    return render_template("compare_hashes_get.html", user=current_user)

@views.route('/sha2', methods=['GET', 'POST'])
@login_required
def SHA2():
    if request.method == 'POST':
        file = request.files['file']
        # method = request.form.get('method')
        fileName = secure_filename(file.filename)
        file.save(os.path.join('./website/static/files/', fileName))
        filePath = './website/static/files/' + fileName
        print(filePath)
        hashedFile = "../static/files/" + sha.secureHashing(filePath)
        return render_template("download.html", user=current_user, title = "SHA-256 Hashing", content = hashedFile, file = list(hashedFile.split("/"))[-1], message = "File hashed successfully!!")
    return render_template("SHA2.html", user=current_user)

@views.route('/md5', methods=['GET', 'POST'])
@login_required
def MD5():
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['file']
        # Get the filename and secure it
        file_name = secure_filename(file.filename)
        # Save the file to the server
        file.save(os.path.join('./website/static/files/', file_name))
        # Define the file path
        file_path = './website/static/files/' + file_name
        
        # Perform MD5 hashing on the file
        hashed_file = "../static/files/" + md5.secure_hashing_md5(file_path)
        
        # Render the download page with the hashed file
        return render_template("download.html", user=current_user, title="MD5 Hashing", content=hashed_file, file=list(hashed_file.split("/"))[-1], message="File hashed successfully!!")
    
    # Render the MD5 hashing page if the request method is GET
    return render_template("message_digest.html", user=current_user)



@views.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


