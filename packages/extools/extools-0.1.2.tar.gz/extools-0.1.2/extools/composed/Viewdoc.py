# generate include c/vb all/single
# prompt where to save
from accpac import *
import sys
import os
import time

def openFile(name):
    try:
        f = open(name) #, encoding="utf8")
    except:
        return None
    return f

def writeFile(name, content):
    f = open(name, "w")
    f.write(content)
    f.close()

class PP:
    def __init__(self):
        self.lines = None
        self.output = []

    def process(self, t):
        self.lines = t.split("\n")
        self.processFile(self.output, self.lines, 0, 0)
        s = ""
        for x in self.output:
            s = s + x + "\n"
        return s

    def processFile(self, output, lines, curLine, nOutput):
        if nOutput == 1:
            haveOutput = False
        else:
            haveOutput = True
        while curLine < len(lines):
            line = lines[curLine]
            line = line.replace("\n", "").replace("\r", "")
            curLine = curLine + 1
            oline = line

            if line.startswith("$if "):
                if nOutput > 0:
                    curLine = self.processFile(output, lines, curLine, nOutput+1)
                elif not eval(line[4:]):
                    curLine = self.processFile(output, lines, curLine, 1)
                else:
                    curLine = self.processFile(output, lines, curLine, 0)
                line = None
            elif line.startswith("$else"):
                if haveOutput == False:
                    nOutput = 0
                    haveOutput = True
                else:
                    nOutput = 1
                line = None
            elif line.startswith("$elif"):
                if haveOutput == False:
                    if eval(line[6:]):
                        nOutput = 0
                        haveOutput = True
                else:
                    nOutput = 1
                line = None
            elif line.startswith("$endif"):
                return curLine

            if nOutput == 0 and line != None:
                output.append(line)
        return output

class TemplateGetValueArgs():
    def __init__(self):
        self.template = None
        self.object = None
        self.value = None

class TemplateValue():
    def __init__(self):
        self.name = None
        self.value = None
        self.getValue = None
        self.data = None

class TemplateFragment():
    def __init__(self):
        self.name = None
        self.body = None

class Template():
    def __init__(self):
        self.values = [] # TemplateValue[]
        self.fragments = [] # TemplateFragment[]
        self.parent = None # Template
        self.output = None

    def findField(self, field, checkParent=True):
        for v in self.values:
            if v.name == field:
                return v
        if (self.parent != None) and (checkParent == True):
            return self.parent.findField(field)
        return None

    def getField(self, field, checkParent=True):
        v = self.findField(field, checkParent)
        if v != None:
            return v
        v = TemplateValue()
        v.name = field
        self.values.append(v)
        return v

    def set(self, field, value):
        v = self.getField(field, False)
        if type(value) is str:
            v.value = value
        else:
            v.getValue = value
        return v

    def findFragment(self, name):
        for f in self.fragments:
            if f.name == name:
                return f
        if self.parent != None:
            return self.parent.findFragment(name)
        return None

    def load(self, template):
        lines = template.split("\n")
        f = None
        for line in lines:
            if line == "--": # end of fragment
                f = None
            elif line.startswith("--"): # start of named fragment
                f = TemplateFragment()
                f.name = line[2:-2]
                f.body = ""
                self.fragments.append(f)
            else:
                # fragment body
                if f == None:
                    f = TemplateFragment()
                    f.body = ""
                    self.fragments.append(f)
                if len(f.body) > 0:
                    f.body = f.body + "\n"
                f.body = f.body + line.replace("\\n", "\n").replace("\\--", "--")

    def render(self, fragmentName=None):
        self.output = ""
        self.renderFragmentName(fragmentName)
        return self.output

    def renderTemplateFragment(self, f, op):
        if op == "each":
            v = self.findField("object")
            if v == None:
                # TODO - perhaps output error?
                return

            v = self.findField(v.value)
            if v == None:
                return

            e = TemplateGetValueArgs()
            e.template = self
            while True:
                v.getValue(e)
                if e.object == None:
                    return
                self.renderTemplateFragment(f, "once")

        b = f.body
        i = 0
        while True:
            oi = i
            i = b.find("{", i)
            if i == -1:
                self.output = self.output + b[oi:len(b)]
                return
            ii = b.find("}", i)
            if ii == -1:
                self.output = self.output + b[oi:len(b)]
                return
            eol = b.find("\n", i)
            if (eol != -1) and (eol < ii):
                self.output = self.output + b[oi:eol+1]
                ii = eol
            else:
                self.output = self.output + b[oi:i]
                self.renderFragmentName(b[i+1:ii])
            i = ii+1

    def format(self, value, formatString):
        if formatString.startswith("%"):
            # %{padside}{padchar}{width}
            # eg:
            #   %L05 means pad with zeros on the left
            #   %R 5 means pad with spaces on the right
            padChar = formatString[2]
            padWidth = int(formatString[3:])
            if formatString[1] == 'L':
                return value.rjust(padWidth, padChar)
            elif formatString[1] == 'R':
                return value.ljust(padWidth, padChar)
        if formatString != "":
            return value + ":" + formatString
        return value

    def renderFragmentName(self, fragmentName):
        op = None
        name = None
        args = None

        if fragmentName != None:
            n = fragmentName
            iColon = n.find(":")
            iSpace = n.find(" ")
            if iSpace == -1:
                iSpace = len(n)-1
            if (iColon == -1) or (iColon > iSpace):
                n = "once:" + n
                iColon = 4
                iSpace += 5
            op = n[0:iColon]
            name = n[iColon+1:iSpace+1].strip()
            args = n[iSpace+1:]

        f = self.findFragment(name)
        if f == None:
            if fragmentName == None:
                return

            formatString = ""
            name = fragmentName
            iColon = name.find(":")
            if iColon != -1:
                formatString = name[iColon+1:]
                name = name[:iColon]

            v = self.findField(name)
            if v != None:
                if v.value != None:
                    self.output = self.output + self.format(v.value, formatString)
                elif v.getValue != None:
                    e = TemplateGetValueArgs()
                    e.template = self
                    v.getValue(e)
                    self.output = self.output + self.format(e.value, formatString)
            else:
                self.output = self.output + "{" + fragmentName + "}"
            return

        if (args != None) and (len(args) > 0):
            t = Template()
            t.parent = self
            t.parseArgs(args)
            t.output = ""
            t.renderTemplateFragment(f, op)
            self.output = self.output + t.output
            return

        self.renderTemplateFragment(f, op)

    def parseArgs(self, args):
        i = 0
        while True:
            start = i
            i = args.find("=", start)
            if i == -1:
                return
            k = args[start:i].strip()

            start = args.find("'", i)
            i = args.find("'", start+1)
            v = args[start+1:i]
            self.set(k, v)
            i = i + 1

class ViewProcessor():
    def __init__(self):
        self.rotoID = None
        self.view = None
        self.output = ""

    def onGetObjKey(self, a):
        if a.object == None:
            # first run
            a.object = 0
        if a.object >= self.view.keyCount():
            a.object = None
            return

        k = self.view.key(a.object)
        a.template.set("NUM0", str(a.object))
        a.template.set("NUM1", str(a.object + 1))
        a.template.set("NAME", k.name)
        s = ""
        for idx in k.fields:
            vf = self.view.fieldByIndex(idx)
            if len(s) > 1:
                s = s + ", "
            s = s + vf.name
        a.template.set("FIELDS", s)
        a.object = a.object + 1

    def onGetObjField(self, a):
        if a.object == None:
            # first run
            a.object = 0
        if a.object >= self.view.fields():
            a.object = None
            return

        f = self.view.fieldByPosition(a.object)
        a.template.set("NAME", f.name)
        a.template.set("SIZE", str(f.size))
        a.template.set("PREC", "-1")
        a.template.set("DESC", str(f.desc))
        a.template.set("INDEX", str(f.index))
        if f.type == FT_CHAR:
            a.template.set("TYPE", "String")
        elif f.type == FT_BYTE:
            a.template.set("TYPE", "Binary")
        elif f.type == FT_DATE:
            a.template.set("TYPE", "Date")
        elif f.type == FT_TIME:
            a.template.set("TYPE", "Time")
        elif f.type == FT_REAL:
            a.template.set("TYPE", "Real")
        elif f.type == FT_BCD:
            a.template.set("TYPE", "BCD")
            a.template.set("PREC", str(f.precision))
        elif f.type == FT_INT:
            a.template.set("TYPE", "Integer")
        elif f.type == FT_LONG:
            a.template.set("TYPE", "Long")
        elif f.type == FT_BOOL:
            a.template.set("TYPE", "Boolean")

        attr = self.view.attribs(f.index)

        a.template.set("VALUE", "")
        if attr & 0x002: # isEnabled
            if f.type == FT_BCD:
                a.template.set("VALUE", self.view.replaceFields("{" + f.name + ":D" + str(f.precision) + "}"))
            else:
                a.template.set("VALUE", str(self.view.get(f.name)))

        s = ""
        if attr & 0x080: # isRequired
            s = s + "R"
        if attr & 0x008: # isKey
            s = s + "K"
        if attr & 0x004: # isEditable
            s = s + "E"
        if attr & 0x002: # isEnabled
            s = s + "A"
        #if attr & 0x001: # isChanged
        #    s = s + ""
        if attr & 0x010: # isCalculate
            s = s + "C"
        if attr & 0x020: # typeChanges
            s = s + "T"
        if attr & 0x040: # presentationChanges
            s = s + "P"
        if attr & 0x100: # editableChanges
            s = s + "X"
        a.template.set("ATTRIB", s)

        a.template.set("HASMASK", "0")
        a.template.set("MASK", "")
        a.template.set("HASLIST", "0")
        a.template.set("NLIST", "")
        if attr & 0x002:
            p = self.view.getPresents(f.index)
            if p != None:
                if p.mask != None:
                    a.template.set("HASMASK", "1")
                    a.template.set("MASK", p.mask)
                else:
                    a.template.set("HASLIST", "1")
                    a.template.set("NLIST", str(len(p.values)))
                    a.template.getField("LIST", False).data = p.values

        a.object = a.object + 1

    def onGetObjList(self, a):
        values = a.template.getField("LIST").data
        if values == None:
            a.object = None
            return
        if a.object == None:
            # first run
            a.object = 0
        if a.object >= len(values):
            a.object = None
            return
        pi = values[a.object]
        a.template.set("VALUE", str(pi.value))
        a.template.set("DESC", pi.desc)
        a.object = a.object + 1

    def onGetObjCompose(self, a):
        if a.object == None:
            # first run
            a.object = 0
        if a.object >= len(self.vci.views):
            a.object = None
            return
        vi = self.vci.views[a.object]
        vh = self.vh
        vh.recordClear()
        vh.put("VIEWID", vi)
        vh.read()
        a.template.set("NAME", vh.get("NAME"))
        a.template.set("DESC", vh.get("DESC"))
        a.template.set("ROTOID", vi)
        a.object = a.object + 1

    def generate(self, template):
        self.output = ""
        if self.rotoID != None:
            if len(self.rotoID) != 6:
                return

            v = openView(self.rotoID)
            if v == None:
                log("Cannot open view " + self.rotoID)
                return output
            self.view = v
        else:
            v = self.view
            self.rotoID = v.rotoID

        vh = View("VI0005") # VIVIEWS
        self.vh = vh
        vh.recordClear()
        vh.put("VIEWID", self.rotoID)
        vh.read()

        self.vci = v.composeInfo()

        content = Template()
        content.load(template)
        self.viewname = vh.get("NAME")
        content.set("VIEWNAME", vh.get("NAME"))
        content.set("VIEWDESC", v.fieldByPosition(-1).desc)
        content.set("ROTOID", self.rotoID)
        content.set("objCompose", self.onGetObjCompose)
        content.set("objKey", self.onGetObjKey)
        content.set("objField", self.onGetObjField)
        content.set("objList", self.onGetObjList)
        content.set("NCOMPOSE", str(len(self.vci.views)))
        content.set("NKEYS", str(v.keyCount()))
        content.set("NFIELDS", str(v.fields()))

        recordSize = 0
        for i in range(0, v.fields()):
            f = v.fieldByPosition(i)
            s = padRight(f.name, 12)
            recordSize = recordSize + f.size
        content.set("RECORDSIZE", str(recordSize))

        r = content.render()
        pp = PP()
        r = pp.process(r)
        return r

def viewIncludeC(rotoID):
    s = ""
    s = s + "--Keys--\n"
    s = s + "{each:Key object='objKey'}\n"
    s = s + "--Key--\n"
    s = s + "#define {VIEWNAME}_KEY{NUM1} {NUM0}\\n\n"

    s = s + "--FieldIndexes--\n"
    s = s + "{each:FieldIndex object='objField'}\n"
    s = s + "--FieldIndex--\n"
    s = s + "#define IDX_{VIEWNAME}_{NAME:%R 12}{INDEX}l\\n\n"

    s = s + "--FieldLengths--\n"
    s = s + "{each:FieldLength object='objField'}\n"
    s = s + "--FieldLength--\n"
    s = s + "#define SIZEOF_{VIEWNAME}_{NAME:%R 12}{SIZE}\\n\n"

    s = s + "--FieldPrecs--\n"
    s = s + "{each:FieldPrec object='objField'}\n"
    s = s + "--FieldPrec--\n"
    s = s + "$if {PREC}!=-1\n"
    s = s + "#define PREC_{VIEWNAME}_{NAME:%R 14}{PREC}\n"
    s = s + "$endif\\n\n"

    s = s + "--\n"
    s = s + "#ifdef __cplusplus\n"
    s = s + "extern \"C\" {\n"
    s = s + "#endif\n"
    s = s + "\n"
    s = s + "#ifndef INC__{VIEWNAME}_H\n"
    s = s + "#define INC__{VIEWNAME}_H\n"
    s = s + "\n"
    s = s + "//View Roto ID\n"
    s = s + "#define {VIEWNAME}_VIEW \"{ROTOID}\"\n"
    s = s + "\n"

    s = s + "//View Keys\n"
    s = s + "{Keys}"
    s = s + "\n"

    s = s + "//View Field Indices\n"
    s = s + "{FieldIndexes}"
    s = s + "\n"

    s = s + "//View Field Lengths\n"
    s = s + "{FieldLengths}"
    s = s + "\n"

    s = s + "//View Field Precisions\n"
    s = s + "{FieldPrecs}"
    s = s + "\n"

    s = s + "//Macros which commonize referencing fields in the manner GENTABLE does\n"
    s = s + "#ifndef {VIEWNAME}_IDX\n"
    s = s + "#define {VIEWNAME}_IDX(__f__)   (IDX_{VIEWNAME}_##__f__)\n"
    s = s + "#endif\n"
    s = s + "#ifndef {VIEWNAME}_SIZ\n"
    s = s + "#define {VIEWNAME}_SIZ(__f__)   (SIZEOF_{VIEWNAME}_##__f__)\n"
    s = s + "#endif\n"
    s = s + "#define {VIEWNAME}_PREC(__f__)   (PREC_{VIEWNAME}_##__f__)\n"
    s = s + "\n"
    s = s + "#endif\n"
    s = s + "\n"
    s = s + "#ifdef __cplusplus\n"
    s = s + "}\n"
    s = s + "#endif\n"
    gen = ViewProcessor()
    gen.rotoID = rotoID
    s = gen.generate(s)
    #writeFile("c:\\shared\\" + getModuleVersion("VI")[0:2] + "\\include\\" + gen.viewname + ".h", s)
    log(s)

def viewIncludeVB(rotoID):
    s = ""
    s = s + "--Keys--\n"
    s = s + "{each:Key object='objKey'}\n"
    s = s + "--Key--\n"
    s = s + "Public Const KEY{NUM1} as Long = {NUM0}\\n\n"

    s = s + "--FieldIndexes--\n"
    s = s + "{each:FieldIndex object='objField'}\n"
    s = s + "--FieldIndex--\n"
    s = s + "Public Const IDX_{NAME:%R 12} as Long = {INDEX}\\n\n"

    s = s + "--FieldLengths--\n"
    s = s + "{each:FieldLength object='objField'}\n"
    s = s + "--FieldLength--\n"
    s = s + "Public Const LEN_{NAME:%R 12} as Integer = {SIZE}\\n\n"

    s = s + "--FieldPrecs--\n"
    s = s + "{each:FieldPrec object='objField'}\n"
    s = s + "--FieldPrec--\n"
    s = s + "$if {PREC}!=-1\n"
    s = s + "#define PREC_{VIEWNAME}_{NAME:%R 14}{PREC}\n"
    s = s + "$endif\\n\n"

    s = s + "--\n"
    s = s + "Attribute VB_Name = \"{VIEWNAME}\"\n"
    s = s + "\n"
    s = s + "'DO NOT CHANGE THIS FILE SINCE IT MAY BE REGENERATED\n"
    s = s + "\n"
    s = s + "'View Roto ID\n"
    s = s + "Public Const ROTOID     as String = \"{ROTOID}\"\n"
    s = s + "Public Const OBJECTNAME as String = \"{VIEWNAME}\"\n"
    s = s + "\n"

    s = s + "'View Keys\n"
    s = s + "{Keys}"
    s = s + "\n"

    s = s + "'View Field Indices\n"
    s = s + "{FieldIndexes}"
    s = s + "\n"

    s = s + "'View Field Lengths\n"
    s = s + "{FieldLengths}"
    s = s + "\n"

    gen = ViewProcessor()
    gen.rotoID = rotoID
    s = gen.generate(s)

    #writeFile("c:\\shared\\" + getModuleVersion("VI")[0:2] + "\\include\\" + gen.viewname + ".bas", s)
    log(s)

def viewMissingStrings(rotoID):
    s = ""
    s = s + "--Keys--\n"
    s = s + "{each:Key object='objKey'}\n"
    s = s + "--Key--\n"
    s = s + "$if \"{NAME}\"==\"\"\n"
    s = s + "\tIDS_{VIEWNAME}_KEY{NUM1}_NAME  , \"\"\n"
    s = s + "$endif\\n\n"

    s = s + "--Fields--\n"
    s = s + "{each:Field object='objField'}\n"
    s = s + "--Field--\n"
    s = s + "$if \"{DESC}\"==\"\"\n"
    s = s + "\tIDS_{VIEWNAME}_{NAME}_FLD  , \"\"\n"
    s = s + "$endif\\n\n"

    s = s + "--\n"
    s = s + "$if \"{VIEWDESC}\"==\"\"\n"
    s = s + "\t{VIEWNAME}_NAME , \"\"\n"
    s = s + "$endif\n"
    s = s + "{Fields}"
    s = s + "{Keys}"

    gen = ViewProcessor()
    gen.rotoID = rotoID
    s = gen.generate(s)

    log(s)

def viewdoc(rotoID, args):
    if len(rotoID) != 6:
        return

    v = openView(rotoID)
    if v == None:
        log("Cannot open view " + rotoID)
        return

    if args != None:
        n = 1
        while "F" + str(n) in args:
            v.put(v.fieldByPosition(n-1).name, args["F" + str(n)], False)
            n = n + 1
        v.read()
    else:
        v.recordGenerate()

    s = ""
    s = s + "--Composes--\n"
    s = s + "{each:Compose object='objCompose'}\n"
    s = s + "--Compose--\n"
    s = s + "^^VIEWDOC.PY^{ROTOID}^^            {ROTOID} {NAME} {DESC}\\n\n"

    s = s + "--Keys--\n"
    s = s + "{each:Key object='objKey'}\n"
    s = s + "--Key--\n"
    s = s + "{NUM0:%L 2} - {NAME}\n"
    s = s + "     {FIELDS}\\n\n"

    s = s + "--Fields--\n"
    s = s + "{each:Field object='objField'}\n"
    s = s + "--Field--\n"
    s = s + "$if {PREC}!=-1\n"
    s = s + "{NAME:%R 12}{TYPE:%R 10}{SIZE:%L 3}       {PREC}   {DESC:%R 32}{INDEX:%L 6}  {ATTRIB:%R 10}{VALUE}\n"
    s = s + "$else\n"
    s = s + "{NAME:%R 12}{TYPE:%R 10}{SIZE:%L 3}           {DESC:%R 32}{INDEX:%L 6}  {ATTRIB:%R 10}{VALUE}\n"
    s = s + "$endif\n"
    s = s + "$if {HASMASK}==1\n"
    s = s + "            Mask - {MASK}\n"
    s = s + "$endif\n"
    s = s + "$if {HASLIST}==1\n"
    s = s + "            List with {NLIST} items in the list:\n"
    s = s + "{each:ListItem object='objList'}"
    s = s + "$endif\\n\n"
    s = s + "--ListItem--\n"
    s = s + "            {VALUE} - {DESC}\\n\n"

    s = s + "--\n"
    s = s + "Roto ID - {ROTOID}  DLL Name - {VIEWNAME} {VIEWDESC}\n" # padRight(vh.get("NAME"), 12)

    s = s + ""
    s = s + "{Composes}"
    s = s + "$if {NCOMPOSE}==1\n"
    s = s + "            View Composition - 1 view\n"
    s = s + "$else\n"
    s = s + "            View Composition - {NCOMPOSE} views\n"
    s = s + "$endif\n"

    s = s + "\n"
    s = s + "\n"
    s = s + "$if {NKEYS}==1\n"
    s = s + "Index List - 1 Index\n"
    s = s + "$else\n"
    s = s + "Index List - {NKEYS} Indexes\n"
    s = s + "$endif\n"
    s = s + "\n"
    s = s + "{Keys}"

    s = s + "\n"
    s = s + "Field List - {NFIELDS} fields\n"
    s = s + "\n"
    s = s + "\\-- Name --   Type     Size    Prec  --------- Description ---------  Index  Attrib    Initial Value\n"
    s = s + "\n"
    s = s + "{Fields}\n"
    s = s + "Record size = {RECORDSIZE}\n"

    gen = ViewProcessor()
    gen.view = v
    s = gen.generate(s)
    log(s)

    #viewIncludeC(rotoID)
    #viewIncludeVB(rotoID)
    #viewMissingStrings(rotoID)

def padLeft(s, len):
    return s.rjust(len, " ")

def padRight(s, len):
    return s.ljust(len, " ")

def main(args):
    rotoID = args
    e = None
    if len(rotoID) > 6:
        e = parseArgs(rotoID[7:])
        rotoID = rotoID[0:6]
    viewdoc(rotoID, e)
