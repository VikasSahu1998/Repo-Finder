import requests

class RepositoryFinder:
    BASE_URL = "https://api.github.com/search/repositories"

    def search_github(self, query, limit=10):
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": limit}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        results = []
        for item in data.get("items", []):
            results.append({
                "full_name": item.get("full_name", item.get("name", "Unknown")),
                "url": item.get("html_url", "#"),
                "stars": item.get("stargazers_count", 0),
                "language": item.get("language", "N/A")
            })
        return results
