from flask import Flask, redirect, render_template, request
import string
import random

app = Flask(__name__)
# Dictionary to store the mappings of short codes to original URLs
url_mapping = {}
def generate_short_code():
    """Generate a random short code."""
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code
@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        url_mapping[short_code] = original_url
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')
@app.route('/<short_code>')

def redirect_to_original_url(short_code):
    if short_code in url_mapping:
        original_url = url_mapping[short_code]
        return redirect(original_url)
    else:
        return "Short URL not found."
if __name__ == '__main__':
    app.run(debug=True)
    