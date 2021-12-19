from django.views.generic import ListView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Table
from .filters import filter_int_table_objects, filter_str_table_objects


# Вьюшка главной страницы
class TableListView(ListView):
    model = Table
    ordering = '-date'
    template_name = 'index.html'
    context_object_name = 'table_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['table_data'] = Table.objects.all().order_by('-date')

        # Этот блок для того, чтоб пагинация не сбилась при фильтрации таблицы. Сама фильтрация происходит во вьюшке filter_data
        try:
            # Вытаскиваем значения с сессии (если уже пользовались фильтром)
            column_value = self.request.session['column_value']
            condition_value = self.request.session['condition_value']
            searchbar_value = self.request.session['search_value']

            if column_value or condition_value or searchbar_value:
                if column_value == 'name':
                    context['table_data'] = filter_str_table_objects(context['table_data'], column_value, condition_value, searchbar_value)
                else:
                    try:
                        context['table_data'] = filter_int_table_objects(context['table_data'], column_value, condition_value, searchbar_value)
                    except ValueError:
                        pass
        except KeyError:
            pass  # если ничего не было в сессии, то пропускаем и используем все значения
        
        # Пагинация
        if context['table_data']:
            paginator = Paginator(context['table_data'], 10)
            page = self.request.GET.get('page')
            try:
                context['table_data'] = paginator.page(page)
            except PageNotAnInteger:
                context['table_data'] = paginator.page(1)
            except EmptyPage:
                context['table_data'] = paginator.page(paginator.num_pages)

        return context


# Фильтрация таблицы
def filter_data(request):
    table_data = Table.objects.all().order_by('-date')
    message = None

    column_value = request.GET.get('column')
    condition_value = request.GET.get('condition')
    searchbar_value = request.GET.get('search_value')

    request.session['column_value'] = column_value  # закидываем значения в сессию, чтоб не сбить всю фильтрацию при переходе на другую страницу в пагинации
    request.session['condition_value'] = condition_value
    request.session['search_value'] = searchbar_value

    if not column_value:
        message = 'Выберите колонку'
    elif not condition_value:
        message = 'Выберите условие'
    elif not searchbar_value:
        message = 'Впишите значение в поиск'
    else:
        if column_value == 'name' and (condition_value == '>' or condition_value == '<'):
            message = 'Так сортировать нельзя'
        elif column_value == 'name':
            table_data = filter_str_table_objects(table_data, column_value, condition_value, searchbar_value)
        else:
            try:
                table_data = filter_int_table_objects(table_data, column_value, condition_value, searchbar_value)
            except ValueError:
                message = 'Для данного фильтра требуются цифры, а не буквы. Попробуйте снова.'

    if table_data:
        paginator = Paginator(table_data, 10)
        page_number = request.GET.get('page', 1)
        table_data = paginator.get_page(page_number)

    data = render_to_string('filtered_table.html', {'table_data': table_data, 'message': message})  # конвертирум в "строку"
    return JsonResponse({'table_data': data})  # возвращаем JSON


# Сброс фильтров
def reset_filter(request):
    table_data = Table.objects.all().order_by('-date')

    request.session['column_value'] = None  # сбрасываем сессию
    request.session['condition_value'] = None
    request.session['search_value'] = None

    paginator = Paginator(table_data, 10)
    page_number = request.GET.get('page', 1)
    table_data = paginator.get_page(page_number)

    data = render_to_string('filtered_table.html', {'table_data': table_data})
    return JsonResponse({'table_data': data})
