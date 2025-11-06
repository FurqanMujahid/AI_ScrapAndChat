# AI_ScrapAndChat

A powerful web application that combines web scraping capabilities with an AI-powered chatbot. Scrape content from any website (static or dynamic) and interact with the scraped data through an intelligent chatbot powered by Google's Gemini AI.

## 🚀 Features

- **Intelligent Web Scraping**: Automatically detects and scrapes both static and dynamic (JavaScript-rendered) websites
- **AI-Powered Chatbot**: Ask questions about the scraped content using Google's Gemini AI model
- **Conversation History**: Maintains context throughout your conversation
- **Modern UI**: Beautiful interface with gold-to-bronze gradient theme
- **Real-time Processing**: Instant scraping and AI responses

## 📋 How It Works

1. **Enter Website URL**: User provides a website URL through the web interface
2. **Web Scraping**: The application determines if the website is static or dynamic:
   - **Static Sites**: Uses `requests` and `BeautifulSoup` for fast scraping
   - **Dynamic Sites**: Uses `Selenium` with ChromeDriver to render JavaScript content
3. **Data Processing**: Extracted text content is cleaned and normalized
4. **AI Context**: The scraped data is provided as context to the Gemini AI model
5. **Chat Interface**: Users can ask questions, and the AI responds based on the scraped website content

## 🏗️ Project Structure

```
AI_ScrapAndChat/
├── SWC/
│   ├── app.py                 # Flask web application (main server)
│   ├── scraper.py             # Web scraping logic
│   ├── chatbotlogic.py        # AI chatbot integration with Gemini
│   ├── chromedriver.exe       # ChromeDriver executable for Selenium
│   ├── templates/
│   │   └── index.html         # Frontend HTML interface
│   └── static/
│       ├── styles.css         # Application styling
│       └── Screenshot 2024-10-13 141346.png  # Logo image
└── README.md
```

## 📁 File Descriptions

### `SWC/app.py`
Flask web application that serves as the backend server:
- **`/` (GET)**: Renders the main HTML interface
- **`/scrape` (POST)**: Accepts a URL, scrapes the website, stores the content globally, and returns the scraped data as JSON
- **`/chat` (POST)**: Accepts user messages and returns AI-generated responses based on the scraped content
- **Global Variable**: `scraped_data` - Stores the most recently scraped website content

### `SWC/scraper.py`
Web scraping module with intelligent site detection:
- **`check_static_site(url)`**: 
  - Attempts to fetch the website using `requests` library
  - Parses HTML with BeautifulSoup
  - Checks for paragraph tags to determine if content is available
  - Returns BeautifulSoup object if static, None otherwise
  
- **`scrape_dynamic_site(url)`**:
  - Configures ChromeDriver with headless options
  - Loads the URL and waits for JavaScript rendering (5 seconds)
  - Scrolls to bottom to trigger lazy-loaded content
  - Extracts all text content from the rendered page
  - Returns cleaned text content
  
- **`scrape_website(url)`**:
  - Main function that orchestrates the scraping process
  - First attempts static scraping
  - Falls back to dynamic scraping if static fails
  - Normalizes whitespace in the final output
  - Returns cleaned text or error message

### `SWC/chatbotlogic.py`
AI chatbot integration using Google's Gemini AI:
- **`get_response(user_input, scraped_data)`**:
  - Configures Gemini API with API key
  - Uses `gemini-1.5-flash` model
  - Maintains conversation history in a global list
  - Prepends scraped data as context to the AI prompt
  - Appends user messages and AI responses to conversation history
  - Returns AI-generated response based on context and conversation

### `SWC/templates/index.html`
Frontend user interface:
- **Sidebar**: Contains logo and application description
- **Web Scraper Section**:
  - URL input field
  - "Scrape" button to initiate scraping
  - "Train" button (currently displays a message)
  - Results display area with loading spinner
- **Chatbot Section**:
  - Chat message display area
  - User input field with "Send" button
  - Enter key support for sending messages
- **JavaScript Functions**:
  - Handles scraping requests and displays results
  - Manages chat message sending and display
  - Updates UI dynamically with responses

### `SWC/static/styles.css`
Styling for the application:
- Gold-to-bronze gradient color scheme (#d4af37, #8C7B50)
- Responsive layout with sidebar and main content area
- Styled chat bubbles (user messages in gold, bot messages in beige)
- Loading spinner animation
- Modern, clean design with rounded corners and shadows

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Google Chrome browser (for Selenium)
- Google Gemini API key

### Dependencies

Install required Python packages:

```bash
pip install flask
pip install requests
pip install beautifulsoup4
pip install selenium
pip install google-generativeai
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/FurqanMujahid/AI_ScrapAndChat.git
cd AI_ScrapAndChat
```

2. Install dependencies (see above)

3. **Important**: Update the API key in `SWC/chatbotlogic.py`:
   - Replace the hardcoded API key with your own Gemini API key
   - Get your API key from: https://makersuite.google.com/app/apikey

4. Ensure `chromedriver.exe` is compatible with your Chrome version, or download the appropriate version from https://chromedriver.chromium.org/

5. Run the application:
```bash
cd SWC
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## 📖 Usage

1. **Scraping a Website**:
   - Enter a website URL in the "Website URL" input field
   - Click the "Scrape" button
   - Wait for the scraping process to complete (loading spinner will appear)
   - Scraped content will be displayed in the results area

2. **Chatting with AI**:
   - After scraping, click the "Train" button (this enables the chatbot)
   - Type your question in the chat input field
   - Press Enter or click "Send"
   - The AI will respond based on the scraped website content

## 🔌 API Endpoints

### `GET /`
Returns the main HTML interface.

### `POST /scrape`
Scrapes a website and returns the content.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "content": "Scraped website text content..."
}
```

### `POST /chat`
Sends a message to the AI chatbot and receives a response.

**Request Body:**
```json
{
  "message": "What is this website about?"
}
```

**Response:**
```json
{
  "response": "AI-generated response based on scraped data..."
}
```

## 🧪 Technologies Used

- **Backend**: Python, Flask
- **Web Scraping**: 
  - BeautifulSoup4 (static sites)
  - Selenium WebDriver (dynamic sites)
  - Requests library
- **AI/ML**: Google Gemini AI (gemini-1.5-flash model)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Browser Automation**: ChromeDriver

## ⚠️ Important Notes

1. **API Key Security**: The Gemini API key is currently hardcoded in `chatbotlogic.py`. For production use, store it as an environment variable:
   ```python
   import os
   genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
   ```

2. **ChromeDriver Compatibility**: Ensure `chromedriver.exe` matches your Chrome browser version. Update it if necessary.

3. **Rate Limiting**: Be aware of API rate limits when using Gemini AI for multiple requests.

4. **Website Scraping Ethics**: Always respect robots.txt and terms of service of websites you scrape. Use responsibly and ethically.

5. **Training Button**: The "Train" button in the UI currently only displays a message. The AI model is not trained locally; it uses the pre-trained Gemini model with scraped data as context.

## 🎯 How the AI Works

The application doesn't train a model on the scraped data. Instead, it uses Google's pre-trained Gemini AI model and provides the scraped website content as context in each request. The AI model uses this context along with conversation history to generate relevant responses about the scraped content.

## 📝 Future Improvements

- [ ] Move API key to environment variables
- [ ] Add support for multiple websites/sessions
- [ ] Implement persistent conversation history storage
- [ ] Add error handling for invalid URLs
- [ ] Support for scraping specific sections of websites
- [ ] Export chat conversations
- [ ] Add authentication/user sessions

## 📄 License

This project is open source and available for educational purposes.

---

**Note**: This application is for educational and personal use. Always ensure you have permission to scrape websites and comply with their terms of service.
