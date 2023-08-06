from MountainRed.dbsm import DataBasesSettingsManager as DBSM
from django.http import JsonResponse
import json
from MountainRed.dbsm import logger, get_writers


def get_databases_options(request):
    options = DBSM().read_profile()
    options = [{"name": key, "options": options[key]}
               for key in options.keys()]
    return JsonResponse(options, safe=False)


def update_or_create_db_option(request):
    if request.method == 'POST':
        raw_options = json.loads(request.body.decode('utf-8'))
        logger.info(str(raw_options))
        options = {}
        for key in raw_options.keys():
            options[key.upper()] = raw_options[key]
        DBSM().update_or_create(options)
        return JsonResponse(dict(code=0, message="ok"))

    return JsonResponse(dict(code=-1, message="请求方法错误"))




def delete_option(request) -> JsonResponse:
    if request.method == 'POST':
        raw_options = json.loads(request.body.decode('utf-8'))
        logger.info(str(raw_options))
        name = raw_options['name']
        DBSM().delete_option(name)
        return JsonResponse(dict(code=0, message="ok"))

    return JsonResponse(dict(code=-1, message="请求方法错误"))
