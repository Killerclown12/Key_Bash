
# author : @Syhrularv_
# -*- coding: utf-8 -*-

import os,sys,fileinput
#warna
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
{}         _nnnn_{}        _________________
{}        dGGGGMMb{}      |                 |
{}       @p~qp~~qMb{}   ._| {}Bash Oubfuscate {}|
{}       M{}({}@{})({}@{}) {}M|{}  /  |_________________|
{}       @,{}----.{}JM|{}_/
{}      JS^{}\__/{}  qKL
    dZP        qKRb
   dZP          qKKb
  fZP            SMMb
  HZM            MMMM    {}Coded by {}: {}Syhrül
{}   FqM            MMMM    {}FB       {}: {}fb.com/sarul.arif.5
{} __|'\ .        |\{}dS qML
{} |    `.       | `' \{}Zq
{}_)      \.{}___.{},|     .'
\____   ){}MMMMMP{}|   .'
    `-'       `--'
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)



print banner


def dekrip():
  try:
      sc = raw_input(ask + W + "Script " + G + "> " + W)
      f = open(sc,'r')
      filedata = f.read()
      f.close()

      newdata = filedata.replace("eval","echo")

      out = raw_input(ask + W + "Output" + G + " > " + W)
      f = open(out,'w')
      f.write(newdata)
      f.close()

      os.system("touch tes.sh")
      os.system("bash " + out + " > tes.sh")
      os.remove(out)
      os.rename("tes.sh", out)
      print (sukses + "Selesai")

  except KeyboardInterrupt:
      print (eror + " Behenti")
  except IOError:
      print (eror + " File Not Found!")
