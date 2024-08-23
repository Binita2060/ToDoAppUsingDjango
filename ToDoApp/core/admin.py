from django.contrib import admin
from core.models import *

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Category, Priority, Status, ToDoList, Task, Comment, Attachment, Reminder, Tag, Notification, ActivityLog

# Register your models here.
# The following lines register the models with the Django admin site, making them manageable through the admin interface.

# Registering the UserProfile model allows for the management of user profiles within the admin interface.
admin.site.register(UserProfile)

# Registering the Category model to manage different categories that tasks can belong to.
admin.site.register(Category)

# Registering the Priority model to define and manage priority levels for tasks.
admin.site.register(Priority)

# Registering the Status model to manage the different statuses that tasks can have.
admin.site.register(Status)

# Registering the ToDoList model to manage lists of tasks owned by different users.
admin.site.register(ToDoList)

# Registering the Task model to manage individual tasks within the admin interface.
admin.site.register(Task)

# Registering the Comment model to manage user comments on tasks.
admin.site.register(Comment)

# Registering the Attachment model to manage file attachments associated with tasks.
admin.site.register(Attachment)

# Registering the Reminder model to manage reminders set for tasks.
admin.site.register(Reminder)

# Registering the Tag model to manage tags that can be associated with tasks.
admin.site.register(Tag)

# Registering the Notification model to manage notifications sent to users.
admin.site.register(Notification)

# Registering the ActivityLog model to keep track of actions performed on tasks.
admin.site.register(ActivityLog)
