Django-SearchableListView
=========================

[![Build Status](https://travis-ci.org/SchroterQuentin/Django-SearchableListView.svg?branch=master)](https://travis-ci.org/SchroterQuentin/Django-SearchableListView)
[![Coverage Status](https://coveralls.io/repos/github/SchroterQuentin/Django-SearchableListView/badge.svg)](https://coveralls.io/github/SchroterQuentin/Django-SearchableListView)

ListView which can be searchable, paginate and which don't lose query parameter and page number

Installation
------------

This library need jQuery ( and Bootstrap for the frond-end ) 
To install it in your vitualenv on your django project

```{r, engine='bash', count_lines}
pip install django_search_model
```


Only paginate ListView
----------------------

```python
class ListDevicePaginate(SearchableListView):
    model = Device
    template_name = "tests/list.html"
    paginate_by = 10
```
        
Paginate + Searchable ListView
------------------------------

```python
class ListDeviceSearchablePaginate(SearchableListView):
    model = Device
    template_name = "tests/list.html"
    paginate_by = 10
    searchable_fields = ["inventory_number", "model_device", "model_device__brand__provider",
    "model_device__brand__name"]
    specifications = {
        "model_device__brand__name": "__icontains"
    }
```

Put the parameter for the query in **searchable_fields** which will be use to filter the queryset. The specifications which be use in the same way.

In the template
---------------

- Where you want the pagination and the search box

```html
<div class="row">
    {% include "search_listview/search_and_page.html" %}
</div>
```

- In the footer

```html
<!--Need jQuery-->
<script src="{% static 'js/django_search_model.js' %}"></script>
<script>
    start_search()
</script> 
```

Now you have a beautifull box with all the fields you need.

![Alt tag](/docs/search_box.png?raw=true "Search box")
