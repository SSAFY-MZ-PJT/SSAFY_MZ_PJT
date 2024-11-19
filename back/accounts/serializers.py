# accounts/serializers.py

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=100)
    profile_image = serializers.ImageField(required=False)

    def validate_nickname(self, nickname):
        """
        닉네임 필드에 대한 커스텀 유효성 검사
        - 최소 길이 2자 이상 검증
        """
        if len(nickname) < 2:
            raise serializers.ValidationError('닉네임은 2자 이상이어야 합니다.')
        return nickname

    def get_cleaned_data(self):
        """
        유효성 검사를 통과한 데이터 반환
        - 부모 클래스의 기본 데이터에 커스텀 필드 추가
        """
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['profile_image'] = self.validated_data.get('profile_image', '')
        return data


def validate_image(image):
    max_size = 2 * 1024 * 1024  # 2MB
    if image.size > max_size:
        raise serializers.ValidationError('이미지 크기는 2MB를 초과할 수 없습니다.')
    return image

class CustomUserDetailsSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(required=True, max_length=100)
    profile_image = serializers.ImageField(required=False, validators=[validate_image])

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'nickname', 'profile_image')
        read_only_fields = ('email',)

    def update(self, instance, validated_data):
        # 프로필 이미지 업데이트 시 기존 이미지 삭제
        if 'profile_image' in validated_data and instance.profile_image:
            instance.profile_image.delete()

        return super().update(instance, validated_data)