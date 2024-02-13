from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    """
    Serializer class for data objects.

    This serializer is used to validate and serialize data objects before they are
    stored or returned in the API responses.

    Attributes:
        name (CharField): The name of the data.
        current_day (DateField): The current day of the data.
        utc_time (DateTimeField): The UTC time of the data.
        language (CharField): The language of the data.
        github_file_url (URLField): The URL of the data file on GitHub.
        github_repo_url (URLField): The URL of the GitHub repository.
        status_code (IntegerField): The status code of the data.

    """

    name = serializers.CharField(max_length=200)
    current_day = serializers.DateField()
    utc_time = serializers.DateTimeField()
    language = serializers.CharField(max_length=100)
    github_file_url = serializers.URLField(max_length=250)
    github_repo_url = serializers.URLField(max_length=250)
    status_code = serializers.IntegerField()