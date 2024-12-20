"""
Django settings for CINERIUM project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env 파일 경로
ENV_PATH = BASE_DIR / '.env'

# .env 파일 읽기
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key] = value


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4n2y78&4llup-dnk1%rum*vsyh_b7a_*sz#je#wmm$jvv&ku6w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# API 키 가져오기
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Application definition

INSTALLED_APPS = [
    # APP
    'accounts',
    'chats',
    'movies',
    'reviews',

    # django-extensions
    'django_extensions',

    # DRF
    'rest_framework',
    'rest_framework.authtoken',

    # REST_AUTH
    'dj_rest_auth',
    'allauth',
    'allauth.account',

    # social login 필요 시 추가
    'django.contrib.sites',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'allauth.socialaccount.providers.google',

    # CORS
    'corsheaders',

    # 기본 APP
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# social login 필요 시 추가
SITE_ID = 1

# DRF auth settings
# Token 인증을 기본으로 사용하도록 설정
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# USER MODEL
AUTH_USER_MODEL = 'accounts.User'

# REST AUTH Serializer 재정의
REST_AUTH = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
    'LOGIN_SERIALIZER': 'accounts.serializers.CustomLoginSerializer',
}

# 이메일 인증
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True ######## 이것도 뭔지 알아내기
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# 이메일로 로그인
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False       # username 불필수
ACCOUNT_UNIQUE_EMAIL = True            # 이메일 중복 방지

# 이메일 인증에 필요한 기본 이메일 설정
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # SMTP 백엔드 사용
EMAIL_HOST = "smtp.gmail.com"  # 이메일 호스트 (예: Gmail)
EMAIL_PORT = 587               # 이메일 포트
EMAIL_USE_TLS = True           # TLS 사용
EMAIL_HOST_USER = "rublin322@gmail.com"  # 발송 이메일 계정
EMAIL_HOST_PASSWORD = "qloq swrq luxe vhjy"  # 발송 이메일 비밀번호
DEFAULT_FROM_EMAIL = "rublin322@gmail.com"  # 기본 발신자 이메일


ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/movies/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/accounts/login/'

ACCOUNT_ADAPTER = "accounts.adapters.CustomAccountAdapter"
FRONTEND_URL = "http://localhost:5173"  # 이메일 인증 시 리디렉션할 프론트엔드 URL

# 인증 백엔드 설정
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# 미디어 파일 설정 (프로필 이미지를 위해 필요)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MIDDLEWARE = [
    # auth, cors 및 기본 미들웨어
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

######## 이건 뭐지??
SESSION_ENGINE = "django.contrib.sessions.backends.db"  # 기본 세션 엔진
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False  # HTTPS 환경에서는 True로 설정
SESSION_SAVE_EVERY_REQUEST = True  # 모든 요청에서 세션 갱신
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 브라우저 닫아도 세션 유지

# CORS
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

# 인증 정보 포함 허용
CORS_ALLOW_CREDENTIALS = True

# CSRF 설정
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

# HTTPS를 통해서만 쿠키 전송
# CSRF_COOKIE_SECURE = True  # 프로덕션 환경
CSRF_COOKIE_SECURE = False # 개발 환경
CSRF_COOKIE_SAMESITE = 'Lax'  # 또는 'None'
CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = False

ROOT_URLCONF = 'CINERIUM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CINERIUM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
