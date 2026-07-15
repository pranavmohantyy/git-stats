import subprocess
import json

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
    unique_authors = len(set(commit['author_name'] for commit in commits))
    date_range = (commits[-1]['date'], commits[0]['date']) if commits else (None, None)
    return {
        'total_commits': total_commits,
        'unique_authors': unique_authors,
        'date_range': date_range
    }

if __name__ == '__main__':
    commit_stats = get_commit_stats()
    summary = summarize_commits(commit_stats)
    print(json.dumps(summary))