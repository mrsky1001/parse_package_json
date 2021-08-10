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

    with open(src) as file_in:
        srcText = file_in.read()

    with open(dst) as file_in:
        dstText = file_in.read()

    for lineF2 in dstText.splitlines():
        lineDst = re.search(r'"\S*":.*"\S*"', lineF2)

        if lineDst:
            nameDst = re.search(r'"\S*":', lineDst[0])[0]

            for lineF1 in srcText.splitlines():
                lineSrc = re.search(r'"\S*":.*"\S*"', lineF1)

                if lineSrc:
                    nameSrc = re.search(r'"\S*":', lineSrc[0])[0]

                    if nameSrc == nameDst:
                        contentMatchSrc = re.search(r':.*"\S*"', lineSrc[0])
                        contentMatchDst = re.search(r':.*"\S*"', lineDst[0])

                        contentSrc = contentMatchSrc[0] if contentMatchSrc else ''
                        contentDst = contentMatchDst[0] if contentMatchDst else ''

                        if contentSrc != contentDst:
                            print(nameDst + contentDst + ' --> ' + contentSrc)
                            dstText = dstText.replace(contentDst, contentSrc)

    with open(dst, "w") as file_out:
        file_out.write(dstText)
