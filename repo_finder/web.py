import os
from flask import Flask, render_template, request
from .core import RepositoryFinder
from .categories import CATEGORIES

# Point to the templates folder inside repo_finder
template_dir = os.path.join(os.path.dirname(__file__), "templates")
app = Flask(__name__, template_folder=template_dir)

finder = RepositoryFinder()

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    selected_category = None
    limit = 10
    if request.method == "POST":
        selected_category = request.form.get("category")
        limit = int(request.form.get("limit", 10))
        keywords = CATEGORIES.get(selected_category, [])
        query = " OR ".join(keywords)
        results = finder.search_github(query, limit=limit)

    return render_template(
        "index.html",
        categories=CATEGORIES.keys(),
        selected_category=selected_category,
        results=results,
        limit=limit
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
