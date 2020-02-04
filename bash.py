import os, sys, fileinput
N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
ask = Y + '[' + W + '?' + Y + '] '
sukses = Y + '[' + W + '\xe2\x88\x9a' + Y + '] '
eror = R + '[' + W + '!' + R + ']'
banner = ('\n\x1b[1;33moooooooooo.        .o.        .oooooo..o ooooo   ooooo\n\x1b[1;33m`888\'   `Y8b      .888.      d8P\'    `Y8 `888\'   `888\' \n\x1b[1;33m 888     888     .8"888.     Y88bo.       888     888  \n\x1b[1;33m 888oooo888\'    .8\' `888.     `"Y8888o.   888ooooo888  \n\x1b[1;33m 888    `88b   .88ooo8888.        `"Y88b  888     888  \n\x1b[1;33m 888    .88P  .8\'     `888.  oo     .d8P  888     888  \n\x1b[1;33mo888bood8P\'  o88o     o8888o 8""88888P\'  o888o   o888o\n           \x1b[1;37m      ENCRYPT & DECRYPT \x1b[1;33mBASH\n                \x1b[1;37m   CODED BY \x1b[1;33mIQBALMH18\n').format(D, W, D, W, D, W, Y, W, D, W, D, W, D, W, D, W, D, Y, D, W, D, Y, D, G, W, G, D, G, W, G, Y, D, Y, D, Y, D, Y, D, Y)
banner2 = ('\n\x1b[90m----------------------------------------------------------\n         \x1b[1;33m[\x1b[1;37m1\x1b[1;33m] \x1b[1;37mEncrypt               \x1b[1;33m[\x1b[1;37m2\x1b[1;33m] \x1b[1;37mDecrypt\n\x1b[90m----------------------------------------------------------\n').format(G, W, G, W, G, W, G, W)
os.system('clear')
print banner
print banner2

def dekrip():
    try:
        sc = raw_input(ask + W + 'Script Name ' + Y + '> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Output' + Y + ' > ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch tes.sh')
        os.system('bash ' + out + ' > tes.sh')
        os.remove(out)
        os.rename('tes.sh', out)
        print sukses + 'Done..'
    except KeyboardInterrupt:
        print eror + ' Stopped!'
    except IOError:
        print eror + ' File Not Found!'

def enkrip():
    try:
        script = raw_input(ask + W + 'Script Name ' + Y + '> ' + W)
        output = raw_input(ask + W + 'Output Name ' + Y + '> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'Done..'
    except KeyboardInterrupt:
        print eror + ' Stopped!'
    except IOError:
        print eror + ' File Not Found!'


takok = raw_input(W + 'Choose Number' + Y + ' > ')
if takok == '1' or takok == '01':
    enkrip()
else:
    if takok == '2' or takok == '02':
        dekrip()
    else:
        print eror + ' Wrong Input, please correct your commands!'
	os.system('sleep 3;python2 bash.py')
