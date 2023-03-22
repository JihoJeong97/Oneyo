import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings

from common.forms import ProfileForm


@login_required(login_url='common:login')
def base(request):
    """
    계정설정 기본화면
    """
    context = {'settings_type': 'base'}
    return render(request, 'common/settings/base.html', context)


class PasswordChangeView(auth_views.PasswordChangeView):
    """
    비밀번호 변경
    """
    template_name = 'common/settings/password_change.html'
    success_url = reverse_lazy('index')

    # def form_valid(self, form):  # 유효성 검사 성공 이후 로직
    #     messages.success(self.request, '암호를 변경했습니다.')  # 성공 메시지
    #     return super().form_valid(form)  # 폼 검사 결과를 반환

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'settings_type': 'password',
        })
        return context
