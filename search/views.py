# Create your views here.
from django.shortcuts import render
from django.conf import settings

from .forms import SearchForm
from utils.file_info import FileInfo

es = settings.ES

def build_query(condition_dict):
    query_body = {"query": {"bool": {"must": []}}}
    highlight_keywords = []
    for condition in condition_dict:
        if condition_dict[condition]:
            query_body['query']['bool']['must'].append({'match':{condition: condition_dict[condition]}})
            highlight_keywords.append(condition_dict[condition])
    highlight_keyword = '|'.join(highlight_keywords)
    return query_body, highlight_keyword

def search(request, template):
    form = SearchForm(request.POST)
    highlight_keyword = ''
    if form.is_valid():
        cleaned_data = form.cleaned_data
        file_title = cleaned_data['file_title']
        file_content = cleaned_data['file_content']
        file_name = cleaned_data['file_name']
        file_author = cleaned_data['file_author']
        
        search_by_content_result = {'hits':{'hits':[]}}
        if 'searching' in request.POST.keys():
            if  not file_title and not file_content and not file_name and not file_author:
                form.add_error('file_title', 'Enter at least one field for searching')
                return render(request, template, {'form': form})
            query_body, highlight_keyword = build_query({'meta.title.cn': file_title,
                                                          'content.cn': file_content,
                                                          'file.filename.cn': file_name,
                                                          'meta.author.cn': file_author})
            
            search_by_content_result = es.search(index = settings.ES_INDEX, body=query_body)
        
        
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
            
            try:
                content_keyword_index = result_one['_source']['content'].index(file_content)
            except ValueError:
                content_keyword_index = 0
                
            content_length = len(result_one['_source']['content'])
            show_len = 500
            result_one_obj_content = result_one['_source']['content'][int(content_keyword_index-show_len if content_keyword_index>=show_len else content_keyword_index):
                                                                      int(content_keyword_index+show_len if content_keyword_index+show_len < content_length else content_length-content_keyword_index)]
            result_one_obj_content = '......' + result_one_obj_content + '......'
            result_one_obj = FileInfo(result_one_obj_title,
                                    result_one_obj_date,
                                    result_one_obj_path,
                                    result_one_obj_content,
                                    result_one_obj_author,
                                    result_one_obj_type)
            result_one_list.append(result_one_obj)
    return render(request, template, {'form': form, 'result_list': result_one_list, 'highlight_keyword': highlight_keyword})