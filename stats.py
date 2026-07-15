import subprocess

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

if __name__ == '__main__':
    commit_stats = get_commit_stats()
    print(commit_stats)