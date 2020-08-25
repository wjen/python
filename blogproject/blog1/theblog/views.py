from django.shortcuts import render, get_object_or_404
# listivew for all, detailview for single
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request, 'theblog/home.html', {})
# class based views querys database for us

# object_list


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'theblog/add_comment.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # post_id is from the model due to post as foreign key
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    like = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        like = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'theblog/home.html'
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'theblog/category_list.html', {
        'cat_menu_list': cat_menu_list
    })
# match cats in the url


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    cat_menu = Category.objects.all()
    return render(request, 'theblog/categories.html', {
        'cats': cats.title().replace('-', ' '), 'category_posts': category_posts,
        'cat_menu': cat_menu
    })


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context = super().get_context_data(** kwargs)

        liked = False
        # can get the request through self.request
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context['liked'] = liked
        context["total_likes"] = total_likes
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'theblog/add_post.html'
    # takes all the fields from the post model
    # not going to use any now that we are using postform, one or the other
    # fields = '__all__'
    # fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'theblog/update_post.html'
    # fields = ['title', 'title_tag', 'body']


class AddCategoryView(CreateView):
    model = Category
    # form_class = CategoryPost
    template_name = 'theblog/add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'theblog/update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'theblog/delete_post.html'
    # use reverse_lazy for delete
    success_url = reverse_lazy('home')
