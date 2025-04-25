
import unittest
from src.api.HTTPHeaders import default_headers
from openapi_client.models.query import Query
from openapi_client.models.read_metadata_request import ReadMetadataRequest

class TestQuery(unittest.TestCase):

    def testQuery(self):
        """
        A unit test that validates the packaging of the VizQL data service python client
        """
        headers = default_headers()

        sample_query_json = ('{"datasource": {"datasourceLuid": "74ff134d-7f8f-475c-a63e-bf14ea26cbb1"}, '
                '"options": {"returnFormat": "OBJECTS"}, "query": {"fields": [{"fieldCaption": "Category"},'
                ' {"fieldCaption": "Sales", "function": "SUM"}]}}')

        # create an instance of ReadMetadataRequest from a JSON string
        read_metadata_request_instance = ReadMetadataRequest.from_json(sample_query_json)
        # convert the object into a dict
        read_metadata_request_dict = read_metadata_request_instance.to_dict()
        # create an instance of ReadMetadataRequest from a dict
        read_metadata_request_from_dict = ReadMetadataRequest.from_dict(read_metadata_request_dict)
        assert read_metadata_request_from_dict.datasource.datasource_luid == '74ff134d-7f8f-475c-a63e-bf14ea26cbb1'
        assert headers.get_header('User-Agent') =='python-sdk-client'
if __name__ == '__main__':
    unittest.main()
