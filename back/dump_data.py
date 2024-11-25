import os
import django
from django.core.management import call_command

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CINERIUM.settings')  # 프로젝트 설정 파일에 맞게 수정
django.setup()  # Django 초기화

# 데이터 덤프
with open('data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', indent=2, stdout=f)