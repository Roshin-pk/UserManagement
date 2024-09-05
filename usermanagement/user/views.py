from django.shortcuts import render,redirect
from django.views import View
import bcrypt
#importing database connectivity
from usermanagement.database_connection import DatabaseConnection

# Create your views here.
class CreateUserPage(View):
    def get(self,request):
        return render('userpage.html')

class EncryptingPassword:
    def encrypt_password(self,password):
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return encrypted_password
 

class CreateUser(View,DatabaseConnection):
    def post(self,request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        username_exists = self.cursor.execute(f'SELECT * FROM users WHERE username = {username};')
        if username_exists:
            return render('userpage.html',context={'msg':'username already exists'})
        email_exists = self.cursor.execute(f'SELECT * FROM users WHERE email = {email};')
        if email_exists:
            return render('userpage.html',context={'msg':'email already exists'})
        encrypt_password = EncryptingPassword().encrypt_password(password)
        user_create = self.cursor.execute(f'INSERT INTO users (username, email, password) VALUES ({username},{email},{encrypt_password});')
        self.connection.commit()
        return render('',context={"msg":"user created successfully"})
    
class UpdateUser(View,DatabaseConnection):
    def post(self,request,id):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        username_exists = self.cursor.execute(f'SELECT * FROM users WHERE username = {username};')
        if username:
            if username_exists:
                return render('userpage.html',context={'msg':'username already exists'})
            else:
                self.cursor.execute(f'UPDATE users SET username ={username}  WHERE id = {id}')
        email_exists = self.cursor.execute(f'SELECT * FROM users WHERE email = {email}')
        if email:
            if email_exists:
                return render('userpage.html',context={'msg':'email already exists'})
            else:
                self.cursor.execute(f'UPDATE users SET email ={email}  WHERE id = {id}')
        if password:
            encrypt_password = EncryptingPassword().encrypt_password(password)
            self.cursor.execute(f'UPDATE users SET password ={encrypt_password}  WHERE id = {id}')
        self.connection.commit()
        return render('',context={"msg":"user edited successfully"})




    
