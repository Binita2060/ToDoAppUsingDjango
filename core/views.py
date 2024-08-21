from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.core.paginator import Paginator

from core.models import *
from core.forms import *

# Create your views here.

#IndexPage view- this is the landing page
def index(request):
    return render(request, 'ToDoApp/index.html')

# Homepage view--# This view renders the home page for authenticated users, showing their to-do lists and pending tasks.
# If the user is not authenticated, it renders the landing page.
def homepage(request):
    if request.user.is_authenticated:
        todo_lists = ToDoList.objects.filter(user=request.user).select_related('user')
        tasks = Task.objects.filter(user = request.user, is_completed=False).order_by('due_date')
        context = {
            'todo_lists': todo_lists,
            'tasks':tasks
        }
        return render(request=request, template_name="ToDoApp/home.html", context=context)
    else:
        return render(request=request, template_name='ToDoApp/index.html')

# Signup view--This view handles user registration. It creates a new user and their associated profile. 
def signup(request):
    the_form = SignupForm()
    if request.method == 'POST':
        the_form = SignupForm(request.POST)
        if the_form.is_valid():
            user = the_form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    context = {
        'the_form': the_form
    }
    return render(request=request, template_name='ToDoApp/signup.html', context=context)
  
# Login View-This view handles user login. It uses Django's built-in authentication view.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return auth_views.LoginView.as_view(template_name='ToDoApp/login.html')(request)  

#UserProfile View-- This view allows the user to view and update their profile. It is accessible only to authenticated users.
@login_required
def profile(request):
    current_profile = get_object_or_404(UserProfile, user = request.user)
    if request.method == 'POST':
        the_form = UserProfileForm(request.POST, instance=current_profile)
        if the_form.is_valid():
            the_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('userprofile')
    else:
        the_form = UserProfileForm(instance=current_profile)
    context = {
        'the_form': the_form,
        'user_profile': current_profile
    }
    return render(request=request, template_name='ToDoApp/userprofile.html', context=context)   

# Get_todolist_details-- This view displays the details of a specific to-do list, including its tasks.
@login_required
def view_all_todolists(request):
    all_todolists = ToDoList.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(all_todolists, 10)  # Show 10 lists per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'todolists': page_obj,
    }
    return render(request=request, template_name='ToDoApp/view_all_todolists.html', context=context)

# Create_todolist-This view allows the user to create a new to-do list. The list is associated with the currently logged-in user.
@login_required
def create_todolist(request):
    the_form = ToDoListForm()
    if request.method == 'POST':
        the_form = ToDoListForm(request.POST)
        if the_form.is_valid():
            todo_list = the_form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            messages.success(request, 'To-Do List created successfully!')
            return redirect('view_all_todolists')
    context = {
            'the_form':the_form
        }
    render(request=request, template_name='ToDoApp/create_todolist.html', context=context)
 
# Update_todolist View -- This view allows the user to update an existing to-do list. It is restricted to the list owner.
@login_required
def update_todolist(request,pk):
    current_todolist_to_update = get_object_or_404(ToDoList,id=pk, user=request.user)
    the_updated_form = ToDoListForm(instance=current_todolist_to_update)
    if request.method == 'POST':
        the_updated_form = ToDoListForm(request.POST, instance=current_todolist_to_update)
        if the_updated_form.is_valid():
            the_updated_form.save()
            messages.success(request, 'To Do List updated successfully!')
            return redirect('view_all_todolists')
    else:
        the_updated_form = ToDoListForm(instance=current_todolist_to_update)
    context = {
        'the_form': the_updated_form,
        'todolist': current_todolist_to_update
    }
    return render(request=request, template_name='ToDoApp/update_todolist.html', context=context)

# Delete To_Do List View -- This view allows the user to delete an existing to-do list. It prompts for confirmation before deletion.
@login_required
def delete_todolist(request,pk):
    current_todolist = get_object_or_404(ToDoList, id=pk)
    if request.method == "POST":
        current_todolist.delete()
        messages.success(request, 'To-Do List deleted successfully!')
        return redirect('view_all_todolists')
    context = {
        'todolist':current_todolist
    }
    return render(request=request, template_name='ToDoApp/delete_todolist.html', context=context)

# Get_Task_Details -- vThis view displays the details of a specific task, including its comments and attachments.
@login_required
def view_all_tasks(request):
    # Fetch tasks based on completion status (default: not completed)
    is_completed = request.GET.get('is_completed', 'false').lower() == 'true'
    all_tasks = Task.objects.filter(user=request.user).order_by('due_date')
    context = {
        'tasks': all_tasks,
    }
    return render(request=request, template_name='ToDoApp/view_all_tasks.html', context=context)

# Utility function to get user's tasks, so it will be used only for view_all tasks
def get_user_tasks(user, is_completed=False):
    return Task.objects.filter(user=user, is_completed=is_completed).order_by('due_date')

# Create_Task_View -- This view allows the user to create a new task within a specific to-do list.
@login_required
def create_task(request):
    current_todolist = get_object_or_404(ToDoList, user=request.user)
    the_form = TaskForm()
    if request.method == "POST":
        the_form = TaskForm(request.POST)
        if the_form.is_valid():
            task = the_form.save(commit=False)  # Create task instance but don't save to DB yet
            task.user = request.user  # Assign the logged-in user
            task.todo_list = current_todolist
            task.save()  # Now save the task with the user assigned
            messages.success(request, 'Task created successfully!')
            return redirect('view_all_tasks')
    context = {
        'the_form': the_form,
        'todolist': current_todolist
    }
    return render(request=request, template_name="add_task.html", context=context)

#Update Task View --  This view allows the user to update an existing task. The task is linked to the to-do list it belongs to.
@login_required
def update_task(request,pk):
    current_task_to_update = get_object_or_404(Task, id=pk, user=request.user)
    the_updated_form = TaskForm(instance=current_task_to_update)
    if request.method == 'POST':
        the_updated_form = TaskForm(request.POST, instance=current_task_to_update)
        if the_updated_form.is_valid():
            the_updated_form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('view_all_tasks')
    else:
        the_updated_form = TaskForm(instance=current_task_to_update)
    context = {
        'the_form': the_updated_form,
        'task': current_task_to_update
    }
    return render(request=request, template_name='ToDoApp/update_task.html', context=context)

# Delete_Task_View -- This view allows the user to delete an existing task. A confirmation is requested before deletion.
@login_required
def delete_task(request,pk):
    current_task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        current_task.delete()
        messages.success(request, 'Task deleted successfully..!')
        return redirect('view_all_tasks')
    context = {
        'task': current_task
    }
    return render(request=request, template_name='ToDoApp/delete_task.html', context=context) 

# Mark Task Complete View-- This view allows the user to mark a task as completed. The task is then updated accordingly.
@login_required
def mark_task_complete(request, pk):
    current_task = get_object_or_404(Task, id=pk, user=request.user)
    current_task.is_completed = True
    current_task.save()
    messages.success(request, 'Task marked as completed!')
    return redirect('get_todolist_detail', pk=current_task.todo_list.pk)

# AddComment View -- This view allows the user to add a comment to a specific task.
@login_required
def add_comment(request, pk):
    current_task = get_object_or_404(Task, id=pk, user=request.user)
    the_form = CommentForm()
    if request.method == 'POST':
        the_form = CommentForm(request.POST)
        if the_form.is_valid():
            comment = the_form.save(commit=False)
            comment.task = current_task
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('view_all_tasks')
    context = {
        'the_form': the_form,
        'task': current_task
    }
    return render(request=request, template_name='ToDoApp/add_comment.html', context=context)

# Add Attachment View -- This view allows the user to add an attachment to a specific task. Files are uploaded and linked to the task.
@login_required
def add_attachment(request, pk):
    current_task = get_object_or_404(Task, id=pk, user=request.user)
    the_form = AttachmentForm()
    if request.method == 'POST':
        the_form = AttachmentForm(request.POST, request.FILES)
        if the_form.is_valid():
            attachment = the_form.save(commit=False)
            attachment.task = current_task
            attachment.save()
            messages.success(request, 'Attachment added successfully!')
            return redirect('view_all_tasks')
    context = {
        'the_form': the_form,
        'task': current_task
    }
    return render(request=request, template_name='ToDoApp/add_attachment.html', context=context)

# Add Remindwe View -- This view allows the user to set a reminder for a specific task.
def add_reminder(request, pk):
    current_task = get_object_or_404(Task, id=pk, user=request.user)
    the_form = ReminderForm()
    if request.method == 'POST':
        the_form = ReminderForm(request.POST)
        if the_form.is_valid():
            reminder = the_form.save(commit=False)
            reminder.task = current_task
            reminder.save()
            messages.success(request, 'Reminder set successfully!')
            return redirect('view_all_tasks')
    context = {
        'the_form': the_form,
        'task': current_task
    }
    return render(request=request, template_name='ToDoApp/add_reminder.html', context=context)

# Notification View -- his view displays unread notifications for the user. Notifications are marked as read once viewed.
@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user, is_read=False)
    for notification in user_notifications:
        notification.is_read = True
        notification.save()
    context = {
        'notifications': user_notifications
    }
    return render(request=request, template_name='ToDoApp/notifications.html', context=context)

# Activity log View -- his view displays the user's activity log, showing their actions on tasks and lists.
@login_required
def activity_log(request):
    log_entries = ActivityLog.objects.filter(user=request.user).order_by('-timestamp')
    context = {
        'log_entries': log_entries
    }
    return render(request=request, template_name='ToDoApp/activity_log.html', context=context)
