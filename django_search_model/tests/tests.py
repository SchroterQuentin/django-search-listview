from django.test import TestCase
from django.test import Client

class SearchTest(TestCase):

    fixtures = ['base.json']

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        """
        Only pagination
        """
        response = self.client.get('/list/devices')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertContains(response, """<li class="active"><a href="#" onclick="change_page(1)" rel="1">1</a></li>""")

        response = self.client.get('/list/devices?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertContains(response, """<li class="active"><a href="#" onclick="change_page(2)" rel="2">2</a></li>""")

        response = self.client.get('/list/devices?page=16')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertContains(response, """<li class="active"><a href="#" onclick="change_page(16)" rel="16">16</a></li>""")

    def test_search_page(self):
        response = self.client.get('/list/devices/search')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertContains(response, """<li class="active"><a href="#" onclick="change_page(1)" rel="1">1</a></li>""")
        self.assertContains(response,"""<ul class="col-sm-12 collapse" id="search_box">""")

        response = self.client.get('/list/devices/search', data={
            "page": 2,
            "Brand-provider": 2,
            "Brand-name" : "HTC"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertContains(response, "211")
        self.assertContains(response, """<input class="form-control" id="id_Brand-name" maxlength="100" name="Brand-name" type="text" value="HTC" />""")
        self.assertContains(response,"""<option value="2" selected="selected">Provider1</option>""")

    def test_out_of_range(self):
        response = self.client.get('/list/devices/search', data={
            "page": 5,
            "Brand-provider": 2,
            "Brand-name" : "HTC"
        })
        self.assertEqual(response.status_code, 404)

    def test_result(self):
        response = self.client.get('/list/devices/search', data={
            "page": 2,
            "Brand-provider": 2,
            "Brand-name" : "HTC",
            "Device-model_device": 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "902114")

        response = self.client.get('/list/devices/search', data={
            "page": 2,
            "Brand-provider": 2,
            "Brand-name" : "H",
            "Device-model_device": 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "902114")

        response = self.client.get('/list/devices/search', data={
            "page": 3,
            "Brand-provider": 2,
            "Brand-name" : "H",
            "Device-model_device": 2
        })
        self.assertEqual(response.status_code, 404)

    def test_number_input(self):
        response = self.client.get('/list/devices/search', data={
            "page": 2,
            "Brand-provider": 2,
            "Brand-name" : "HTC",
            "Device-model_device": 2
        })
        self.assertContains(response, "<input", count=3)
        self.assertContains(response, "<select", count=2)


    def test_full_reverse_relation(self):
        response = self.client.get("/list/provider",data={
            "page": 1,
            "ModelDevice-device": 6,
            "Provider-brand": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<select", count=2)
        #2 in the list 1 in the form
        self.assertContains(response, "HTC", count=3)

    def test_full_way(self):
        response = self.client.get("/list/brand")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/list/brand",data={
            "page": 1,
            "Brand-provider": 2,
            "Brand-modeldevice": 1,
            "Device-inventory_number": 1
        })
        self.assertEqual(response.status_code, 200)
