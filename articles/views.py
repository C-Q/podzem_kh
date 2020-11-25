from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe

from .models import ArticleData, Category
from .forms import ChoiceCategoryForm


def articles_list(request):
	"""Отображение списка статей с возможностью фильтрации по категориям"""
	artycle_set = ArticleData.objects.all()
	category_set = Category.objects.all()
	template_path = "static_pages/articles_list.html"
	filterform = ChoiceCategoryForm(request.POST)
	categ_obj = None
	active_page = "class=active_page"

	if request.method == 'POST':
		category_url = request.POST['choice']

		if category_url == 'all' or None:
			artycle_set = ArticleData.objects.all()
		else:
			categ_obj = get_object_or_404(Category, url=category_url)
			artycle_set = ArticleData.objects.filter(categories=categ_obj)

	return render(request, template_path, {'artic_list': artycle_set,
	                                       'filter_index': categ_obj,
	                                       'categ_list': category_set,
	                                       'filterform': filterform,
	                                       'articles_highlight': active_page})


def render_article(request, article_url):
	"""Отображение статьи (как HTML-template-file, так и HTML-string из БД)"""
	article_obj = ArticleData.objects.get(article_url=article_url)
	active_page = "class=active_page"

	if not article_obj.is_template:
		template_path = 'articles/html_from_DB.html'
		article_body = mark_safe(article_obj.text)
		article_photo = None
	else:
		template_path = f'articles/{article_url}.html'
		article_photo = article_obj.articlephoto_set.all()
		article_body = None

	return render(request, template_path, {'article_object': article_obj,
	                                       'article_body': article_body,
	                                       'article_photo': article_photo,
	                                       'articles_highlight': active_page})
