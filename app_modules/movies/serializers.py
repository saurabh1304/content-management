from rest_framework import serializers

from app_modules.movies.models import Cast, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "runtime", "language", "tagline", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ["id", "name", "gender", "dob", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class MovieDetailSerializer(serializers.ModelSerializer):
    cast = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "runtime", "language", "tagline", "cast", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_cast(self, obj):
        return CastSerializer(obj.cast_set.all(), many=True).data


class CastDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ["id", "movie", "name", "gender", "dob", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
