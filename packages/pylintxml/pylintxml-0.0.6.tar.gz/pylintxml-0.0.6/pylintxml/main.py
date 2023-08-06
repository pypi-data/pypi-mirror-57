import argparse
import re
import sys
from pathlib import Path

import demjson
import lxml
from lxml import etree


def lint(content, rules):
    if isinstance(content, Path):
        print(str(content).center(80, '-'))
        content = content.read_text(encoding="utf-8").encode("utf-8")
    elif not isinstance(content, str):
        raise Exception("lint_ui error: unsupported type")

    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.fromstring(content, parser)
    lines = []

    for rule in rules:
        xpath = rule["selector"]
        for w in tree.xpath(xpath):
            is_valid = True
            args = {}
            for attrib in rule["attrs"]:
                key = attrib["attr"]
                value = w.attrib[key]
                args[key] = value
                m = re.match(attrib["regex"], value)
                is_valid = is_valid and bool(m)

            desc = rule['description'] % args
            lines.append({
                "line": w.sourceline,
                "desc": desc,
                "is_valid": is_valid
            })

    return lines


def main():
    parser = argparse.ArgumentParser(description='Lint a xml or set of xml files',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('paths', nargs='+', help='Xml files')
    parser.add_argument('-v', '--verbose', action="store_true", default=False)
    parser.add_argument('-s', '--sort', action="store_true",
                        help='Sort by rules (output sorted by lines by default)', default=False)
    parser.add_argument('-r', '--rules', help='Filename containing rules', default=".lintxml")
    args = parser.parse_args()

    try:
        rules = demjson.decode(Path(args.rules).read_text())
    except Exception:
        print(f"Error: {args.rules} not found")
        sys.exit(1)

    exit_code = 0
    for path in args.paths:
        try:
            lines = lint(Path(path), rules)
        except lxml.etree.XMLSyntaxError as e:
            print(f"Error parsing xml: {e}")
            continue

        if any([l['is_valid'] is False for l in lines]):
            exit_code = 1

        if not args.verbose:
            lines = [l for l in lines if not l["is_valid"]]
        if args.sort:
            lines = sorted(lines, key=lambda x: x["desc"])
        else:
            lines = sorted(lines, key=lambda x: x["line"])

        print("\n".join([
            f"Line {l['line']:<5}{'Ok' if l['is_valid'] else 'Fail':<6}: {l['desc']}"
            for l in lines
        ]))

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
