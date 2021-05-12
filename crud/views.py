from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from .forms import *

# Create your views here.


def song(request):

    form = SongForm()

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            form = SongForm()

    song_list = Song.objects.all()

    return render(request, 'index.html', {'form': form, 'song_list': song_list})


def podcast(request):

    form = PodcastForm()

    if request.method == 'POST':
        form = PodcastForm(request.POST)
        if form.is_valid():
            form.save()
            form = PodcastForm()

    podcast_list = Podcast.objects.all()

    return render(request, 'podcast.html', {'form': form, 'podcast_list': podcast_list})


def audiobook(request):

    form = AudiobookForm()

    if request.method == 'POST':
        form = AudiobookForm(request.POST)
        if form.is_valid():
            form.save()
            form = AudiobookForm()

    audiobook_list = Audiobook.objects.all()

    return render(request, 'audiobook.html', {'form': form, 'audiobook_list': audiobook_list})


def songupdateform(request, pk):

    song_list = Song.objects.get(id=pk)

    form = SongForm(instance=song_list)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song_list)
        if form.is_valid():
            form.save()
            return redirect('song')

    return render(request, 'update.html', {'form': form})


def podcastupdateform(request, pk):

    podcast_list = Podcast.objects.get(id=pk)

    form = PodcastForm(instance=podcast_list)

    if request.method == 'POST':
        form = PodcastForm(request.POST, instance=podcast_list)
        if form.is_valid():
            form.save()
            return redirect('podcast')

    return render(request, 'update.html', {'form': form})


def audiobookupdateform(request, pk):

    audiobook_list = Audiobook.objects.get(id=pk)

    form = AudiobookForm(instance=audiobook_list)

    if request.method == 'POST':
        form = AudiobookForm(request.POST, instance=audiobook_list)
        if form.is_valid():
            form.save()
            return redirect('audiobook')

    return render(request, 'update.html', {'form': form})


def songdeleteform(request, pk):

    song_list = Song.objects.get(id=pk)
    song_list.delete()

    return redirect('song')


def podcastdeleteform(request, pk):

    podcast_list = Podcast.objects.get(id=pk)
    podcast_list.delete()

    return redirect('podcast')


def audiobookdeleteform(request, pk):

    audiobook_list = Audiobook.objects.get(id=pk)
    audiobook_list.delete()

    return redirect('audiobook')


@api_view(['GET'])
def songlist(request):

    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def podcastlist(request):

    podcasts = Podcast.objects.all()

    serializer = PodcastSerializer(podcasts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def audiobooklist(request):

    audiobooks = Audiobook.objects.all()
    serializer = AudiobookSerializer(audiobooks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def songdetail(request, pk):

    songs = Song.objects.get(id=pk)
    serializer = SongSerializer(songs, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def podcastdetail(request, pk):

    podcasts = Podcast.objects.get(id=pk)
    serializer = PodcastSerializer(podcasts, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def audiobookdetail(request, pk):

    audiobooks = Audiobook.objects.get(id=pk)
    serializer = AudiobookSerializer(audiobooks, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def songcreate(request):

    serializer = SongSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def podcastcreate(request):

    serializer = PodcastSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def audiobookcreate(request):

    serializer = AudiobookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def songupdate(request, pk):

    song = Song.objects.get(id=pk)

    serializer = SongSerializer(instance=song, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def podcastupdate(request, pk):

    podcast = Podcast.objects.get(id=pk)

    serializer = PodcastSerializer(instance=podcast, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def audiobookupdate(request, pk):

    audiobook = Audiobook.objects.get(id=pk)
    serializer = AudiobookSerializer(instance=audiobook, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def songdelete(request, pk):

    song = Song.objects.get(id=pk)
    song.delete()

    return Response("Song successfully deleted")


@api_view(['DELETE'])
def podcastdelete(request, pk):

    podcast = Podcast.objects.get(id=pk)
    podcast.delete()

    return Response("Podcast successfully deleted")


@api_view(['DELETE'])
def audiobookdelete(request, pk):

    audiobook = Audiobook.objects.get(id=pk)
    audiobook.delete()

    return Response("Audiobook successfully deleted")
