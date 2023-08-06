from . import tablemaker
import re
import collections
from .asciiMathConverter import convert
from .messages import error

asciimath_delimiter_left="\$"
asciimath_delimiter_right="\$"

def ascii_math_to_latex(inp):
    asciimath_regex = re.compile(asciimath_delimiter_left + '([\w\W]+?)'+ asciimath_delimiter_right, re.MULTILINE)
    PLACEHOLDER = "HALLGRIMASCIIMATHPLACEHOLDER"
    asciimath_parts = collections.deque()
    for m in re.finditer(asciimath_regex, inp):
        converted = convert(m.groups(2)[0], 'asciimath', 'latex')
        asciimath_parts.append(converted)
    source = re.sub(asciimath_regex, PLACEHOLDER, inp)
    texts = collections.deque(source.split(PLACEHOLDER))
    final = collections.deque()
    for _ in range(min(len(texts), len(asciimath_parts))):
            text = texts.popleft()
            if text != "":
                    final.append(text)
            final.append(asciimath_parts.popleft())
    final.extend(asciimath_parts)
    final.extend(texts)
    final = "".join(final)
    return final

def pre_process_text(inp):
    """ Performs preprocessing on the text in the tasks. Currently consists of processing [table]-tags and asciiMath."""
    output = tablemaker.prepareTables(inp)
    output = ascii_math_to_latex(output)
    return output

