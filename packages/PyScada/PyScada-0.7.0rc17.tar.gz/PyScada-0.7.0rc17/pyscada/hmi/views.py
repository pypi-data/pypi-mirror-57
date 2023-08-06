# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.core import version as core_version
from pyscada.models import RecordedData, VariableProperty
from pyscada.hmi.models import ControlItem
from pyscada.hmi.models import Form
from pyscada.hmi.models import DropDown
from pyscada.hmi.models import GroupDisplayPermission
from pyscada.hmi.models import Widget
from pyscada.hmi.models import View

from pyscada.models import Log
from pyscada.models import DeviceWriteTask

from django.http import HttpResponse
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import requires_csrf_token
from django.conf import settings

import time
import json
import logging

logger = logging.getLogger(__name__)

UNAUTHENTICATED_REDIRECT = settings.UNAUTHENTICATED_REDIRECT \
    if hasattr(settings, 'UNAUTHENTICATED_REDIRECT') else '/accounts/login/'


def unauthenticated_redirect(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return redirect('%s?next=%s' % (UNAUTHENTICATED_REDIRECT, args[0].path))
        return func(*args, **kwargs)

    return wrapper


@unauthenticated_redirect
def index(request):
    if GroupDisplayPermission.objects.count() == 0:
        view_list = View.objects.all()
    else:
        view_list = View.objects.filter(groupdisplaypermission__hmi_group__in=request.user.groups.iterator()).distinct()
    c = {
        'user': request.user,
        'view_list': view_list,
        'version_string': core_version,
        'link_target': settings.LINK_TARGET if hasattr(settings, 'LINK_TARGET') else '_blank'
    }
    return TemplateResponse(request, 'view_overview.html', c)  # HttpResponse(t.render(c))


@unauthenticated_redirect
@requires_csrf_token
def view(request, link_title):
    page_template = get_template('content_page.html')
    widget_row_template = get_template('widget_row.html')

    try:
        v = View.objects.get(link_title=link_title)
    except View.DoesNotExist or View.MultipleObjectsReturned:
        return HttpResponse(status=404)

    if GroupDisplayPermission.objects.count() == 0:
        # no groups
        page_list = v.pages.all()
        sliding_panel_list = v.sliding_panel_menus.all()

        visible_widget_list = Widget.objects.filter(page__in=page_list.iterator()).values_list('pk', flat=True)
        # visible_custom_html_panel_list = CustomHTMLPanel.objects.all().values_list('pk', flat=True)
        # visible_chart_list = Chart.objects.all().values_list('pk', flat=True)
        # visible_xy_chart_list = XYChart.objects.all().values_list('pk', flat=True)
        visible_control_element_list = ControlItem.objects.all().values_list('pk', flat=True)
        visible_form_list = Form.objects.all().values_list('pk', flat=True)
        visible_dropdown_list = DropDown.objects.all().values_list('pk', flat=True)
    else:
        page_list = v.pages.filter(groupdisplaypermission__hmi_group__in=request.user.groups.iterator()).distinct()

        sliding_panel_list = v.sliding_panel_menus.filter(
            groupdisplaypermission__hmi_group__in=request.user.groups.iterator()).distinct()

        visible_widget_list = Widget.objects.filter(
            groupdisplaypermission__hmi_group__in=request.user.groups.iterator(),
            page__in=page_list.iterator()).values_list('pk', flat=True)
        """
        # todo update permission model to reflect new widget structure
        visible_custom_html_panel_list = CustomHTMLPanel.objects.filter(
            groupdisplaypermission__hmi_group__in=request.user.groups.iterator()).values_list('pk', flat=True)
        visible_chart_list = Chart.objects.filter(
            groupdisplaypermission__hmi_group__in=request.user.groups.iterator()).values_list('pk', flat=True)
        visible_xy_chart_list = XYChart.objects.filter(
            groupdisplaypermission__hmi_group__in=request.user.groups.iterator()).values_list('pk', flat=True)
        """
        visible_control_element_list = GroupDisplayPermission.objects.filter(
            hmi_group__in=request.user.groups.iterator()).values_list('control_items', flat=True)
        visible_form_list = GroupDisplayPermission.objects.filter(
            hmi_group__in=request.user.groups.iterator()).values_list('forms', flat=True)
        visible_dropdown_list = GroupDisplayPermission.objects.filter(
            hmi_group__in=request.user.groups.iterator()).values_list('dropdowns', flat=True)

    panel_list = sliding_panel_list.filter(position__in=(1, 2,))
    control_list = sliding_panel_list.filter(position=0)

    pages_html = ""
    for page in page_list:
        # process content row by row
        current_row = 0
        widget_rows_html = ""
        main_content = list()
        sidebar_content = list()
        has_chart = False
        for widget in page.widget_set.all():
            # check if row has changed
            if current_row != widget.row:
                # render new widget row and reset all loop variables
                widget_rows_html += widget_row_template.render(
                    {'row': current_row, 'main_content': main_content, 'sidebar_content': sidebar_content,
                     'sidebar_visible': len(sidebar_content) > 0}, request)
                current_row = widget.row
                main_content = list()
                sidebar_content = list()
            if widget.pk not in visible_widget_list:
                continue
            if not widget.visible:
                continue
            mc, sbc = widget.content.create_panel_html(widget_pk=widget.pk, user=request.user)
            if mc is not None and mc is not "":
                main_content.append(dict(html=mc, widget=widget))
            else:
                logger.info("main_content of widget : %s is %s !" % (widget, mc))
            if sbc is not None:
                sidebar_content.append(dict(html=sbc, widget=widget))
            if widget.content.content_model == "pyscada.hmi.models.Chart":
                has_chart = True

        widget_rows_html += widget_row_template.render(
            {'row': current_row, 'main_content': main_content, 'sidebar_content': sidebar_content,
             'sidebar_visible': len(sidebar_content) > 0}, request)

        pages_html += page_template.render({'page': page, 'widget_rows_html': widget_rows_html, 'has_chart': has_chart},
                                           request)

    c = {
        'page_list': page_list,
        'pages_html': pages_html,
        'panel_list': panel_list,
        'control_list': control_list,
        'user': request.user,
        'visible_control_element_list': visible_control_element_list,
        'visible_form_list': visible_form_list,
        'visible_dropdown_list': visible_dropdown_list,
        'view_title': v.title,
        'view_show_timeline': v.show_timeline,
        'version_string': core_version,
        'link_target': settings.LINK_TARGET if hasattr(settings, 'LINK_TARGET') else '_blank'
    }

    return TemplateResponse(request, 'view.html', c)


@unauthenticated_redirect
def log_data(request):
    if 'timestamp' in request.POST:
        timestamp = float(request.POST['timestamp'])
    else:
        timestamp = (time.time() - 300) * 1000  # get log of last 5 minutes

    data = Log.objects.filter(level__gte=6, id__gt=int(int(timestamp) * 2097152) + 2097151).order_by('-timestamp')
    odata = []
    for item in data:
        odata.append({"timestamp": item.timestamp * 1000, "level": item.level, "message": item.message,
                      "username": item.user.username if item.user else "None"})
    jdata = json.dumps(odata, indent=2)

    return HttpResponse(jdata, content_type='application/json')


@unauthenticated_redirect
def form_write_task(request):
    if 'key' in request.POST and 'value' in request.POST:
        key = int(request.POST['key'])
        item_type = request.POST['item_type']
        value = request.POST['value']
        #logger.debug("key : %s - value %s - type %s" % (key, value, item_type))
        # check if float as DeviceWriteTask doesn't support string values
        try:
            float(value)
        except ValueError:
            logger.debug("form_write_task input is not a float")
            return HttpResponse(status=403)
        if GroupDisplayPermission.objects.count() == 0:
            if item_type == 'variable':
                cwt = DeviceWriteTask(variable_id=key, value=value, start=time.time(),
                                      user=request.user)
                cwt.save()
                return HttpResponse(status=200)
            elif item_type == 'variable_property':
                cwt = DeviceWriteTask(variable_property_id=key, value=value, start=time.time(),
                                      user=request.user)
                cwt.save()
                return HttpResponse(status=200)
        else:
            if item_type == 'variable':
                if GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator(),
                                                         control_items__type=5, control_items__variable__pk=key):
                    cwt = DeviceWriteTask(variable_id=key, value=value, start=time.time(),
                                          user=request.user)
                    cwt.save()
                    return HttpResponse(status=200)
                elif GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator(),
                                                           dropdowns__variable__pk=key):
                    cwt = DeviceWriteTask(variable_id=key, value=value, start=time.time(),
                                          user=request.user)
                    cwt.save()
                    return HttpResponse(status=200)
            elif item_type == 'variable_property':
                if GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator(),
                                                         control_items__type=5,
                                                         control_items__variable_property__pk=key):
                    cwt = DeviceWriteTask(variable_property_id=key, value=value, start=time.time(),
                                          user=request.user)
                    cwt.save()
                    return HttpResponse(status=200)
                elif GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator(),
                                                           dropdowns__variable_property__pk=key):
                    cwt = DeviceWriteTask(variable_property_id=key, value=value, start=time.time(),
                                          user=request.user)
                    cwt.save()
                return HttpResponse(status=200)
    return HttpResponse(status=404)


@unauthenticated_redirect
def form_write_property2(request):
    if 'variable_property' in request.POST and 'value' in request.POST:
        value = request.POST['value']
        try:
            variable_property = int(request.POST['variable_property'])
            VariableProperty.objects.update_property(variable_property=variable_property, value=value)
        except ValueError:
            variable_property = str(request.POST['variable_property'])
            if VariableProperty.objects.get(name=variable_property).value_class.upper() in ['STRING']:
                VariableProperty.objects.update_property(variable_property=VariableProperty.objects.get(
                    name=variable_property), value=value)
            else:
                return HttpResponse(status=404)
        return HttpResponse(status=200)
    return HttpResponse(status=404)


def int_filter(someList):
    for v in someList:
        try:
            int(v)
            yield v  # Keep these
        except ValueError:
            continue  # Skip these


@unauthenticated_redirect
def get_cache_data(request):
    if 'init' in request.POST:
        init = bool(float(request.POST['init']))
    else:
        init = False
    active_variables = []
    if 'variables[]' in request.POST:
        active_variables = request.POST.getlist('variables[]')
        active_variables = list(int_filter(active_variables))
    """
    else:
        active_variables = list(
            GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator()).values_list(
                'charts__variables', flat=True))
        active_variables += list(
            GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator()).values_list(
                'xy_charts__variables', flat=True))
        active_variables += list(
            GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator()).values_list(
                'control_items__variable', flat=True))
        active_variables += list(
            GroupDisplayPermission.objects.filter(hmi_group__in=request.user.groups.iterator()).values_list(
                'custom_html_panels__variables', flat=True))
        active_variables = list(set(active_variables))
    """

    active_variable_properties = []
    if 'variable_properties[]' in request.POST:
        active_variable_properties = request.POST.getlist('variable_properties[]')

    timestamp_from = time.time()
    if 'timestamp_from' in request.POST:
        timestamp_from = float(request.POST['timestamp_from']) / 1000.0

    timestamp_to = time.time()

    if 'timestamp_to' in request.POST:
        timestamp_to = min(timestamp_to, float(request.POST['timestamp_to']) / 1000.0)

    if timestamp_to == 0:
        timestamp_to = time.time()

    if timestamp_from == 0:
        timestamp_from == time.time() - 60

    if timestamp_to - timestamp_from > 120 * 60 and not init:
        timestamp_from = timestamp_to - 120 * 60

    #if not init:
        #timestamp_to = min(timestamp_from + 30, timestamp_to)

    if len(active_variables) > 0:
        data = RecordedData.objects.db_data(
            variable_ids=active_variables,
            time_min=timestamp_from,
            time_max=timestamp_to,
            time_in_ms=True,
            query_first_value=init)
    else:
        data = None

    if data is None:
        data = {}

    data['variable_properties'] = {}

    for item in VariableProperty.objects.filter(pk__in=active_variable_properties):
        data['variable_properties'][item.pk] = item.value()

    data["server_time"] = time.time() * 1000
    return HttpResponse(json.dumps(data), content_type='application/json')


def logout_view(request):
    logger.info('logout %s' % request.user)
    logout(request)
    # Redirect to a success page.
    return redirect('%s?next=%s' % (UNAUTHENTICATED_REDIRECT, '/'))


def user_profile_change(request):
    return redirect('%s?next=%s' % (UNAUTHENTICATED_REDIRECT, request.path))
