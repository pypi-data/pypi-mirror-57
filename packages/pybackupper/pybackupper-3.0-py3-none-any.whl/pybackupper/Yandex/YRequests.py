import requests
import os


class Yandex_Requests:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_files(self):
        """
        Get All Files from your Yandex disk
        Output: [ (string path, string filename) ]
        """
        result = []
        headers = {"Authorization": "OAuth " + self.access_token}
        query_link = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        query_params = "?limit=1000"
        url = '{0}{1}'.format(query_link, query_params)
        response = requests.get(url, headers=headers)
        content = response.json()
        for file in content['items']:
            result.append(file['path'])
        return result

    def get_upload_url(self, filepath):
        """
        Get upload link
        With it you can complete file uploading
        """
        headers = {"Authorization": "OAuth " + self.access_token}
        query_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        query_params = "?path={0}&overwrite=true".format(filepath)
        url = '{0}{1}'.format(query_link, query_params)
        response = requests.get(url, headers=headers)
        return Yandex_Requests.handle_response(response, [200], 'href')

    def upload_file(self, filename, upload_link):
        """
        Upload file on Yandex Disk
        Don't forget to get upload link before
        """
        headers = {"Authorization": "OAuth " + self.access_token}
        response = requests.put(upload_link, data=open(filename, 'rb'))
        return Yandex_Requests.handle_response(response, [201])

    def create_folder(self, foldername, parents):
        """
        Create folder on disk
        full foldername wiil be parents/foldername
        """
        headers = {"Authorization": "OAuth " + self.access_token}
        query_link = 'https://cloud-api.yandex.net/v1/disk/resources'
        query_params = "?path={0}".format(parents + foldername)
        url = '{0}{1}'.format(query_link, query_params)
        response = requests.put(url, headers=headers)
        return Yandex_Requests.handle_response(response, [201, 409])

    @staticmethod
    def handle_response(response, good_statuses, return_content=None):
        """
        Checks response for OK condition and raise exception if it's not
        """
        for status in good_statuses:
            if response.status_code == status:
                if return_content is None:
                    return status
                else:
                    content = response.json()
                    return content[return_content]
        raise ConnectionError
