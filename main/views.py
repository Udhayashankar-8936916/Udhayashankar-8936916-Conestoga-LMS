from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from django.contrib.auth import get_user, logout
from django.contrib import messages
from login.models import User
from .models import Book


#Continue by: Extending the Edit Profile link for a non-admin user

def home(request):

    user = get_user(request)
    if not user.is_authenticated:
        messages.error(request, 'Sorry, you cannot go to this page if you are not logged in')
        return redirect('login')

   
    
    return render(request, 'main/home.html', {"user": user})

def issue_books(request):
    user = get_user(request)

    # users2 = User.objects.all()

    users = [User.objects.get(id=user.id)]

    books = Book.objects.filter(is_issued=False)

    if request.method == 'POST':

        student_name = request.POST.get('studentList')
        book_title = request.POST.get('bookList')

        user = User.objects.get(name = student_name)
        book = Book.objects.get(title = book_title)

        if not book.is_issued:
            book.user = user
            book.is_issued = True
            book.issue_date = datetime.now()
            return_date = datetime.now() + timedelta(days=15)
            book.return_date = return_date
            book.save()
            messages.success(request, f'This book has been issues to { user.name }')
            return redirect('issue_book')

        else:
            messages.error(request, 'This book has already been issued to someone')
            return redirect('issue_book')




    return render(request, "main/issue book.html", {"users":users ,"books":books})
def issue_books1(request):
    user = get_user(request)

    # users2 = User.objects.all()

    users = User.objects.all()

    books = Book.objects.filter(is_issued=False)

    if request.method == 'POST':

        student_name = request.POST.get('studentList')
        book_title = request.POST.get('bookList')

        user = User.objects.get(name = student_name)
        book = Book.objects.get(title = book_title)

        if not book.is_issued:
            book.user = user
            book.is_issued = True
            book.issue_date = datetime.now()
            book.save()
            messages.success(request, f'This book has been issues to { user.name }')
            return redirect('issue_book1')

        else:
            messages.error(request, 'This book has already been issued to someone')
            return redirect('issue_book1')




    return render(request, "main/issue book1.html", {"users":users ,"books":books})

def add_new_book(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')

        #Check if the title field is empty or less than 3 characters
        if len(title) < 3 :

            messages.error(request, 
            'The title field cannot be empty or less than 3 characters')
            return redirect('new_book')

        if len(author) < 3:
            messages.error(request, 
            'The author field cannot be empty or less than 3 characters')
            return redirect('new_book')

        if len(isbn) < 10 or len(isbn) > 13:
            messages.error(request, 
            'The ISBN must be at least 10-13 characters, this field should not be empty')
            return redirect('new_book')

        
        new_book = Book.objects.create(title = title, author = author, isb_number = isbn)
        new_book.save()
        messages.success(request, 'A new book has been added')
        return redirect('new_book')


    return render(request, "main/new book.html")

def view_books(request):

    books = Book.objects.all()
    user = get_user(request)

    return render(request, 'main/book view.html', {"books": books, 'user': user})

def available_books(request):

    
    books = Book.objects.all()
    return render(request, 'main/available books.html', {"books": books})

def update_profile_pic(request):

    user = get_user(request)
    if request.method == 'POST':

        if len(request.FILES) != 0:
            user.profile_picture = request.FILES['file']
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.student_number = request.POST.get('student_number')
            # user.password = request.POST.get('password')
            user.save()
            messages.success(request, 'Profile Picture has been updated')
            return redirect('update_profile')
        else:
            messages.error(request, 'There is no file part')
            return redirect('update_profile')


    return render(request, 'main/update profile.html', {"user": user})

def update_profile_pic1(request):

    user = get_user(request)
    if request.method == 'POST':

        if len(request.FILES) != 0:
            user.profile_picture = request.FILES['file']
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, 'Profile Picture has been updated')
            return redirect('update_profile1')
        else:
            messages.error(request, 'There is no file part')
            return redirect('update_profile1')


    return render(request, 'main/update profile1.html', {"user": user})


def delete_user(request, Book_id):
    user = Book.objects.all(Book, id = Book_id)
    user.delete()
    return redirect('remove_issue')


# def remove_issue(request, book_id):

#     book = Book.objects.get(id=book_id)

#     if book.is_issued:
#         book.user = None
#         book.is_issued = False
#         book.save()
#         messages.success(request, f'The issue for {book.title} has been removed')
#     else:
#         messages.error(request, 'This book is not currently issued')

#     return redirect('remove_issue')


def remove_issue(request):
    user = get_user(request)

    users = [User.objects.get(id=user.id)]
    books = Book.objects.filter(user=user)

    if request.method == 'POST':
        student_name = request.POST.get('studentList')
        book_title = request.POST.get('bookList')

        user = User.objects.get(name=student_name)
        book = Book.objects.get(title=book_title)

        if book.is_issued:
            if (book.return_date- book.issue_date).days > 15:
                book.user = None
                book.is_issued = False
                book.returened_date = datetime.now()
                book.fine = 20  # Assuming a fine of 20 units
                book.save()
                messages.success(request, f'This book has been Removed with a fine of 20 units')
            else:
                book.user = None
                book.is_issued = False
                book.returened_date = datetime.now()
                book.fine = 0
                book.save()
                messages.success(request, f'This book has been Removed')
        else:
            messages.error(request, 'This book is not issued')

        return redirect('issue_book')

    return render(request, "main/remove issue.html", {"users": users, "books": books})

def remove_issue1(request):
    books = Book.objects.filter(is_issued=True)

    if request.method == 'POST':
        student_name = request.POST.get('studentList')
        book_title = request.POST.get('bookList')

        # user = User.objects.get(name=student_name)
        book = Book.objects.get(title=book_title)

        if book.is_issued:
            if (book.return_date- book.issue_date).days > 15:
                book.user = None
                book.is_issued = False
                book.returened_date = datetime.now()
                book.fine = 20  # Assuming a fine of 20 units
                book.save()
                messages.success(request, f'This book has been Removed with a fine of 20 units')
            else:
                book.user = None
                book.is_issued = False
                book.returened_date = datetime.now()
                book.fine = 0
                book.save()
                messages.success(request, f'This book has been Removed')
        else:
            messages.error(request, 'This book is not issued')

        return redirect('remove_issue1')

    return render(request, "main/remove issue1.html", {"books": books})




def remove_book(request, id):
    removed_book = Book.objects.get(id = id)
    removed_book.delete()
    return redirect('av_book')

def logout_user(request):

    logout(request)
    return redirect('login')

def view_student(request):
    user = get_user(request)

    # users2 = User.objects.all()

    users = User.objects.all()

    books = Book.objects.filter(is_issued=False)

    if request.method == 'POST':

        student_name = request.POST.get('studentList')
        book_title = request.POST.get('bookList')

        user = User.objects.get(name = student_name)
        book = Book.objects.get(title = book_title)

        if not book.is_issued:
            book.user = user
            book.is_issued = True
            book.issue_date = datetime.now()
            book.fine = 0
            book.save()
            messages.success(request, f'This book has been issues to { user.name }')
            return redirect('slist')

        else:
            messages.error(request, 'This book has already been issued to someone')
            return redirect('slist')




    return render(request, "main/slist.html", {"users":users ,"books":books})
