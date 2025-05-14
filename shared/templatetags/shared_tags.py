from django import template

register = template.Library()


@register.filter
def truncate_chars(value, max_length):
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value


# kullanımı:: {{ text|truncate_chars:10 }}
"""
 {% load shared_tags %}

<p>{{ text|truncate_chars:50 }}</p>
"""
