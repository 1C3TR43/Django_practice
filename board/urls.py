from django.urls import path
from board.views import BoardListView, BoardManageView, BoardRetrieveView, CommentListView

urlpatterns = [
    path('', BoardListView.as_view()),
    path('<int:id>/', BoardRetrieveView.as_view()),
    path('<int:id>/edit/', BoardManageView.as_view()),
    path('<int:board_id>/comment/', CommentListView.as_view()),
]