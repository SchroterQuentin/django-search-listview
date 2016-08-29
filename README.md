Django-SearchableListView
=========================

ListView which can be searchable, paginate and which don't lose query parameter and page number

Installation
------------

This library need jQuery.
To install it in your vitualenv on your django project

    pip install ...


Only paginate ListView
----------------------

    class ListDevicePaginate(SearchableListView):
        model = Device
        template_name = "tests/list.html"
        paginate_by = 10

In the template

- In the header

        <link rel="stylesheet" href="{% static 'css/django_search_model.css' %}" >

- Where you want the pagination and the search box

        <div class="row">
            {% include "search_and_page.html" %}
        </div>

- In the footer

        <!--Need jQuery-->
        <script src="{% static 'js/django_search_model.js' %}">
            start_search()
        </script> 


Paginate + Searchable ListView
------------------------------

    class ListDeviceSearchablePaginate(SearchableListView):
        model = Device
        template_name = "tests/list.html"
        paginate_by = 10
        searchable_fields = ["inventory_number", "model_device", "model_device__brand__provider",
        "model_device__brand__name"]
        specifications = {
            "model_device__brand__name": "__icontains"
        }

Put the parameter for the query in **searchable_fields** which will be use to filter the queryset. The specifications which be use in the same way.

Now you have a beautifull box with all the fields you need.

![alt tag](https://github.com/SchroterQuentin/Django-SearchableListView/tree/master/docs/search_box.png)