from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import status

from notices.models import Notice, NoticeSerializer, UserComment, UserCommentSerializer

# Create your views here.
# For announcement of notice
class FetchAllNotice(APIView):
    def get(self, request: Request):
        notice_list = list()
        for notice in Notice.objects.all():
            notice_list.append(NoticeSerializer(notice).data)

        return Response(notice_list, status=status.HTTP_200_OK)
    

class CommentsHandle(APIView):
    def get(self, request: Request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        content_comments = list()
        for comment in UserComment.objects.filter(notice=notice):
            content_comments.append(UserCommentSerializer(comment).data)

        return Response({"comments": content_comments, "notice": NoticeSerializer(notice).data}, status=status.HTTP_200_OK)
    
    def post(self, request: Request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        request_body = request.data
        new_comment_body = request_body.get('newComment')

        # new_comment = UserComment.objects.create(new_comment_body)

        return Response({"message": "Comment send success!"}, status=status.HTTP_200_OK)