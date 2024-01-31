import scrapy
from scrapy import Request
import json
from urllib.parse import urlencode

HEADERS = {
    "authority": "www.pinterest.com",
    "accept": "application/json, text/javascript, */*, q=0.01",
    "accept-language": "en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.pinterest.com",
    "referer": "https://www.pinterest.com/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.86", "Chromium";v="121.0.6167.86"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua-platform-version": "10.0.0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "x-app-version": "8f6731f",
    "x-csrftoken": "bcd4b8864808d788713238fc9e0d68e6",
    "x-pinterest-appstate": "background",
    "x-pinterest-pws-handler": "www/search/[scope].js",
    "x-pinterest-source-url": "/search/pins/?q=taylor%20swift&rs=typed",
    "x-requested-with": "XMLHttpRequest",
}


class TaylorSpider(scrapy.Spider):
    name = "taylor"
    allowed_domains = ["pinterest.com"]
    start_urls = ["https://www.pinterest.com/resource/BaseSearchResource/get/"]

    # start req
    def start_requests(self):
        req = self.makeRequest("")
        req.callback = self.parse
        yield req

    def parse(self, response):
        # print(f"response: {response.text}")
        with open("data2.json", "w") as f:
            data = json.loads(response.text)
            json.dump(data, f, indent=2)

    def makeRequest(self, bookmark: str):
        options = {
            "options": {
                "article": None,
                "applied_filters": None,
                "appliedProductFilters": "---",
                "auto_correction_disabled": False,
                "corpus": None,
                "customized_rerank_type": None,
                "domains": None,
                "filters": None,
                "page_size": None,
                "price_max": None,
                "price_min": None,
                "query": "taylorswift",
                "query_pin_sigs": None,
                "redux_normalize_feed": None,
                "rs": "content_type_filter",
                "scope": "pins",
                "source_id": None,
                "top_pin_id": None,
                "bookmarks": [
                    "Y2JVSG81V2sxcmNHRlpWM1J5VFVaU1ZWRllhR3RXTVVZMldWVlZNVlV4U25Sak0yaFhVbTFvTTFaWGN6RldhekZXVm14b1YxSllRbEJYVm1ONFZEQTFWMVZzYkdwU1ZGWlFWV3hvVTJWV1pISlhhM1JYVm10V05sVldVbE5XVmxwR1kwZG9XbUpHVmpSV2JGcFRaRVV4Vms1V1RsTldWbGt4Vm10YVYyRXhXbkpOV0U1b1RUSjRWRlpyVm5kaFJsWnlWbXQwYVUxV1NqRlpNRlpyWVVVeFJWSnVhRmRTYkVwTVYxWmFTbVF3TVZWV2JGWlhZa1Z3VFZkV1pIcGxSVFZ6Vld4c1lWSlVWbTlaVkVvd1RsWlplRnBJWkZOaGVrWjVWR3hXYjFaSFNsaGhSMmhYWVRGYWVWcFZXbE5XTVhCR1RsVTFVMkpyU2xkV2JYaHZZakZTYzFOcldsZFdSVnBXVm10V2QxVkdiRmhqTTJoVFZteHdNRmt3VlRGV01ERldWMVJDVjFKdFRYaFVhMXBTWlVaT2MxcEhSbE5TTWswMVdtdGFWMU5YU2paVmJYaHBWbTVDUjFaWGVHOWhNVkY1VW01U2ExSkdjRlpaVkVaTFpWWndSVkZVUm1wV2JWSmFXV3RWTldKSFJYbGtla3BYVW0xb00xbHRNVTlXTVU1WllVWk9hR1ZyV2s1WFZ6QXhZakpPUjFwR2FHcFNlbFp6V1Zod1YyVkdWbGhOV0dSV1VteHNORmxZY0VkV1YwVjVWV3hPVldKR1ZqUlZiRnBQWkVkU1NGSnNaRTVTYkZreVZtcEtOR0V4VVhsU2JrNW9UVEo0VmxaclZURlZSbHB4VVd4YWJGWnNTbGhYYTFwM1lrZEdObEpVU2xwV1JUVjZWbFZhU21ReVJYcGlSbFpwVjBWS1JGWkdaSHBsUjA1WFYyNVNhbEp1UWxoVmFrRjNaVVpaZVdSSGRGcFdNRnBYVkd0b2MxWldXa1pPVjJoYVZqTlNTRlJzV210ak1YQkhWRzFvYVZORlNrZFdiWGh2WXpGc1YxZFlaRTlYUlRWb1dWUkdWbVZHVm5SbFJuQnNZbFpKTWxSVlVYaFBSVEZWVVZSS1VGWkZNSGRVTVZKQ1RXczFjVk5VVGs1aGF6RTJWREJPZDFOR1ZsWmtNMFp0VWtVd2VsZHNaRmRoUm10NVZsUkNZV0pWYTNsVVZXUlNUVVpzY1ZOdE1XRlNNV3cyVjFod2EyRkZNVlZVVkVKUVZqQlZkMWR0Y0d0aE1XdzJWRlJLVGxKRlZURlVibkJTVFd4d1NGWlljRnBpVlRCNVZHcEtUazFHY0hGVmJYaFBUV3RhY0Zkc1pGWk9SVGxZVTIxd1RsSkhaelJXUjNSWFYwZGFRbEJVTVRoTlZFRXlUMVJOTUU5VVFUSk9ha2t6VFdwTmVrOURjRWhWVlhkeFprUlZlVmxxVG0xT2VrWnNXa1JWZWxwdFZtaFBSRUpxVFdwbk5VNXRXbXRaVkVwcFRUSktiRTU2UlhwYVJGSm9UbFJWZUUxcVkzcE9ha0V4VFZSck1sbDZWbWxQVkZGM1RXMWFiVmt5V1ROYVZFMHhUakpPT0ZSclZsaG1RVDA5fFVIbzVSV1ZZVWpGaFJ6VjBXVzFvUkdONk1XWk9lbFptVFROM2VFMUVXVFZOZWxFMVRVUlpNazFxWTNsTmVrMDBTMnRrVWxSRGNEaE9SRVUxV1RKYWExbFViR3RQVkZGNFRXMUZOVmx0VVROYVYxSnRUMVJSTVU1NlRteE5WMFV4V21wS2EwNUhUbXRaVkd4cFRWUkJlVmw2U1RCYVJHUnNXVmRhYUZsdFRUUk5lbGw0VFZSU2ExbDZWVEpOV0hoUFVsWmtPQT09fE5vbmV8MTA2OTM0OTA2NjI3MjMzOCpHUUwqfDFmYjAyODI5MTE2MmE2ZDVjNjg2NDQ5YmUwODlhNTIwNzc3MzA3ZTQzNDgxMjZlZGNmZDk3NTYwNWYzMTU1NTV8TkVXfA=="
                ],
            },
            "context": {},
        }

        data = {
            "source_url": ["/search/pins/?q=taylorswift&rs=content_type_filter"],
            "data": [f"{json.dumps(options)}"],
        }

        req = scrapy.Request.from_curl(
            f"""curl 'https://www.pinterest.ca/resource/BaseSearchResource/get/' \
            -H 'authority: www.pinterest.ca' \
            -H 'accept: application/json, text/javascript, */*, q=0.01' \
            -H 'accept-language: en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5' \
            -H 'content-type: application/x-www-form-urlencoded' \
            -H 'cookie: csrftoken=b3409071190d3e513bc0b955fdd0515f; _routing_id="5ab875f9-49eb-436d-bd4e-855cb7c3b656"; sessionFunnelEventLogged=1; _auth=1; _pinterest_sess=TWc9PSZXbERqR3JFOWNxaDEzWk9yMmFrZkRsQUN6NnVlYmc0c1RuRjY4dE9Welo3d1Mya3FIRkNKLzFXRGtBWVczQWpXNkVYdnB5SDhyaFM5M3JXZTlvY0FaZ0F4OGpnc3NpUFRmNEMrcmV3WUJUVjBqUWZyNWRYUmgrNnN1Sm4xcS9RbWxVSmhrU2lVWnJYeDB6S3pMUEJBMWpuWGtWa0pDN1dLT1FqL0RqMjVXM1BCSkRkTkVMZUNrSDNqS3g1bnNVb1ZFQUxHOE5TUDg0WmYrbEtMaUgwYWQwclBPanVWa01LQ2ZFZXg4S2E1NUczTmRUaTVNL1Rhem1GdFI4dXMxc0ViTmVsQ0pJbXJQaG95VDZEbENHbEQ1MlpuYzRsMk1CS1hFSHdmcFAyQ2syU2dmSVpPY3dkWEk1aWI4U2ZjUXVkZWMwRTcxeWtKRVoreDB4WjRFc2h4ZXdYSUZwZi9oWXE2MUc1ZzI5UVQrenc9JjZGZVI4T2dyd1lHR2lEL1laTk5JWjQxVnRmcz0=; __Secure-s_a=Vy93ZSt0dlVmWktvcUxYREt3dW9nSTRTUURqaGhseEhZa3Y0djU5YmtYRnVZZmF6TzZMRzZUZmN5dlFVcmc2NVZ3TEZiYzdPc3A4YVNCK0NKdWduaFdpcElLRGFVeVNVMU5LWnpjWDlGVUhSLzhMMUlSVmZqUjZ0SUt0OTE4VWwxeENlQ1BuUU9qZzFKbXA4UVE3c3FHUG0wZ3ZrajZWbnZ3ejBmek1oWmNzOWVEbDN6VjE0a2I5b3hKcWNpeHhpeW1QNHU1a2Uxa2xnSDdNcW5ZRmhOTDQ2OEUxMS9pNWFiWVpRUFhPSjBnbEhXeXhIbHNHUlJsTE4yV0pGNk9hcyZIanB4YVUxcEExUjJpTWdyZ1RmT2NxREZ3Tm89; cm_sub=dismissed; ar_debug=1' \
            -H 'origin: https://www.pinterest.ca' \
            -H 'referer: https://www.pinterest.ca/' \
            -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
            -H 'sec-ch-ua-full-version-list: "Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.86", "Chromium";v="121.0.6167.86"' \
            -H 'sec-ch-ua-mobile: ?0' \
            -H 'sec-ch-ua-model: ""' \
            -H 'sec-ch-ua-platform: "Windows"' \
            -H 'sec-ch-ua-platform-version: "10.0.0"' \
            -H 'sec-fetch-dest: empty' \
            -H 'sec-fetch-mode: cors' \
            -H 'sec-fetch-site: same-origin' \
            -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
            -H 'x-app-version: efbbfb8' \
            -H 'x-csrftoken: b3409071190d3e513bc0b955fdd0515f' \
            -H 'x-pinterest-appstate: active' \
            -H 'x-pinterest-pws-handler: www/search/[scope].js' \
            -H 'x-pinterest-source-url: /search/pins/?q=taylorswift&rs=content_type_filter' \
            -H 'x-requested-with: XMLHttpRequest' \
            --data-raw '{urlencode(data, doseq=True)}'\
            --compressed"""
        )
        req.callback = self.parse
        return req
