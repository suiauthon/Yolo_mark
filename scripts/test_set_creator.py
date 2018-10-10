#!/usr/bin/env python2.7

import os, sys, glob

VERSION_MINOR = 0
VERSION_MAJOR = 1
VERSION_YEAR = "2018"
VERSION_MONTH = "07"
VERSION_DAY = "10"

def usage(program_name):
    print('{} IMAGES_DIR OUTPUT_DIR PERCENTAGE [OPTIONS]'.format(program_name))
    print('Creates test and validation set.\n')
    print(' IMAGES_DIR:             Full path to the folder with images.')
    print(' OUTPUT_DIR:             Path to folder where test and validation set will be saved.')
    print(' PERCENTAGE:             Percentage of images that will be put in to validation set.')
    print(' OPTIONS:')
    print('     -h  |   --help      Print a help message and exit.')
    print('     -V  |   --version   Display version information and exit.')

def version(program_name):
    print('{} {}.{} {}{}{}'.format(program_name, VERSION_MAJOR, VERSION_MINOR, VERSION_DAY, VERSION_MONTH, VERSION_YEAR))

def create_train_and_val_set(image_dir, output_dir, percentage_test):
    if os.path.isfile(output_dir+"/train.txt"):
        os.remove(output_dir+"/train.txt") 
    if os.path.isfile(output_dir+"/test.txt"):
        os.remove(output_dir+"/test.txt") 
    file_train = open(output_dir + "/train.txt", 'w')
    file_test = open(output_dir + "/test.txt",'w')
    counter = 1
    index_test = round(100 / percentage_test)
    for pathAndFilename in glob.iglob(os.path.join(image_dir, "*.jpg")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
            counter = 1
            file_test.write(image_dir + '/' + title + '.jpg' + "\n")
        else:
            file_train.write(image_dir + '/' + title + '.jpg' + "\n")
            counter = counter + 1


if __name__ == "__main__":

    for i in range(len(sys.argv)):
        if (sys.argv[i] == '--help' or sys.argv[i] == '-h' or sys.argv[i] == '--version' or sys.argv[i] == '-V'):
            if (sys.argv[i] == '--help' or sys.argv[i] == '-h'):
                usage(sys.argv[0])
                sys.exit(0)
            elif (sys.argv[i] == '--version' or sys.argv[i] == '-V'):
                version(sys.argv[0])
            sys.exit(0)

    if (len(sys.argv) < 2):
        print('{}: missing  operand'.format(sys.argv[0]))
        print('Try {} --help or {} -h for more information.'.format(sys.argv[0], sys.argv[0]))
        sys.exit(0)
    elif (len(sys.argv) < 4):
        print('{}: wrong usage'.format(sys.argv[0]))
        print('Try {} --help or {} -h for more information.'.format(sys.argv[0], sys.argv[0]))
        sys.exit(0)

    images_dir = sys.argv[1]
    output_dir = sys.argv[2]
    percentage = int(sys.argv[3])

    create_train_and_val_set(images_dir, output_dir, percentage)
