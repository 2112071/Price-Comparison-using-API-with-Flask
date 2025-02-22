from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Dummy API Function (Replace with real APIs like Amazon, Flipkart, etc.)
def fetch_prices(product):
    sample_data = [
        {"name": product, "price": 5999, "link": "https://www.flipkart.com"},
        {"name": product, "price": 6200, "link": "https://www.amazon.in"},
        {"name": product, "price": 5800, "link": "https://www.snapdeal.com"},
    ]
    return sample_data

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        product = request.form.get("product")
        results = fetch_prices(product)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
