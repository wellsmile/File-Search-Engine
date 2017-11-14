from django.shortcuts import render
from django.conf import settings

from utils.file_info import FileInfo

es = settings.ES
# Create your views here.
def browse(request, template):
    search_by_content_result = es.search(index = settings.ES_INDEX)
    content_result_list = search_by_content_result['hits']['hits']
    result_one_list = []
    for result_one in content_result_list:
        try:
            result_one_obj_title = result_one['_source']['meta']['title']
        except KeyError:
            result_one_obj_title = '无法获取'
        try:    
            result_one_obj_date = result_one['_source']['meta']['created']
        except KeyError:
            result_one_obj_date = '无法获取'
        try:
            result_one_obj_path = result_one['_source']['path']['real']
        except KeyError:
            result_one_obj_path = '无法获取'
        try:
            result_one_obj_author = result_one['_source']['meta']['author']
        except KeyError:
            result_one_obj_author = '无法获取'
        try:
            result_one_obj_type = result_one['_source']['file']['content_type']
        except KeyError:
            result_one_obj_type = '无法获取'
        
        show_len = 500 if len(result_one['_source']['content']) >= 500 else len(result_one['_source']['content'])
        result_one_obj_content = result_one['_source']['content'][0:show_len]+'......'
        
        result_one_obj = FileInfo(result_one_obj_title,
                                result_one_obj_date,
                                result_one_obj_path,
                                result_one_obj_content,
                                result_one_obj_author,
                                result_one_obj_type)
        result_one_list.append(result_one_obj)
    return render(request, template, {'result_list': result_one_list})