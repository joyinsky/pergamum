from django import template

register = template.Library()


@register.filter
def pagination_range(obj, current=1, limit=10):
    """
    Used with pagination page_range object when you have a lot of pages
    > obj = range(100)
    > pagination_limit(obj, 1)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    > pagination_limit(obj, 6)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    > pagination_limit(obj, 7)
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    > pagination_limit(obj, 9)
    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    > pagination_limit(obj, 99)
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    Use within a template with a paginator:
    {% for page in obj_list.paginator.page_range|pagination_limit:obj_list.number %}
        {{ page }}
    {% endfor %}
    """

    left = (limit / 2) + 1
    right = limit / 2
    total = len(obj)

    if limit % 2 == 0:
        right -= 1

    if current < left:
        return obj[:limit]
    if current > total - right:
        return obj[total - limit:]

    return obj[current - int(left):current + int(right)]
