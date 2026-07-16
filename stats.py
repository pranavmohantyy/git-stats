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


def get_file_change_stats():
    result = subprocess.run(['git', 'log', '--numstat'], capture_output=True, text=True)
    file_stats = defaultdict(lambda: {'added': 0, 'deleted': 0})
    for line in result.stdout.splitlines():
        if line.strip() == '':
            continue
        parts = line.split('\t')
        if len(parts) == 3:
            added, deleted, filename = parts
            file_stats[filename]['added'] += int(added)
            file_stats[filename]['deleted'] += int(deleted)
    return file_stats


if __name__ == '__main__':
    commit_stats = get_commit_stats()
    file_stats = get_file_change_stats()
    print(json.dumps({'commits': commit_stats, 'file_stats': file_stats}))