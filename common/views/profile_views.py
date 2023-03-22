from itertools import chain

from django.db.models import F
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView


def profile_base(request, user_id):
    """
    프로필 기본정보
    """
    profile = get_object_or_404(User, pk=user_id).profile
    context = {'profile': profile, 'profile_type': 'base'}
    return render(request, 'common/profile/profile_base.html', context)


class ProfileObjectListView(ListView):
    """
    프로필 목록 추상 클래스 뷰
    """
    paginate_by = 10

    class Meta:
        abstract = True

    def get_queryset(self):
        self.profile_user = get_object_or_404(User, pk=self.kwargs['user_id'])
        self.so = self.request.GET.get('so', 'recent')  # 정렬기준
        object_list = self.model.objects.filter(author=self.profile_user)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'profile': self.profile_user.profile,
            'profile_type': self.profile_type,
            'so': self.so
        })
        return context


