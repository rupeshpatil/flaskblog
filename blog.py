from flask import Flask, render_template, url_for, flash, redirect
from forms import UserRegistrationForm, UserLoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '28f004a8127b9ba1ab3145a50de36b49'


posts = [
    {
        "author": "rupesh",
        "title": "blog 1",
        "content": "xsdg ssf sdsfdsf ssfsd ",
        "date_posted": "2020-02-10"

    },
    {
        "author": "rupesh",
        "title": "blog 2",
        "content": "second blog ",
        "date_posted": "2020-02-18"

    }
]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
   return render_template('about.html',title="Rupesh Blog")

@app.route('/register', methods=['GET','POST'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

@app.route('/login')
def login():
    form = UserLoginForm()
    return render_template('login.html', form=form, title='Login')

if __name__ == "__main__":
    app.run(debug=True)
