from django.shortcuts import render
from board.permissions import IsOwnerPermission
from rest_framework import generics

from board.models import Board, Comment
from board.serializers import BoardsSerializer, CommentSerializer
from board.pagenation import LargeResultsSetPagination

# Create your views here.
class BoardListView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardsSerializer
    pagination_class = LargeResultsSetPagination
    
    def get_queryset(self):
        queryset = Board.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__contains=title)
        return queryset
    
class BoardRetrieveView(generics.RetrieveAPIView):
    '''
    아무나 할 수 있는 상세 조회 API
    '''
    queryset = Board.objects.all()
    serializer_class = BoardsSerializer
    lookup_field = "id"
    
class BoardManageView(generics.RetrieveUpdateDestroyAPIView):
    '''
    작성자만 조회할 수 있는 상세 API
    '''
    queryset = Board.objects.all()
    serializer_class = BoardsSerializer
    lookup_field = "id"
    permission_classes = [IsOwnerPermission]
    
    # def get_queryset(self):
    #     pass
    
    # def get(self, request, *args, **kwargs):
    #     pass
    
    # def update(self, request, *args, **kwargs):
    #     pass
    
    # def destroy(self, request, *args, **kwargs):
    #     pass
    
class CommentListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pegination_class = LargeResultsSetPagination
    
    lookup_field = "board_id"
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        id = self.request.query_params.get('board_id')
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
    
    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)