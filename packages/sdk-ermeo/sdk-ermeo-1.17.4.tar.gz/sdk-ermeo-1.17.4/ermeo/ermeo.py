from .const import API_ERMEO_URL, API_ERMEO_LOGIN_URL, API_ERMEO_VERSION_URL


class ErmeoV1(object):
    def __init__(
            self,
            client_id: str = False,
            client_secret: str = False,
            username: str = False,
            password: str = False,
            api_ermeo_url: str = API_ERMEO_URL,
            access_token: str = False,
            refresh_token: str = False,
    ):
        """
        Init of all variables use for the calls + Modules

        @param client_id: str
        @param client_secret: str
        @param username: str
        @param password: str
        @param api_ermeo_url: str
        @param access_token: str
        @param refresh_token: str
        """
        self.api_ermeo_url = api_ermeo_url
        self.api_ermeo_ressources_url = self.api_ermeo_url + API_ERMEO_VERSION_URL
        self.api_ermeo_login_url = self.api_ermeo_url + API_ERMEO_LOGIN_URL
        self.username = username
        self.password = password
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

        self.load_modules()

    def load_modules(self):
        """
        # We load modules here, for avoid circular imports
        :return:
        """
        from .common.folder import Folder
        from .common.auth import Auth

        self.folder = Folder(self)
        self.auth = Auth(self)

        return self

    def check_request(self, r):
        """
        Check each request, and send error if any
        @param r: Request
        @return:
        """
        if r.status_code > 202:
            raise Exception(r.content, r.status_code)

    # def get_documents(self, documents=None, page=1, recursive=False, limit=API_LIMIT):
    #     """
    #     Get All Documents of the current Client
    #     @param documents: list
    #     @param page: int
    #     @param recursive: boolean
    #     @param limit: int
    #     @return: List
    #     """
    #     _documents = documents if documents else []
    #     r = requests.get(
    #         API_ERMEO_DOCUMENT_URL,
    #         headers=self.get_headers(),
    #         params={"page": page, "limit": limit},
    #     )
    #     self.check_request(r)
    #     data = r.json()
    #     if "items" in data:
    #         items = data["items"]
    #
    #         for item in items:
    #             _documents.append(item)
    #
    #         if data["next_page"] and recursive:
    #             next_page = page + 1
    #             self.get_documents(_documents, next_page, True)
    #
    #     return _documents
    #

    # # def create_document(self, document):
    # #     """
    # #
    # #     @param document:
    # #     @return: Json
    # #     """
    # #     document_validation = DocumentSchema().load(document)
    # #     if document_validation.errors:
    # #         raise Exception(document_validation.errors)
    # #
    # #     r = requests.post(API_ERMEO_DOCUMENT_URL, json=document, headers=self.get_headers())
    # #     self.check_request(r)
    # #     return r.json()
    #
    # def upload_file(self, binary_file, timeout=10):
    #     """
    #
    #     @param binary_file:
    #     @return:
    #     """
    #     r = requests.post(
    #         API_ERMEO_UPLOAD_URL,
    #         files={"file": binary_file},
    #         data={"type": "documents"},
    #         headers=self.get_headers(),
    #         timeout=timeout,
    #     )
    #     self.check_request(r)
    #     return r.json()
    #
    # def create_user(self, data):
    #     """
    #     @param data:
    #     @return:
    #     """
    #     r = requests.post(API_ERMEO_USER_URL, json=data, headers=self.get_headers())
    #     self.check_request(r)
    #     return r.json()
    #
    # def update_user(self, data):
    #     """
    #     @param data:
    #     @return:
    #     """
    #     r = requests.put(API_ERMEO_USER_URL, json=data, headers=self.get_headers())
    #     self.check_request(r)
    #     return r.json()
