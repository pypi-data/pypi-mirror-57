import gocept.jasmine.jasmine
import gocept.jasmine.resource


class MyTestApp(gocept.jasmine.jasmine.TestApp):

    def need_resources(self):
        gocept.jasmine.resource.selftest.need()

    @property
    def body(self):
        return '<div id="my_container"></div>'


class MyJasmineTestCase(gocept.jasmine.jasmine.TestCase):

    layer = gocept.jasmine.jasmine.get_layer(MyTestApp())

    def test_integration(self):
        self.run_jasmine()
