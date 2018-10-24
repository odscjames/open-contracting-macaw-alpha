from collections import OrderedDict

COVE_CONFIG = {
    'app_name': 'cove_ocds',
    'app_base_template': 'cove_ocds/base.html',
    'app_verbose_name': 'Open Contracting Data Standard Validator',
    'app_strapline': 'Validate and Explore your data.',
    'schema_name': {'release': 'release-package-schema.json', 'record': 'record-package-schema.json'},
    'schema_item_name': 'release-schema.json',
    'schema_host': None,
    'schema_version_choices': OrderedDict((  # {version: (display, url)}
        ('1.0', ('1.0', 'http://standard.open-contracting.org/schema/1__0__3/')),
        ('1.1', ('1.1', 'http://standard.open-contracting.org/schema/1__1__3/')),
    )),
    'schema_codelists': OrderedDict((  # {version: codelist_dir}
        ('1.1', 'https://raw.githubusercontent.com/open-contracting/standard/1.1/standard/schema/codelists/'),
    )),
    'root_list_path': 'releases',
    'root_id': 'ocid',
    'convert_titles': False,
    'input_methods': ['upload', 'url', 'text'],
    'support_email': 'data@open-contracting.org'
}

# Set default schema version to the latest version
COVE_CONFIG['schema_version'] = list(COVE_CONFIG['schema_version_choices'].keys())[-1]
