#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Copyright 2019 黎慧剑
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
import os
import copy
import subprocess
import time
from HiveNetLib.base_tools.string_tool import StringTool
from HiveNetLib.base_tools.file_tool import FileTool
from HiveNetLib.base_tools.run_tool import RunTool
from HiveNetLib.prompt_plus import PromptPlus
from HiveNetLib.base_tools.import_tool import ImportTool
from HiveNetLib.simple_i18n import _, SimpleI18N, set_global_i18n
# 根据当前文件路径将包路径纳入，在非安装的情况下可以引用到
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

"""
控制台服务框架模块
@module server
@file server.py
"""

__MOUDLE__ = 'server'  # 模块名
__DESCRIPT__ = u'控制台服务框架模块'  # 模块描述
__VERSION__ = '0.1.0'  # 版本
__AUTHOR__ = u'黎慧剑'  # 作者
__PUBLISH__ = '2019.12.3'  # 发布日期


class ConsoleServer(object):
    """
    控制台服务框架
    """
    #############################
    # 内部变量
    #############################
    _import_object_dict = None  # 登记已经导入的对象字典
    _CMD_HELP_INFO = None
    _CMD_PARA = None

    #############################
    # 构造函数
    #############################

    def __init__(self, config_dict):
        """
        初始化构造函数

        @param {dict} server_config_dict - 服务器的初始化参数字典（console节点）
        """
        # 初始化参数
        self._config_dict = copy.deepcopy(config_dict)

        # 将部分公共参数放到全局变量
        self._console_global_para = RunTool.get_global_var('CONSOLE_GLOBAL_PARA')
        self._console_global_para['name'] = self._config_dict['name']
        self._console_global_para['language'] = self._config_dict['language']
        self._console_global_para['shell_encoding'] = self._config_dict['shell_encoding']  # 控制台编码

        # i18n多语言加载
        _trans_file_path = None
        if self._config_dict['i18n'] == '':
            _trans_file_path = os.path.join(
                self._console_global_para['execute_file_path'], 'i18n/'
            )
        else:
            _trans_file_path = self._config_dict['i18n']
        _i18n_obj = SimpleI18N(
            lang=self._config_dict['language'],
            trans_file_path=_trans_file_path,
            trans_file_prefix='message',
            auto_loads=True
        )
        set_global_i18n(_i18n_obj)

        # 装载默认执行函数
        _temp_dict = self._config_dict['default_dealfun']
        self._default_cmd_dealfun = self._import_and_init_class(
            _temp_dict['module_name'],
            _temp_dict['class_name'],
            _temp_dict['extend_path'],
            _temp_dict['init_para']
        ).cmd_dealfun

        _temp_dict = self._config_dict['on_abort']
        self._on_abort = self._import_and_init_class(
            _temp_dict['module_name'],
            _temp_dict['class_name'],
            _temp_dict['extend_path'],
            _temp_dict['init_para']
        ).cmd_dealfun

        _temp_dict = self._config_dict['on_exit']
        self._on_exit = self._import_and_init_class(
            _temp_dict['module_name'],
            _temp_dict['class_name'],
            _temp_dict['extend_path'],
            _temp_dict['init_para']
        ).cmd_dealfun

        # 遍历参数装载
        self._init_cmd_paras()

        # 加入到CONSOLE_GLOBAL_PARA参数中
        self._console_global_para['CMD_PARA'] = self._CMD_PARA
        self._console_global_para['CMD_HELP_INFO'] = self._CMD_HELP_INFO

        # 控制台启动时的提示语言
        self._CONSOLE_TIPS = StringTool.json_to_object(self._config_dict['start_tips'])

        # 初始化命令行工具对象
        self._prompt = PromptPlus(
            message=self._config_dict['message'],
            default='',  # 默认输入值
            cmd_para=self._CMD_PARA,  # 命令定义参数
            default_dealfun=self._default_cmd_dealfun,  # 默认处理函数
            on_abort=self._on_abort,  # Ctrl + C 取消本次输入执行函数
            on_exit=self._on_exit  # Ctrl + D 关闭命令行执行函数
        )

    #############################
    # 公共函数
    #############################
    def start_console(self):
        """
        启动控制台服务

        @returns {CResult} - 启动结果，result.code：'00000'-成功，'21401'-服务不属于停止状态，不能启动，其他-异常
        """
        _lang = self._console_global_para['language']
        _tips = ''
        # 如果找不到对应的语言，优先找英语，如果再找不到就找第一个
        if _lang in self._CONSOLE_TIPS.keys():
            _tips = self._CONSOLE_TIPS[_lang]
        elif 'en' in self._CONSOLE_TIPS.keys():
            _tips = self._CONSOLE_TIPS['en']
        else:
            _tips = self._CONSOLE_TIPS[self._CONSOLE_TIPS.keys()[0]]

        self._prompt.start_prompt_service(
            tips='\r\n'.join(_tips).replace('{{VERSION}}', self._config_dict['version']),
            is_async=False,
            is_print_async_execute_info=True
        )

    #############################
    # 内部函数
    #############################
    def _import_and_init_class(self, module_name, class_name, extend_path, init_para):
        """
        装载并初始化对象返回（如果对象已存在则直接返回）

        @param {string} module_name - 模块名
        @param {string} class_name - 处理类名
        @param {string} extend_path - 模块所在搜索路径
        @param {string} init_para - 初始化的json字符串

        @return {object} - 初始化后的模块对象

        @throws {ImportError} - 初始化失败返回该异常
        """
        # 检查对象是否已存在
        _key = '%s.%s' % (module_name, class_name)
        if self._import_object_dict is None:
            self._import_object_dict = dict()
        if _key in self._import_object_dict.keys():
            # 已存在，直接返回即可
            return self._import_object_dict[_key]

        # 装载模块
        _class = None
        if ImportTool.check_moudle_imported(module_name):
            # 模块已存在
            _class = ImportTool.get_member_from_moudle(
                ImportTool.get_imported_moudle(module_name),
                class_name
            )
        else:
            # 动态装载模块
            _class = ImportTool.get_member_from_moudle(
                ImportTool.import_module(
                    module_name,
                    extend_path=extend_path
                ),
                class_name
            )

        if _class is None:
            raise ImportError(_("config file error: can't import module: $1!", (_key, )))

        # 初始化对象并返回
        _init_para = dict()
        if init_para != '':
            _init_para = StringTool.json_to_object(init_para)
        self._import_object_dict[_key] = _class(**_init_para)
        return self._import_object_dict[_key]

    def _init_cmd_paras(self):
        """
        初始化控制台参数
        实现self._CMD_HELP_INFO和self._CMD_PARA字典的装载
        """
        if self._CMD_HELP_INFO is None:
            self._CMD_HELP_INFO = dict()
        else:
            self._CMD_HELP_INFO.clear()

        if self._CMD_PARA is None:
            self._CMD_PARA = dict()
        else:
            self._CMD_PARA.clear()

        # 遍历cmd_list进行装载命令参数
        for _item in self._config_dict['cmd_list']:
            try:
                # 帮助信息
                self._CMD_HELP_INFO[_item['command']] = StringTool.json_to_object(_item['help'])
            except Exception as e:
                print('config file cmd [%s] help json string error!' % _item['command'])
                raise e

            try:
                # 命令信息
                self._CMD_PARA[_item['command']] = StringTool.json_to_object(_item['cmd_para'])
            except Exception as e:
                print('config file cmd [%s] cmd_para json string error!' % _item['command'])
                raise e

            # 处理函数
            self._CMD_PARA[_item['command']]['deal_fun'] = self._import_and_init_class(
                _item['module_name'],
                _item['class_name'],
                _item['extend_path'],
                _item['init_para']
            ).cmd_dealfun


if __name__ == '__main__':
    # 当程序自己独立运行时执行的操作
    # 打印版本信息
    print(('模块名：%s  -  %s\n'
           '作者：%s\n'
           '发布日期：%s\n'
           '版本：%s' % (__MOUDLE__, __DESCRIPT__, __AUTHOR__, __PUBLISH__, __VERSION__)))
