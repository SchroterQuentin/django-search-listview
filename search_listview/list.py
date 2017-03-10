from copy import deepcopy
from math import floor

from django.views.generic.list import ListView

from django.db.models.base import Q
from django.db.models.constants import LOOKUP_SEP

from django.forms import Form, MultipleChoiceField, ChoiceField

from .forms import PageForm

EMPTY_DICT = {'empty' : True}

class SearchableListView(ListView):
    """
    ListView which can be searchable, paginate and which don't lose
    query parameter and page
    """
    searchable_fields = []
    specifications = {}
    nb_form_per_line = 4
    css_class = "form-control"
    disable_search_button = False

    def get_q_object(self):
        """
        Build Q object to filter the queryset
        """
        q_object = Q()
        for field in self.searchable_fields:
            value = self.request.GET.getlist(alias_field(self.model, field), None)
            mini_q = Q()
            for val in value:
                attr = "{0}{1}".format(field, self.specifications.get(field, ''))
                if val:
                    dic_tmp = {
                        attr: val
                    }
                    mini_q |= Q(**dic_tmp)
            q_object &= mini_q
        return q_object

    def get_search_form(self):
        """
        Return list of form based on model
        """
        magic_dico_form = self.get_dict_for_forms()
        forms = []
        initial = list(self.request.GET.lists())

        for key, value in magic_dico_form.items():
            form = Form()
            model = value["model"]
            if not value["fields"]:
                continue
            for field in value["fields"]:
                formfield = get_formfield(model, field)
                formfield.widget.attrs.update({'class': self.css_class})
                form.fields.update({
                    field : formfield
                })

            initial_tmp = {}
            for k, vals in initial:
                tmp_list = k.split(model.__name__ + "-")
                if len(tmp_list) == 2:
                    list_val_tmp = vals[0] if len(vals) == 1 else [val for val in vals if val != '']
                    initial_tmp[tmp_list[-1]] = list_val_tmp

            form.initial = initial_tmp
            form.prefix = model.__name__
            forms.append(form)
        return sorted(forms, key=lambda form: form.prefix)

    def get_page_input(self, num_page):
        """
        Return hidden input which contains the page number
        """
        return PageForm(
            initial={
                "page": num_page
            }
        )

    def get_context_data(self, **kwargs):
        context = super(SearchableListView, self).get_context_data(**kwargs)

        forms = self.get_search_form()

        if context["page_obj"] is not None:
            page_number_form = self.get_page_input(context["page_obj"].number)
        else:
            page_number_form = None

        context.update({
            "search_box_form": forms,
            "search_size": max(
                floor(12/len(forms)),
                floor(12/self.nb_form_per_line)
                ) if len(forms) else 0,
            "search_page": page_number_form,
            "disable_search_button": self.disable_search_button
        })
        return context

    def get_queryset(self):
        self.queryset = super(SearchableListView, self).get_queryset()
        return self.queryset.filter(self.get_q_object()).distinct()

    def get_dict_for_forms(self):
        """
        Build a dictionnary where searchable_fields are
        next to their model to be use in modelform_factory

            dico = {
                "str(model)" : {
                    "model" : Model,
                    "fields" = [] #searchable_fields which are attribute of Model
                }
            }
        """
        magic_dico = field_to_dict(self.searchable_fields)
        dico = {}

        def dict_from_fields_r(mini_dict, dico, model):
            """
            Create the dico recursively from the magic_dico
            """

            dico[str(model)] = {}
            dico[str(model)]["model"] = model
            dico[str(model)]["fields"] = []

            for key, value in mini_dict.items():
                if isinstance(value, bool):
                    continue
                if value == EMPTY_DICT:
                    dico[str(model)]["fields"].append(key)
                elif EMPTY_DICT.items() <= value.items():
                    dico[str(model)]["fields"].append(key)
                    model_tmp = associate_model(model, key)
                    dict_from_fields_r(value, dico, model_tmp)
                else:
                    model_tmp = associate_model(model, key)
                    dict_from_fields_r(value, dico, model_tmp)

        if magic_dico:
            dict_from_fields_r(magic_dico, dico, self.model)
        return dico


def field_to_dict(fields):
    """
    Build dictionnary which dependancy for each field related to "root"

        fields = ["toto", "toto__tata", "titi__tutu"]
        dico = {
            "toto": {
                EMPTY_DICT,
                "tata": EMPTY_DICT
                },
            "titi" : {
                "tutu": EMPTY_DICT
            }
        }

    EMPTY_DICT is useful because we don't lose field
    without it dico["toto"] would only contains "tata"

    inspired from django.db.models.sql.add_select_related
    """
    field_dict = {}
    for field in fields:
        d_tmp = field_dict
        for part in field.split(LOOKUP_SEP)[:-1]:
            d_tmp = d_tmp.setdefault(part, {})
        d_tmp = d_tmp.setdefault(
            field.split(LOOKUP_SEP)[-1],
            deepcopy(EMPTY_DICT)
        ).update(deepcopy(EMPTY_DICT))
    return field_dict

def alias_field(model, field):
    """
    Return the prefix name of a field
    """
    for part in field.split(LOOKUP_SEP)[:-1]:
        model = associate_model(model,part)
    return model.__name__ + "-" + field.split(LOOKUP_SEP)[-1]

def associate_model(model, field):
    """
    Return the model associate to the ForeignKey or ManyToMany
    relation
    """
    class_field = model._meta.get_field(field)
    if hasattr(class_field, "field"):
        return class_field.field.related.related_model
    else:
        return class_field.related_model

def get_formfield(model, field):
    """
    Return the formfied associate to the field of the model
    """
    class_field = model._meta.get_field(field)

    if hasattr(class_field, "field"):
        formfield = class_field.field.formfield()
    else:
        formfield = class_field.formfield()
    
    # Otherwise the formfield contain the reverse relation
    if isinstance(formfield, ChoiceField):
        formfield.choices = class_field.get_choices()
    
    return formfield
