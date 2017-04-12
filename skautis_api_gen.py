#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import pystache
import urllib2

import xml.etree.ElementTree as ElementTree

from urlparse import urljoin
from BeautifulSoup import BeautifulSoup as Soup

INDEX = 'https://test-is.skaut.cz/JunakWebservice/'
LIB_PATH = 'skautis'

reload(sys)
sys.setdefaultencoding('UTF8')



def get_soup(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return Soup(resp.content)

def main():
    sections = get_sections()

    if not os.path.exists(LIB_PATH):
        os.mkdir(LIB_PATH)
    for section in sections:
        write_section(section)

    with open(os.path.join(LIB_PATH, '__init__.py'), 'wb') as fd:
        renderer = pystache.Renderer()
        skautis_api = SkautisApi([module_name(section) for section in sections])
        fd.write(renderer.render(skautis_api))

def get_sections():
    sections = []
    soup = get_soup(INDEX)

    ul = soup.find('ul')
    for li in ul.findAll('li', recursive=False):
        sections.append(urljoin(INDEX, li.a['href']) + '?wsdl')
    return sections

def parse_wsdl(section_url):
    # wsdl namespaces
    ns = {'wsdl': 'http://schemas.xmlsoap.org/wsdl/',
          's': 'http://www.w3.org/2001/XMLSchema'}

    # load wsdl from the web
    tree = ElementTree.ElementTree(file=urllib2.urlopen(section_url))

    # extract service documentation
    doc_tree = tree.find('wsdl:documentation', ns)
    main_doc = "No documentation"
    if doc_tree is not None:
        main_doc = doc_tree.text

    # load interesting parts of wsdl file
    ports = tree.find('wsdl:portType', ns)

    # index parts of wsdl
    types = {}
    messages = {}
    for mes in tree.findall('wsdl:message', ns):
        messages[mes.attrib['name']] = mes.find('wsdl:part', ns)
    for schema in tree.find('.//wsdl:types/s:schema', ns):
        if 'name' in schema.attrib:
            types[schema.attrib['name']] = schema

    operations = []
    for port in ports:
        # load and check port documentation
        doc_tag = port.find('wsdl:documentation', ns)
        doc = doc_tag.text if doc_tag is not None else "No documentation"

        # load port name
        name = port.attrib['name']

        # load port message and recursively search for attributes
        message = port.find('wsdl:input', ns).attrib['message'].split(':')[1]
        element = messages[message].attrib['element'].split(':')[1]

        attributes = []
        attribute = None

        # find all attributes of outer container
        inner = types[element].find('.//s:element', ns)
        if inner is not None:
            # attributes are nested in other type
            if 'type' in inner.attrib and inner.attrib['type'].split(':')[0] == 'tns':
                inner_name = inner.attrib['type'].split(':')[1]
                for attr in types[inner_name].findall('.//s:element', ns):
                    attr_name = attr.attrib['name']
                    attr_type = attr.attrib['type'].split(':')[1] if 'type' in attr.attrib else ""
                    attr_required = True if attr.attrib['minOccurs'] == "1" else False
                    attributes.append((attr_name, attr_required, attr_type))

            else: # one attribute is on this level
                attr_name = inner.attrib['name']
                attr_type = inner.attrib['type'].split(':')[1] if 'type' in inner.attrib else ""
                attr_required = True if inner.attrib['minOccurs'] == "1" else False
                attribute = ((attr_name, attr_required, attr_type))

        # append this parsed operation to final list
        operations.append({'name': name, 'args': attributes, 'arg': attribute, 'doc': doc})

    return operations, main_doc

def module_name(section_url):
    module = section_url.split('/')[-1]
    module = module.split('.')[0]
    return module

def write_section(section_url):
    print section_url

    module = module_name(section_url)
    with open(os.path.join(LIB_PATH, '{}.py'.format(module)), 'wb') as fd:
        renderer = pystache.Renderer(string_encoding='utf-8', escape=lambda u: u)
        fd.write(renderer.render(ApiClass(section_url)))

def function_args(req_args, opt_args):
    return ', '.join(['self'] + req_args + [arg + '=None' for arg in opt_args])

def request_args(req_args, opt_args):
    args = req_args + opt_args
    data = '{{{}}}'.format(', '.join(['"{}": {}'.format(arg, arg) for arg in args])) if args else None
    return data

class ApiClass(object):
    def __init__(self, section_url):
        super(ApiClass, self).__init__()
        self._module = module_name(section_url)

        parsed = parse_wsdl(section_url)
        self._operations = parsed[0]
        self._doc = parsed[1]

    def class_name(self):
        return self._module

    def doc(self):
        return self._doc

    def methods(self):
        methods = []

        for op in self._operations:
            method_name = op['name']
            doc = op['doc']

            if op['arg'] is not None:
                args = '{}={}'.format(op['arg'][0], op['arg'][0])
                def_args = 'self, ' + op['arg'][0] + ('=None' if not op['arg'][1] else '')
            else:
                req_args = [arg[0] for arg in op['args'] if arg[1]]
                opt_args = [arg[0] for arg in op['args'] if not arg[1]]
                def_args = function_args(req_args, opt_args)
                args = request_args(req_args, opt_args)

            methods.append(dict(def_args=def_args, args=args, name=method_name, doc=doc))

        return methods

class SkautisApi(object):
    def __init__(self, sections):
        super(SkautisApi, self).__init__()
        self.sections = [{'module': section, 'class': section} for section in sections]

if __name__ == '__main__':
    main()
