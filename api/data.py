from datetime import datetime

class TextData:
    def __init__(self, name, language):
        self.name = name
        self.current_day = datetime.now().strftime("%A")
        self.language = language
        self.utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.github_file_url = "testing.com"
        self.github_repo_url = "testing.com"
        self.status_code = 200
