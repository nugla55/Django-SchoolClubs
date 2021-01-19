from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    department_category = (
        ('Computer Engineering', 'Computer Engineering'),
        ('Software Engineering', 'Software Engineering'),
        ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'),
        ('Industrial Engineering', 'Industrial Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Civil  Engineering', 'Civil  Engineering'),
    )
    department = models.CharField(max_length=100, choices=department_category, blank=True, null=True)

    def __str__(self):
        return self.first_name


class Advisor(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    department = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.first_name


class Administration(models.Model):
    president = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='president', related_query_name='president')
    vicePresident = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='vicePresident', related_query_name='vicePresident')
    agent = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='agent', related_query_name='agent')
    accountant = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='accountant', related_query_name='accountant')
    secretary = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='secretary', related_query_name='secretary')


class Club(models.Model):
    club_name = models.CharField(max_length=150, )
    email = models.EmailField(blank=True)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, blank=True, null=True)
    club_pic = models.ImageField( null=True, blank=True, upload_to='images/')
    administration = models.OneToOneField(Administration, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.club_name

    @property
    def get_photo_url(self):
        if self.club_pic and hasattr(self.club_pic, 'url'):
            return self.club_pic.url
        else:
            return "/static/images/user.jpg"


class ClubStudent(models.Model):
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)


class Announcement(models.Model):
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    publisher = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)


class Survey(models.Model):
    end_date = models.DateTimeField(auto_now_add=False, null=True, blank=True, )
    question = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    element1 = models.CharField(max_length=50, blank=True, null=True)
    counter1 = models.IntegerField(default=0)
    element2 = models.CharField(max_length=50, blank=True, null=True)
    counter2 = models.IntegerField(default=0)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.question)


class Discussion(models.Model):
    topic = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    publisher = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, models.SET_NULL, blank=True, null=True)
    person = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )


class Posts(models.Model):
    publisher = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    content = models.TextField(blank=True, null=True)
    post_pic = models.ImageField(null=True, blank=True)


class MessageDialog(models.Model):
    sender = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True,
                               related_name='senders', related_query_name='sender')
    receiver = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True,
                                 related_name='receivers', related_query_name='receiver')
    content = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )

class Event(models.Model):
    publisher = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey(Club, models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
    until_date = models.DateTimeField(null=True, blank=True, )
    content = models.TextField(blank=True, null=True)
    event_name = models.CharField(max_length=150, null=True, blank=True, )
    location = models.CharField(max_length=150, null=True, blank=True, )


class Student_event(models.Model):
    attendee = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)


class Report(models.Model):
    reporter = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, null=True, blank=True, )
    content = models.TextField(blank=True, null=True)
    report_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, )
