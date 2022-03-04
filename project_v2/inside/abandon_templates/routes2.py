# @app.route('/register', methods=['GET', 'POST'])
# def register():
#      # connect
#     conn = mysql.connect()
#     cursor = conn.cursor(pymysql.cursors.DictCursor)
  
#     # Output message if something goes wrong...
#     msg = ''
#     # Check if "username", "password" and "email" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         # Create variables for easy access
#         fullname = request.form.get('fullname')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         email = request.form.get('email')
   
#   #Check if account exists using MySQL
#         cursor.execute(f'SELECT * FROM user WHERE username = %s',(username))
#         account = cursor.fetchone()
#         # If account exists show error and validation checks
#         if account:
#             msg = 'Account already exists!'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address!'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'Username must contain only characters and numbers!'
#         elif not username or not password or not email:
#             msg = 'Please fill out the form!'
#         else:
#             # Account doesnt exists and the form data is valid, now insert new account into accounts table
#             cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s, %s)', (fullname, username, password, email)) 
#             conn.commit()
   
#             msg = 'You have successfully registered!'
#     elif request.method == 'POST':
#         # Form is empty... (no POST data)
#         msg = 'Please fill out the form!'
#     # Show registration form with message (if any)
#     return render_template('register.html', msg=msg)