from github import Github
import os
from pprint import pprint
from operator import itemgetter 

# GitHub API access token: https://github.com/settings/tokens
githubToken = os.getenv('GITHUB_TOKEN', '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')
# GitHub repository
githubRepo = os.getenv('GITHUB_REPO', 'lpakarinen/repo_stats')


# Authenticate and fetch repository details
gh = Github(githubToken)
repo = gh.get_repo(githubRepo)

# Get statistics
clones = repo.get_clones_traffic(per="day")
views = repo.get_views_traffic(per="day")

# Print statistics
print(f"Repository has {clones['count']} clones out of which {clones['uniques']} are unique.")
print(f"Repository has {views['count']} views out of which {views['uniques']} are unique.")
if(views['count'] > 0):
  print('Repository views:')
  pprint(views)
  # Find day(s) with most views
  best_day = max(list((day.count, day.timestamp) for day in views["views"]), key=itemgetter(0))
  print(f"Repository had most views on {best_day[1]} with {best_day[0]} views")
