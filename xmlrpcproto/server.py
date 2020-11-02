from typing import Union, List, Mapping, Tuple, cast
from lxml.builder import E
from lxml.etree import _Element, XMLParser, fromstring, tostring

from .common import XmlRpcTypes, py2xml, validate_schema, xml2py


def format_success(result: XmlRpcTypes) -> _Element:
    return E(
        "methodResponse", E("params", E("param", E("value", py2xml(result))))
    )


def format_error(exception: Exception) -> _Element:
    return E("methodResponse", E("fault", E("value", py2xml(exception))))


def parse_xml(xml_string: bytes) -> _Element:
    parser = XMLParser(resolve_entities=False)
    root = fromstring(xml_string, parser)
    if not validate_schema(root):
        raise ValueError("Invalid body")
    return root


def build_xml(tree: _Element) -> Union[str, bytes]:
    return tostring(tree, xml_declaration=True, encoding="utf-8")


def parse_reqeuest(
    body: bytes, headers: Mapping[str, str]
) -> Tuple[str, List[XmlRpcTypes]]:
    if "xml" not in headers.get("Content-Type", ""):
        raise ValueError()

    xml_request = parse_xml(body)

    method_name = cast(str, xml_request.xpath("//methodName[1]/text()"))

    params = cast(
        List[Union[_Element, str]],
        xml_request.xpath(
            "//params/param/value/* | //params/param/value[not(*)]/text()"
        ),
    )
    args = [xml2py(param) for param in params]

    return method_name, args
