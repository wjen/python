from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Easiest way to restrict access using function-based views is with decorator
from django.contrib.auth.decorators import login_required
# For class-based views use Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available copies of books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context={'num_books': num_books, 'num_instances': num_instances,
                'num_instances_available': num_instances_available, 'num_authors': num_authors,
                'num_visits': num_visits}
                
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

class BookDetailView(generic.DetailView):
    # Within the template you can access the list of books with the template variable named object OR book
    model = Book

# Impleted with the function view below:
# def book_detail_view(request, primary_key):
#     try:
#         book = Book.objects.get(pk=primary_key)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')
    
#     return render(request, 'catalog/book_detail.html', context={'book': book})

# An alternate way to do the above
# from django.shortcuts import get_object_or_404

# def book_detail_view(request, primary_key):
#     book = get_object_or_404(Book, pk=primary_key)
#     return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorsListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author