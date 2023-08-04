from rest_framework import serializers

from board.models import Board, Comment

class BoardsSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        read_only = True,
        slug_field='username'
    )
    
    class Meta:
        model = Board
        fields = ['id', 'writer', 'title', 'contents', 'created_at']
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'board', 'user', 'comment', 'created_at']