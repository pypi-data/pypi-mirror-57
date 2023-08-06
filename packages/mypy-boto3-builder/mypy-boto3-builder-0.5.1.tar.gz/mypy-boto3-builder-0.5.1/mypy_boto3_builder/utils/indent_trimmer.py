"""
Utility for removing indentation for sections and lines.
"""

from typing import Iterable, List


__all__ = ["IndentTrimmer"]


class IndentTrimmer:
    """
    Utility for removing indentation for sections and lines.
    """

    @staticmethod
    def trim_empty_lines(lines: List[str]) -> List[str]:
        """
        Trim empty lines in the begging and the end of the text.

        Examples::

            IndentTrimmer.trim_empty_lines([
                '',
                '  asd',
                ' asd',
                '   asd',
                '  ',
                '',
            ])
            [
                '  asd',
                ' asd',
                '   asd',
            ]

        Returns:
            Lines wih no empty lines at start and end.
        """
        result = list(lines)
        while result and not result[0].strip():
            result.pop(0)
        while result and not result[-1].strip():
            result.pop()

        return result

    @classmethod
    def trim_text(cls, text: str) -> str:
        """
        Trim minimum indent from each line of text.

        Examples::

            IndentTrimmer.trim_text('  asd\\n asd\\n   asd\\n')
            ' asd\\nasd\\n  asd\\n'

        Arguments:
            text -- Multiline text.

        Returns:
            A text with trimmed indent.
        """
        new_lines = IndentTrimmer.trim_lines(text.split("\n"))
        return "\n".join(new_lines)

    @classmethod
    def trim_lines(cls, lines: Iterable[str]) -> List[str]:
        """
        Trim minimum indent from each line of text.

        Examples::

            IndentTrimmer.trim_lines([
                '  asd',
                ' asd',
                '   asd',
            ])
            [
                ' asd',
                'asd',
                '  asd',
            ]

        Arguments:
            lines -- List of lines.

        Returns:
            A list of lines with trimmed indent.
        """
        indents = [cls.get_line_indent(line) for line in lines if line.strip()]
        min_indent = 0
        if indents:
            min_indent = min(indents)

        new_lines = []
        for line in lines:
            new_lines.append(cls.trim_line(line, min_indent))

        return new_lines

    @staticmethod
    def trim_line(line: str, indent: int) -> str:
        """
        Trim indent from line if it is empty.

        Examples::

            IndentTrimmer.trim_line('     test', 2)
            '   test'

            IndentTrimmer.trim_line('     test', 6)
            'test'

            IndentTrimmer.trim_line('     test', 1)
            '    test'

        Arguments:
            line -- A line of text.

        Returns:
            A line with removed indent.
        """
        if not line[:indent].strip():
            return line[indent:]

        return line.lstrip()

    @staticmethod
    def get_line_indent(line: str) -> int:
        """
        Get indent length of the line.

        Examples::

            IndentTrimmer.get_line_indent('   test')
            3

            IndentTrimmer.get_line_indent('test')
            0

        Arguments:
            line -- Line of text.

        Returns:
            A number of indentation characters in a beginning of the line.
        """
        return len(line) - len(line.lstrip())

    @staticmethod
    def indent_line(line: str, indent: int) -> str:
        """
        Indent line with givent length `indent`

        Examples::

            IndentTrimmer.indent_line('test', 2)
            '  test'

        Arguments:
            line -- Line to indent.
            indent -- Length of indent in spaces.

        Returns:
            An indented line.
        """
        return u"{}{}".format(" " * indent, line)
