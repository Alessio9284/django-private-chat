import os
import pymysql
import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directory privateChat
ROOT_PATH = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3%6-$%u@&df@949i^nhe3ubp687&txqa$g8z=p^9fa)4mw22zz'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	'chat',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
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

ROOT_URLCONF = 'privateChat.urls'

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

WSGI_APPLICATION = 'privateChat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# database://username:password@hostname:port/database_name

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# mysql://bf199d2688f63a:8296016b@eu-cdbr-west-02.cleardb.net/heroku_e3f89a5afdbe8e0?reconnect=true
# username: bf199d2688f63a
# password: 8296016b

'''
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql', 
		'NAME': 'heroku_e3f89a5afdbe8e0',
		'USER': 'bf199d2688f63a',
		'PASSWORD': '8296016b',
		'HOST': 'eu-cdbr-west-02.cleardb.net',
		'PORT': '',
		#'OPTIONS': {
		#	'ssl': {
		#		'ca': 'certificates/cleardb-ca.pem',
		#		'cert': 'certificates/bf199d2688f63a-cert.pem',
		#		'key': 'certificates/bf199d2688f63a-key.pem'
		#	}
		#}
	}
}
'''

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

LANGUAGE_CODE = 'it-it'
#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'static')]

django_heroku.settings(locals())
