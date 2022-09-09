from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import BookMark
# Create your views here.


class BookmarkLV(ListView):
    model = BookMark


class BookmarkDV(DetailView):
    model = BookMark


