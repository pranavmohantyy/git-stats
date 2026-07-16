import subprocess
import json
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

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
    monthly_activity = defaultdict(int)
    for commit in commits:
        date = commit['date'][:7]
        monthly_activity[date] += 1
    return monthly_activity


def plot_monthly_activity(monthly_activity):
    months = list(monthly_activity.keys())
    counts = list(monthly_activity.values())
    plt.bar(months, counts)
    plt.xlabel('Month')
    plt.ylabel('Number of Commits')
    plt.title('Monthly Activity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    commits = get_commit_stats()
    activity = summarize_commits(commits)
    plot_monthly_activity(activity)