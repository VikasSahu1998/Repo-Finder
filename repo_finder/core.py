import re
import requests

class RepositoryFinder:
    def __init__(self, github_token=None):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Repository-Finder/1.0'})
        if github_token:
            self.session.headers.update({'Authorization': f'token {github_token}'})

    def search_github(self, query, limit=10):
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={limit}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            repos = []
            for repo in data.get("items", []):
                repo_info = {
                    "full_name": repo["full_name"],
                    "url": repo["html_url"],
                    "stars": repo["stargazers_count"],
                    "language": repo["language"] or "N/A",
                    "api_endpoints": self.find_api_endpoints(repo["full_name"])
                }
                repos.append(repo_info)
            return repos
        except requests.exceptions.HTTPError as e:
            print(f"GitHub API Error: {e}")
            return []

    def find_api_endpoints(self, full_name):
        endpoints = []
        try:
            contents_url = f"https://api.github.com/repos/{full_name}/contents"
            response = self.session.get(contents_url)
            response.raise_for_status()
            items = response.json()

            for file in items:
                if file["type"] == "file" and file["name"].endswith((".py", ".js", ".json", ".env", ".md")):
                    file_content = self.session.get(file["download_url"]).text
                    # Detect URLs or typical API route patterns
                    urls = re.findall(r'https?://[^\s\'"]+', file_content)
                    routes = re.findall(r'@app\.route\([\'"]([^\'"]+)[\'"]\)', file_content)
                    endpoints.extend(urls + routes)
        except Exception as e:
            pass
        return endpoints
