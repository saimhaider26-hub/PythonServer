from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# This function handles the request
def hello_world(request):
    return HttpResponse("Hello Saim! This is Django running on your custom server.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello_world),  # This tells Django: "If user asks for /hello, run the function above"
]