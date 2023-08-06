########################################################################################################################
#                                          N-HANS speech denoiser: apply                                               #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#   Description:      Loading denoiser model.                                           .                              #
#   Authors:          Shuo Liu, Gil Keren, Bjoern Schuller                                                             #
#   Affiliation:      ZD.B Chair of Embedded Intelligence for Health Care and Wellbeing, University of Augsburg (UAU)  #
#   Version:          1.0                                                                                              #
#   Last Update:      Nov. 14, 2019                                                                                    #
#   Dependence Files: xxx                                                                                              #
#   Contact:          shuo.liu@informatik.uni-augburg.de                                                               #
########################################################################################################################

import os
def main():
    dropbox_link = 'https://www.dropbox.com/s/x2fsb7wcwcpdmqr/N_HANS___Denoiser.zip?dl=0'
    download_filename = 'N_HANS_denoiser.zip'
    command_download = 'wget {} -O {}'.format(dropbox_link, download_filename)
    command_unzip = 'unzip N_HANS_denoiser.zip'

    os.system(command_download)
    os.system(command_unzip)

