WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess' # When you write your own apps make sure to set the secret key to something that is difficult to guess.
SOCIAL_FACEBOOK = {
    'consumer_key': '1912813858993514'
}
SOCIAL_FACEBOOK['consumer_secret'] = input("What is the Facebook Secret? ")
SECURITY_POST_LOGIN = '/profile'