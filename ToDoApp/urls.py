"""
URL configuration for ToDoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import *

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # Index Page: The landing page for the application. 
    path('', index, name = 'index'),
    
    #Homepage for aunthenticated users# Homepage for Authenticated Users: Displays to-do lists and pending tasks for logged-in users.
    path('home/', homepage, name='home'),
    
    #About Us and Contact US 
    path("about/", about_us, name="about_us"),   
    path("contact/", contact_us, name="contact_us"),
    
    #User signup, login, and logout
    path('signup/', signup, name='signup'),  # User Signup: Route for user registration. Handles user creation and profile setup.
    path('login/', login, name='login'),  # User Login: Route for user login using Django's built-in authentication view
    path('logout/', user_logout, name='logout'),  # User Logout: Route for user logout using Django's built-in authentication view
     
    # User Profile: Allows users to view and update their profile information.
    path('userprofile/', userprofile, name='userprofile'),
    
    #To-DO List Operations
    path('todolist/',view_all_todolists, name='view_all_todolists'), # View All To-Do Lists: Displays all to-do lists for the authenticated user.
    path('todolist/create/',create_todolist, name='create_todolist'), # Create To-Do List: Form for creating a new to-do list associated with the logged-in user
    path('todolist/update/<int:pk>/', update_todolist, name='update_todolist'), # Update To-Do List: Form for updating an existing to-do list. Restricted to the list owner.
    path('todolist/delete/<int:pk>/', delete_todolist, name='delete_todolist'), # Delete To-Do List: Confirmation and deletion of a specific to-do list

    #Task Management
    path('task/delete/<int:pk>/' , delete_task, name='delete_task'), # Delete Task: Confirmation and deletion of a specific task.
    path('tasks/<int:pk>/',view_all_tasks, name='view_all_tasks'), # View All Tasks: Displays all tasks, with an option to filter by completion status.
    path('task/create/<int:pk>/', create_task, name='create_task'),  # Create Task: Form for creating a new task within a specific to-do list.
    path('task/update/<int:pk>/', update_task, name='update_task'), # Update Task: Form for updating an existing task. The task must be associated with the logged-in user.
    path('task/complete/<int:pk>/', mark_task_complete, name='mark_task_complete'), # Mark Task Complete: Allows the user to mark a task as completed.

    # Comments, Attachments, Reminders
    path('task/<int:pk>/comment/', add_comment, name='add_comment'), # Add Comment: Form for adding a comment to a specific task.
    path('task/<int:pk>/attachment/', add_attachment, name='add_attachment'), # Add Attachment: Form for adding an attachment to a specific task.
    path('task/<int:pk>/reminder/', add_reminder, name='add_reminder'), # Add Reminder: Form for setting a reminder for a specific task.
    
    # Notifications and Activity Log
    path('notifications/', notifications, name='notifications'), # Notifications: Displays unread notifications for the user and marks them as read.
    path('activity-log/', activity_log, name='activity_log'), # Activity Log: Shows the user's activity log, detailing actions on tasks and to-do lists.
  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
