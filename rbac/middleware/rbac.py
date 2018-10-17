from django.conf import settings
from django.shortcuts import HttpResponse, redirect
import re


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):
    """
    检查用户请求的url是否在其权限范围之内
    """
    def process_request(self, request):
        request_url = request.path_info
        permission_url = request.session.get(settings.SESSION_PERMISSION_URL_KEY)
        if settings.DEBUG:
            print('---当前访问url---', request_url)
            print('------权限------', permission_url)

        # 如果请求的url中，则允许
        for url in settings.SAFE_URL:
            if re.match(url, request_url):
                return None

        # 如过permission_url为空，重定向登陆界面
        if not permission_url:
            return redirect(settings.LOGIN_URL)

        # 循环正则匹配
        flag = False
        for url in permission_url:
            url_pattern = settings.REGEX_URL.format(url=url)
            if re.match(url_pattern, request_url):
                flag = True # 匹配成功
                break
        if flag:
            return None
        else:
            if settings.DEBUG:
                info = '<br/>' + ('<br/>'.join(permission_url))
                return HttpResponse('无权限，请尝试访问以下地址：%s' % info)
            else:
                return HttpResponse('无权限访问')