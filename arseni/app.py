import random

from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session
#import requests
#import random


app = Flask(__name__)
app.secret_key = '123'


users ={"user1": {"username": "sapir", "First name": "sap", "Last name":  "bibi" ,"Email": "bibis@post.bgu.ac.il"},
        "user2": {"username": "sapir2","First name": "sap1" , "Last name": "bibi1","Email": "galo@galo.com"},
        "user3": {"username": "sapir3","First name": "sap2", "Last name":  "bibi2","Email": "galo@galo2.com"},
        "user4": {"username": "sapir4","First name": "sap3" , "Last name": "bibi3","Email": "galo@galo3.com"},
        "user5": {"username": "sapir5","First name": "sap4" , "Last name":  "bibi4","Email": "galo@galo4.com"}
        }




@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    #DB
    found=True
    if found:
     return render_template('CVgrid-exersize5.html' ,name='sapir')
    else:
      return render_template('CVgrid-exersize5.html')

@app.route('/assignment8')
#DB
def hello_world2():  # put application's code here
    found=True
    if found:
     return render_template('CVgrid-exersize5.html' ,name='sapir')
    else:
      return render_template('CVgrid-exersize5.html')

@app.route('/aboutme')
def aboutme_func():

    return render_template('aboutme.html',
                           profile={'name': 'sapir'},
                           university='bgu', age='31',
                           degrees=['first', 'second', 'third'])


@app.route('/forms')
def check_forms():
    return render_template('forms.html')


@app.route('/assignment9',methods=['GET','POST'])
def user_func():
        current = request.method
        if current == 'GET':
            if 'username' in request.args:
                username = request.args['username']
                if username is '':
                    return render_template('assignment9.html', search=True, users=users, correctuser=True)
                userlist = {}
                #for user in users.value():
                #    if user in ['username'] ==username:
                 #       userlist[1] = user
               #  if len(userlist) != 0:
                #     return render_template('assignment9.html', search=True, correctuser=True, users=userlist)
                #else:
                 #   return render_template('assignment9.html', correctuser=False, search=True)
            return render_template('assignment9.html')
       #  elif current == 'POST':
            session['login'] = True
            users[request.form['email']] = {'First Name': request.form['firstName'],
                                            'Last Name': request.form['lastName'],
                                            'Email': request.form['email'],
                                            'User Name': request.form['userName']}
            session['userName'] = request.form['userName']
            return render_template('assignment9.html')

   # if 'product' in request.args:
    #    product = request.args['product']
     #   size = request.args['size']
      #       return render_template('assignment9.html', p_name=product, p_size=size)
           # return render_template('assignment9.html')







@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('CVgrid-exersize5.html')

@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # DB
        found = True
        if found:
            session['username'] = username
            return redirect(url_for('aboutme_func'))
        else:
            return render_template('login.html')

@app.route('/CV-SAPIR-BIBI')
def CVGRID_func():
    return render_template('CVgrid-exersize5.html')


if __name__ == '__main__':
    app.run(debug=True)


#@app.route('/req_front')
#def req_front():
#    return render_template('req_front.html')


#def get_pockemons(num):
#    pockemons = []
#    for i in range(num):
#        random_n=random.randint(1, 100)
#        res = request.get(f'https://pokeapi.co/api/v2/poclemon/{random_n}')
#        res = res.json()
#        pockemons.append(res)
#    return pockemons

#@app.route('/req_backend')
#def req_backend():
#    num = 3
#    if "number" in request.args:
#        num = int(request.args['number'])
#    pockemons = get_pockemons(num)
#    return render_template('req_backend.html' , pockemons=pockemons)