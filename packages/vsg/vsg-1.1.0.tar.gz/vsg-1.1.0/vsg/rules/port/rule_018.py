
from vsg import rule
from vsg import check
from vsg import fix
from vsg import utils


class rule_018(rule.rule):
    '''
    Port rule 018 checks the port type is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '018')
        self.solution = 'Change port type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if self._is_vsg_off(oLine):
                continue
            if oLine.isPortDeclaration:
                sLine = oLine.line.split(':')[1]
                if '(' in sLine:
                    sLine = sLine.split('(')[0]
                if not utils.is_port_mode(sLine.split()[0]):
                    continue
                if utils.is_vhdl_keyword(sLine.split()[1]):
                    check.is_lowercase(self, sLine.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1]
            if '(' in sLine:
                sLine = sLine.split('(')[0]
            sWord = sLine.split()[1]
            fix.lower_case(oLine, sWord)
