#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import re

src = ''
dst = ''

if __name__ == "__main__":
    src = sys.argv[1] if sys.argv[1] else ''
    dst = sys.argv[2] if sys.argv[2] else ''

print(src)
print(dst)

if (os.path.exists(src) & os.path.exists(dst)):
    srcText = ''
    dstText = ''

    with open('log.txt', "w+") as log_out:
        log_out.write('====================== Starting compare files: ==========================\n')
        log_out.write('src: ' + src + '\n')
        log_out.write('dst: ' + dst + '\n')

        with open(src) as file_in:
            srcText = file_in.read()

        with open(dst) as file_in:
            dstText = file_in.read()

        for lineF2 in dstText.splitlines():
            lineDst = re.search(r'"\S*":.*"\S*"', lineF2)
            flagIsExist = False

            if lineDst:
                nameDst = re.search(r'"\S*":', lineDst[0])[0]

                for lineF1 in srcText.splitlines():
                    lineSrc = re.search(r'"\S*":.*"\S*"', lineF1)

                    if lineSrc:
                        nameSrc = re.search(r'"\S*":', lineSrc[0])[0]

                        contentMatchDst = re.search(r':.*"\S*"', lineDst[0])
                        content = contentMatchDst[0] if contentMatchDst else ''
                        contentDst = content.replace('^', '')
                        contentDst = contentDst.replace('~', '')

                        dstText = dstText.replace(content, contentDst)


                        if nameSrc == nameDst:
                            flagIsExist = True

                            contentMatchSrc = re.search(r':.*"\S*"', lineSrc[0])
                            contentSrc = contentMatchSrc[0] if contentMatchSrc else ''

                            if contentSrc != contentDst:
                                msg = nameDst + contentDst + ' --> ' + contentSrc + '\n'

                                print(msg)
                                log_out.write(msg)

                                dstText = dstText.replace(contentDst, contentSrc)

                if not flagIsExist:
                    msg = 'Warning! That dependency not exist in template!\n --->' + lineDst[0] + '\n'
                    print(msg)
                    log_out.write(msg)

        msg = 'Replace all [^, ~]!\n'
        print(msg)
        log_out.write(msg)

        with open(dst, "w") as file_out:
            file_out.write(dstText)

        msg = 'Finish parse!'
        print(msg)
        log_out.write(msg)
