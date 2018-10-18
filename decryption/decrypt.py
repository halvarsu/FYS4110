import numpy as np

class Decrypt(object):

    """Docstring for Decrypt. """

    def __init__(self, string, to_lowercase = True, symbols = '-; .,\n' ):
        """TODO: to be defined1.

        :string: TODO

        """
        self._string = string.lower() if to_lowercase else string
        self._symbols = symbols
        
    def print_useful_stuff(self):
        letters = list(set(self._string) - set(self._symbols))
        num_letters = []
        double_letters = []

        for l in letters:
            num_letters.append(self._string.count(l))

        for l in letters:
            double_letters.append(self._string.count(l+l))


        i = np.argsort(num_letters)[::-1]
        print("=========")
        print(np.array(letters)[i])
        print(np.array(num_letters)[i])

        i2 = np.argsort(double_letters)[::-1]
        print("=========")
        print(np.array(letters)[i2])
        print(np.array(double_letters)[i2])

    def load_code(self, file = 'code.txt'):
        """Accepts a file with a code, two words (aka characters) on a line
        is parsed as a key and a value. May thus be partial."""

        keys = []
        values = []
        self.code = {s:s for s in self._symbols}
        temp_s = string

        with open(file) as infile:
            for line in infile:
                try:
                    k,v = line.split()
                    self.code[k] = v
                    keys.append(k)
                    values.append(v)
                except ValueError:
                    pass
            
    def decrypt(self, string = None, compare_print = False):
        try:
            code = self.code
        except AttributeError:
            print('please load a code with self.load_code first')
            raise

        string = string or self._string
        s_list = list(string)
        translated = ''.join(['-' if s not in code else code[s] for s in string])

        compare_print = False
        if compare_print:
            for w1, w2 in zip(translated.replace('\n',' ').split(' '), string.replace('\n',' ').split(' ')):
                print(f"{w1:16}, {w2:16}")

        else:
            print(translated)

    def encrypt(self, string, to_lowercase = True):
        try:
            code = self.code
        except AttributeError:
            print('please load a code with self.load_code first')
            raise
        code_inv = {v:k for k,v in code.items()}
        string = string.lower() if to_lowercase else string

        s_list = list(string)
        translated = ''.join(['-' if s not in code_inv else code_inv[s] for s in string])

        compare_print = False
        if compare_print:
            for w1, w2 in zip(translated.replace('\n',' ').split(' '), string.replace('\n',' ').split(' ')):
                print(f"{w1:16}, {w2:16}")

        else:
            print(translated)
        


# print(is_letter)
if __name__ == "__main__":
    string = '''Zvd zvpvyb lzvdc imcq dktat qkt pvmzysab ptqdttz qkt jhsccgjsh
szy omszqme yvesgz gc cgqmsqty. Evcq utth qksq trwtagetzqsh
cdgqjk ctqqgznc szy wvgzqta atsygznc sat vz qkgc cgyt. Pmq cvet
dvmhy qkgzl qkt pvmzysab ztsata, vqktac dvmhy qkgzl gq usaqkta,
szy eszb dvmhy watuta zvq qv qkgzl spvmq gq. Gz usjq, qkt esqqta
gc vu ftab hgqqht gewvaqszjt gz wasjqgjt. Qkgc gc ptjsmct vu qkt
geetzct yguutatzjt gz cjsht ptqdttz qkgznc uva dkgjk
omszqme-etjkszgjsh ytcjagwqgvz gc zmetagjshhb tcctzqgsh szy qkvct
vaygagzsaghb wtajtwqgpht pb kmesz ptgznc. Ztftaqkthtcc, qkt
evfspghgqb vu qkt pvmzysab gc vu vzhb swwavrgesqt fshgygqb;
ytevzcqasqgvzc vu gq ytwtzy vz ztnhtjqgzn zmeptac dkgjk sat
ceshh, pmq zvq xtav, dkgjk egnkq qtzy qv xtav uva gzugzgqthb
hsant cbcqtec, pmq sat vzhb ftab ceshh uva atsh ugzgqt cbcqtec.
S qktvab uvmzyty gz qkgc dsb vz sanmetzqc vu eszgutcqhb
swwavrgesqt jksasjqta, kvdtfta nvvy qkt swwavrgesqgvz, gc cmathb
vu wavfgcgvzsh zsqmat. Gq cttec htngqgesqt qv cwtjmhsqt vz kvd
qkt qktvab egnkq tfvhft.  Pmq vu jvmact zv vzt gc vphgnty qv ivgz
gz cmjk cwtjmhsqgvz.
                                                   Ivkz Pthh'''

    d = Decrypt(string)
    d.load_code()
    d.print_useful_stuff()
    d.decrypt('Is, lvc tz uatysnclfthy! Jtjghgt'.lower())
    # d.encrypt('')
    # d.encrypt('dette er veldig goey, kan skrive hva som helst naa som jeg foerst har en kode!')
