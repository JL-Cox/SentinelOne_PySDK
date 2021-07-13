from config import Config
from json import loads
from validations import push_by_id_validation


class Agents: 

    


class Call:

    url = "https://usea1-swprd1.sentinelone.net/web/api/v2.1"
    options = {"agents": "/agents","decommission": "/agents/actions/decommission"}
    api_key = Config.api_key
    auth_header = {'Authorization': f"ApiToken {api_key}"}

    def PushByID(ids):

        if push_by_id_validation(ids):
            return loads(str({"data":{}, "filter":  {"ids": ids}}).replace("'", "\""))
        else: 
            raise TypeError(f"PushCall() takes one argument 'ids' that should be of type 'list' instead of '{type(ids)}'")

   
