from django.shortcuts import render
from users.forms import UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
# Create your views here.

class AddUserView(View):

    def get(self, request):
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request, "register.html", {"form1": user_form, "form2": profile_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            password = user.password
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username,
                                password=password)

            login(self.request, user)
            return redirect("home")
        else:
            return render(request, "register.html", {"form1": user_form, "form2": profile_form})