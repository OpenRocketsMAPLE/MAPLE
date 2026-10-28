import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from scripts.sync_license import extract_license


class LicenseExtractionTests(unittest.TestCase):
    def write_odt(self, directory, body):
        path = Path(directory) / "license.odt"
        content = f'''<?xml version="1.0" encoding="UTF-8"?>
<office:document-content
 xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
 xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
 xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0">
 <office:body><office:text>{body}</office:text></office:body>
</office:document-content>'''
        with ZipFile(path, "w") as document:
            document.writestr("content.xml", content)
        return path

    def test_text_spacing_and_paragraph_breaks(self):
        body = ('<text:sequence-decls/><text:h>Title</text:h><text:p/>'
                '<text:p>A<text:s text:c="3"/><text:span>B'
                '<text:tab/>C</text:span><text:line-break/>D &amp; E</text:p>')
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(extract_license(self.write_odt(directory, body)),
                             "Title\n\nA   B\tC\nD & E\n")

    def test_unsupported_table_is_not_silently_omitted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_odt(directory, "<text:p>Text</text:p><table:table/>")
            with self.assertRaisesRegex(ValueError, "Unsupported ODT body element"):
                extract_license(path)

    def test_unsupported_inline_fields_are_not_silently_omitted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_odt(directory, "<text:p>Text<text:page-number/></text:p>")
            with self.assertRaisesRegex(ValueError, "Unsupported ODT inline element"):
                extract_license(path)


if __name__ == "__main__":
    unittest.main()
