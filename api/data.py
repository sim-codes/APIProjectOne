from datetime import datetime

class TextData:
    def __init__(self, name, language):
        self.name = name
        self.current_day = datetime.now().strftime("%A")
        self.language = language
        self.utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.github_file_url = "https://github.com/sim-codes/APIProjectOne/blob/main/api/data.py"
        self.github_repo_url = "https://github.com/sim-codes/APIProjectOne"
        self.status_code = 200
