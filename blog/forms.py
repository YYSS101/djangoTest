from django import forms
from .models import Post, Yukyu

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('user', 'title', 'text' )

class YukyuForm(forms.ModelForm):
	class Meta:
		model = Yukyu
		fields = ('busyo', 'name', 'start_date', 'kikan', 'kyuka_type', 'riyuu' )
		widgets = {
			'start_date': forms.SelectDateWidget
		}
