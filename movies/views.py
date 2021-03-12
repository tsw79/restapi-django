from django.http import Http404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views  import APIView

# 
# MovieList class returns a collection of resources
# 
class MovieList(APIView):

  # 
  # Get all tutorials 
  def get(self, request, format=None):
    movies = Movie.objects.all()
    title = request.GET.get('title', None)

    # search functionality
    if title is not None:
      movies = movies.filter(title__icontains=title)
    
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)  # 'safe=False' for objects serialization

  # 
  # Creates a new movie
  def post(self, request, format=None):
    request_data = JSONParser().parse(request)
    serializer = MovieSerializer(data=request_data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 
# MovieDetail class modifies and returns a single instance
# 
class MovieDetail(APIView):

  # 
  # Checks if the given key exists
  def get_object(self, pk):    
    try:
      return Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      raise Http404

  # 
  # Retrieves a single object
  def get(self, request, pk, format=None):
    movie = self.get_object(pk)
    serializer = MovieSerializer(movie) 
    return JsonResponse(serializer.data) 

  # 
  # Updates a single object
  def put(self, request, pk, format=None):
    movie = self.get_object(pk)
    request_data = JSONParser().parse(request) 
    serializer = MovieSerializer(movie, data=request_data) 
    if serializer.is_valid(): 
      serializer.save() 
      return JsonResponse(serializer.data) 
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

  # 
  # Updates a single object
  def delete(self, request, pk, format=None):
    movie = self.get_object(pk)
    movie.delete() 
    return JsonResponse({'message': 'Movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
