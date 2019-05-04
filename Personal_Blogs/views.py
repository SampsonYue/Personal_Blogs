import datetime

from django.db.models import Sum
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.cache import cache

from blog.models import Blog
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
        .filter(read_details__date__lt=today, read_details__date__gte=date) \
        .values('id', 'title') \
        .annotate(read_num_sum=Sum('read_details__read_num')) \
        .order_by('-read_num_sum')
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    # 获取七天热门博客的缓存数据
    get_blogs_for_7_days = cache.get('get_blogs_for_7_days')
    if get_blogs_for_7_days is None:
        get_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('get_blogs_for_7_days', get_blogs_for_7_days, 3600)
        print('cach')
    else:
        print('use cache')

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_for_7_days'] = get_blogs_for_7_days
    return render(request, 'home.html', context)
