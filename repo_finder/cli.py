import sys
from repo_finder.core import RepositoryFinder
from repo_finder.categories import CATEGORIES

def main():
    finder = RepositoryFinder()

    # Show categories
    print("Select a category:")
    for i, cat in enumerate(CATEGORIES.keys(), 1):
        print(f"{i}. {cat}")
    choice = input("Enter choice number: ")

    try:
        choice = int(choice)
        category = list(CATEGORIES.keys())[choice-1]
    except:
        print("Invalid choice")
        sys.exit(1)

    # Build search query
    keywords = CATEGORIES[category]
    query = " OR ".join(keywords)

    # Ask for limit
    limit = input("Enter number of results to fetch (default 10): ")
    try:
        limit = int(limit)
    except:
        limit = 10

    # Search GitHub
    print(f"\nSearching GitHub for category '{category}'...\n")
    results = finder.search_github(query, limit=limit)

    # Display results
    for repo in results:
        print(f"⭐ {repo['stars']} | {repo['full_name']} ({repo['language']}) → {repo['url']}")

if __name__ == "__main__":
    main()
