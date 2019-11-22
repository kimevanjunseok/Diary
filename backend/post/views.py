from django.shortcuts import render

from .models import Post

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post

from .serializers import PostSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    content = request.data['content']
    imgfile = request.data['image']

    post = Post(content=content, imgfile=imgfile)
    post.save()
    
    return Response(status=status.HTTP_200_OK)

