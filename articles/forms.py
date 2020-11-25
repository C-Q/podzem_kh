from django import forms

from .models import Category


class ChoiceCategoryForm(forms.Form):
	"""choice the category to filter of article-names
	ideas from:
		https://stackoverflow.com/questions/34781524/django-populate-a-form-choicefield-field-from-a-queryset-and-relate-the-choice-b
		https://stackoverflow.com/questions/11936470/django-choicefield-populated-from-database-values
	"""
	choice = forms.ModelChoiceField(queryset=Category.objects.all(),
	                                widget=forms.Select(attrs={'onchange': 'this.form.submit()'}),
	                                empty_label=None,
	                                to_field_name='url',
	                                label='Показать ',
	                                label_suffix=' ',
	                                required=False,)
