from flask import Flask, render_template, url_for, request, redirect
import email
import csv

app = Flask( __name__ )


@app.route( '/' )
def my_home():
    return render_template( 'index.html' )


@app.route( '/<string:page_name>' )
def html_page(page_name):
    return render_template( page_name )


def write_to_file(data):
    with open( 'database.txt', mode='a' ) as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route( '/submit_form', methods=['POST', 'GET'] )
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect( '/thankyou.html' )
    else:
        return 'something went wrong , try again'

    # return 'form submitte foo'
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)

# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def about():
#     return render_template('contact.html')
# @app.route('/')
# def he(username=None, post_i=None, post_id=None):
#     return render_template('index.html', name=username,  post_id=post_id)


# @app.route('/favicon.ico')
# def blog():
#    return 'Hagura iafivfnbvnbsljjnvjfnvjnsvjjvl!'

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/blogs')
# def blogs():
#     return 'emiraaaaa!'
