from django import template

register = template.Library()

@register.simple_tag
def pagination_slow(state, url, current_page):
    url_split = url.split('&')
    if state == 'previous':
        url_split[url_split.index(f'page={current_page}')] = url_split[url_split.index(f'page={current_page}')].replace(f'page={current_page}', f'page={str(current_page-1)}')
    else:
        if f"page={current_page}" in url_split:
            url_split[url_split.index(f'page={current_page}')] = url_split[url_split.index(f'page={current_page}')].replace(f'page={current_page}', f'page={str(current_page+1)}')
        else:
            return f"?page={current_page+1}&{'&'.join(url_split)}"
    return f"?{'&'.join(url_split)}"
    
@register.simple_tag
def pagination_fast(page, url, current_page):
    url_split = url.split('&')
    page = 1 if page == None else page
    if f"page={current_page}" in url_split:
        url_split[url_split.index(f'page={current_page}')] = url_split[url_split.index(f'page={current_page}')].replace(f'page={current_page}', f'page={str(page)}')
        return f"?{'&'.join(url_split)}"
    else:
        return f"?page={page}&{'&'.join(url_split)}"