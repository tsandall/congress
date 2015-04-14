# $ANTLR 3.5 /Users/thinrichs/Code/congress/congress/datalog/Congress.g 2015-04-14 16:46:46

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__52=52
T__53=53
T__54=54
AND=4
ATOM=5
BYTESTRPREFIX=6
BYTES_CHAR_DQ=7
BYTES_CHAR_SQ=8
BYTES_ESC=9
BYTES_TESC=10
COLONMINUS=11
COLUMN_NAME=12
COLUMN_NUMBER=13
COMMA=14
COMMENT=15
DIGIT=16
EQUAL=17
EXPONENT=18
FLOAT=19
FLOAT_EXP=20
FLOAT_NO_EXP=21
FLOAT_OBJ=22
FRAC_PART=23
HEX_DIGIT=24
ID=25
INT=26
INTEGER_OBJ=27
INT_PART=28
LBRACKET=29
LITERAL=30
LPAREN=31
MODAL=32
NAMED_PARAM=33
NEGATION=34
NOT=35
PROG=36
RBRACKET=37
RPAREN=38
RULE=39
SIGN=40
SLBYTESTRING=41
SLSTRING=42
STRING=43
STRING_ESC=44
STRING_OBJ=45
STRPREFIX=46
STRUCTURED_NAME=47
SYMBOL_OBJ=48
THEORY=49
VARIABLE=50
WS=51


class CongressLexer(Lexer):

    grammarFileName = "/Users/thinrichs/Code/congress/congress/datalog/Congress.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(CongressLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )

        self.dfa23 = self.DFA23(
            self, 23,
            eot = self.DFA23_eot,
            eof = self.DFA23_eof,
            min = self.DFA23_min,
            max = self.DFA23_max,
            accept = self.DFA23_accept,
            special = self.DFA23_special,
            transition = self.DFA23_transition
            )

        self.dfa24 = self.DFA24(
            self, 24,
            eot = self.DFA24_eot,
            eof = self.DFA24_eof,
            min = self.DFA24_min,
            max = self.DFA24_max,
            accept = self.DFA24_accept,
            special = self.DFA24_special,
            transition = self.DFA24_transition
            )

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )






    # $ANTLR start "COLONMINUS"
    def mCOLONMINUS(self, ):
        try:
            _type = COLONMINUS
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:7:12: ( ':-' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:7:14: ':-'
            pass 
            self.match(":-")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLONMINUS"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:8:7: ( ',' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:8:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "LBRACKET"
    def mLBRACKET(self, ):
        try:
            _type = LBRACKET
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:9:10: ( '[' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:9:12: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LBRACKET"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:10:8: ( '(' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:10:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RBRACKET"
    def mRBRACKET(self, ):
        try:
            _type = RBRACKET
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:11:10: ( ']' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:11:12: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RBRACKET"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:12:8: ( ')' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:12:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "T__52"
    def mT__52(self, ):
        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:13:7: ( '.' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:13:9: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):
        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:14:7: ( ':' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:14:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):
        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:15:7: ( ';' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:15:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__54"



    # $ANTLR start "NEGATION"
    def mNEGATION(self, ):
        try:
            _type = NEGATION
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:89:5: ( 'not' | 'NOT' | '!' )
            alt1 = 3
            LA1 = self.input.LA(1)
            if LA1 == 110:
                alt1 = 1
            elif LA1 == 78:
                alt1 = 2
            elif LA1 == 33:
                alt1 = 3
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae


            if alt1 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:89:7: 'not'
                pass 
                self.match("not")



            elif alt1 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:90:7: 'NOT'
                pass 
                self.match("NOT")



            elif alt1 == 3:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:91:7: '!'
                pass 
                self.match(33)


            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEGATION"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):
        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:137:5: ( '=' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:137:8: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "SIGN"
    def mSIGN(self, ):
        try:
            _type = SIGN
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:141:5: ( '+' | '-' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SIGN"



    # $ANTLR start "INT"
    def mINT(self, ):
        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:148:5: ( '1' .. '9' ( '0' .. '9' )* | ( '0' )+ | '0' ( 'o' | 'O' ) ( '0' .. '7' )+ | '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ | '0' ( 'b' | 'B' ) ( '0' | '1' )+ )
            alt7 = 5
            LA7_0 = self.input.LA(1)

            if ((49 <= LA7_0 <= 57)) :
                alt7 = 1
            elif (LA7_0 == 48) :
                LA7 = self.input.LA(2)
                if LA7 == 79 or LA7 == 111:
                    alt7 = 3
                elif LA7 == 88 or LA7 == 120:
                    alt7 = 4
                elif LA7 == 66 or LA7 == 98:
                    alt7 = 5
                else:
                    alt7 = 2

            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae


            if alt7 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:148:7: '1' .. '9' ( '0' .. '9' )*
                pass 
                self.matchRange(49, 57)

                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:148:16: ( '0' .. '9' )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((48 <= LA2_0 <= 57)) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop2



            elif alt7 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:149:7: ( '0' )+
                pass 
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:149:7: ( '0' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 48) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:149:7: '0'
                        pass 
                        self.match(48)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



            elif alt7 == 3:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:150:7: '0' ( 'o' | 'O' ) ( '0' .. '7' )+
                pass 
                self.match(48)

                if self.input.LA(1) == 79 or self.input.LA(1) == 111:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:150:23: ( '0' .. '7' )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 55)) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 55):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1



            elif alt7 == 4:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:151:7: '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
                pass 
                self.match(48)

                if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:151:23: ( HEX_DIGIT )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 70) or (97 <= LA5_0 <= 102)) :
                        alt5 = 1


                    if alt5 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1



            elif alt7 == 5:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:152:7: '0' ( 'b' | 'B' ) ( '0' | '1' )+
                pass 
                self.match(48)

                if self.input.LA(1) == 66 or self.input.LA(1) == 98:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:152:23: ( '0' | '1' )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((48 <= LA6_0 <= 49)) :
                        alt6 = 1


                    if alt6 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 49):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:158:5: ( FLOAT_NO_EXP | FLOAT_EXP )
            alt8 = 2
            alt8 = self.dfa8.predict(self.input)
            if alt8 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:158:7: FLOAT_NO_EXP
                pass 
                self.mFLOAT_NO_EXP()



            elif alt8 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:159:7: FLOAT_EXP
                pass 
                self.mFLOAT_EXP()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:182:5: ( ( STRPREFIX )? ( SLSTRING )+ | ( BYTESTRPREFIX ) ( SLBYTESTRING )+ )
            alt12 = 2
            LA12 = self.input.LA(1)
            if LA12 == 114:
                LA12_1 = self.input.LA(2)

                if (LA12_1 == 66 or LA12_1 == 98) :
                    alt12 = 2
                elif (LA12_1 == 34 or LA12_1 == 39) :
                    alt12 = 1
                else:
                    nvae = NoViableAltException("", 12, 1, self.input)

                    raise nvae


            elif LA12 == 34 or LA12 == 39 or LA12 == 85 or LA12 == 117:
                alt12 = 1
            elif LA12 == 66 or LA12 == 98:
                alt12 = 2
            elif LA12 == 82:
                LA12_4 = self.input.LA(2)

                if (LA12_4 == 66 or LA12_4 == 98) :
                    alt12 = 2
                elif (LA12_4 == 34 or LA12_4 == 39) :
                    alt12 = 1
                else:
                    nvae = NoViableAltException("", 12, 4, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 12, 0, self.input)

                raise nvae


            if alt12 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:182:7: ( STRPREFIX )? ( SLSTRING )+
                pass 
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:182:7: ( STRPREFIX )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 82 or LA9_0 == 85 or LA9_0 == 114 or LA9_0 == 117) :
                    alt9 = 1
                if alt9 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                    pass 
                    if self.input.LA(1) == 82 or self.input.LA(1) == 85 or self.input.LA(1) == 114 or self.input.LA(1) == 117:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:182:20: ( SLSTRING )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 34 or LA10_0 == 39) :
                        alt10 = 1


                    if alt10 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:182:21: SLSTRING
                        pass 
                        self.mSLSTRING()



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1



            elif alt12 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:183:7: ( BYTESTRPREFIX ) ( SLBYTESTRING )+
                pass 
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:183:7: ( BYTESTRPREFIX )
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:183:8: BYTESTRPREFIX
                pass 
                self.mBYTESTRPREFIX()





                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:183:23: ( SLBYTESTRING )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 34 or LA11_0 == 39) :
                        alt11 = 1


                    if alt11 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:183:24: SLBYTESTRING
                        pass 
                        self.mSLBYTESTRING()



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:189:5: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '.' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )* )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:189:7: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '.' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )*
            pass 
            if self.input.LA(1) == 46 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:189:35: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_' | '.' )*
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 46 or (48 <= LA13_0 <= 57) or (65 <= LA13_0 <= 90) or LA13_0 == 95 or (97 <= LA13_0 <= 122)) :
                    alt13 = 1


                if alt13 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                    pass 
                    if self.input.LA(1) == 46 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop13




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:194:5: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' | '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            alt19 = 3
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 47) :
                LA19_1 = self.input.LA(2)

                if (LA19_1 == 47) :
                    alt19 = 1
                elif (LA19_1 == 42) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 1, self.input)

                    raise nvae


            elif (LA19_0 == 35) :
                alt19 = 3
            else:
                nvae = NoViableAltException("", 19, 0, self.input)

                raise nvae


            if alt19 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:194:7: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:194:12: (~ ( '\\n' | '\\r' ) )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((0 <= LA14_0 <= 9) or (11 <= LA14_0 <= 12) or (14 <= LA14_0 <= 65535)) :
                        alt14 = 1


                    if alt14 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop14


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:194:26: ( '\\r' )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 13) :
                    alt15 = 1
                if alt15 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:194:26: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            elif alt19 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:195:7: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:195:12: ( options {greedy=false; } : . )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 42) :
                        LA16_1 = self.input.LA(2)

                        if (LA16_1 == 47) :
                            alt16 = 2
                        elif ((0 <= LA16_1 <= 46) or (48 <= LA16_1 <= 65535)) :
                            alt16 = 1


                    elif ((0 <= LA16_0 <= 41) or (43 <= LA16_0 <= 65535)) :
                        alt16 = 1


                    if alt16 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:195:40: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop16


                self.match("*/")


                #action start
                _channel=HIDDEN;
                #action end



            elif alt19 == 3:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:196:7: '#' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match(35)

                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:196:11: (~ ( '\\n' | '\\r' ) )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if ((0 <= LA17_0 <= 9) or (11 <= LA17_0 <= 12) or (14 <= LA17_0 <= 65535)) :
                        alt17 = 1


                    if alt17 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop17


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:196:25: ( '\\r' )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == 13) :
                    alt18 = 1
                if alt18 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:196:25: '\\r'
                    pass 
                    self.match(13)




                self.match(10)

                #action start
                _channel=HIDDEN;
                #action end



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:200:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:200:7: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:214:5: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:214:7: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:214:17: ( '+' | '-' )?
            alt20 = 2
            LA20_0 = self.input.LA(1)

            if (LA20_0 == 43 or LA20_0 == 45) :
                alt20 = 1
            if alt20 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:214:28: ( '0' .. '9' )+
            cnt21 = 0
            while True: #loop21
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((48 <= LA21_0 <= 57)) :
                    alt21 = 1


                if alt21 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt21 >= 1:
                        break #loop21

                    eee = EarlyExitException(21, self.input)
                    raise eee

                cnt21 += 1





        finally:
            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:219:5: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:224:5: ( ( '0' .. '9' ) )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if (48 <= self.input.LA(1) <= 57):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "FLOAT_NO_EXP"
    def mFLOAT_NO_EXP(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:229:5: ( ( INT_PART )? FRAC_PART | INT_PART '.' )
            alt23 = 2
            alt23 = self.dfa23.predict(self.input)
            if alt23 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:229:7: ( INT_PART )? FRAC_PART
                pass 
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:229:7: ( INT_PART )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if ((48 <= LA22_0 <= 57)) :
                    alt22 = 1
                if alt22 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:229:7: INT_PART
                    pass 
                    self.mINT_PART()





                self.mFRAC_PART()



            elif alt23 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:230:7: INT_PART '.'
                pass 
                self.mINT_PART()


                self.match(46)



        finally:
            pass

    # $ANTLR end "FLOAT_NO_EXP"



    # $ANTLR start "FLOAT_EXP"
    def mFLOAT_EXP(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:235:5: ( ( INT_PART | FLOAT_NO_EXP ) EXPONENT )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:235:7: ( INT_PART | FLOAT_NO_EXP ) EXPONENT
            pass 
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:235:7: ( INT_PART | FLOAT_NO_EXP )
            alt24 = 2
            alt24 = self.dfa24.predict(self.input)
            if alt24 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:235:9: INT_PART
                pass 
                self.mINT_PART()



            elif alt24 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:235:20: FLOAT_NO_EXP
                pass 
                self.mFLOAT_NO_EXP()





            self.mEXPONENT()





        finally:
            pass

    # $ANTLR end "FLOAT_EXP"



    # $ANTLR start "INT_PART"
    def mINT_PART(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:240:5: ( ( DIGIT )+ )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:240:7: ( DIGIT )+
            pass 
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:240:7: ( DIGIT )+
            cnt25 = 0
            while True: #loop25
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if ((48 <= LA25_0 <= 57)) :
                    alt25 = 1


                if alt25 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt25 >= 1:
                        break #loop25

                    eee = EarlyExitException(25, self.input)
                    raise eee

                cnt25 += 1





        finally:
            pass

    # $ANTLR end "INT_PART"



    # $ANTLR start "FRAC_PART"
    def mFRAC_PART(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:245:5: ( '.' ( DIGIT )+ )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:245:7: '.' ( DIGIT )+
            pass 
            self.match(46)

            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:245:11: ( DIGIT )+
            cnt26 = 0
            while True: #loop26
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if ((48 <= LA26_0 <= 57)) :
                    alt26 = 1


                if alt26 == 1:
                    # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt26 >= 1:
                        break #loop26

                    eee = EarlyExitException(26, self.input)
                    raise eee

                cnt26 += 1





        finally:
            pass

    # $ANTLR end "FRAC_PART"



    # $ANTLR start "STRPREFIX"
    def mSTRPREFIX(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:253:5: ( 'r' | 'R' | 'u' | 'U' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if self.input.LA(1) == 82 or self.input.LA(1) == 85 or self.input.LA(1) == 114 or self.input.LA(1) == 117:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "STRPREFIX"



    # $ANTLR start "STRING_ESC"
    def mSTRING_ESC(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:258:5: ( '\\\\' . )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:258:7: '\\\\' .
            pass 
            self.match(92)

            self.matchAny()




        finally:
            pass

    # $ANTLR end "STRING_ESC"



    # $ANTLR start "SLSTRING"
    def mSLSTRING(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:265:5: ( '\\'' ( STRING_ESC |~ ( '\\\\' | '\\r' | '\\n' | '\\'' ) )* '\\'' | '\"' ( STRING_ESC |~ ( '\\\\' | '\\r' | '\\n' | '\"' ) )* '\"' | '\\'\\'\\'' ( STRING_ESC |~ ( '\\\\' ) )* '\\'\\'\\'' | '\"\"\"' ( STRING_ESC |~ ( '\\\\' ) )* '\"\"\"' )
            alt31 = 4
            LA31_0 = self.input.LA(1)

            if (LA31_0 == 39) :
                LA31_1 = self.input.LA(2)

                if (LA31_1 == 39) :
                    LA31_3 = self.input.LA(3)

                    if (LA31_3 == 39) :
                        alt31 = 3
                    else:
                        alt31 = 1

                elif ((0 <= LA31_1 <= 9) or (11 <= LA31_1 <= 12) or (14 <= LA31_1 <= 38) or (40 <= LA31_1 <= 65535)) :
                    alt31 = 1
                else:
                    nvae = NoViableAltException("", 31, 1, self.input)

                    raise nvae


            elif (LA31_0 == 34) :
                LA31_2 = self.input.LA(2)

                if (LA31_2 == 34) :
                    LA31_5 = self.input.LA(3)

                    if (LA31_5 == 34) :
                        alt31 = 4
                    else:
                        alt31 = 2

                elif ((0 <= LA31_2 <= 9) or (11 <= LA31_2 <= 12) or (14 <= LA31_2 <= 33) or (35 <= LA31_2 <= 65535)) :
                    alt31 = 2
                else:
                    nvae = NoViableAltException("", 31, 2, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 31, 0, self.input)

                raise nvae


            if alt31 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:265:7: '\\'' ( STRING_ESC |~ ( '\\\\' | '\\r' | '\\n' | '\\'' ) )* '\\''
                pass 
                self.match(39)

                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:265:12: ( STRING_ESC |~ ( '\\\\' | '\\r' | '\\n' | '\\'' ) )*
                while True: #loop27
                    alt27 = 3
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == 92) :
                        alt27 = 1
                    elif ((0 <= LA27_0 <= 9) or (11 <= LA27_0 <= 12) or (14 <= LA27_0 <= 38) or (40 <= LA27_0 <= 91) or (93 <= LA27_0 <= 65535)) :
                        alt27 = 2


                    if alt27 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:265:13: STRING_ESC
                        pass 
                        self.mSTRING_ESC()



                    elif alt27 == 2:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:265:26: ~ ( '\\\\' | '\\r' | '\\n' | '\\'' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop27


                self.match(39)


            elif alt31 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:266:7: '\"' ( STRING_ESC |~ ( '\\\\' | '\\r' | '\\n' | '\"' ) )* '\"'
                pass 
                self.match(34)

                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:266:11: ( STRING_ESC |~ ( '\\\\' | '\\r' | '\\n' | '\"' ) )*
                while True: #loop28
                    alt28 = 3
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == 92) :
                        alt28 = 1
                    elif ((0 <= LA28_0 <= 9) or (11 <= LA28_0 <= 12) or (14 <= LA28_0 <= 33) or (35 <= LA28_0 <= 91) or (93 <= LA28_0 <= 65535)) :
                        alt28 = 2


                    if alt28 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:266:12: STRING_ESC
                        pass 
                        self.mSTRING_ESC()



                    elif alt28 == 2:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:266:25: ~ ( '\\\\' | '\\r' | '\\n' | '\"' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop28


                self.match(34)


            elif alt31 == 3:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:267:7: '\\'\\'\\'' ( STRING_ESC |~ ( '\\\\' ) )* '\\'\\'\\''
                pass 
                self.match("'''")


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:267:16: ( STRING_ESC |~ ( '\\\\' ) )*
                while True: #loop29
                    alt29 = 3
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == 39) :
                        LA29_1 = self.input.LA(2)

                        if (LA29_1 == 39) :
                            LA29_4 = self.input.LA(3)

                            if (LA29_4 == 39) :
                                LA29_5 = self.input.LA(4)

                                if ((0 <= LA29_5 <= 65535)) :
                                    alt29 = 2


                            elif ((0 <= LA29_4 <= 38) or (40 <= LA29_4 <= 65535)) :
                                alt29 = 2


                        elif ((0 <= LA29_1 <= 38) or (40 <= LA29_1 <= 65535)) :
                            alt29 = 2


                    elif (LA29_0 == 92) :
                        alt29 = 1
                    elif ((0 <= LA29_0 <= 38) or (40 <= LA29_0 <= 91) or (93 <= LA29_0 <= 65535)) :
                        alt29 = 2


                    if alt29 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:267:17: STRING_ESC
                        pass 
                        self.mSTRING_ESC()



                    elif alt29 == 2:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:267:30: ~ ( '\\\\' )
                        pass 
                        if (0 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop29


                self.match("'''")



            elif alt31 == 4:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:268:7: '\"\"\"' ( STRING_ESC |~ ( '\\\\' ) )* '\"\"\"'
                pass 
                self.match("\"\"\"")


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:268:13: ( STRING_ESC |~ ( '\\\\' ) )*
                while True: #loop30
                    alt30 = 3
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 34) :
                        LA30_1 = self.input.LA(2)

                        if (LA30_1 == 34) :
                            LA30_4 = self.input.LA(3)

                            if (LA30_4 == 34) :
                                LA30_5 = self.input.LA(4)

                                if ((0 <= LA30_5 <= 65535)) :
                                    alt30 = 2


                            elif ((0 <= LA30_4 <= 33) or (35 <= LA30_4 <= 65535)) :
                                alt30 = 2


                        elif ((0 <= LA30_1 <= 33) or (35 <= LA30_1 <= 65535)) :
                            alt30 = 2


                    elif (LA30_0 == 92) :
                        alt30 = 1
                    elif ((0 <= LA30_0 <= 33) or (35 <= LA30_0 <= 91) or (93 <= LA30_0 <= 65535)) :
                        alt30 = 2


                    if alt30 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:268:14: STRING_ESC
                        pass 
                        self.mSTRING_ESC()



                    elif alt30 == 2:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:268:27: ~ ( '\\\\' )
                        pass 
                        if (0 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop30


                self.match("\"\"\"")




        finally:
            pass

    # $ANTLR end "SLSTRING"



    # $ANTLR start "BYTESTRPREFIX"
    def mBYTESTRPREFIX(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:5: ( 'b' | 'B' | 'br' | 'Br' | 'bR' | 'BR' | 'rb' | 'rB' | 'Rb' | 'RB' )
            alt32 = 10
            LA32 = self.input.LA(1)
            if LA32 == 98:
                LA32 = self.input.LA(2)
                if LA32 == 114:
                    alt32 = 3
                elif LA32 == 82:
                    alt32 = 5
                else:
                    alt32 = 1

            elif LA32 == 66:
                LA32 = self.input.LA(2)
                if LA32 == 114:
                    alt32 = 4
                elif LA32 == 82:
                    alt32 = 6
                else:
                    alt32 = 2

            elif LA32 == 114:
                LA32_3 = self.input.LA(2)

                if (LA32_3 == 98) :
                    alt32 = 7
                elif (LA32_3 == 66) :
                    alt32 = 8
                else:
                    nvae = NoViableAltException("", 32, 3, self.input)

                    raise nvae


            elif LA32 == 82:
                LA32_4 = self.input.LA(2)

                if (LA32_4 == 98) :
                    alt32 = 9
                elif (LA32_4 == 66) :
                    alt32 = 10
                else:
                    nvae = NoViableAltException("", 32, 4, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 32, 0, self.input)

                raise nvae


            if alt32 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:7: 'b'
                pass 
                self.match(98)


            elif alt32 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:13: 'B'
                pass 
                self.match(66)


            elif alt32 == 3:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:19: 'br'
                pass 
                self.match("br")



            elif alt32 == 4:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:26: 'Br'
                pass 
                self.match("Br")



            elif alt32 == 5:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:33: 'bR'
                pass 
                self.match("bR")



            elif alt32 == 6:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:40: 'BR'
                pass 
                self.match("BR")



            elif alt32 == 7:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:47: 'rb'
                pass 
                self.match("rb")



            elif alt32 == 8:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:54: 'rB'
                pass 
                self.match("rB")



            elif alt32 == 9:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:61: 'Rb'
                pass 
                self.match("Rb")



            elif alt32 == 10:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:279:68: 'RB'
                pass 
                self.match("RB")




        finally:
            pass

    # $ANTLR end "BYTESTRPREFIX"



    # $ANTLR start "SLBYTESTRING"
    def mSLBYTESTRING(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:284:5: ( '\\'' ( BYTES_CHAR_SQ | BYTES_ESC )* '\\'' | '\"' ( BYTES_CHAR_DQ | BYTES_ESC )* '\"' | '\\'\\'\\'' ( BYTES_CHAR_SQ | BYTES_TESC )* '\\'\\'\\'' | '\"\"\"' ( BYTES_CHAR_DQ | BYTES_TESC )* '\"\"\"' )
            alt37 = 4
            LA37_0 = self.input.LA(1)

            if (LA37_0 == 39) :
                LA37_1 = self.input.LA(2)

                if (LA37_1 == 39) :
                    LA37_3 = self.input.LA(3)

                    if (LA37_3 == 39) :
                        alt37 = 3
                    else:
                        alt37 = 1

                elif ((0 <= LA37_1 <= 9) or (11 <= LA37_1 <= 12) or (14 <= LA37_1 <= 38) or (40 <= LA37_1 <= 127)) :
                    alt37 = 1
                else:
                    nvae = NoViableAltException("", 37, 1, self.input)

                    raise nvae


            elif (LA37_0 == 34) :
                LA37_2 = self.input.LA(2)

                if (LA37_2 == 34) :
                    LA37_5 = self.input.LA(3)

                    if (LA37_5 == 34) :
                        alt37 = 4
                    else:
                        alt37 = 2

                elif ((0 <= LA37_2 <= 9) or (11 <= LA37_2 <= 12) or (14 <= LA37_2 <= 33) or (35 <= LA37_2 <= 127)) :
                    alt37 = 2
                else:
                    nvae = NoViableAltException("", 37, 2, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 37, 0, self.input)

                raise nvae


            if alt37 == 1:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:284:7: '\\'' ( BYTES_CHAR_SQ | BYTES_ESC )* '\\''
                pass 
                self.match(39)

                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:284:12: ( BYTES_CHAR_SQ | BYTES_ESC )*
                while True: #loop33
                    alt33 = 3
                    LA33_0 = self.input.LA(1)

                    if ((0 <= LA33_0 <= 9) or (11 <= LA33_0 <= 12) or (14 <= LA33_0 <= 38) or (40 <= LA33_0 <= 91) or (93 <= LA33_0 <= 127)) :
                        alt33 = 1
                    elif (LA33_0 == 92) :
                        alt33 = 2


                    if alt33 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:284:13: BYTES_CHAR_SQ
                        pass 
                        self.mBYTES_CHAR_SQ()



                    elif alt33 == 2:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:284:29: BYTES_ESC
                        pass 
                        self.mBYTES_ESC()



                    else:
                        break #loop33


                self.match(39)


            elif alt37 == 2:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:285:7: '\"' ( BYTES_CHAR_DQ | BYTES_ESC )* '\"'
                pass 
                self.match(34)

                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:285:11: ( BYTES_CHAR_DQ | BYTES_ESC )*
                while True: #loop34
                    alt34 = 3
                    LA34_0 = self.input.LA(1)

                    if ((0 <= LA34_0 <= 9) or (11 <= LA34_0 <= 12) or (14 <= LA34_0 <= 33) or (35 <= LA34_0 <= 91) or (93 <= LA34_0 <= 127)) :
                        alt34 = 1
                    elif (LA34_0 == 92) :
                        alt34 = 2


                    if alt34 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:285:12: BYTES_CHAR_DQ
                        pass 
                        self.mBYTES_CHAR_DQ()



                    elif alt34 == 2:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:285:28: BYTES_ESC
                        pass 
                        self.mBYTES_ESC()



                    else:
                        break #loop34


                self.match(34)


            elif alt37 == 3:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:286:7: '\\'\\'\\'' ( BYTES_CHAR_SQ | BYTES_TESC )* '\\'\\'\\''
                pass 
                self.match("'''")


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:286:16: ( BYTES_CHAR_SQ | BYTES_TESC )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == 39) :
                        LA35_1 = self.input.LA(2)

                        if (LA35_1 == 39) :
                            LA35_3 = self.input.LA(3)

                            if (LA35_3 == 39) :
                                LA35_4 = self.input.LA(4)

                                if ((0 <= LA35_4 <= 91) or (93 <= LA35_4 <= 127)) :
                                    alt35 = 1


                            elif ((0 <= LA35_3 <= 38) or (40 <= LA35_3 <= 91) or (93 <= LA35_3 <= 127)) :
                                alt35 = 1


                        elif ((0 <= LA35_1 <= 38) or (40 <= LA35_1 <= 91) or (93 <= LA35_1 <= 127)) :
                            alt35 = 1


                    elif ((0 <= LA35_0 <= 38) or (40 <= LA35_0 <= 91) or (93 <= LA35_0 <= 127)) :
                        alt35 = 1


                    if alt35 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 91) or (14 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 127):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop35


                self.match("'''")



            elif alt37 == 4:
                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:287:7: '\"\"\"' ( BYTES_CHAR_DQ | BYTES_TESC )* '\"\"\"'
                pass 
                self.match("\"\"\"")


                # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:287:13: ( BYTES_CHAR_DQ | BYTES_TESC )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == 34) :
                        LA36_1 = self.input.LA(2)

                        if (LA36_1 == 34) :
                            LA36_3 = self.input.LA(3)

                            if (LA36_3 == 34) :
                                LA36_4 = self.input.LA(4)

                                if ((0 <= LA36_4 <= 91) or (93 <= LA36_4 <= 127)) :
                                    alt36 = 1


                            elif ((0 <= LA36_3 <= 33) or (35 <= LA36_3 <= 91) or (93 <= LA36_3 <= 127)) :
                                alt36 = 1


                        elif ((0 <= LA36_1 <= 33) or (35 <= LA36_1 <= 91) or (93 <= LA36_1 <= 127)) :
                            alt36 = 1


                    elif ((0 <= LA36_0 <= 33) or (35 <= LA36_0 <= 91) or (93 <= LA36_0 <= 127)) :
                        alt36 = 1


                    if alt36 == 1:
                        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
                        pass 
                        if (0 <= self.input.LA(1) <= 91) or (14 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 127):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop36


                self.match("\"\"\"")




        finally:
            pass

    # $ANTLR end "SLBYTESTRING"



    # $ANTLR start "BYTES_CHAR_SQ"
    def mBYTES_CHAR_SQ(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:292:5: ( '\\u0000' .. '\\u0009' | '\\u000B' .. '\\u000C' | '\\u000E' .. '\\u0026' | '\\u0028' .. '\\u005B' | '\\u005D' .. '\\u007F' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 127):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "BYTES_CHAR_SQ"



    # $ANTLR start "BYTES_CHAR_DQ"
    def mBYTES_CHAR_DQ(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:301:5: ( '\\u0000' .. '\\u0009' | '\\u000B' .. '\\u000C' | '\\u000E' .. '\\u0021' | '\\u0023' .. '\\u005B' | '\\u005D' .. '\\u007F' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 127):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "BYTES_CHAR_DQ"



    # $ANTLR start "BYTES_ESC"
    def mBYTES_ESC(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:310:5: ( '\\\\' '\\u0000' .. '\\u007F' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:310:7: '\\\\' '\\u0000' .. '\\u007F'
            pass 
            self.match(92)

            self.matchRange(0, 127)




        finally:
            pass

    # $ANTLR end "BYTES_ESC"



    # $ANTLR start "BYTES_TESC"
    def mBYTES_TESC(self, ):
        try:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:316:5: ( '\\u0000' .. '\\u005B' | '\\u005D' .. '\\u007F' )
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:
            pass 
            if (0 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 127):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "BYTES_TESC"



    def mTokens(self):
        # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:8: ( COLONMINUS | COMMA | LBRACKET | LPAREN | RBRACKET | RPAREN | T__52 | T__53 | T__54 | NEGATION | EQUAL | SIGN | INT | FLOAT | STRING | ID | COMMENT | WS )
        alt38 = 18
        alt38 = self.dfa38.predict(self.input)
        if alt38 == 1:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:10: COLONMINUS
            pass 
            self.mCOLONMINUS()



        elif alt38 == 2:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:21: COMMA
            pass 
            self.mCOMMA()



        elif alt38 == 3:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:27: LBRACKET
            pass 
            self.mLBRACKET()



        elif alt38 == 4:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:36: LPAREN
            pass 
            self.mLPAREN()



        elif alt38 == 5:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:43: RBRACKET
            pass 
            self.mRBRACKET()



        elif alt38 == 6:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:52: RPAREN
            pass 
            self.mRPAREN()



        elif alt38 == 7:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:59: T__52
            pass 
            self.mT__52()



        elif alt38 == 8:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:65: T__53
            pass 
            self.mT__53()



        elif alt38 == 9:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:71: T__54
            pass 
            self.mT__54()



        elif alt38 == 10:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:77: NEGATION
            pass 
            self.mNEGATION()



        elif alt38 == 11:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:86: EQUAL
            pass 
            self.mEQUAL()



        elif alt38 == 12:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:92: SIGN
            pass 
            self.mSIGN()



        elif alt38 == 13:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:97: INT
            pass 
            self.mINT()



        elif alt38 == 14:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:101: FLOAT
            pass 
            self.mFLOAT()



        elif alt38 == 15:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:107: STRING
            pass 
            self.mSTRING()



        elif alt38 == 16:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:114: ID
            pass 
            self.mID()



        elif alt38 == 17:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:117: COMMENT
            pass 
            self.mCOMMENT()



        elif alt38 == 18:
            # /Users/thinrichs/Code/congress/congress/datalog/Congress.g:1:125: WS
            pass 
            self.mWS()








    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\3\uffff\1\6\1\uffff\1\6\1\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\2\56\2\60\1\uffff\1\60\1\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\1\71\1\145\1\71\1\145\1\uffff\1\145\1\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA8_special = DFA.unpack(
        u"\7\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u"\12\5"),
        DFA.unpack(u"\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\5\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack(
        u"\3\uffff\1\4\1\uffff"
        )

    DFA23_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA23_min = DFA.unpack(
        u"\2\56\1\uffff\1\60\1\uffff"
        )

    DFA23_max = DFA.unpack(
        u"\2\71\1\uffff\1\71\1\uffff"
        )

    DFA23_accept = DFA.unpack(
        u"\2\uffff\1\1\1\uffff\1\2"
        )

    DFA23_special = DFA.unpack(
        u"\5\uffff"
        )


    DFA23_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\3\1\uffff\12\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\2"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #23

    class DFA23(DFA):
        pass


    # lookup tables for DFA #24

    DFA24_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA24_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA24_min = DFA.unpack(
        u"\2\56\2\uffff"
        )

    DFA24_max = DFA.unpack(
        u"\1\71\1\145\2\uffff"
        )

    DFA24_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA24_special = DFA.unpack(
        u"\4\uffff"
        )


    DFA24_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\2\1\uffff\12\1\13\uffff\1\3\37\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #24

    class DFA24(DFA):
        pass


    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\1\uffff\1\32\5\uffff\1\33\1\uffff\2\26\3\uffff\2\40\1\26\1\uffff"
        u"\4\26\6\uffff\1\41\2\26\1\40\2\uffff\1\40\11\26\2\13\1\41"
        )

    DFA38_eof = DFA.unpack(
        u"\57\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\11\1\55\5\uffff\1\56\1\uffff\1\157\1\117\3\uffff\2\56\1\42\1"
        u"\uffff\4\42\6\uffff\1\56\1\164\1\124\1\56\2\uffff\1\56\10\42\1"
        u"\53\3\56"
        )

    DFA38_max = DFA.unpack(
        u"\1\172\1\55\5\uffff\1\172\1\uffff\1\157\1\117\3\uffff\2\145\1\142"
        u"\1\uffff\2\162\1\142\1\47\6\uffff\1\172\1\164\1\124\1\145\2\uffff"
        u"\1\145\10\47\1\71\3\172"
        )

    DFA38_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\5\1\6\1\uffff\1\11\2\uffff\1\12\1\13\1\14"
        u"\3\uffff\1\17\4\uffff\1\20\1\21\1\22\1\1\1\10\1\7\4\uffff\1\15"
        u"\1\16\15\uffff"
        )

    DFA38_special = DFA.unpack(
        u"\57\uffff"
        )


    DFA38_transition = [
        DFA.unpack(u"\2\30\2\uffff\1\30\22\uffff\1\30\1\13\1\21\1\27\3\uffff"
        u"\1\21\1\4\1\6\1\uffff\1\15\1\2\1\15\1\7\1\27\1\17\11\16\1\1\1\10"
        u"\1\uffff\1\14\3\uffff\1\26\1\23\13\26\1\12\3\26\1\24\2\26\1\25"
        u"\5\26\1\3\1\uffff\1\5\1\uffff\1\26\1\uffff\1\26\1\22\13\26\1\11"
        u"\3\26\1\20\2\26\1\25\5\26"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26\1\uffff\12\34\7\uffff\32\26\4\uffff\1\26\1\uffff"
        u"\32\26"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41\1\uffff\12\37\13\uffff\1\41\37\uffff\1\41"),
        DFA.unpack(u"\1\41\1\uffff\1\42\11\41\13\uffff\1\41\37\uffff\1\41"),
        DFA.unpack(u"\1\21\4\uffff\1\21\32\uffff\1\44\37\uffff\1\43"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\21\4\uffff\1\21\52\uffff\1\46\37\uffff\1\45"),
        DFA.unpack(u"\1\21\4\uffff\1\21\52\uffff\1\50\37\uffff\1\47"),
        DFA.unpack(u"\1\21\4\uffff\1\21\32\uffff\1\52\37\uffff\1\51"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26\1\uffff\12\34\7\uffff\4\26\1\53\25\26\4\uffff"
        u"\1\26\1\uffff\4\26\1\53\25\26"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\41\1\uffff\12\37\13\uffff\1\41\37\uffff\1\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41\1\uffff\1\42\11\41\13\uffff\1\41\37\uffff\1\41"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\21\4\uffff\1\21"),
        DFA.unpack(u"\1\41\1\uffff\1\41\2\uffff\12\56"),
        DFA.unpack(u"\1\26\1\uffff\12\26\7\uffff\32\26\4\uffff\1\26\1\uffff"
        u"\32\26"),
        DFA.unpack(u"\1\26\1\uffff\12\26\7\uffff\32\26\4\uffff\1\26\1\uffff"
        u"\32\26"),
        DFA.unpack(u"\1\26\1\uffff\12\56\7\uffff\32\26\4\uffff\1\26\1\uffff"
        u"\32\26")
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(CongressLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
