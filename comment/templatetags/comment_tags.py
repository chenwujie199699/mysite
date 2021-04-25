from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm

register = template.Library()


# 获取评论数标签
@register.simple_tag
def get_comment_count(obj):
    blog_content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=blog_content_type, object_id=obj.pk)
    return comments.count()


# 获取评论form
@register.simple_tag
def get_comment_form(obj):
    blog_content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={
        'content_type': blog_content_type.model,
        'object_id': obj.pk,
        'reply_comment_id': 0})
    return form


# 获取某条评论列表
@register.simple_tag
def get_comment_list(obj):
    blog_content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=blog_content_type, object_id=obj.pk, parent=None)
    return comments.order_by('-comment_time')
