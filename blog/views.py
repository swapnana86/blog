from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy  # new

# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()


class BlogListView(ListView):
    def get(self, request,):
        model = Post
        context_object_name = "posts"
        template_name = 'home.html'

        # logger.debug('FFFFFFFF')
        # logger.info('Start reading database')
        # # read database here
        # records = {'john': 55, 'tom': 66}
        # logger.debug('Records: %s', records)
        # logger.critical('Updating records ...')
        # # update records here
        # logger.info('Finish updating records')
        # logger.warning("WARNNNNinggsdgsg")

        return render(request, "home.html", {'posts': Post.objects.all()})


class BlogDetailView(DetailView):  # new
    # logger.debug('NOT work here, only with def')
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):  # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):  # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
