# accounts/adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    사용자 계정 관리를 위한 커스텀 어댑터
    """

    def save_user(self, request, user, form, commit=True):
        """
        회원가입 시 사용자 정보를 저장하는 로직
        """
        user = super().save_user(request, user, form, commit=False)

        # 추가 데이터 저장
        data = form.cleaned_data
        user.introduce = data.get('introduce', "")
        user.save()

        if 'favorite_genres' in data:
            user.favorite_genres.set(data['favorite_genres'])

        if commit:
            user.save()
        return user
    
    def format_email_subject(self, subject):
        # 이메일 제목 앞의 [example.com]을 제거
        return subject

    def get_email_confirmation_url(self, request, emailconfirmation):
        """
        이메일 인증 URL 생성
        """
        return f"{settings.FRONTEND_URL}/email-verification?key={emailconfirmation.key}"
