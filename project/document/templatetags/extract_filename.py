from django import template



register = template.Library()


## 파일명 추출 필터
@register.filter
def extract_filename(value):
    return str(value).split('/')[-1]