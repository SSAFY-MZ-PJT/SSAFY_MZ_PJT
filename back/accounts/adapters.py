# accounts/adapters.py

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    사용자 계정 관리를 위한 커스텀 어댑터
    - 실제 DB 저장 및 부가 기능 구현
    """
    def save_user(self, request, user, form, commit=True):
        """
        사용자 정보 저장 메서드
        Parameters:
            - request: HTTP 요청 객체
            - user: 저장할 User 모델 인스턴스
            - form: 검증된 폼 데이터
            - commit: DB 저장 여부 (기본값: True)
        """
        # 기본 사용자 정보 저장 (DB 저장은 보류)
        user = super().save_user(request, user, form, False)
        # 검증된 폼 데이터 가져오기
        data = form.cleaned_data

        # 커스텀 필드 데이터 저장
        user.nickname = data.get('nickname', '')

        # 프로필 이미지가 있는 경우에만 저장
        if 'profile_image' in data:
            user.profile_image = data['profile_image']

        # 최종 DB 저장
        user.save()
        return user
    
    def format_email_subject(self, subject):
        # 이메일 제목 앞의 [example.com]을 제거
        return subject
    
    def delete_user(self, request, user):
        """
        회원탈퇴 처리를 위한 메서드
        - 연관 데이터 처리
        - 파일 삭제
        - 이메일 발송 등 복잡한 로직 처리
        """
        try:
            # 1. 사용자의 게시글을 논리적 삭제 처리
            user.reviews.update(is_deleted=True)
            user.comments.update(is_deleted=True)
            
            # 2. 프로필 이미지 파일 삭제
            if user.profile_image:
                user.profile_image.delete()
                
            # 3. 주문 내역 익명화 처리
            # user.orders.update(anonymous=True)
            
            # 4. 탈퇴 확인 이메일 발송
            # self.send_goodbye_email(user.email)
            
            # 5. 사용자 계정 삭제
            user.delete()
            
            return True
        except Exception as e:
            return False