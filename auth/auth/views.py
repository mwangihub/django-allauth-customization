from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from django.urls import reverse
from alts.models import User
from alts.forms import CustomAuthForm
from .decorators import non_required


class HomeView(generic.View):
    form_class = CustomAuthForm
    def get(self, request, *args, **kwargs):
        context = {
            'form':self.form_class
        }
        return render(request, "default/index.html", context)

@method_decorator([login_required(login_url='user_urls:user_login'),], name='dispatch')
class ProfileView(generic.View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, "default/profile.html", context)


@method_decorator([login_required(login_url="home"), non_required, ], name="dispatch",)
class ChooseUserTypeView(generic.View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "default/choose_user_type.html", context)

    def user_account_selector(self, ):
        pass


    def post(self, request, *args, **kwargs):
        u_type = str(request.POST['type'])
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            user = None
        if user is not None:
            context = {
                "selected":f"You have choosen {u_type} account",
            }
            if hasattr(user, u_type):
                if u_type is not 'staff' and u_type is not 'none':
                    setattr(user, u_type, True)
                    user.non = False
                    user.save()
                    context["title"] = f"Welcome to {u_type} Account"
                    return redirect("home")
                else:
                    if u_type == 'staff':
                        return redirect("staff_register")
            if u_type == 'none':
                none = "You have to select one of the existing accounts"
                context["selected"] = none
                return render(request, "default/choose_user_type.html", context)
        else:
            context = {
                "selected":f"Your account was not created!",
                }
            return render(request, "default/choose_user_type.html", context)
        

class StaffRegisterProcessView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'default/staff_reg_process.html')

