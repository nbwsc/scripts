#!/usr/bin/env python
from PIL import Image
import json
import sys
import os
sizes = json.load(open(os.path.join(sys.path[0], 'defalut_config.json')))


def mkdir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError as err:
        pass


# check path and files
resources = 'resources'
if not os.path.exists(resources):
    raise Exception('resources not exist')

iconFile = 'resources/icon.png'
if not os.path.exists(iconFile):
    print(iconFile + ' is exists')
else:
    print('processing icon')
    with Image.open(iconFile) as img:
        for platform in sizes['icon']:
            targetPath = os.path.join(resources, platform)
            mkdir(os.path.join(targetPath, 'icon'))
            for tgt in sizes['icon'][platform]:
                width = tgt["width"]
                height = tgt["height"]
                print(platform, width, height)
                targetName = tgt["targetName"]
                resized = img.resize((width, height), resample=Image.LANCZOS)
                resized.save(os.path.join(targetPath,
                                          'icon', targetName), format="png")

splashFile = 'resources/splash.png'
if not os.path.exists(splashFile):
    print(splashFile + ' is exists')
else:
    print('processing splash')
    with Image.open(splashFile) as img:
        for platform in sizes['splash']:
            targetPath = os.path.join(resources, platform)
            mkdir(os.path.join(targetPath, 'splash'))
            for tgt in sizes['splash'][platform]:
                width = tgt["width"]
                height = tgt["height"]
                print(platform, width, height)
                targetName = tgt["targetName"]
                resizeSize = max(width, height)
                resized = img.resize(
                    (resizeSize, resizeSize), resample=Image.LANCZOS)
                if width < height:
                    resized = resized.crop(((resizeSize-width)/2, 0,
                                            resizeSize-(height-width)/2, resizeSize))
                else:
                    resized = resized.crop((0, (resizeSize-height)/2, resizeSize,
                                            resizeSize-(width-height)/2))
                resized.save(os.path.join(targetPath,
                                          'splash', targetName), format="png")
