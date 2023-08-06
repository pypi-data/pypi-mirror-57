#!/usr/bin/env bash
# @Project      : tql-Python
# @Time         : 2019-11-28 11:49
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : siege -c 500 r -1  'HTTP_URL POST <./postfile.json'

siege -c 200 -r 1000 'http://web.algo.browser.miui.srv/ai-pipeline/push POST <./post.json' \
> request.txt

