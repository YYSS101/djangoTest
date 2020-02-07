from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Yukyu
from .forms import PostForm, YukyuForm

'''
	renderはHTMLを読み込んでレンダリングするようなイメージ
	第三引数は辞書型{ key1:value1, key2:value2 }
	HTML側はkey指定して値にアクセス、アクセスは二重カッコで記載
	{{ key1.name }}

	get_object_or_404は指定したpkのモデルを引っ張ってくる
	なければ404エラーを表示する。（使わない場合はServer Errorみたいなよくわからない表示が出てしまう）

	pkはプライマリキー、db.sqlite3の中身見るとidで記されているやつ
	レコードを直接指定できるようなもの

	requestは、HttpRequestオブジェクトだった
'''

def debug_test(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:20]
    return render(request, 'blog/test.html', {'posts': posts})

def page_non(request):
    return render(request, 'blog/page_non.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:20]
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	# 指定したpkが存在しない場合、404エラー画面を表示させる
    post = get_object_or_404(Yukyu, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	# HTMLから"POST"が送られてきた時
	if request.method == "POST":
		# 受け取ったPOSTデータを渡す（フォームの入力情報などをここで受け取る）
		form = YukyuForm(request.POST)

		# is_validで正当性チェック
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_new')
			#return render(request, 'blog/post_check.html', {'post': post})

	# 最初のページ表示時の処理
	form = YukyuForm()
	posts = Yukyu.objects.filter(published_date__lte=timezone.now()).order_by('-start_date')[:20]
	return render(request, 'blog/post_edit.html', {'form': form, 'posts': posts, 'now': timezone.now() })

def post_chk(request):
	# HTMLから"POST"が送られてきた時
	if request.method == "POST":
		post.save()
		return redirect('post_new')

	return render(request, 'blog/post_check.html', {'post': post})



def tips_kitei(request):
    return render(request, 'blog/tips_kitei.html')
