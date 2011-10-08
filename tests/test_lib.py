__author__ = 'dgraziotin'
import datapkggui.lib as lib
class TestLib:
    def test_list(self):
        ckan_list = lib.list("ckan://")
        assert len(ckan_list) > 2000
        package_names = []
        for package in ckan_list:
            package_names.append(package.name)
        assert "datapkg-gui-test" in package_names #datapkg-gui-test is an already imported package

    def TestSearch(self):
        test_package = lib.search("ckan://", "datapkg-gui-test")
        assert len(test_package) > 0
        assert test_package[0].name == "datapkg-gui-test"

    def TestInfo(self):
        test_package_metadata = lib.info("ckan://datapkg-gui-test") #metadata request
        assert test_package_metadata['name'] == "datapkg-gui-test"
        assert len(test_package_metadata['resources']) == 2