#!/usr/bin/env python
'''
sort or tar CFMM' data with DicomSorter


Update: 2019-11-21

Add DICOM tag option arguments to handel DICOM files missing(or empty): 
StudyDesciption, StudyDate, PatientName, StudyID, StudyInstanceUID,
SeriesNumber,InstanceNumber, and SOPInstanceUID. These tags are 
necessary to CFMM sort rule


Author: YingLi Lu
Email:  yinglilu@gmail.com
Date:   2018-05-22

Note:
    Tested on windows 10/ubuntu 16.04, python 2.7.14

'''
import sys
import os
import logging
import argparse

import sort_rules
import DicomSorter

import clinical_helpers as ch

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s -%(message)s')


def main(dicom_dir, output_dir, args):
    '''
    use DicomSorter sort or tar CFMM's dicom data

    input:
        dicom_dir: folder contains dicom files(and/or compressed files:.zip/.tgz/.tar.gz/.tar.bz2)
        output_dir: output sorted or tar files to this folder
    '''

    logger = logging.getLogger(__name__)

    if not os.path.exists(dicom_dir):
        logger.error("{} not exist!".format(dicom_dir))
        return False

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ######
    # CFMM sort rule
    ######
    try:
        if not args.clinical_scans:

            with DicomSorter.DicomSorter(dicom_dir, sort_rules.sort_rule_CFMM, output_dir, args) as d:
                # #######
                # # sort
                # #######
                # sorted_dirs = d.sort()
                # # logging
                # for item in sorted_dirs:
                #     logger.info("sorted directory created: {}".format(item))

                #######
                # tar
                #######
                # pi/project/study_date/patient/studyID_and_hash_studyInstanceUID
                tar_full_filenames = d.tar(5)
                # logging
                for item in tar_full_filenames:
                    logger.info("tar file created: {}".format(item))

            # ######
            # # demo sort rule
            # ######
            # with DicomSorter.DicomSorter(dicom_dir, sort_rules.sort_rule_demo, output_dir) as d:
            #     # sort
            #     sorted_dirs = d.sort()
            #     #logging
            #     for item in sorted_dirs:
            #         logger.info("sorted directory created: {}".format(item))

            #     # tar
            #     # patient_name/study_date/series_number/new_filename.dcm
            #     tar_full_filenames = d.tar(2)
            #     # logging
            #     for item in tar_full_filenames:
            #         logger.info("tar file created: {}".format(item))

        else:
            ######
            # Clinical sort rule
            ######
            logger.info("These are clinical scans.")

            with DicomSorter.DicomSorter(dicom_dir, sort_rules.sort_rule_clinical, output_dir, args) as d:
                # tar
                # study_date/patient/modality/series_number/new_filename.dcm
                tar_full_filenames = d.tar(4)

                # logging
                for item in tar_full_filenames:
                    logger.info("tar file created: {}".format(item))

            ch.tarSession(output_dir, dicom_dir, modality_sep=True)
            ch.combine_or_dates(dicom_dir, output_dir)
            ch.combine_error_info_tsv(dicom_dir, output_dir)

    except Exception as e:
        logger.exception(e)


def run():

    # arg parser
    parser = argparse.ArgumentParser()

    parser.add_argument("dicom_dir")
    parser.add_argument('output_dir')
    parser.add_argument("--clinical_scans", action="store_true")
    parser.add_argument("--StudyDescription",
                        nargs='?', default='PI^Project')
    parser.add_argument("--StudyDate",
                        nargs='?', default='19000101')
    parser.add_argument("--PatientName",
                        nargs='?', default='Anonymous')
    args = parser.parse_args()

    dicom_dir = args.dicom_dir
    output_dir = args.output_dir

    # main
    main(dicom_dir, output_dir, args)


if __name__ == "__main__":
    run()
