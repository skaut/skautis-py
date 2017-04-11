import logging

from flask import Flask
from flask import g, render_template, redirect, request, session, url_for
from skautis import SkautisApi

app = Flask(__name__)
app.config.from_pyfile('config.py')

logger = logging.getLogger(__name__)

skautis = SkautisApi(app.config['SKAUTIS_APPID'], test=True)
skautis_token = None


@app.route('/hello')
def authors():
    return 'Hello World!', 200

@app.route('/')
def index():
    # Render out the login page
    return render_template('login.html', 
                           login_link=skautis.get_login_url(),
                           app_name=app.config['APP_NAME'])

@app.route('/login', methods=['POST'])
def login():
    global skautis_token
    skautis_token = request.form['skautIS_Token']
    skautis_idrole = request.form['skautIS_IDRole']
    skautis_idunit = request.form['skautIS_IDUnit']
    skautis_datelogout = request.form['skautIS_DateLogout']

    user_info = skautis.UserManagement.UserDetail(skautis_token, None)
    #role_info = skautis.UserManagement.RoleAll(skautis_token)

    return render_template('index.html',
                           login_link=skautis.get_login_url(),
                           app_name=app.config['APP_NAME'],
                           skautis_token=skautis_token,
                           skautis_idunit=skautis_idunit,
                           skautis_idrole=skautis_idrole,
                           skautis_datelogout=skautis_datelogout,
                           user_info=user_info)

@app.route('/logout')
def logout():
    skautis.UserManagement.LoginUpdateLogout(skautis_token)
    return redirect(url_for('index'))
