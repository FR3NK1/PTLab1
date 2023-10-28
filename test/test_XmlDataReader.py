import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml = """<?xml version="1.0" encoding="UTF-8" ?>
                <root>
                    <Иванов_Иван_Иванович>
                        <математика>90</математика>
                        <химия>100</химия>
                    </Иванов_Иван_Иванович>
                    <Тестов_Тест_Тестович>
                        <русский_язык>98</русский_язык>
                        <литература>89</литература>
                    </Тестов_Тест_Тестович>
                </root>"""
        data = {
            "Иванов_Иван_Иванович": [
                ("математика", 90), ("химия", 100)
            ],
            "Тестов_Тест_Тестович": [
                ("русский_язык", 98), ("литература", 89)
            ]
        }
        return xml, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        xml_content = XmlDataReader().read(filepath_and_data[0])
        assert xml_content == filepath_and_data[1]