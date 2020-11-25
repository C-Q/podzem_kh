from django.shortcuts import render

# done: 1) нарисовать макет, определиться с внешним видом и функционалом.
# done: 2) разметить макет в шаблоне
# todo: 3) запилить функционал


def to_book(request):
	template_path = "booking/booking.html"
	active_page = "class=active_page"
	return render(request, template_path, {'booking_highlight': active_page})