# THIS FILE IS GENERATED FROM PADDLEPADDLE SETUP.PY
#
full_version    = '1.6.2'
major           = '1'
minor           = '6'
patch           = '2'
rc              = '0'
istaged         = False
commit          = '2de10293964e29169d75f7aa732c294bc2b98c01'
with_mkl        = 'ON'

def show():
    if istaged:
        print('full_version:', full_version)
        print('major:', major)
        print('minor:', minor)
        print('patch:', patch)
        print('rc:', rc)
    else:
        print('commit:', commit)

def mkl():
    return with_mkl
