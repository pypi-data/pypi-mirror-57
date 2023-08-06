#
# * This file is subject to the terms and conditions defined in
# * file 'LICENSE.txt', which is part of this source code package.

from .shared_properties import Publication, Person, CodeRepository, WebSite, Keyword, ApplicationSuite, object_attributes
from hashlib import md5
import uuid




def _mk_hashes(arg1, *args):
    arg1 = str(arg1)
    hashes = [md5(arg1.encode(encoding='utf-8')).hexdigest()]
    for arg in args:
        arg = str(arg)
        hashes.append(md5(arg.encode(encoding='utf-8')).hexdigest())
    return hashes


def mk_tool_identifier(name, version, start=0):
    name_hash, version_hash = _mk_hashes(name, version)
    identifier = f"TL_{name_hash[start:start + 6]}.{version_hash[:2]}"
    return identifier


def mk_tool_instance_identifier(tool_identifier):
    uuid_string = uuid.uuid4().hex[:4]
    return f"{tool_identifier}.{uuid_string}"


def mk_subtool_identifier():
    raise NotImplementedError


def mk_script_identifier():
    raise NotImplementedError


def mk_workflow_identifier():
    raise NotImplementedError


def mk_empty_prop_object(property_name):
    """
    Should only call this to override a None value for a property.
    :param property_name:
    :return:
    """
    prop_map = {'codeRepository': {'name': None}, 'publication': [{'identifier': None}],
                'contactPoint': [{'name': None}], 'creator': [{'name': None}], 'WebSite': [{'name': None}], 'keywords': [Keyword()], 'applicationSuite': {'name': None, 'softwareVersion': None, 'identifier': None}}
    if not property_name in prop_map:
        return None

    return prop_map[property_name]


def is_attr_empty(attribute):
    # Need to check for lists.
    if isinstance(attribute, list):
        is_empty = True
        for item in attribute:
            if not is_attr_empty(item):
                is_empty = False
                break
    elif isinstance(attribute, object_attributes):
        is_empty = attribute.is_empty()
    else:
        if attribute:
            is_empty = False
        else:
            is_empty = True
    return is_empty


class CommonPropsMixin:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError(f"'name'' must be set.")
        self._name = new_name

    @property
    def softwareVersion(self):
        return str(self._softwareVersion)

    @softwareVersion.setter
    def softwareVersion(self, new_softwareVersion):

        if not new_softwareVersion:  # softwareVersion not defined. Check in parentMetadata
            raise ValueError(f"'softwareVersion must be set.")
        self._softwareVersion = new_softwareVersion
        return

    @property
    def publication(self):
        return self._publication

    @publication.setter
    def publication(self, publication_list):
        if publication_list:
            publications = [Publication(**pub) for pub in publication_list]
        else:
            publications = None
        self._publication = publications

    @property
    def contactPoint(self):
        return self._contactPoint

    @contactPoint.setter
    def contactPoint(self, person_list):
        if person_list:
            people = [Person(**person) for person in person_list]
        else:
            people = None
        self._contactPoint = people

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, person_list):
        if person_list:
            people = [Person(**person) for person in person_list]
        else:
            people = None
        self._creator = people

    @property
    def codeRepository(self):
        return self._codeRepository

    @codeRepository.setter
    def codeRepository(self, code_repo_dict):
        if code_repo_dict:
            code_repos = CodeRepository(**code_repo_dict)
        else:
            code_repos = None
        self._codeRepository = code_repos

    @property
    def applicationSuite(self):
        return self._applicationSuite

    @applicationSuite.setter
    def applicationSuite(self, application_suite_dict):
        if application_suite_dict:
            application_suite = ApplicationSuite(**application_suite_dict)
        else:
            application_suite = None
        self._applicationSuite = application_suite

    @property
    def WebSite(self):
        return self._website

    @WebSite.setter
    def WebSite(self, website_list):
        if website_list:
            websites = [WebSite(**website_dict) for website_dict in website_list]
        else:
            websites = None
        self._website = websites
