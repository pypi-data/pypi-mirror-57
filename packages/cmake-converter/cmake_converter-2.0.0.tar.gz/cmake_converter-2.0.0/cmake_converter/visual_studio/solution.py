#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2019:
#   Matthieu Estrada, ttamalfor@gmail.com
#   Pavel Liavonau, liavonlida@gmail.com
#
# This file is part of (CMakeConverter).
#
# (CMakeConverter) is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# (CMakeConverter) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with (CMakeConverter).  If not, see <http://www.gnu.org/licenses/>.

"""
Module of Visual Studio solution related logic for converting.
"""

import re
import os
import shutil
from collections import OrderedDict

from cmake_converter.data_converter import DataConverter
from cmake_converter.context_initializer import ContextInitializer
from cmake_converter.utils import message


class VSSolutionConverter(DataConverter):
    """
    Implementation of Converter for Visual Studio solution
    """
    def parse_solution(self, root_context, sln_text):
        """
        Parse given solution
        :param root_context: context from input file
        :type root_context: Context
        :param sln_text: full solution text
        :type sln_text: str
        :return: data from solution
        :rtype: dict
        """

        solution_data = {}
        projects_data = OrderedDict()
        solution_folders = {}

        self.__check_solution_version(root_context, sln_text)

        self.__parse_projects_data(sln_text, solution_folders, projects_data)

        self.__parse_configurations_of_solution(root_context, sln_text, solution_data)

        self.__parse_project_configuration_platforms(sln_text, projects_data)

        solution_folders_map = {}

        self.__parse_nested_projects_in_solution_folders(sln_text, solution_folders_map)

        self.set_solution_dirs_to_projects(projects_data, solution_folders_map, solution_folders)

        # replace GUIDs with Project names in dependencies
        for project_guid in projects_data:
            project_data = projects_data[project_guid]
            if 'sln_deps' in project_data:
                target_deps = []
                dependencies_list = project_data['sln_deps']
                for dep_guid in dependencies_list:
                    dep = projects_data[dep_guid]
                    target_deps.append(dep['name'])
                project_data['sln_deps'] = target_deps
        solution_data['projects_data'] = projects_data

        return solution_data

    @staticmethod
    def __check_solution_version(root_context, sln_text):
        version_pattern = re.compile(
            r'Microsoft Visual Studio Solution File, Format Version (.*)'
        )
        version_match = version_pattern.findall(sln_text)
        if not version_match or float(version_match[0]) < 9:
            message(root_context, 'Solution files with versions below 9.00 are not supported.'
                                  ' Version {} found. Upgrade you solution and try again, please'
                    .format(version_match[0]), 'error')
            exit(1)

        message(root_context, 'Version of solution is {}'.format(version_match[0]), '')

    @staticmethod
    def __parse_projects_data(sln_text, solution_folders, projects_data):
        """
        Parse section with information about project at *.sln file

        :param sln_text:
        :param solution_folders:
        :param projects_data:
        :return:
        """
        p = re.compile(
            r'(Project.*\s=\s\"(.*)\",\s\"(.*)\",.*({.*\})(?:.|\n)*?EndProject(?!Section))'
        )

        for project_data_match in p.findall(sln_text):
            path = project_data_match[2]
            guid = project_data_match[3]

            _, ext = os.path.splitext(os.path.basename(path))

            if 'proj' not in ext:
                solution_folders[guid] = path
                continue

            projects_data[guid] = VSSolutionConverter.__parse_project_data(project_data_match, path)

    @staticmethod
    def __parse_project_data(project_data_match, path):
        """
        Parse project section at *.sln file

        :param project_data_match:
        :param path:
        :return:
        """
        project = dict()
        project['name'] = project_data_match[1]
        project['path'] = path
        if 'ProjectDependencies' in project_data_match[0]:
            project['sln_deps'] = []
            dependencies_section = re.compile(
                r'ProjectSection\(ProjectDependencies\) = '
                r'postProject(?:.|\n)*?EndProjectSection'
            )
            dep_data = dependencies_section.findall(project_data_match[0])
            dependencies_guids = re.compile(r'(({.*\}) = ({.*\}))')
            guids_deps_matches = dependencies_guids.findall(dep_data[0])
            for guids_deps_match in guids_deps_matches:
                project['sln_deps'].append(guids_deps_match[2])
        return project

    @staticmethod
    def __parse_configurations_of_solution(root_context, sln_text, solution_data):
        solution_configurations_re = re.compile(
            r'GlobalSection\(SolutionConfigurationPlatforms\) = '
            r'preSolution((?:.|\n)*?)EndGlobalSection'
        )

        solution_configurations_matches = solution_configurations_re.findall(sln_text)
        solution_data['sln_configurations'] = []
        sln_configuration_re = re.compile(r'([\w |]+) = ([\w |]+)')
        for solution_configuration_match in solution_configurations_matches:
            configurations = sln_configuration_re.findall(solution_configuration_match)
            for configuration in configurations:
                solution_data['sln_configurations'].append(configuration[0])
                arch = configuration[0].split('|')[1]
                if arch == 'x86':
                    message(
                        root_context,
                        'Solution architecture is x86 and may be mapped onto Win32 at projects.'
                        'To avoid problems rename x86 -> Win32.',
                        'warn')
                root_context.supported_architectures.add(arch)

    @staticmethod
    def __parse_project_configuration_platforms(sln_text, projects_data):
        projects_configurations_re = re.compile(
            r'GlobalSection\(ProjectConfigurationPlatforms\) = '
            r'postSolution((?:.|\n)*?)EndGlobalSection'
        )
        projects_configurations_matches = projects_configurations_re.findall(sln_text)
        projects_configuration_re = re.compile(r'({.+\})\.([\w |]+)\.ActiveCfg = ([\w |]+)')
        for projects_configuration_match in projects_configurations_matches:
            configurations = projects_configuration_re.findall(projects_configuration_match)
            for configuration in configurations:
                p = projects_data[configuration[0]]
                if 'sln_configs_2_project_configs' not in p:
                    p['sln_configs_2_project_configs'] = OrderedDict({(None, None): (None, None)})
                p['sln_configs_2_project_configs'][tuple(configuration[1].split('|'))] = \
                    tuple(configuration[2].split('|'))

    @staticmethod
    def __parse_nested_projects_in_solution_folders(sln_text, solution_folders_map):
        nested_projects_re = re.compile(
            r'GlobalSection\(NestedProjects\) = preSolution((?:.|\n)*?)EndGlobalSection'
        )
        nested_projects_matches = nested_projects_re.findall(sln_text)
        solution_dir_link_re = re.compile(r'(\{.+\}) = (\{.+\})')
        for nested_projects_match in nested_projects_matches:
            solution_dir_links = solution_dir_link_re.findall(nested_projects_match)
            for solution_dir_link in solution_dir_links:
                solution_folders_map[solution_dir_link[0]] = solution_dir_link[1]

    @staticmethod
    def set_solution_dirs_to_projects(projects_data, solution_folders_map, solution_folders):
        """ Evaluate locations of projects in Solution explorer tree of Visual Studio UI """
        for project_guid in projects_data:
            project_solution_dir = ''

            if project_guid in solution_folders_map:
                guid = project_guid
                while guid in solution_folders_map:
                    if project_solution_dir:
                        project_solution_dir = '/' + project_solution_dir
                    project_solution_dir = solution_folders[solution_folders_map[guid]]\
                        + project_solution_dir
                    guid = solution_folders_map[guid]

            projects_data[project_guid]['project_solution_dir'] = project_solution_dir

    @staticmethod
    def set_dependencies_for_project(context, project_data):
        """ Copy dependencies on other solution projects into project context """
        if 'sln_deps' not in project_data:
            return

        context.sln_deps = project_data['sln_deps']

    @staticmethod
    def clean_cmake_lists_file(context, subdirectory, cmake_lists_set):
        """ Clean previous CMake script before converting """
        cmake_path_to_clean = \
            ContextInitializer.set_cmake_lists_path(context, subdirectory) + '/CMakeLists.txt'
        if context.dry:
            return

        if cmake_path_to_clean in cmake_lists_set:
            return
        cmake_lists_set.add(cmake_path_to_clean)

        if os.path.exists(cmake_path_to_clean):
            os.remove(cmake_path_to_clean)
            message(context, 'removed {}'.format(cmake_path_to_clean), '')
        else:
            message(context, 'not found {}'.format(cmake_path_to_clean), 'warn')

    def clean_cmake_lists_of_solution(self, context, projects_data):
        """ Clean previous set of CMake scripts before converting """
        if not os.path.exists(os.path.join(context.solution_path, 'CMake')):
            return  # first run

        message(context, 'Cleaning CMake Scripts', '')
        cmake_lists_set = set()
        for guid in projects_data:
            project_path = projects_data[guid]['path']
            project_path = '/'.join(project_path.split('\\'))
            project_abs = os.path.join(context.solution_path, project_path)
            subdirectory = os.path.dirname(project_abs)
            self.clean_cmake_lists_file(context, subdirectory, cmake_lists_set)

        self.clean_cmake_lists_file(context, context.solution_path, cmake_lists_set)
        print('\n')

    def convert_solution(self, root_context, sln_file_path):
        """
        Routine converts Visual studio solution into set of CMakeLists.txt scripts
        """
        with open(sln_file_path, encoding='utf8') as sln:
            solution_data = self.parse_solution(root_context, sln.read())

        root_context.solution_path = os.path.dirname(sln_file_path)
        subdirectories_set = set()
        subdirectories_to_project_name = {}
        projects_data = solution_data['projects_data']

        self.clean_cmake_lists_of_solution(root_context, projects_data)

        input_data_for_converter = self.__get_input_data_for_converter(
            root_context,
            projects_data
        )

        results = self.do_conversion(root_context, input_data_for_converter)

        self.__get_info_from_results(
            root_context,
            results,
            subdirectories_set,
            subdirectories_to_project_name
        )

        configuration_types_list = self.__get_global_configuration_types(solution_data)

        self.write_root_cmake_file(
            root_context,
            configuration_types_list,
            subdirectories_set,
            subdirectories_to_project_name
        )

    def __get_input_data_for_converter(self, root_context, projects_data):
        input_data_for_converter = {}
        project_number = 0
        projects_filter_pattern = re.compile(root_context.projects_regexp)
        for guid in projects_data:
            project_number += 1
            project_context = root_context.clone()
            project_context.project_number = project_number
            project_path = projects_data[guid]['path']

            m = projects_filter_pattern.match(project_path)
            if m is None:
                continue

            project_path = '/'.join(project_path.split('\\'))
            project_abs = os.path.join(root_context.solution_path, project_path)
            subdirectory = os.path.dirname(project_abs)
            self.set_dependencies_for_project(project_context, projects_data[guid])
            project_context.sln_configurations_map = \
                projects_data[guid]['sln_configs_2_project_configs']
            project_context.solution_folder = projects_data[guid]['project_solution_dir']
            if subdirectory not in input_data_for_converter:
                input_data_for_converter[subdirectory] = []
            input_data_for_converter[subdirectory].append(
                {
                    'project_context': project_context,
                    'project_abs': project_abs,
                    'subdirectory': subdirectory
                }
            )

        return input_data_for_converter

    @staticmethod
    def __get_info_from_results(
            root_context,
            results,
            subdirectories_set,
            subdirectories_to_project_name
    ):
        for directory_results in results:
            for project_result in directory_results:
                subdirectory = os.path.relpath(project_result['cmake'], root_context.solution_path)
                if subdirectory != '.':
                    subdirectories_set.add(subdirectory)
                subdirectories_to_project_name[subdirectory] = project_result['project_name']
                root_context.solution_languages.update(project_result['solution_languages'])
                if root_context.target_windows_version and \
                        project_result['target_windows_ver'] and \
                        root_context.target_windows_version != project_result['target_windows_ver']:
                    message(
                        root_context,
                        'CMake does not support more than 1 version of windows SDK', 'warn'
                    )
                if project_result['target_windows_ver']:
                    root_context.target_windows_version = project_result['target_windows_ver']
                root_context.warnings_count += project_result['warnings_count']

    @staticmethod
    def __get_global_configuration_types(solution_data):
        configuration_types_set = set()
        for config in solution_data['sln_configurations']:
            configuration_types_set.add(config.split('|')[0])
        configuration_types_list = list(configuration_types_set)
        configuration_types_list.sort(key=str.lower)
        return configuration_types_list

    def copy_cmake_utils(self, cmake_lists_path):
        super(VSSolutionConverter, self).copy_cmake_utils(cmake_lists_path)

        utils_path = os.path.join(cmake_lists_path, 'CMake')
        if not os.path.exists(utils_path):
            os.makedirs(utils_path)
        src_dir = os.path.dirname(os.path.abspath(__file__))
        shutil.copyfile(os.path.join(src_dir, 'Default.cmake'), utils_path + '/Default.cmake')
        shutil.copyfile(os.path.join(src_dir, 'DefaultCXX.cmake'),
                        utils_path + '/DefaultCXX.cmake')
        shutil.copyfile(os.path.join(src_dir, 'DefaultFortran.cmake'),
                        utils_path + '/DefaultFortran.cmake')
