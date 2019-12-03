from django.shortcuts import render, get_object_or_404

from .models import Post

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post

from .serializers import PostSerializer, PostUpdateSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    print(request)
    content = request.data['content']
    imgfile = request.data['image']

    post = Post(content=content, imgfile=imgfile)
    post.save()
    
    return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH'])
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = PostUpdateSerializer(post)
    if request.method == 'GET':
        return Response(serializer.data)
    
    if request.method == 'PATCH':
        post.content = request.data['content']
        if request.data['image'] != 'null':
            post.imgfile = request.data['image']
        post.save()
        return Response(status=status.HTTP_200_OK)