from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/GiveByClick')
@app.route('/')
def home_page_func():
    return 'Welcome to Give By Click'


@app.route('/About_Us')
def about_func():
    return 'Our Story'


@app.route('/Our_Events')
def our_evens_func():
    return redirect('/About_Us')


@app.route('/Products_page')
def product_func():
    return 'Our Special Products'


@app.route('/Products_Details')
def product_detail_func():
    return redirect(url_for('product_func'))


@app.route('/Donation')
def make_donation_func():
    return 'Donate here'


if __name__ == '__main__':
    app.run(debug=True)
