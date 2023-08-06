from django.test import TestCase

from rdmo.core.testing.mixins import TestImportManageMixin


class DomainManageTestCase(TestCase):

    fixtures = (
        'users.json',
        'groups.json',
        'accounts.json',
        'domain.json',
        'options.json',
    )


class DomainImportManageTests(TestImportManageMixin, DomainManageTestCase):

    import_file = 'testing/xml/domain.xml'

    compare_import_to_export_data = True
    compare_import_to_export_ignore_list = []
    export_api = 'domain_export'
    export_api_kwargs = {'format': 'xml'}
    export_api_format_list = ['pdf', 'rtf', 'odt', 'docx', 'html', 'markdown', 'mediawiki', 'tex', 'xml']
