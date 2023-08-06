# This script contains a function to create an Information Manager note.
# To use it:
#
# from InformationManager import *
# AddEBNote("CUSTOMER", "1200", "Plain text note.\nAnother line.")

from accpac import *

def AddEBNote(sNoteType, sKey, sNoteText, sNoteRtf=""):
    vEBNOTE = openView("EB0033", 1000)
    vEBDOC = openView("EB0035", 1000)
    vEBNOTE.recordGenerate()
    vEBNOTE.put("NOTETYPE", sNoteType)
    vEBNOTE.put("KEY", sKey)
    x = 250
    if x > len(sNoteText):
        x = len(sNoteText)
    s = sNoteText[0:x]
    vEBNOTE.put("NOTETEXT", sNoteText)
    vEBNOTE.insert()

    segment = 1
    while sNoteText != "":
        vEBDOC.recordGenerate()
        vEBDOC.put("TEXTID", vEBNOTE.get("TEXTID"))
        vEBDOC.put("SEGMENT", segment)
        for i in range(1, 15):
            x = 250
            if x > len(sNoteText):
                x = len(sNoteText)
            s = sNoteText[0:x]
            sNoteText = sNoteText[x:]
            vEBDOC.put("TEXT" + str(i), s)
        vEBDOC.insert()
        segment = segment + 1

    segment = 1
    while sNoteRtf != "":
        vEBDOC.recordGenerate()
        vEBDOC.put("TEXTID", vEBNOTE.get("RTFID"))
        vEBDOC.put("SEGMENT", segment)
        for i in range(1, 15):
            x = 250
            if x > len(sNoteRtf):
                x = len(sNoteRtf)
            s = sNoteRtf[0:x]
            sNoteRtf = sNoteRtf[x:]
            vEBDOC.put("TEXT" + str(i), s)
        vEBDOC.insert()
        segment = segment + 1
