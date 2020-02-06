from django.contrib import admin
from .models import Post

admin.site.register(Post)

'''
root
ts8081ts

ユーザー名忘れたらコレ
python manage.py shell
from django.contrib.auth.models import User
users = User.objects.all()
user = users[0]
user
<User: skw>	←ここにユーザー名

パスワードも忘れたらこれ
user.set_password('mypass') ←新しいパスワード
user.save()
'''