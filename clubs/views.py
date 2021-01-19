from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


def homepage(request):
    return render(request, 'clubs/home.html')

@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    from clubs.models import Club,Report

    reports = Report.objects.all()
    clubs = Club.objects.all()

    context = {'clubs':clubs, 'reports':reports}
    return render(request, 'clubs/home_admin.html', context)

@user_passes_test(lambda u: u.is_superuser)
def manage_club(request, pk):
    from clubs.models import Club, Report, ClubStudent

    club = Club.objects.get(id = pk)
    reports = Report.objects.all()
    clubs = Club.objects.all()
    administration = Club.administration
    students = ClubStudent.objects.filter(club=club)


    context = {'clubs': clubs, 'reports': reports, 'administration':administration, 'club':club, 'students':students}
    return render(request, 'clubs/manage_clubs.html', context)


def all_clubs(request):
    from clubs.models import Club
    allclubs = Club.objects.all()

    context = {'allclubs': allclubs}
    return render(request, 'clubs/allClubs.html', context)


def all_events(request):
    from clubs.models import Event
    allevents = Event.objects.all()

    context = {'allevents': allevents}
    return render(request, 'clubs/allEvents.html', context)

@login_required(login_url='login')
def my_clubs(request, pk):
    from clubs.models import ClubStudent, Student
    student = Student.objects.get(id = pk)
    myclubs = ClubStudent.objects.filter(student = student)
    print(myclubs)

    context = {'myclubs': myclubs}
    return render(request, 'clubs/myclubs.html', context)



@login_required(login_url='login')
def socialclubs(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    club = Club.objects.get(id=pk)


    user = request.user.student
    try:
        myclubs = ClubStudent.objects.filter(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None
    try:
        club = ClubStudent.objects.get(club=club, student=request.user.student)
    except ClubStudent.DoesNotExist:
        club = ClubStudent.objects.get(club=club)[0]


    context = {'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events':events}
    return render(request, 'clubs/SocialClubs.html', context)

@login_required(login_url='login')
def socialclubs_def(request):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()

    user = request.user.student
    try:
        myclubs = ClubStudent.objects.filter(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None

    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    context = {'allclubs': allclubs, 'myclubs': myclubs, 'events':events}
    return render(request, 'clubs/SocialClubs_def.html', context)

def announcement(request, pk):
    from clubs.models import Club,ClubStudent,Event
    allclubs = Club.objects.all()
    user = request.user.student
    club = Club.objects.get(id=pk)

    try:
        myclubs = ClubStudent.objects.filter(student=user)
        events = Event.objects.all()
    except ClubStudent.DoesNotExist:
        myclubs = None
    except Event.DoesNotExist:
        events = None

    announcements = club.event_set.all()

    try:
        club = ClubStudent.objects.get(club=club, student=request.user.student)
    except ClubStudent.DoesNotExist:
        club = ClubStudent.objects.filter(club=club)[0]

    context = {'announcements':announcements,'allclubs': allclubs, 'myclubs': myclubs, 'club':club, 'events':events}
    return render(request, 'clubs/announcements.html', context)



def post(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    user = request.user.student
    try:
        myclubs = ClubStudent.objects.filter(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None

    try:
        club = Club.objects.get(id=pk)
    except Club.DoesNotExist:
        club = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    posts = club.posts_set.all()
    try:
        club = ClubStudent.objects.get(club=club, student=request.user.student)
    except ClubStudent.DoesNotExist:
        club = ClubStudent.objects.filter(club=club)[0]

    context = {'posts': posts, 'allclubs': allclubs, 'myclubs': myclubs,'club':club, 'events':events}
    return render(request, 'clubs/posts.html', context)



def chat(request, pk):
    context = {}
    return render(request, 'clubs/chat.html')

def survey(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    user = request.user.student

    club = Club.objects.get(id=pk)

    try:
        myclubs = ClubStudent.objects.filter(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    surveys = club.survey_set.all()
    try:
        club = ClubStudent.objects.get(club=club, student=request.user.student)
    except ClubStudent.DoesNotExist:
        club = ClubStudent.objects.filter(club=club)[0]

    context = {'surveys': surveys, 'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events':events}
    return render(request, 'clubs/surveys.html', context)



def discussion(request, pk):
    from clubs.models import Club, ClubStudent, Event
    allclubs = Club.objects.all()
    user = request.user.student

    club = Club.objects.get(id=pk)

    try:
        myclubs = ClubStudent.objects.filter(student=user)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    discussions = club.discussion_set.all()
    try:
        club = ClubStudent.objects.get(club=club, student=request.user.student)
    except ClubStudent.DoesNotExist:
        club = ClubStudent.objects.filter(club=club)[0]

    context = {'discussions': discussions, 'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events': events}
    return render(request, 'clubs/discussions.html', context)

@user_passes_test(lambda u: u.is_superuser)
def addClub(request):
    from clubs.models import ClubStudent
    from clubs.forms import AddClubForm, AddAdministrationForm
    form= AddClubForm()
    form_administration = AddAdministrationForm()

    if request.method == "POST":
        form = AddClubForm(request.POST, request.FILES)
        form_administration = AddAdministrationForm(request.POST)
        if form.is_valid():
            addministration = form_administration.save()
            club = form.save()

            club.administration = addministration
            club.save()

            ClubStudent.objects.create(
                club=club,
                student=addministration.vicePresident
            )
            ClubStudent.objects.create(
                club=club,
                student=addministration.president
            )
            ClubStudent.objects.create(
                club=club,
                student=addministration.agent
            )
            ClubStudent.objects.create(
                club=club,
                student=addministration.accountant
            )
            ClubStudent.objects.create(
                club=club,
                student=addministration.secretary
            )

            return redirect('manage')

    context = {'form': form, 'form_administration':form_administration}
    return render(request, 'forms/addClub.html', context)

@user_passes_test(lambda u: u.is_superuser)
def removeClub(request, pk):
    from clubs.models import ClubStudent,Club,Administration

    club = Club.objects.get(id = pk)
    administration = club.administration
    ClubStudent.objects.filter(club = club).delete()
    administration.delete()
    club.delete()

    return redirect('manage')



def messages(request):
    return render(request, 'clubs/message.html')


def ccalendar(request):
    return render(request, 'clubs/ccalendar.html')


def clupDetail(request , pk):
    from clubs.models import Club
    club = Club.objects.get(id=pk)
    from clubs.models import ClubStudent
    administration = club.administration
    count = ClubStudent.objects.filter(club=club).count()

    context={'club' : club , 'count': count , 'administration' : administration}

    return render(request, 'clubs/detailPage.html' , context)

def eventPage(request, pk):
    from clubs.models import Event
    event = Event.objects.get(id=pk)
    from clubs.models import Student_event
    s_e = Student_event.objects.filter(event=event).all()

    students = []
    from clubs.models import Student
    for s in s_e:

        print(Student.objects.get(id=s.attendee.id))
        students.append(Student.objects.get(id=s.attendee.id))
    context = {'event': event, 'students': students, }

    return render(request, 'clubs/eventPage.html', context)


def joinEvent(request, pk):
    from clubs.models import Event
    event = Event.objects.get(id=pk)
    from clubs.models import Student_event
    Student_event.objects.create(
        event=event,
        attendee=request.user.student,
    )
    return redirect('eventPage', pk=pk)


def leaveEvent(request, pk):
    from clubs.models import Student_event
    from clubs.models import Event
    event = Event.objects.get(id=pk)
    Student_event.objects.get(event=event, attendee=request.user.student).delete()
    return redirect('eventPage', pk=pk)


def eventPageJoined(request):
    return render(request, 'clubs/eventPageJoined.html')

def userPage(request):
    student = request.user.student
    from clubs.forms import StudentForm
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

    from clubs.models import Student_event
    events = Student_event.objects.filter(attendee=request.user.student)
    from clubs.models import ClubStudent
    clubs = ClubStudent.objects.filter(student=request.user.student)
    posts = []
    from clubs.models import Club
    from clubs.models import Posts
    for club in clubs:
        c = Club.objects.get(id=club.club.id)
        posts.append(c.posts_set.all())
    context = {'events': events, 'posts': posts, 'form': form}
    return render(request, 'clubs/userpage.html', context)

def addEvent(request, pk):
    from clubs.models import Club, Posts
    club = Club.objects.get(id=pk)
    user = request.user.student

    from clubs.forms import addEventForm
    form = addEventForm()
    if request.method == "POST":
        form = addEventForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get("content")
            location = form.cleaned_data.get("location")
            event_name = form.cleaned_data.get("event_name")
            until_date = form.cleaned_data.get("until_date")

            from clubs.models import Event
            Event.objects.create(
                publisher=user,
                location=location,
                event_name=event_name,
                content=content,
                until_date=until_date,
                club=club,
            )

            return redirect('announcement', pk=club.id)

    context = {'form': form}
    return render(request, 'forms/addEvent.html', context)


def addPost(request, pk):
    from clubs.models import Club, Posts
    from clubs.forms import addPostForm

    user = request.user.student
    club = Club.objects.get(id=pk)

    form = addPostForm()
    if request.method == "POST":
        form = addPostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get("content")
            club_pic = form.cleaned_data.get("club_pic")


            Posts.objects.create(
                publisher = user,
                club = club,
                content = content,
                post_pic = club_pic,
            )

            return redirect('post', pk=club.id)

    context = {'form': form}
    return render(request, 'forms/addPost.html', context)



def addSurvey(request, pk):
    from clubs.models import Club,Survey
    from clubs.forms import addSurveyForm

    user = request.user.student
    club = Club.objects.get(id=pk)

    form = addSurveyForm()
    if request.method == "POST":
        form = addSurveyForm(request.POST)
        if form.is_valid():

            end_date = form.cleaned_data.get("end_date")
            question = form.cleaned_data.get("question")
            element1 = form.cleaned_data.get("element1")
            element2 = form.cleaned_data.get("element2")

            Survey.objects.create(
                end_date = end_date,
                question = question,
                publisher = user,
                element1 = element1,
                element2 = element2,
                counter1 = 0,
                counter2 = 0,
                club = club,
            )

            return redirect('survey', pk=club.id)

    context = {'form': form}
    return render(request, 'forms/addSurvey.html', context)




def addDiscussion(request, pk):
    from clubs.models import Club, Discussion
    from clubs.forms import addDiscussionForm

    user = request.user.student
    club = Club.objects.get(id=pk)

    form = addDiscussionForm()
    if request.method == "POST":
        form = addDiscussionForm(request.POST)
        if form.is_valid():

            topic = form.cleaned_data.get("topic")
            content = form.cleaned_data.get("content")

            Discussion.objects.create(
                topic = topic,
                content = content,
                club = club,
                publisher = user,
            )
            return redirect('discussion', pk=club.id)

    content = {'form': form}
    return render(request, 'forms/addDiscussion.html', content)

def join(request, pk):
    from clubs.models import ClubStudent,Student,Club

    student = request.user.student
    club = Club.objects.get(id=pk)

    if len(ClubStudent.objects.filter(club=club, student=student)) == 0:
        ClubStudent.objects.create(
            club = club,
            student = student,
        )
        return redirect('socialclubs', pk=club.id)
    return redirect('socialclubs', pk=club.id)

def leave(request, pk):
    from clubs.models import ClubStudent,Club, Event

    student = request.user.student
    club = Club.objects.get(id=pk)
    ClubStudent.objects.get(club = pk, student = student).delete()

    allclubs = Club.objects.all()

    try:
        myclubs = ClubStudent.objects.filter(student=student)
    except ClubStudent.DoesNotExist:
        myclubs = None
    try:
        events = Event.objects.all()
    except Event.DoesNotExist:
        events = None

    try:
        club = ClubStudent.objects.get(club=club, student=request.user.student)
    except ClubStudent.DoesNotExist:
        club = ClubStudent.objects.filter(club=club)[0]

    context = {'allclubs': allclubs, 'myclubs': myclubs, 'club': club, 'events': events}
    return render(request, 'clubs/SocialClubs.html', context)


def report(request):
    return render(request, 'forms/report.html')