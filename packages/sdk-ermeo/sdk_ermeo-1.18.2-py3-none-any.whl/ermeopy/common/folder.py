from ..const import API_ERMEO_FOLDER_URL, API_LIMIT, API_SORT_DEFAULT
from ..ermeo import ErmeoV1
from ..resource import Resource
from ..schema.folder_schema import FolderSchema


class Folder(Resource):
    """
    @param ermeo_v1: ErmeoV1
    """

    def __init__(self, ermeo_v1: ErmeoV1):
        self.ermeo_v1 = ermeo_v1
        super().__init__(ermeo_v1, self.ermeo_v1.api_ermeo_ressources_url + API_ERMEO_FOLDER_URL, FolderSchema)
