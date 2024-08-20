from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# UserProfile Model
# This model extends the default Django User model to include additional user information.
class UserProfile(models.Model):
    gender_option = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User:")
    bio = models.TextField(blank=True, null=True, verbose_name="Your Bio:")
    address = models.CharField(max_length=100, blank=False, null=True, verbose_name="Your Address:")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Your BirthDate")
    age = models.CharField(max_length=2, null=True, blank=False, verbose_name="Your Age:")
    email = models.EmailField(max_length=1000, null=True, blank=False, verbose_name="Your Email address:")
    gender = models.CharField(max_length=1000, null=True, blank=False, choices=gender_option)
    phone_number = models.CharField(max_length=15, blank=False, null=True, verbose_name="Your Phone Number:")

    def __str__(self):
        return self.user.username

# Category Model
# This model represents a category that can be assigned to tasks, such as "Work" or "Personal".
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name", blank=False, null=True)
    description = models.TextField(blank=True, verbose_name="Category Description")

    def __str__(self):
        return self.name

# Priority Model
# This model represents the priority level of a task, such as "High", "Medium", or "Low".
class Priority(models.Model):
    name = models.CharField(max_length=50, verbose_name="Priority Level", blank=False, null=True)
    level = models.IntegerField(default=0, verbose_name="Priority Level (1-10)", blank=True, null=True)

    def __str__(self):
        return self.name

# Status Model
# This model represents the status of a task, such as "Pending", "In Progress", or "Completed".
class Status(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True, verbose_name="Status Name:")
    description = models.TextField(blank=True, null=True, verbose_name='Status Description')

    def __str__(self):
        return self.name

# ToDoList Model
# This model represents a to-do list that can contain multiple tasks.
class ToDoList(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True, verbose_name="List Title:")
    description = models.TextField(blank=True, null=True, verbose_name="List Description")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")

    def __str__(self):
        return self.title

# Task Model
# This model represents an individual task that belongs to a to-do list and can have a category, priority, and status.
class Task(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True, verbose_name="Task Title")
    description = models.TextField(blank=True, null=True, verbose_name="Task Description")
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, verbose_name="Priority Level")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status", default=1)
    is_completed = models.BooleanField(default=False, verbose_name="Completed")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Assigned User")
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title

# Comment Model
# This model allows users to comment on tasks, providing a way to leave notes or feedback.
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=True, verbose_name="Comment Text")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"

# Attachment Model
# This model allows files to be attached to tasks, such as documents or images.
class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Attachment for {self.task.title}"

# Reminder Model
# This model allows users to set reminders for tasks, which can notify them before the task's due date.
class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reminders")
    reminder_time = models.DateTimeField(verbose_name="Reminder Time")
    is_sent = models.BooleanField(default=False, verbose_name="Reminder Sent")

    def __str__(self):
        return f"Reminder for {self.task.title} at {self.reminder_time}"

# Tag Model
# This model allows tags to be assigned to tasks for better organization and filtering.
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tag Name", blank=False, null=True)
    tasks = models.ManyToManyField(Task, related_name="tags")

    def __str__(self):
        return self.name

# Notification Model
# This model represents notifications sent to users, such as reminders or updates about tasks.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Notification Message")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    is_read = models.BooleanField(default=False, verbose_name="Read")

    def __str__(self):
        return f"Notification for {self.user.username}"

# Activity Log Model
# This model tracks changes and actions performed on tasks, such as edits, completions, or deletions.
class ActivityLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="activity_logs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, verbose_name="Action Performed")
    timestamp = models.DateTimeField(default=timezone.now, verbose_name="Timestamp")

    def __str__(self):
        return f"{self.action} on {self.task.title} by {self.user.username}"
