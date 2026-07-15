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
    commits_by_day = defaultdict(int)

    for commit in commits:
        day = commit['date'][:10]  # Just take the date part
        weekday = commit['date'][8:10]  # Extract weekday
        commits_by_day[weekday] += 1

    return commits_by_day


def display_commit_frequency(commits_by_day):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range(7):
        day = days[i]
        bar = '*' * (commits_by_day.get(str(i), 0) // 2)
        print(f'{day}: {bar}')


if __name__ == '__main__':
    commits = get_commit_stats()
    commit_summary = summarize_commits(commits)
    display_commit_frequency(commit_summary)
