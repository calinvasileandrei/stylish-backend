from flask import Flask,request, jsonify

from src.scraper.scraper import Scraper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Stylish API!'

@app.route('/scrape',methods=['POST'])
def scrape():
    data = request.get_json()
    link = data.get("link")
    scraper= Scraper(link)
    response = scraper.scrape_link()

    return jsonify(response)


if __name__ == '__main__':
    app.run()
