import re

MARKDOWN_CONVERTER_SOURCE = "https://cdn.jsdelivr.net/npm/showdown@1.9.0"
CODE_EDITOR_SOURCE = "https://pagecdn.io/lib/ace/1.4.6/ace.js"

CLEAN_HTML = """function HGCleaner(inp){
    var whitelist = ["P", "DIV", "H1","H2","H3","H4","H5","H6", "PRE", "CODE", "UL", "OL", "BLOCKQUOTE", "SPAN", "B", "BODY", "BR"]
    var clean = document.createElement("HGCleanerTemp");
    clean.innerHTML = inp;
    var a = 0;
    while (a < clean.childNodes.length){
        var elm = clean.childNodes[a];
        if(((typeof elm.tagName) != 'undefined') && whitelist.indexOf(elm.tagName.toString()) == -1){
            console.log("HG-BAD TAG:"+elm.tagName.toString());
            var warnElm = document.createElement('WARNING');
            warnElm.innerHTML = '<div>UNERLAUBTER HTML-TAG ERKANNT!</div>';
            elm.parentNode.replaceChild(warnElm, elm)
        }
    a = a + 1;
    }
    return clean.innerHTML;
}
"""

# encodes < and >, used for protection against XSS attacks
ENCODE_COMPARATORS ="""function HGCompEnc(inp){
    inp = inp.replace(/</g,"&lt;");
    inp = inp.replace(/>/g,"&gt;");
    return inp;
}
"""

# converts markdown with AsciiMath to HTML which can then be correctly displayed with MathJax
MD_AND_AM_TO_HTML = """function HGConvertMarkdown(val){
    HGMarkdownConverter = new showdown.Converter(); // we decided to initialize every time because otherwise we have to wait and check if showdown has been loaded already and this doesnt cost much
    return HGMarkdownConverter.makeHtml(val);
}

function HGAsciiMathToTexHelperA(match, p1, p2, p3, offset, string){
    p2 = AMTparseAMtoTeX(p2) // convert to latex
    p2 = p2.replace(/&lt/g,"<"); // fix html-encoded < and >
    p2 = p2.replace(/&gt/g,">");
    return ["&#92;[", p2, "&#92;]"].join(''); // escaped characters because conversion from markdown ruins this otherwise
}

function HGAsciiMathToTexHelperB(match, p1, p2, p3, offset, string){
    p2 = AMTparseAMtoTeX(p2) // convert to latex
    p2 = p2.replace(/&lt/g,"<"); // fix html-encoded < and >
    p2 = p2.replace(/&gt/g,">");
    return ["&#92;(", p2, "&#92;)"].join(''); // escaped characters because conversion from markdown ruins this otherwise
}

function HGAsciiMathToTex(val){
    val = val.replace(/(\$\$)([^\$]*)(\$\$)/g, HGAsciiMathToTexHelperA);
    val = val.replace(/(\$)([^\$]*)(\$)/g, HGAsciiMathToTexHelperB);
    return val;
}

function HGDAndAMToHTMLCodeFixer(val){
    fixed = document.createElement("HGFixerTemp");
    fixed.innerHTML = val;
    var a = 0;
    while (a < fixed.childNodes.length){
        var elm = fixed.childNodes[a];
        if(((typeof elm.tagName) != 'undefined') && (elm.tagName == "CODE" || elm.tagName == "PRE")){
            elm.innerHTML = elm.innerHTML.replace(/&amp;lt;/g,"<");
            elm.innerHTML = elm.innerHTML.replace(/&amp;gt;/g,">");
        }
    a = a + 1;
    }
    return fixed.innerHTML;
}

function HGDAndAMToHTML(val){
    val = HGCompEnc(val); // to prevent insertion of html tags, against XSS attacks
    val = HGAsciiMathToTex(val);
    val = val.replace(/\\\\/g,"&#92;"); // replaces backslashes, 4 backslashes in regex needed which double-escape themselves to one backslash
    val = val.replace(/_/g,'HALLGRIMUNDERSCOREPLACEHOLDER');
    val = HGConvertMarkdown(val);
    val = val.replace(/HALLGRIMUNDERSCOREPLACEHOLDER/g,'_');
    val = HGDAndAMToHTMLCodeFixer(val);
    return val;
}"""

SKULPT_PY = """

function HGSkulptBuiltInRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}


async function HGRunPython(code, outputID, errorElement) { 
   if(errorElement != undefined){
     errorElement.innerHTML = ""; // clear error message
   }
   var output = document.getElementById(outputID);
   output.innerHTML = ""; 
   Sk.pre = "output";
   var outf = new Function("text","var output = document.getElementById('" + outputID + "');output.innerHTML = output.innerHTML + HGCompEnc(text) + 'HGLINEBREAK';") // outputID has to be inserted here manually, because Skulpt wants to call this function with just the output text and I want to avoid global variables; Line breaks have to be changed like this because on each print an empty line is printed also, but I want to retain the ability to print empty lines so I can't just remove all double-breaks
   Sk.configure({output:outf, read:HGSkulptBuiltInRead}); 
   var myPromise = Sk.misceval.asyncToPromise(function() {
       Sk.importMainWithBody("<stdin>", false, code, true);
   });
   var endPromise = myPromise.then(function(mod) {
       output.innerHTML = output.innerHTML.replace(/HGLINEBREAK\\nHGLINEBREAK/g,"<br>")// things went well on execution, fix line breaks
   },
       function(err) {
       if(errorElement != undefined){
         errorElement.textContent = err.toString(); // output error message from Skulpt
       }
   });
   return endPromise;
} 
"""

CODE_EDITOR = """ 
function HGEditor(partId, language){
    outer = HGElement(partId); // we make a container for the editor as a handle
    outer.innerHTML = "<div id=" + partId + "InnerEditor></div>";
    var editor = ace.edit(partId + "InnerEditor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/" + language);
    editor.setOptions({minLines: 10, maxLines: 10000}); // maxLines have to be set, else always size of about one line
    editor.setFontSize(16);
    outer.editor = editor;
    return outer;
}
"""

UTILITY = """
function HGElement(inp){
    return document.getElementById(inp);
}

function HGToB64(inp) {
 return btoa(unescape(encodeURIComponent(inp)));
}

function HGFromB64(inp) {
 return decodeURIComponent(escape(atob(inp)));
}

function HGRand(){
  HGMetaData["RandomSeed"] = (((2 ** 31) - 1) & (Math.imul(13466917, HGMetaData["RandomSeed"]))); // 32-bit linear congruence generator, do not use for any cryptographic purposes
  return HGMetaData["RandomSeed"];
}

function HGSRand(seed){
  HGMetaData["RandomSeed"] = seed;
}
"""


IO_MANAGEMENT = """
function HGInput(inputID){
  return document.querySelectorAll("[HGInput = " + inputID + "]")[0];
}

function HGOutput(outputID){
  return document.querySelectorAll("[HGOutput = " + outputID + "]")[0];
}

HGOutputSeparator = "\\nHallgrim-Antwortenseparator\\n";

function HGSaveInputs(){
  var aggregate = "";
  var first = true;
  var inputs = document.querySelectorAll("[HGInput]")
  for (var InpNum = 0; InpNum < inputs.length; InpNum++){
    var ID = inputs[InpNum].getAttribute("HGInput");
    if(!first){aggregate += HGOutputSeparator;}
    first = false;
    aggregate += ID + "\\n" + inputs[InpNum].HGGetter();
  }
  HGOutput("raw").HGSetter(aggregate)
}

function HGLoadInputs(){
  var aggregate = HGOutput("raw").HGGetter();
  var split = aggregate.split(HGOutputSeparator)
  for (var contentNum = 0; contentNum < split.length; contentNum++){
    var content = split[contentNum];
    content = content.split("\\n");
    var ID = content.splice(0, 1)[0];
    content = content.join("");
    document.querySelectorAll("[HGInput = " + ID + "]")[0].HGSetter(content);
  }
}

function HGSaveMeta(){
  var aggregate = "";
  var first = true;
  var data = Object.getOwnPropertyNames(HGMetaData);
  for (var IDNum = 0; IDNum < data.length; IDNum++){
    var ID = data[IDNum]
    if(!first){aggregate += HGOutputSeparator;}
    first = false;
    aggregate += ID + "\\n" + HGMetaData[ID];
    console.log("META:"+ID+" to "+aggregate);
  }
  HGOutput("meta").HGSetter(aggregate)
}

function HGLoadMeta(){
  var aggregate = HGOutput("meta").HGGetter();
  var split = aggregate.split(HGOutputSeparator)
  for (var contentNum = 0; contentNum < split.length; contentNum++){
    var content = split[contentNum];
    content = content.split("\\n");
    var ID = content.splice(0, 1)[0];
    content = content.join("");
    HGMetaData[ID] = content;
  }
}

function HGSaveAll(){
  HGSaveInputs();
  HGSaveMeta();
}

function HGLoadAll(){
  HGLoadInputs();
  HGLoadMeta();
}

async function HGAutoSave(period){
  while(true){
    await (new Promise(resolve => setTimeout(resolve, period)));
    HGSaveAll();
  }
}

function HGFinish(){
  HGSaveAll();
  HGEvaluator();
}

async function HGTimeEnder(){
  HGFinish();
  await (new Promise(resolve => setTimeout(resolve, 200))); // else value sometimes not saved
  il.TestPlayerQuestionEditControl.saveOnTimeReached();
}

function HGTimeEndReplacer(){
  if(typeof setWorkingTime != 'undefined'){
    setWorkingTimeRenewer = new Function(setWorkingTime.toSource().replace(/il.TestPlayerQuestionEditControl.saveOnTimeReached\(\)/g,"HGTimeEnder()") + "return setWorkingTime;")
    setWorkingTime = setWorkingTimeRenewer();
  }
}

async function HGSaveAndClick(toclick){
  HGFinish();
  toclick.click();
}

function HGNavButtonReplacer(){
  if(document.getElementsByClassName("ilTstNavElem btn btn-default btn-primary")[0]){
    realEnd = document.getElementsByClassName("ilTstNavElem btn btn-default btn-primary")[0];
    realEnd.style.display="none";
    fakeEnd = document.createElement("NewEndButton");
    fakeEnd.innerHTML='<button  type="button" onclick="HGSaveAndClick(realEnd);"  class="ilTstNavElem btn btn-default btn-primary">&nbsp;Test beenden&nbsp;</button>';
    realEnd.parentNode.appendChild(fakeEnd);
  }
}

function HGEvaluate(){
  return HGEvaluator();
}

function HGRegisterEvaluator(evaluator){
  HGEvaluator = evaluator;
}
"""

# for preparing task (mostly putting answers back in the right place and reloading or setting the random seed), especially when continuing or correcting

PREPPER = """ function HGPrep(){
    HGInputs = []
    HGMetaData = {}
    HGEvaluator = new Function("HGOutput('answer').HGSetter(HGOutput('raw').HGGetter());")
    if(HGMode == "ANSWERING"){
      HGSRand((new Date).getTime())
      HGAutoSave({STANDARDTIME});
      HGTimeEndReplacer();
      HGNavButtonReplacer();
    }
    else if(HGMode == "CONTINUING"){
      HGLoadAll();
      HGAutoSave({STANDARDTIME});
      HGTimeEndReplacer();
      HGNavButtonReplacer();
    }
    else if(HGMode == "CORRECTING"){
      HGLoadAll();
    }
}
"""

PREPPER = PREPPER.replace("{STANDARDTIME}", "10000") # using 'format' bad idea due to curly braces


def import_string(source):
    return """<script src = {Fsource}></script>""".format(Fsource = source);

def InterleaveWithTags(text, tagIDs, placeholder):
    taskParts = text.split(placeholder)
    pos = 0
    text = ""
    while(pos < len(tagIDs)):
        text += taskParts[pos]
        text += "<div id=\"" + str(tagIDs[pos]) + "\"></div>"
        pos = pos + 1
    text += taskParts[-1]
    return text

def hg_js_tag_processor(task):
    """Replaces tags for different inputs with replacable HTML-Elements and creates code for conversion."""
    #source-code-editors
    converters = "";
    reg = re.compile('\[editor(\([^)]*\))??\]([\w\W]+?)(\[\/editor\])', re.MULTILINE)
    IDs = [];
    for point in re.finditer(reg, task):
        counter = 0
        ID = point.groups()[0][1:-1]
        lang = point.groups()[1]
        IDs.append(ID);
        converters += """
        HGTempEditor = HGEditor({DOMID}, {EditorLang});
        HGTempEditor.setAttribute("HGInput", {DOMID});
        HGTempEditor.HGGetter = (function(useEditor){ var editorCopy=useEditor; var func = function(){return editorCopy.getValue()}; return func;})(HGTempEditor.editor);
        HGTempEditor.HGSetter = (function(useEditor){ var editorCopy=useEditor; var func = function(content){editorCopy.setValue(content)}; return func;})(HGTempEditor.editor);
        """.replace("{DOMID}", "\"" + ID + "\"").replace("{EditorLang}", "\"" + lang + "\"") # using 'format' bad idea due to curly braces
    task = re.sub(reg, "HGEDITORINPUTPLACE", task)
    task = InterleaveWithTags(task, IDs, "HGEDITORINPUTPLACE")    
    
    #gaps

    #text-fields

    #text-areas

    #checkboxes

    #radio buttons

    #drawing surfaces (canvas with mouse-drawing)

    #buttons

    #text-display (wrapping for p-tag)
    return (task, converters)

def pre_process_js(code, task):
    """Adds functions and function calls for automatic processing of inputs and outputs, management of submissions and abstraction for additional provided functionality and DOM-JS-Interaction. Also adds the needed imports."""
    imp = ""; # imports
    (task , converters) = hg_js_tag_processor(task)
    code = ENCODE_COMPARATORS + CLEAN_HTML + IO_MANAGEMENT + UTILITY + converters + PREPPER + "HGPrep()" + code
    task = "<h1 id = 'NOJAVASCRIPTERROR'>FALLS DIESER TEXT NICHT VERSCHWINDET GIBT ES EIN PROBLEM MIT DER AUSFÜHRUNG VON JAVASCRIPT. STELLEN SIE SICHER, DASS IHR BROWSER NICHT VERALTET IST UND SIE PLUGINS DEAKTIVIEREN, WELCHE JAVASCRIPT AUF ILIAS BLOCKIEREN! KONTAKTIEREN SIE ANDERNFALLS EINEN TUTOR!</h1>" + task
    code = code + "HGElement('NOJAVASCRIPTERROR').style.display = 'none';" # remove warning after all other code has run
    #following parts add imports if relevant function calls are detected
    if("HGDAndAMToHTML(" in code):
        imp = import_string(MARKDOWN_CONVERTER_SOURCE) + imp
        with open("ASCIIMathTeXImg.js","r") as conv_file:
            code = conv_file.read() + code
        code = MD_AND_AM_TO_HTML + code 
    reg = re.compile('HGProcessLatex\(', re.MULTILINE)
    code = re.sub(reg, "MathJax.Hub.Typeset(", code)
    if("HGRunPython(" in code):
        code = SKULPT_PY + code
        with open("skulpt-stdlib.js","r") as conv_file:
            code = conv_file.read() + code
        with open("skulpt.min.js","r") as conv_file:
            code = conv_file.read() + code
    if("HGEditor(" in code):
        imp = import_string(CODE_EDITOR_SOURCE) + imp;
        code = CODE_EDITOR + code;
    return (code, imp, task)

