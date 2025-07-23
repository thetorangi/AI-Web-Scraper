### 🧠 IntelliScrape

**IntelliScrape** is an AI-powered web scraper that combines traditional scraping tools (Selenium + BeautifulSoup) with intelligent language models using LangChain and Ollama. It features a Streamlit-based UI, supports both **Chrome** and **Firefox** drivers, and enables structured or semantic data extraction from webpages.

---

## 🚀 Features

- 🔍 AI-powered data extraction and summarization using LangChain + Ollama
- 🖥️ GUI with Streamlit for easy use
- 🌐 Supports both **Chrome** and **Firefox** with Selenium WebDriver
- 🧠 Parses and cleans HTML using **BeautifulSoup**, **lxml**, or **html5lib**
- 📦 Environment management via `.env` file

---

## 🧰 Requirements

Install all dependencies via:

```bash
pip install -r requirements.txt
````

Your `requirements.txt` should include:

```
python-dotenv
selenium
streamlit
langchain
langchain_ollama
beautifulsoup4
lxml
html5lib
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/thetorangi/intelliscrape.git
cd intelliscrape
```

2. **Set up the `.env` file:**

Create a `.env` file in the root directory with your config:

```env
BROWSER=chrome            # or 'firefox'
HEADLESS=True             # optional: run browser in headless mode
OLLAMA_MODEL=llama3       # model name if using Ollama (optional)
```

3. **Download WebDrivers:**

* For **Chrome**, download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
* For **Firefox**, download [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

Make sure they are accessible in your system `PATH`.

---

## 🖥️ Run the App

```bash
streamlit run main.py
```

---

## 🧠 AI Integration (LangChain + Ollama)

If you're using AI summarization or parsing, ensure Ollama is running:

```bash
ollama run llama3
```

You can modify the LangChain logic in the `parse.py`.   

---

## 📁 Project Structure

```text
intelliscrape/
├── main.py               # Main Streamlit app
├── scrape.py           # Selenium + BeautifulSoup scraping logic
├── parse.py            # LangChain + Ollama integration
├── .env                 # Environment configuration
├── requirements.txt
└── README.md
```

---



## 🧑‍💻 Author

Built with ❤️ by CoderKarma⚡ [https://github.com/thetorangi](https://github.com/thetorangi)

```

---

Let me know if you want:
- A sample `app.py` boilerplate with `Streamlit + Selenium`
- An AI summarization example using `LangChain` + `Ollama`
- Docker support or deployment instructions

Happy to help build it out!
```
