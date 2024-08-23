from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from core.models import *

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label='Enter your email address', max_length=254)
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-field'}),
        help_text="We'll never share your email with anyone else.",
        label="Email Address"
    )
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Display Name', 'class': 'form-field'}),
        label="Display Name"
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
        label="Date of Birth"
    )
    gender = forms.ChoiceField(
        choices=[('gender', 'Gender'),('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        widget=forms.Select(attrs={'placeholder': 'Gender','class': 'form-field'}),
        label="Gender"
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-field'}),
        label="Phone"
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-field'}),
        label="Address"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-field'}),
        help_text="Enter a strong password.",
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-field'}),
        help_text="Enter the same password as above, for verification.",
        label="Confirm Password"
    )
    profile_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-field'}),
        label="Profile Image"
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'dob', 'gender', 'phone_number', 'address', 'profile_image']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose a username...', 'class': 'form-field'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter password...', 'class': 'form-field'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password...', 'class': 'form-field'}),
        }
        labels = {
            'username': "Username",
            'email': "Email Address",
            'password1': "Password",
            'password2': "Confirm Password",
            'full_name': "Display Name",
            'dob': "Date of Birth",
            'gender': "Gender",
            'phone_number': "Phone",
            'address': "Address",
            'profile_image': "Profile Image",
        }
        help_texts = {
            'username': "Choose a unique username for your account.",
        }

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username...', 'class': 'form-field'}),
        label="Username" 
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password...', 'class': 'form-field'}),
        label="Password"
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username...', 'class': 'form-field'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter password...', 'class': 'form-field'}),
        }
        labels = {
            'username': "Username",
            'password': "Password",
        }

# TaskForm
class TaskForm(forms.ModelForm):
    # Customizing the due_date field with a date picker widget, a label, and help text.
    due_date = forms.DateField(
        widget= forms.SelectDateWidget, # Using a date picker widget for the due_date field.
        label= "Due Date",  # Adding a label to make the form field user-friendly.
        help_text="Select the due date for the task."  # Adding a label to make the form field user-friendly.
    )
    class Meta:
        model = Task # indicate association with Task Model
        fields = ['title', 'description', 'due_date', 'category', 'priority', 'status', 'is_completed'] # Specifies the field to include in the form
        widgets = { #Customizes how specific field are rendered in home
            'title': forms.TextInput(attrs={'placeholder': 'Enter task title here...'}),  # Placeholder for title.
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter task description...'}),  # Placeholder and row size for description.
            'category': forms.Select(attrs={'class': 'form-control'}),  # Styling category dropdown.
            'priority': forms.Select(attrs={'class': 'form-control'}),  # Styling priority dropdown.
            'status': forms.Select(attrs={'class': 'form-control'}),  # Styling status dropdown.
        }
        labels = {
            'is_completed': "Task Completed",  # Custom label for is_completed field.
        }
        help_texts = {
            'priority': "Select the priority level for this task.",  # Help text for priority.
            'category': "Choose a category to organize your tasks.",  # Help text for category.
        }
# Explanation:
# - The `TaskForm` is tied to the `Task` model.
# - It includes important fields like title, description, due_date, category, priority, status, and is_completed.
# - We've added custom labels, help texts, and placeholders to make the form more intuitive.
# - Custom widgets are used for specific fields to enhance user interaction.

# ToDoList Form
class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ENter to-do list title..'}), # Placeholder for title.
            'description' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Enter a brief description...'}),  # Placeholder and row size for description.
        }
        labels = {
                'title': "To-Do List Title",  # Custom label for title.
            }
        help_texts = {
                'description': "Provide a brief overview of this to-do list.",  # Help text for description.
            }
# Explanation:
# - The `ToDoListForm` is tied to the `ToDoList` model.
# - It focuses on essential fields: title and description.
# - Custom widgets, labels, and help texts are used to make the form user-friendly.

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment...'}),  # Placeholder for text.
        }
        labels = {
            'text': "Comment",  # Custom label for text field.
        }
        help_texts = {
            'text': "Share your thoughts or feedback on the task.",  # Help text for the comment field.
        }
# Explanation:
# - The `CommentForm` is tied to the `Comment` model.
# - It includes the `text` field where users can enter their comments.
# - Custom widgets, labels, and help texts improve usability and guide the user.   

# UserProfile Form
class UserProfileForm(forms.ModelForm):
     # Customizing the birth_date field with a date picker widget, a label, and help text.
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget,  # Date picker widget for birth_date.
        label="Birth Date",  # Custom label for birth_date.
        help_text="Select your birth date."  # Help text for birth_date.
    )
    class Meta:
        model = UserProfile
        fields = ['bio', 'address', 'birth_date', 'age', 'email', 'gender', 'phone_number']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us something about yourself...'}),  # Placeholder for bio.
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address...'}),  # Placeholder for address.
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...'}),  # Placeholder for email.
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number...'}),  # Placeholder for phone number.
            'gender': forms.Select(attrs={'class': 'form-control'}),  # Styling gender dropdown.
        }
        labels = {
            'bio': "Biography",  # Custom label for bio.
            'phone_number': "Phone Number",  # Custom label for phone number.
        }
        help_texts = {
            'email': "We'll never share your email with anyone else.",  # Help text for email.
            'gender': "Select your gender.",  # Help text for gender.
        }
# Explanation:
# - The `UserProfileForm` is tied to the `UserProfile` model.
# - It captures comprehensive user details such as bio, address, birth_date, age, email, gender, and phone number.
# - The form includes custom widgets, labels, and help texts to make it easy to use and visually appealing.
  
 # Attachment Form
class AttachmentForm(forms.ModelForm):
   class Meta:
       model = Attachment
       fields = ['file', 'description', 'uploaded_at', 'task']
       widgets = {
           'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # Custom widget for file upload.
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter a description for the attachment...'}),  # Placeholder for description.
            'uploaded_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),  # Readonly datetime input for uploaded_at.
            'task': forms.Select(attrs={'class': 'form-control'}),  # Styling task dropdown.
       }   
       labels = {
            'file': "Attachment File",  # Custom label for file field.
            'description': "Description",  # Custom label for description field.
        }
       help_texts = {
            'file': "Upload a file related to this task.",  # Help text for file field.
            'task': "Select the task to which this attachment belongs.",  # Help text for task field.
        }
# Explanation:
# - The `AttachmentForm` is tied to the `Attachment` model.
# - It includes fields like file, description, uploaded_at, and task.
# - Custom widgets, labels, and help texts are provided to enhance the user experience.

# Reminder Form
class ReminderForm(forms.ModelForm):
    reminder_date = forms.DateField(
        widget=forms.SelectDateWidget,  # Date picker widget for reminder_date.
        label="Reminder Date",  # Custom label for reminder_date.
        help_text="Select the date you want to be reminded about this task."  # Help text for reminder_date.
    )
    reminder_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'placeholder': 'Enter reminder time...'}),  # Time input widget for reminder_time.
        label="Reminder Time",  # Custom label for reminder_time.
        help_text="Set the time for your reminder."  # Help text for reminder_time.
    )

    class Meta:
        model = Reminder
        fields = ['reminder_date', 'reminder_time', 'message', 'task']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter a reminder message...'}),  # Placeholder for message.
            'task': forms.Select(attrs={'class': 'form-control'}),  # Styling task dropdown.
        }
        labels = {
            'message': "Reminder Message",  # Custom label for message field.
        }
        help_texts = {
            'message': "Enter a short message to accompany this reminder.",  # Help text for message field.
            'task': "Select the task for which this reminder is being set.",  # Help text for task field.
        }
# Explanation:
# - The `ReminderForm` is tied to the `Reminder` model.
# - It includes fields like reminder_date, reminder_time, message, and task.
# - Custom widgets, labels, and help texts are included to make the form user-friendly.
