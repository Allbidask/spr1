  """
Django settings for spr3 project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'article.apps.ArticleConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
	'mathfilters',
    'djangojs',

]
#ACCOUNT_EMAIL_REQUIRED = True #користувач має ввести мейл при регістрації
#ACCOUNT_EMAIL_VERIFICATION  = ("mandatory") #обов'язково має підтвердити мейд
ACCOUNT_USERNAME_REQUIRED = False #ім'я необов'язково вводити при реєстрації
#ACCOUNT_UNIQUE_EMAIL = True # мейл має бути унікальним
#ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2 #кількість днів для підтвердження листа
#ACCOUNT_EMAIL_CONFIRMATION_HMAC = True # ключ для підтвердження мейлу
#ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 #Количество неудачных попыток входа
#ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 #Количество секунд, когда запрещено входить в систему
#ACCOUNT_LOGOUT_REDIRECT_URL  = "logout" #URL (или имя URL), к которому нужно вернуться после выхода пользователя из системы. 
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #пустышка для разработки



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spr3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
 
)

WSGI_APPLICATION = 'spr3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase7',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'uk-UK'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
SITE_ID = 1

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cryptohit777@gmail.com'
EMAIL_HOST_PASSWORD ='' #ПОМЕНЯЙ ПАРОЛЬ

EMAIL_SUBJECT_PREFIX = '[Hello from Django] '

#Префикс добавляемый к теме электронного письма отправленного функциями django.core.mail.mail_admins или django.core.mail.mail_managers. Возможно, вы захотите добавить пробелы в конце.

EMAIL_USE_TLS = True
LOGIN_REDIRECT_URL = '/article/index5/'
