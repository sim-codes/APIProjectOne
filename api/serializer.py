from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    current_day = serializers.DateField()
    utc_time = serializers.DateTimeField()
    language = serializers.CharField(max_length=100)
    github_file_url = serializers.CharField(max_length=200)
    github_repo_url = serializers.CharField(max_length=200)
    status_code = serializers.IntegerField()