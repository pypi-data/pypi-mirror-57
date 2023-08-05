#!/usr/bin/env python
'''
dicom sort rule functions:

    sort_rule_demo: a simple demo sort rule
    sort_rule_CFMM: CFMM's sort rule

Author: YingLi Lu
Email:  yinglilu@gmail.com
Date:   2018-05-22

note:
    Tested on windows 10/ubuntu 16.04, python 2.7.14
'''

import os
import re
import pydicom
import logging
import csv
import dcmstack as ds


def sort_rule_demo(filename):
    '''
    A simple sort rule:

    patient_name
      |-study_date
        |-series_number
          |-{patient_name}.{study_data}.{series_number}.{image_instance_number:04d}.dcm
          ... 
        |-series_number
        ...

    intput:
        filename: dicom filename
    output:
        a dictionary:
            key: filename
            value: patient_name/study_date/sereis_number/{patient_name}.{study_data}.{series_number}.{image:04d}.dcm

    '''
    logger = logging.getLogger(__name__)

    def clean_path(path):
        return re.sub(r'[^a-zA-Z0-9.-]', '_', '{0}'.format(path))

    try:
        dataset = pydicom.read_file(filename, stop_before_pixels=True)

        patient_name = clean_path(dataset.PatientName.replace('^', '_'))
        #print('patient_name', patient_name)
        study_date = clean_path(dataset.StudyDate)
        series_number = clean_path(
            '{series_number:04d}'.format(series_number=dataset.SeriesNumber))

        path = os.path.join(patient_name, study_date, series_number)
        sorted_filename = '{patient}.{study_date}.{series_number}.{image_instance_number:04d}.dcm'.format(
            patient=patient_name,
            study_date=study_date,
            series_number=dataset.SeriesNumber,
            image_instance_number=dataset.InstanceNumber,
        )
        sorted_filename = clean_path(sorted_filename)

    except Exception as e:
        logger.exception('something wrong with {}'.format(filename))
        logger.exception(e)
        return None

    sorted_full_filename = os.path.join(path, sorted_filename)
    return sorted_full_filename


def sort_rule_CFMM(filename, args):
    '''
    CFMM's Dicom sort rule

    intput:
        filename: dicom filename
    output:
        a dictionary:
            key: filename
            value: pi/project/study_date/patient/studyID_and_hash_studyInstanceUID/series_number
                   /{patient}.{modality}.{study}.{series:04d}.{image:04d}.{date}.{unique}.dcm

    CFMM's DICOM data Hierarchical structure: (same with CFMM's dcmrcvr.https://gitlab.com/cfmm/dcmrcvr)
    root_dir/
        -PI->first part of StudyDescription: John^Project.
            -project ->second part of StudyDescription: John^3T_Project.
                -19700101 ->StudyDate
                    -1970_01_01_C001 ->patientName
                    -1.AC168B21 -> dataset.StudyID + '.' + hashcode(dataset.StudyInstanceUID)
                            -0001->series number
                            -0002
                            -0003
                            -0004
                            -0005
                            -0006
                            -0007
                            ...
                    -1970_01_01_C002
                        -1.AC168B24
                            ...
                    -1970_01_01_C003
                        -1.AC168B3C
    '''

    logger = logging.getLogger(__name__)

    def clean_path(path):
        return re.sub(r'[^a-zA-Z0-9.-]', '_', '{0}'.format(path))

    def hashcode(value):
        code = 0
        for character in value:
            code = (code * 31 + ord(character)) & 0xffffffff
        return '{0:08X}'.format(code)

    try:
        dataset = pydicom.read_file(filename, stop_before_pixels=True)

        # StudyDescription
        # CFMM's newer data:'PI^project'->['PI','project']
        # CFMM's older GE data:'PI project'->['PI','project']
        if 'StudyDescription' in dataset and len(dataset.StudyDescription) > 0:
            StudyDescription = dataset.StudyDescription
        else:
            StudyDescription = args.StudyDescription

        pi_project = StudyDescription.replace('^', ' ').split()
        pi = clean_path(pi_project[0])
        project = clean_path(pi_project[1])

        # StudyDate
        if 'StudyDate' in dataset and len(dataset.StudyDate) > 0:
            StudyDate = dataset.StudyDate
        else:
            StudyDate = args.StudyDate

        study_date = clean_path(StudyDate)

        # PatientName
        if 'PatientName' in dataset and len(dataset.PatientName) > 0:
            PatientName = dataset.PatientName
        else:
            PatientName = args.PatientName

        patient = clean_path(PatientName.partition('^')[0])

        # studyID_and_hash_studyInstanceUID

        if 'StudyID' in dataset and len(dataset.StudyID) > 0:
            StudyID = dataset.StudyID
        else:
            StudyID = 'NA'

        if 'StudyInstanceUID' in dataset and len(dataset.StudyInstanceUID) > 0:
            StudyInstanceUID = dataset.StudyInstanceUID
        else:
            StudyInstanceUID = pydicom.uid.generate_uid()

        studyID_and_hash_studyInstanceUID = clean_path('.'.join([StudyID,
                                                                 hashcode(StudyInstanceUID)]))

        # SeriesNumber
        series_number = clean_path(
            '{series:04d}'.format(series=dataset.SeriesNumber))

        path = os.path.join(pi, project, study_date, patient,
                            studyID_and_hash_studyInstanceUID, series_number)
        sorted_filename = '{patient}.{modality}.{study}.{series:04d}.{image:04d}.{date}.{unique}.dcm'.format(
            patient=patient.upper(),
            modality=dataset.Modality,
            study=StudyDescription.upper(),
            series=dataset.SeriesNumber,
            image=dataset.InstanceNumber,
            date=StudyDate,
            unique=hashcode(dataset.SOPInstanceUID),
        )

        sorted_filename = clean_path(sorted_filename)

    except Exception as e:
        logger.exception('something wrong with {}'.format(filename))
        logger.exception(e)
        return None

    sorted_full_filename = os.path.join(path, sorted_filename)

    return sorted_full_filename


def sort_rule_clinical(filename):
    '''
    Clinical sort rule:

    patient_name
        |-study_date
            |-modality
                |-series_number
                  |-{patient}.{modality}.{series:04d}.{image:04d}.{study_date}.{unique}.dcm
                  ... 
                |-series_number
                ...
    intput:
        filename: dicom filename
    output:
        a dictionary:
            key: filename
            value: patient_name/study_date/modality/sereis_number/{patient}.{modality}.{series:04d}.{image:04d}.{study_date}.{unique}.dcm

    '''
    def write_error_file(my_file, errorInfoTemp):
        if os.path.exists(my_file):
            with open(my_file, 'r') as readFile:
                reader = csv.reader(readFile, delimiter='\t')
                lines = list(reader)
                if errorInfoTemp.split('\t') not in lines:
                    with open(my_file, 'a') as writeFile:
                        writeFile.write(errorInfoTemp)
                        writeFile.write("\n")
        else:
            with open(my_file, 'w') as writeFile:
                writeFile.write(
                    "\t".join(['subject', 'date', 'series', 'issue']))
                writeFile.write("\n")
                writeFile.write(errorInfoTemp)
                writeFile.write("\n")

    def clean_path(path):
        return re.sub(r'[^a-zA-Z0-9.-]', '_', '{0}'.format(path))

    def hashcode(value):
        code = 0
        for character in value:
            code = (code * 31 + ord(character)) & 0xffffffff
        return '{0:08X}'.format(code)

    # This will ignore any dicomdir present in the folder
    if all(['DICOMDIR' not in filename, not filename.endswith('OR_dates.tsv')]):
        logger = logging.getLogger(__name__)

        try:
            dataset = pydicom.read_file(
                filename, stop_before_pixels=True, force=True)
            study_date = dataset.StudyDate[0:4] + '_' + \
                dataset.StudyDate[4:6] + '_' + dataset.StudyDate[6:8]

            # This will skip any order sheets
            if dataset.Modality in {'SR', 'PR'}:
                errorInfoTemp = "\t".join(['P' + [s for s in filename.split('\\') if 'sub' in s][0].split('-')[1], study_date,
                                           clean_path('{series:04d}'.format(series=dataset.SeriesNumber)), dataset.Modality])
                my_file = os.path.join("\\".join(filename.split('\\')[:[i for i, s in enumerate(
                    filename.split('\\')) if 'sub' in s][0]]), 'errorInfo.tsv')
                write_error_file(my_file, errorInfoTemp)
                return None

            # This will skip any order sheets and localizers
            elif [x for x in dataset.ImageType if x in {'SECONDARY', 'LOCALIZER'}]:
                return None
            else:
                if 'SIEMENS' in dataset.Manufacturer:
                    errorInfoTemp = "\t".join(['P' + [s for s in filename.split('\\') if 'sub' in s][0].split('-')[1], study_date,
                                               clean_path('{series:04d}'.format(series=dataset.SeriesNumber)), 'SIEMENS'])
                    my_file = os.path.join("\\".join(filename.split('\\')[:[i for i, s in enumerate(
                        filename.split('\\')) if 'sub' in s][0]]), 'errorInfo.tsv')
                    write_error_file(my_file, errorInfoTemp)
                    return None
                else:
                    try:
                        csaReader = ds.wrapper_from_data(dataset)
                        modality = dataset.Modality

                        # --- INTRAOP X-RAY determination
                        if any(substring in modality for substring in {'Intraoperative', 'Skull', 'OT', 'XA', 'RF'}):
                            if 'CR' not in dataset.Modality:
                                or_date = dataset.StudyDate[0:4] + '_' + \
                                    dataset.StudyDate[4:6] + \
                                    '_' + dataset.StudyDate[6:8]
                                orDateTemp = "\t".join(
                                    ['P' + [s for s in filename.split('\\') if 'sub' in s][0].split('-')[1], or_date])
                                my_file = os.path.join("\\".join(filename.split('\\')[:[i for i, s in enumerate(
                                    filename.split('\\')) if 'sub' in s][0]+1]), 'OR_dates.tsv')

                                if os.path.exists(my_file):
                                    with open(my_file, 'r') as readFile:
                                        reader = csv.reader(
                                            readFile, delimiter='\t')
                                        lines = list(reader)
                                        if orDateTemp.split('\t') not in lines:
                                            with open(my_file, 'a') as writeFile:
                                                writeFile.write(orDateTemp)
                                                writeFile.write("\n")
                                else:
                                    with open(my_file, 'w') as writeFile:
                                        writeFile.write(
                                            "\t".join(['subject', 'or_date']))
                                        writeFile.write("\n")
                                        writeFile.write(orDateTemp)
                                        writeFile.write("\n")
                                return None

                            elif all(['CR' in dataset.Modality, 'Skull Routine Portable' in dataset.StudyDescription]):
                                errorInfoTemp = "\t".join(['P' + [s for s in filename.split('\\') if 'sub' in s][0].split('-')[1], study_date,
                                                           clean_path('{series:04d}'.format(series=dataset.SeriesNumber)), dataset.StudyDescription])
                                my_file = os.path.join("\\".join(filename.split('\\')[:[i for i, s in enumerate(
                                    filename.split('\\')) if 'sub' in s][0]]), 'errorInfo.tsv')
                                write_error_file(my_file, errorInfoTemp)
                                return None
                            else:
                                patient = 'P' + \
                                    [s for s in filename.split('\\') if 'sub' in s][0].split(
                                        '-')[1] + '_' + study_date
                                series_number = clean_path(
                                    '{series:04d}'.format(series=dataset.SeriesNumber))
                                studyID_and_hash_studyInstanceUID = clean_path('.'.join([dataset.StudyID or 'NA',
                                                                                         hashcode(dataset.StudyInstanceUID)]))

                                path = os.path.join(
                                    patient, dataset.StudyDate, studyID_and_hash_studyInstanceUID, modality, series_number)
                                sorted_filename = '{patient}.{modality}.{series:04d}.{image:04d}.{study_date}.{unique}.dcm'.format(
                                    patient=patient.upper(),
                                    modality=modality,
                                    series=dataset.SeriesNumber,
                                    image=dataset.InstanceNumber,
                                    study_date=dataset.StudyDate,
                                    unique=hashcode(dataset.SOPInstanceUID),
                                )
                        else:
                            if dataset.SeriesDescription.lower() not in {'loc', 'dose report'}:
                                patient = 'P' + \
                                    [s for s in filename.split('\\') if 'sub' in s][0].split(
                                        '-')[1] + '_' + study_date
                                series_number = clean_path(
                                    '{series:04d}'.format(series=dataset.SeriesNumber))
                                studyID_and_hash_studyInstanceUID = clean_path('.'.join([dataset.StudyID or 'NA',
                                                                                         hashcode(dataset.StudyInstanceUID)]))

                                path = os.path.join(
                                    patient, dataset.StudyDate, studyID_and_hash_studyInstanceUID, modality, series_number)
                                sorted_filename = '{patient}.{modality}.{series:04d}.{image:04d}.{study_date}.{unique}.dcm'.format(
                                    patient=patient.upper(),
                                    modality=modality,
                                    series=dataset.SeriesNumber,
                                    image=dataset.InstanceNumber,
                                    study_date=dataset.StudyDate,
                                    unique=hashcode(dataset.SOPInstanceUID),
                                )
                    except Exception as e:
                        errorInfoTemp = "\t".join(['P' + [s for s in filename.split('\\') if 'sub' in s][0].split('-')[1], study_date,
                                                   clean_path('{series:04d}'.format(series=dataset.SeriesNumber)), 'csaReader'])
                        my_file = os.path.join("\\".join(filename.split('\\')[:[i for i, s in enumerate(
                            filename.split('\\')) if 'sub' in s][0]]), 'errorInfo.tsv')
                        write_error_file(my_file, errorInfoTemp)
                        return None

        except Exception as e:
            logger.exception('something wrong with {}'.format(filename))
            logger.exception(e)
            return None

        if 'path' in locals():
            sorted_full_filename = os.path.join(path, sorted_filename)
            return sorted_full_filename
        else:
            return None
