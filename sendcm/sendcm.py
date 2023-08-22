import requests

class SendCM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://send.cm/api"

    def _make_request(self, endpoint, params=None):
        headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            headers["key"] = self.api_key

        response = requests.get(f"{self.base_url}{endpoint}", headers=headers, params=params)
        response_data = response.json()
        return response_data

    def get_account_info(self):
        """
        Return account info of account
        """
        endpoint = "/account/info"
        params = {"key": self.api_key}
        return self._make_request(endpoint, params=params)

    def get_account_stats(self, last=7):
        """
        Return account stats
        """
        endpoint = "/account/stats"
        params = {"key": self.api_key, "last": last}
        return self._make_request(endpoint, params=params)

    def get_next_upload_server_url(self):
        """
        return data containing url for uploading server and a session key required to upload!
        """
        endpoint = "/upload/server"
        params = {"key": self.api_key}
        return self._make_request(endpoint, params=params)

    def get_upload_server_url_without_account(self):
        """
        return upload server url to upload to without session key for public/guest usage.
        """
        endpoint = "/upload/server"
        return self._make_request(endpoint)

    def upload_remote_url(self, url):
        """
        url = pass url of the remote source file to be uploaded to sendcm
        Return the url of the file uploaded remotely to your account!
        """
        endpoint = "/upload/url"
        params = {"key": self.api_key, "url": url}
        return self._make_request(endpoint, params=params)

    def upload_remote_url_without_account(self, url):
        """
        it will take remote file url and return the sendcm public url and file id of file uploaded!
        
        """
        endpoint = "/upload/url"
        params = {"url": url}
        return self._make_request(endpoint, params=params)

    def get_file_info(self, file_code):
        """
        file_code = file code / file id 
        Return the info of the file!
        """
        endpoint = "/file/info"
        params = {"key": self.api_key, "file_code": file_code}
        return self._make_request(endpoint, params=params)

    def get_file_list(self, page=None, per_page=None, fld_id=None, public=None, created=None, name=None):
        """
    
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + page: 2 (optional,number) - page number
        + per_page: 20 (optional,number) - number of results per page
        + fld_id: 15 (optional,number) - folder id
        + public: 1 (optional,number) - show public (1) or private (0) files only
        + created: `2018-06-21 05:07:10` (optional,string) - show only files uploaded after timestamp. Specify number to show only files uploaded X minutes ago.
        + name: `Iron man` (optional,string) - filter file names
        """
        endpoint = "/file/list"
        params = {
            "key": self.api_key,
            "page": page,
            "per_page": per_page,
            "fld_id": fld_id,
            "public": public,
            "created": created,
            "name": name
        }
        return self._make_request(endpoint, params=params)

    def rename_file(self, file_code, new_name):
        """
        + Parameters
        + file_code: gi4o0tlro01u,gi4o0tlro012 (string) - file code, or list separated by comma
        + name: cool_video.mp4 (string) - new file name
        """
        endpoint = "/file/rename"
        params = {"key": self.api_key, "file_code": file_code, "name": new_name}
        return self._make_request(endpoint, params=params)

    def clone_file(self, file_code):
        """
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + file_code: gi4o0tlro01u,gi4o0tlro012 (string) - file code"""
        endpoint = "/file/clone"
        params = {"key": self.api_key, "file_code": file_code}
        return self._make_request(endpoint, params=params)

    def set_file_folder(self, file_code, fld_id):
        '''
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + file_code: gi4o0tlro01u,gi4o0tlro012 (string) - file code, or list separated by comma
        + fld_id: 15 (number) - folder id
        '''
        endpoint = "/file/set_folder"
        params = {"key": self.api_key, "file_code": file_code, "fld_id": fld_id}
        return self._make_request(endpoint, params=params)

    def get_folder_or_file_list(self, fld_id = None):
        """
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + fld_id: 15 (optional,number) - folder id
        """
        endpoint = "/folder/list"
        params = {"key" : self.api_key , "fld_id" : fld_id}
        return self._make_request(endpoint,params=params)

    def create_folder(self,name,parent_id=None):
        """
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + parent_id: 15 (optional,number) - parent folder id
        + name: New Folder (string) - folder name
        """
        endpoint = "/folder/create"
        params = {"key":self.api_key, "parent_id" : parent_id,"name":name}
        return self._make_request(endpoint,params=params)
    
    def rename_folder(self,fld_id,name):
        """
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + fld_id: 15 (number) - folder id
        + name: New Folder (string) - folder name
        """
        endpoint ="/folder/rename"
        params = {"key" : self.api_key, "name" : name, "fld_id" : fld_id}
        return self._make_request(endpoint,params=params)

    def get_deleted_files(self, last = None):
        """
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + last: 20 (optional,number) - number of files limit
        """
        endpoint = "/files/deleted"
        params = {"key" : self.api_key, "last" : last}
        return self._make_request(endpoint,params = params)
    
    def get_files_scheduled_for_DCMA_delete(self, last=None):
        """
        + Parameters
        + key: 1l5ftrilhllgwx2bo (string) - API key
        + last: 20 (optional,number) - number of files limit
        """
        endpoint= "/files/dmca"
        params = {"key" : self.api_key,"last": last}
        return self._make_request(endpoint, params= params)

