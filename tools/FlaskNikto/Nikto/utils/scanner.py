#!/usr/bin/env python

import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class Scanner:
    def __init__(self, url):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []

    def extract_links_from(self,url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features = "lxml")
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urljoin(url, action)
        method = form.get("method")
        input_list = form.findAll("input")
        post_data = {}

        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
            post_data[input_name] = input_value

        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print(f"[+] Testing form in {link}")
                is_vuln_to_xss = self.test_xss_in_form(form, link)
                if is_vuln_to_xss:
                    print(f"\n\n[***] XSS discovered in {link}, in the following form: ")
                    print(form)

            if "=" in link:
                print(f"\n\n[+] Testing in {link}")
                is_vuln_to_xss = self.test_xss_in_link(link)
                if is_vuln_to_xss:
                    print(f"[***] XSS discovered in {link}")

    def test_xss_in_link(self, url):
        xss_test_script = "<sCript>alert('test')</scrIpt>"
        url = url.replace("=", f"={xss_test_script}")
        response = self.session.get(url)
        return xss_test_script.encode() in response.content

    def test_xss_in_form(self, form, url):
        xss_test_script = "<sCript>alert('test')</scrIpt>"
        response = self.submit_form(form, xss_test_script, url)
        return xss_test_script.encode() in response.content


    # def form_details(self, form):
    #     detailsOfForm = {}
    #     action = form.attrs.get("action").lower()
    #     method = form.attrs.get("method", "get").lower()
    #     inputs = []

    #     for input_tag in form.find_all("input"):
    #         input_type = input_tag.attrs.get("type", "text")
    #         input_name = input_tag.attrs.get("name")
    #         input_value = input_tag.attrs.get("value", "")
    #         inputs.append(
    #             {"type": input_type, "name": input_name, "value": input_value}
    #         )

    #     detailsOfForm["action"] = action
    #     detailsOfForm["method"] = method
    #     detailsOfForm["inputs"] = inputs
    #     return detailsOfForm

    # def vulnerable(self, response):
    #     errors = {"quoted string not properly terminated",
    #               "unclosed quotation mark after the character string",
    #               "you have an error in your sql syntax;"}

    #     for error in errors:
    #         if error in response.content.decode().lower():
    #             return True
    #     return False

    # def sql_injection_scan(self, url):
    #     forms = self.extract_forms(url)
    #     print(f"[+] Detected {len(forms)} forms on {url}.")

    #     for form in forms:
    #         details = self.form_details(form)

    #         for c in "\"'":
    #             data = {}

    #             for input_tag in details["inputs"]:
    #                 if input_tag["type"] == "hidden" or input_tag["value"]:
    #                     data[input_tag["name"]] = input_tag["value"] + c
    #                 elif input_tag["type"] != "submit":
    #                     data[input_tag["name"]] = f"test{c}"
    #             a = self.form_details("action")
    #             url = urljoin(url, a)

    #             if details["method"] == "post":
    #                 res = self.session.post(url, data=data)
    #             elif details["method"] == "get":
    #                 res = self.session.get(url, params=data)
    #             if self.vulnerable(res):
    #                 print("SQL Injection attack vulnerability detected in link:", url)
    #             else:
    #                 print("No SQL Injection vulnerability detected")
    #                 break