from django.shortcuts import render, redirect
from clubs.models import Student


# Create your views here.
def registerPage(request):
    from accounts.forms import SignupForm
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            eml = form.cleaned_data.get('email')
            dep = form.cleaned_data.get('dep')
            Student.objects.create(
                user=user,
                first_name=firstname,
                last_name=lastname,
                email=eml,
                department=dep,

            )

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)