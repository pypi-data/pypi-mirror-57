from . import tablemaker
import re
import collections
from .asciiMathConverter import convert
from .messages import error

asciiMathDelimiterLeft="\$"
asciiMathDelimiterRight="\$"

def asciiMathToLatex(inp):
    asciiMathRegex = re.compile(asciiMathDelimiterLeft+'([\w\W]+?)'+asciiMathDelimiterRight, re.MULTILINE)
    PlaceHolder = "HALLGRIMASCIIMATHPLACEHOLDER"
    asciiMathParts = collections.deque()
    for m in re.finditer(asciiMathRegex, inp):
        converted = convert(m.groups(2)[0], 'asciimath', 'latex')
        asciiMathParts.append(converted)
    source = re.sub(asciiMathRegex, PlaceHolder, inp)
    texts = collections.deque(source.split(PlaceHolder))
    final = collections.deque()
    for _ in range(min(len(texts), len(asciiMathParts))):
            text = texts.popleft()
            if text != "":
                    final.append(text)
            final.append(asciiMathParts.popleft())
    final.extend(asciiMathParts)
    final.extend(texts)
    final = "".join(final)
    return final

def preProcessText(inp):
    """ Performs preprocessing on the text in the tasks. Currently consists of processing [table]-tags and asciiMath."""
    output = tablemaker.prepareTables(inp)
    output = asciiMathToLatex(output)
    return output
