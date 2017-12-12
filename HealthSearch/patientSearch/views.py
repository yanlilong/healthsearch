# -*- coding: utf-8 -*-



from django.template.loader import get_template
import create_view
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from patient_search_form import QueryFrom
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import pdb
import logging

logger = logging.getLogger("patientSearch")


def index(request):
  template = get_template('patientSearch/search_form.html')
  resource_name_list = create_view.create_resource()
  if (request.method == 'POST'):
    query_form = QueryFrom(request.POST)
    print query_form.fields
    if (query_form.is_valid()):
      age = request.POST.get("age", "")
      sex = request.POST.get("sex", "")
      sympo = request.POST.get("sympo", "")
      disease = request.POST.get("disease", "")

      create_view.save_query(age, sex, sympo, disease)
      selected_datsource = request.POST.get("datasource_list", "")
      resource_name_list.remove(selected_datsource)
      resource_name_list.insert(0, selected_datsource)
      url = create_view.get_dataresource(selected_datsource)
      print(url)
      logger.info(msg=url)
      # rest_url = url?age=)age&sex=create_view.create_sex(sex)&sym
      # return redirect('/patientSearch')
    return (HttpResponse(template.render(
        {'query_form': query_form, 'resource_name_list': resource_name_list},
        request)))

  else:

    query_form = QueryFrom()
    template = get_template('patientSearch/search_form.html')
    return (HttpResponse(template.render(
        {'query_form': query_form, 'resource_name_list': resource_name_list},
        request)))
