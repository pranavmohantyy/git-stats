import subprocess
import json
from collections import defaultdict

def get_commit_stats():
    result = subprocess.run(['git', 'log', '--pretty=format:%h|%an|%ae|%ai|%s'], capture_output=True, text=True)
    commits = []
    for line in result.stdout.splitlines():
        hash, author_name, author_email, date, message = line.split('|')
        commits.append({
            'hash': hash,
            'author_name': author_name,
            'author_email': author_email,
            'date': date,
            'message': message
        })
    return commits


def summarize_commits(commits):
    total_commits = len(commits)
    unique_authors = set()
    author_stats = defaultdict(lambda: {'commits': 0, 'first_commit': None, 'last_commit': None, 'active_days': defaultdict(int)})

    for commit in commits:
        author = commit['author_name']
        unique_authors.add(author)
        author_stats[author]['commits'] += 1
        commit_date = commit['date'][:10]
        author_stats[author]['active_days'][commit_date] += 1

        if author_stats[author]['first_commit'] is None:
            author_stats[author]['first_commit'] = commit['date']
        author_stats[author]['last_commit'] = commit['date']

    return {
        'total_commits': total_commits,
        'unique_authors': len(unique_authors),
        'author_stats': author_stats
    }