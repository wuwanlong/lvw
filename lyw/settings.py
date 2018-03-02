"""
Django settings for lyw project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import logging
import django.utils.log
import logging.handlers
import pymysql
pymysql.install_as_MySQLdb()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^_^k5d_3@h=xaex3xm_t501mbg+fz_b!pteg9ypmzjowm83)_7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lvw_cart',
    'lvw_goods',
    'lvw_order',
    'lvw_user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lyw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'lyw.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lvw',
        'USER': 'root',
        'PASSWORD':'19950520',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]
MEDIA_ROOT=os.path.join(BASE_DIR,'static')


#日志
# LOGGING = {
#     'version': 1,     # version表示版本，一般不用改
#     'disable_existing_loggers': True, #disable_existing_loggers表示弃用已经存在的日志，True表示弃用，False表示不弃用。
#     'formatters': {   #fomatters表示多个格式化格式
#         'verbose': {  #,verbose表示详细的格式化，包括文件名，时间，模块，进程，线程，信息
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },   #用于生成日志消息的格式字符串
#         'standard': {  #standard表示标准的格式化包括文件名，时间和信息
#             'format': '%(levelname)s %(asctime)s %(message)s'
#         },
#         'simple': {  #simple就是简单的只有文件名和信息
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters': {  #filters表示过滤器,如果有需要可以添加，如何添加查看官方文档，一般不需要。
#     },
#     'handlers': {  #handlers表示处理日志程序定义了两个一个是把日志发送给站点管理员，一个是自定义的。level表示等级，一共五个
#         'mail_admins': {
#             'level': 'ERROR',  #level设置记录器的级别，一共五个
#             #DEBUG：用于调试目的的底层系统信息，INFO：普通的系统信息，WARNING：表示出现一个较小的问题，ERROR：表示出现一个较大的问题，CRITICAL：表示出现一个致命的问题。
#             'class': 'django.utils.log.AdminEmailHandler', #class表示的意思大概是python自带的处理程序吧
#             'formatter':'standard',  #class表示的意思大概是python自带的处理程序吧
#         },
#         'my_handler': {
#             'level': 'WRANING',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': '/logging/my_handler.log',  #将日志消息附加到指定文件名的文件
#             'formatter': 'standard',
#         },
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'my_logger': {
#             'handlers': ['my_handler'],
#             'level': 'WARNNING',
#             'propagate': False,
#         },
#     },
# }
#
# logger = logging.getLogger('default')
# logger.warning('text')

# logger = logging.getLogger('default')
# logger.error("This is an error msg")
#可用的函数主要有五种
# logger.debug()
# logger.info()
# logger.warning()
# logger.error()
# logger.critical()