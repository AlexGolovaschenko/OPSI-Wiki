from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.urls import reverse
from processmap.models import MapAreaLink


register = template.Library()

map_area_reverse = dict((v, k) for k, v in MapAreaLink.MAP_AREA_CHOICES)


@register.filter
@stringfilter
def get_map_area_link(area_name):
    try:
        area = MapAreaLink.objects.get( map_area=map_area_reverse[area_name] )
        url = reverse('pages:detail', args = (area.page.id, ))
    except: 
        url = '#'
    return url



@register.filter
@stringfilter
def get_map_area(area_name, coords):
    try:
        m = MapAreaLink.objects.get( map_area=map_area_reverse[area_name] )
        url = reverse('pages:detail', args = (m.page.id, ))
        area = f'<area target="" href="{url}" alt="{area_name}" title="{area_name}" coords="{coords}" shape="rect">'
    except: 
        area = ''
    return mark_safe(area)