from flask import Flask, render_template, request, jsonify
import chatbotlogic  
from scraper import scrape_website  

app = Flask(__name__)

scraped_data = ""


@app.route('/scrape', methods=['POST'])
def scrape():
    global scraped_data
    data = request.get_json()
    url = data.get('url')
    content = scrape_website(url)
    scraped_data = content 
    return jsonify({'content': content})  


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    response = chatbotlogic.get_response(user_input, scraped_data)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)


