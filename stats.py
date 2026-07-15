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
    author_stats = defaultdict(int)
    hour_count = defaultdict(int)

    for commit in commits:
        author_stats[commit['author_name']] += 1
        hour = commit['date'][11:13]
        hour_count[hour] += 1

    peak_hour = max(hour_count, key=hour_count.get)

    return {
        'total_commits': total_commits,
        'author_stats': author_stats,
        'peak_hour': peak_hour
    }


if __name__ == '__main__':
    commits = get_commit_stats()
    summary = summarize_commits(commits)
    print(json.dumps(summary, indent=2))