from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import CommentForm, PostForm, ImageForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Image, Comment

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def handler403(request, exception):
    return render(request, '403.html', status=403)
def handler405(request, exception):
    return render(request, '405.html', status=405)

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 3  # Show 3 posts per page

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['image_form'] = ImageForm(self.request.POST, self.request.FILES)
        else:
            data['image_form'] = ImageForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['image_form']
        if image_form.is_valid():
            form.instance.author = self.request.user
            form.instance.slug = slugify(form.instance.title)
            self.object = form.save()
            for image in self.request.FILES.getlist('image'):
                Image.objects.create(post=self.object, image=image)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        images = post.images.all()
        liked = post.likes.filter(id=self.request.user.id).exists()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "images": images,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    @method_decorator(login_required)
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        images = post.images.all()
        liked = post.likes.filter(id=request.user.id).exists()

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            commented = True
            comment_form = CommentForm()
        else:
            commented = False

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "images": images,
                "commented": commented,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['image_form'] = ImageForm(self.request.POST, self.request.FILES)
        else:
            data['image_form'] = ImageForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['image_form']
        if image_form.is_valid():
            response = super().form_valid(form)
            for image in self.request.FILES.getlist('photo'):
                Image.objects.create(post=self.object, image=image)
            return response
        else:
            return self.form_invalid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser

class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
