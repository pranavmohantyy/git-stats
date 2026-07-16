# Git Stats

Analyze a git repository's commit history with contributor stats and trends.

## Usage

Run the script by providing the repository path and optional filters:

```bash
python stats.py --repo_path /path/to/repo --author_name "Author Name" --since_date "2023-01-01"
```

## Example Output

```plaintext
commit_hash|author_name|author_email|commit_date|commit_message
abcd123|John Doe|john@example.com|2023-01-15 10:00:00|Initial commit
1234efg|Jane Smith|jane@example.com|2023-01-20 14:30:00|Added new feature
```

## Requirements
- Python 3.x
- matplotlib

## License
MIT
