import logging

from flask import Flask
from flask import g, render_template, redirect, request, session, url_for
from skautis import SkautisApi

app = Flask(__name__)
app.config.from_pyfile('config.py')

logger = logging.getLogger(__name__)

skautis = SkautisApi(app.config['SKAUTIS_APPID'], test=True)


@app.route('/hello')
def authors():
    return app.config['SKAUTIS_APPID'], 200


@app.route('/index')
def index():
    # Check if user is logged in
    #if g.user:
        # Render out page for authorized users.
    #    return render_template('index.html', app_name="skautIS-py test", user=g.user)

    # Render out the login form
    return render_template('login.html', 
                           login_link=skautis.get_login_url(),
                           app_name=app.config['APP_NAME'])

@app.route('/login', methods=['POST'])
def login():
    skautis_token = request.form['skautIS_Token']
    skautis_idrole = request.form['skautIS_IDRole']
    skautis_idunit = request.form['skautIS_IDUnit']
    skautis_datelogout = request.form['skautIS_DateLogout']

    return render_template('index.html',
                           login_link=skautis.get_login_url(),
                           app_name=app.config['APP_NAME'],
                           skautis_token=skautis_token,
                           skautis_idunit=skautis_idunit,
                           skautis_idrole=skautis_idrole,
                           skautis_datelogout=skautis_datelogout)

@app.route('/logout')
def logout():
    # session.pop('user', None)
    return redirect(url_for('index'))
