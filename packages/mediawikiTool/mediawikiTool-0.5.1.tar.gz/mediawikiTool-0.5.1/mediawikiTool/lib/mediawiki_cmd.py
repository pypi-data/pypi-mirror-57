#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Copyright 2019 黎慧剑
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
mediawiki工具命令模块
@module mediawiki_cmd
@file mediawiki_cmd.py
"""

import os
import sys
import re
import shutil
import requests
import traceback
import platform
import subprocess
import time
try:
    import chardet
except:
    pass
from HiveNetLib.base_tools.run_tool import RunTool
from HiveNetLib.prompt_plus import PromptPlus
from HiveNetLib.base_tools.file_tool import FileTool
from HiveNetLib.base_tools.string_tool import StringTool
from HiveNetLib.simple_i18n import _
# 根据当前文件路径将包路径纳入，在非安装的情况下可以引用到
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
from mediawikiTool.lib.base_cmd import CmdBaseFW


__MOUDLE__ = 'mediawiki_cmd'  # 模块名
__DESCRIPT__ = u'mediawiki工具命令模块'  # 模块描述
__VERSION__ = '0.1.0'  # 版本
__AUTHOR__ = u'黎慧剑'  # 作者
__PUBLISH__ = '2019.12.09'  # 发布日期


class MediaWikiCmd(CmdBaseFW):
    """
    通用命令处理
    支持help、syscmd命令
    """
    #############################
    # 构造函数，在里面增加函数映射字典
    #############################

    def _init(self, **kwargs):
        """
        实现类需要覆盖实现的初始化函数

        @param {kwargs} - 传入初始化参数字典（config.xml的init_para字典）

        @throws {exception-type} - 如果初始化异常应抛出异常
        """
        self._CMD_DEALFUN_DICT = {
            'mdtowiki': self._mdtowiki_cmd_dealfun,
            'docxtowiki': self._docxtowiki_cmd_dealfun,
            'filestowiki': self._filestowiki_cmd_dealfun
        }
        self._console_global_para = RunTool.get_global_var('CONSOLE_GLOBAL_PARA')

    #############################
    # 实际处理函数
    #############################
    def _cmd_dealfun(self, message='', cmd='', cmd_para='', **kwargs):
        """
        通用处理函数，通过cmd区别调用实际的处理函数

        @param {string} message='' - prompt提示信息
        @param {string} cmd - 执行的命令key值
        @param {string} cmd_para - 传入的命令参数（命令后的字符串，去掉第一个空格）
        @param {kwargs} - 传入的主进程的初始化kwargs对象

        @return {string|iter_string} - 执行命令完成后要输到屏幕的内容，可以是iter对象（yield返回）
            注：如果是on_abort和on_exit可以返回CResult对象
        """
        # 获取真实执行的函数
        _real_dealfun = None  # 真实调用的函数
        if 'ignore_case' in kwargs.keys() and kwargs['ignore_case']:
            # 区分大小写
            if cmd in self._CMD_DEALFUN_DICT.keys():
                _real_dealfun = self._CMD_DEALFUN_DICT[cmd]
        else:
            # 不区分大小写
            if cmd.lower() in self._CMD_DEALFUN_DICT.keys():
                _real_dealfun = self._CMD_DEALFUN_DICT[cmd.lower()]

        # 执行函数
        if _real_dealfun is not None:
            return _real_dealfun(message=message, cmd=cmd, cmd_para=cmd_para, **kwargs)
        else:
            return _("'$1' is not support command!", (cmd, ))

    #############################
    # 实际处理函数
    #############################
    def _mdtowiki_cmd_dealfun(self, message='', cmd='', cmd_para='', **kwargs):
        """
        将markdown格式文件转换为mediawiki格式

        @param {string} message='' - prompt提示信息
        @param {string} cmd - 执行的命令key值
        @param {string} cmd_para - 传入的命令参数（命令后的字符串，去掉第一个空格）

        @return {string} - 执行命令完成后要输到屏幕的内容
        """
        try:
            if not self._para_dict_check(cmd=cmd, cmd_para=cmd_para):
                return ''

            # 展示处理信息
            print(
                '%s ( %s ):' % (
                    _('convert info'),
                    _('change stander pic name' if self._para_dict['stdpic']
                      else 'use source pic name')
                )
            )
            print('  %s: %s' % (_('source file'), self._para_dict['in']))
            print('  %s: %s' % (_('out path'), self._para_dict['out']))
            print('  %s: %s' % (_('wiki page title'), self._para_dict['name']))
            print('  %s: %s' % (_('copy pic path'), self._para_dict['pic_dir']))
            print('')
            print('%s  =================>' % (_('begin convert'), ))
            print('')

            # 删除原有复制图片
            self._create_pic_dir()

            # 预处理markdown文件
            print('\r\n%s %s: ' % (_('begin'), _('copy pic file')))
            _md_text = FileTool.get_file_text(self._para_dict['in'], encoding=None)
            _temp_text = re.sub(
                r'!\[.*?\]\(.*?\)|\<img .*? /\>',
                self._deal_md_pic,
                _md_text
            )
            print('%s %s' % (_('copy pic file'), _('done')))
            with open(
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '_temp.md'),
                "w", encoding='utf-8'
            ) as f:
                f.write(_temp_text)
            print('\r\n%s %s' % (_('pre convert to temp file'), _('done')))

            # 调用Pandoc进行转换处理
            print('%s:' % (_('use Pandoc convert'), ))
            if platform.system() == 'Windows':
                # Win平台要先执行chcp 65001命令
                _sys_cmd = 'chcp 65001'
                self._console_global_para['shell_encoding'] = 'utf-8'
                print('%s: %s' % (_('execute'), _sys_cmd))
                if(self._exe_syscmd(_sys_cmd, shell_encoding='utf-8') != 0):
                    return ''

            # 执行转换命令
            _sys_cmd = 'pandoc %s -f markdown -t mediawiki -s -o %s' % (
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '_temp.md'),
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '.txt')
            )
            print('%s: %s' % (_('execute'), _sys_cmd))
            if(self._exe_syscmd(_sys_cmd, shell_encoding='utf-8') != 0):
                return ''

            # 删除临时文件
            FileTool.remove_file(os.path.join(
                self._para_dict['out'], self._para_dict['name'] + '_temp.md'))

            print('\r\n=================>  %s %s' % (_('convert'), _('done')))
        except Exception as e:
            _prin_str = '%s (%s):\r\n%s' % (
                _('execution exception'), str(e), traceback.format_exc()
            )
            print(_prin_str)

        # 结束
        return ''

    def _docxtowiki_cmd_dealfun(self, message='', cmd='', cmd_para='', **kwargs):
        """
        将docx格式文件转换为mediawiki格式

        @param {string} message='' - prompt提示信息
        @param {string} cmd - 执行的命令key值
        @param {string} cmd_para - 传入的命令参数（命令后的字符串，去掉第一个空格）

        @return {string} - 执行命令完成后要输到屏幕的内容
        """
        try:
            if not self._para_dict_check(cmd=cmd, cmd_para=cmd_para):
                return ''

            self._para_dict['stdpic'] = True

            # 展示处理信息
            print(
                '%s:' % (
                    _('convert info')
                )
            )
            print('  %s: %s' % (_('source file'), self._para_dict['in']))
            print('  %s: %s' % (_('out path'), self._para_dict['out']))
            print('  %s: %s' % (_('wiki page title'), self._para_dict['name']))
            print('  %s: %s' % (_('copy pic path'), self._para_dict['pic_dir']))
            print('')
            print('%s  =================>' % (_('begin convert'), ))
            print('')

            # 删除原有复制图片
            self._create_pic_dir()

            # 先将docx转换为md
            print('%s: ' % (_('change docx file to markdown'), ))
            if platform.system() == 'Windows':
                # Win平台要先执行chcp 65001命令
                _sys_cmd = 'chcp 65001'
                self._console_global_para['shell_encoding'] = 'utf-8'
                print('%s: %s' % (_('execute'), _sys_cmd))
                if(self._exe_syscmd(_sys_cmd, shell_encoding='utf-8') != 0):
                    return ''

            _sys_cmd = 'pandoc %s -f docx -t markdown -s -o %s --extract-media=%s' % (
                self._para_dict['in'],
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '_temp.md'),
                self._para_dict['pic_dir']
            )
            print('%s: %s' % (_('execute'), _sys_cmd))
            if(self._exe_syscmd(_sys_cmd, shell_encoding='utf-8') != 0):
                return ''

            # 预处理markdown文件
            print('\r\n%s %s: ' % (_('begin'), _('begin copy pic file')))
            _md_text = FileTool.get_file_text(os.path.join(
                self._para_dict['out'], self._para_dict['name'] + '_temp.md'), encoding=None)
            _temp_text = re.sub(
                r'(!\[.*?\]\(.*?\)|\<img .*? /\>)(\{[width=|height=][\s\S]*?\})*',
                self._deal_md_pic,
                _md_text
            )

            print('%s %s' % (_('copy pic file'), _('done')))
            with open(
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '_temp.md'),
                "w", encoding='utf-8'
            ) as f:
                f.write(_temp_text)
            print('\r\n%s %s' % (_('pre convert to temp file'), _('done')))

            # 调用Pandoc进行转换处理
            print('\r\n%s:' % (_('use Pandoc convert'), ))

            # 执行转换命令
            _sys_cmd = 'pandoc %s -f markdown -t mediawiki -s -o %s' % (
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '_temp.md'),
                os.path.join(self._para_dict['out'], self._para_dict['name'] + '.txt')
            )
            print('%s: %s' % (_('execute'), _sys_cmd))
            if(self._exe_syscmd(_sys_cmd, shell_encoding='utf-8') != 0):
                return ''

            # 删除临时文件
            FileTool.remove_file(os.path.join(
                self._para_dict['out'], self._para_dict['name'] + '_temp.md'))
            FileTool.remove_dir(os.path.join(self._para_dict['pic_dir'], 'media'))

            print('\r\n=================>  %s %s' % (_('convert'), _('done')))
        except Exception as e:
            _prin_str = '%s (%s):\r\n%s' % (
                _('execution exception'), str(e), traceback.format_exc()
            )
            print(_prin_str)

        # 结束
        return ''

    def _filestowiki_cmd_dealfun(self, message='', cmd='', cmd_para='', **kwargs):
        """
        将指定目录下的文件批量转换为mediawiki格式

        @param {string} message='' - prompt提示信息
        @param {string} cmd - 执行的命令key值
        @param {string} cmd_para - 传入的命令参数（命令后的字符串，去掉第一个空格）

        @return {string} - 执行命令完成后要输到屏幕的内容
        """
        try:
            # 获取参数及处理参数
            _cmd_list = PromptPlus.get_cmd_para_list(cmd_para)
            _in = ''
            _out = ''
            _stdpic = False
            for _item in _cmd_list:
                if '-in' == _item[0]:
                    _in = _item[1].strip("'")
                elif '-out' == _item[0]:
                    _out = _item[1].strip("'")
                elif '-stdpic' == _item[0]:
                    _stdpic = True

            if _in == '':
                _in = self._console_global_para['work_path']
            else:
                if not os.path.exists(_in) or not os.path.isdir(_in):
                    print(_("Path '$1' not exists, please check [-in] para!", _in))
                    return ''
                _in = os.path.realpath(_in)
            if _out == '':
                _out = self._console_global_para['work_path']
            else:
                if not os.path.exists(_out):
                    # 创建对应目录
                    FileTool.create_dir(_out)
                _out = os.path.realpath(_out)

            # 遍历文件并进行处理
            print(_("begin convert files in $1", _in) + ' =======================>')
            print('')
            _file_list = FileTool.get_filelist(path=_in, is_fullname=True)
            for _file in _file_list:
                _ext = FileTool.get_file_ext(_file)
                if _ext == 'md':
                    print('%s: %s' % (_('convert'), _file))
                    self._mdtowiki_cmd_dealfun(
                        message=message, cmd='mdtowiki',
                        cmd_para="-in '%s' -out '%s'%s" % (
                            _file, _out, ' -stdpic' if _stdpic else ''
                        ),
                        **kwargs
                    )
                elif _ext == 'docx':
                    print('%s: %s' % (_('convert'), _file))
                    self._docxtowiki_cmd_dealfun(
                        message=message, cmd='docxtowiki',
                        cmd_para="-in '%s' -out '%s'" % (
                            _file, _out
                        ),
                        **kwargs
                    )
                else:
                    print('%s: %s' % (_('not support file format'), _file))

            # 处理完成
            print('\r\n=======================>  %s %s' % (_('convert files'), _('done')))
        except Exception as e:
            _prin_str = '%s (%s):\r\n%s' % (
                _('execution exception'), str(e), traceback.format_exc()
            )
            print(_prin_str)

        # 结束
        return ''

    #############################
    # 内部函数
    #############################
    def _para_dict_check(self, cmd='', cmd_para=''):
        """
        检查并生成

        @param {string} cmd - 执行的命令key值
        @param {string} cmd_para - 传入的命令参数（命令后的字符串，去掉第一个空格）

        @return {string} - 如果返回空字符串代表成功，有值的字符串代表失败
        """
        # 获取命令执行参数
        _cmd_list = PromptPlus.get_cmd_para_list(cmd_para)
        self._para_dict = {
            'in': '',
            'out': '',
            'name': '',
            'stdpic': False,
            'pic_dir': '',
            'pic_list': {},
            'pic_num': 0
        }
        for _item in _cmd_list:
            if '-in' == _item[0]:
                self._para_dict['in'] = _item[1].strip("'")
            elif '-out' == _item[0]:
                self._para_dict['out'] = _item[1].strip("'")
            elif '-name' == _item[0]:
                self._para_dict['name'] = _item[1].strip("'")
            elif '-stdpic' == _item[0]:
                self._para_dict['stdpic'] = True

        # 参数检查及初始化
        if self._para_dict['in'] == '' or not os.path.exists(self._para_dict['in']) or not os.path.isfile(self._para_dict['in']):
            # 输入文件不存在
            print(_('File \'$1\' not exists, please check [-in] para!', self._para_dict['in']))
            return False

        self._para_dict['in'] = os.path.realpath(self._para_dict['in'])  # 获取全路径
        self._para_dict['in_dir'] = FileTool.get_file_path(self._para_dict['in'])

        if self._para_dict['out'] == '':
            self._para_dict['out'] = self._console_global_para['work_path']  # 使用工作路径
        else:
            if not os.path.exists(self._para_dict['out']):
                # 创建对应目录
                FileTool.create_dir(self._para_dict['out'])
            self._para_dict['out'] = os.path.realpath(self._para_dict['out'])

        if self._para_dict['name'] == '':
            self._para_dict['name'] = FileTool.get_file_name_no_ext(self._para_dict['in'])

        self._para_dict['pic_dir'] = os.path.join(
            self._para_dict['out'], self._para_dict['name'] + '_copy_pic')

        return True

    def _deal_md_pic(self, match_str):
        """
        针对获取到的md图片路径字符串进行文件处理和替换

        @param {re.Match} match_str - 匹配到的对象

        @return {string} - 替换后的图片字符串
        """
        _str = match_str.group()
        # 提取图片路径信息
        _alt = ''
        _src = ''
        _name = ''
        if _str.startswith('!['):
            # ![img004](mdtowiki_pic/img004.png)的格式
            _p_alt = re.compile(r'!\[(.*?)\]')
            _p_src = re.compile(r'\((.*?)\)')
            _alt = re.findall(_p_alt, _str)[0]
            _src = re.findall(_p_src, _str)[0]
        else:
            # <img src="https://yt-adp.ws.126.net/channel4/1200125_pads_20190404.jpg" alt="163" style="zoom:33%;" />的格式
            _p_alt = re.compile(r'\salt=(.*?)\s')
            _p_src = re.compile(r'\ssrc=(.*?)\s')
            _temp = re.findall(_p_alt, _str)
            if len(_temp) > 0:
                _alt = _temp[0].strip('\'"')
            _temp = re.findall(_p_src, _str)
            if len(_temp) > 0:
                _src = _temp[0].strip('\'"')

        # 检查文件是否已经处理过
        if _src in self._para_dict['pic_list']:
            _name = self._para_dict['pic_list'][_src]
            print('%s: %s -> %s %s' % (_('copy pic file'), _src, _name, _('done')))
        else:
            # 未处理过
            if self._para_dict['stdpic']:
                # 按顺序命名
                self._para_dict['pic_num'] = self._para_dict['pic_num'] + 1
                _name = '%s_%s_%s.%s' % (
                    self._para_dict['name'], _('embed'),
                    StringTool.fill_fix_string(str(self._para_dict['pic_num']), 5, '0'),
                    FileTool.get_file_ext(_src)
                )
            else:
                # 使用原名称
                _temp_str = _src.replace('\\', '/').replace(' ', '_')
                _index = _temp_str.rfind("/")
                if _index == -1:
                    _name = _temp_str
                else:
                    _name = _temp_str[_index + 1:]

                _name = '%s_%s_%s' % (
                    self._para_dict['name'], _('embed'), _name
                )

            # 加入到清单中
            self._para_dict['pic_list'][_src] = _name

            # 复制或下载文件
            try:
                self._down_md_pic(_src, os.path.join(self._para_dict['pic_dir'], _name))
                print('%s: %s -> %s %s' % (_('copy pic file'), _src, _name, _('done')))
            except Exception as e:
                # 提示
                print(
                    '%s: %s -> %s %s ( %s ):\r\n %s' % (
                        _('copy pic file'), _src, _name, _('execution exception'), str(e),
                        traceback.format_exc()
                    )
                )

        # 改写文件
        if _alt == '':
            return '[[Image:%s]]' % (_name, )
        else:
            return '[[Image:%s|%s]]' % (_name, _alt)

    def _down_md_pic(self, src, dest):
        """
        将图片文件下载到指定路径

        @param {string} src - 要下载的文件路径
        @param {string} dest - 目标文件
        """
        if src.startswith('http://') or src.startswith('https://'):
            # 网络图片，需要下载
            _resp = requests.get(src)
            with open(dest, "wb") as f:
                f.write(_resp.content)
        else:
            # 本地文件，进行复制
            _src_file = os.path.join(self._para_dict['in_dir'], src)
            shutil.copyfile(_src_file, dest)

    def _exe_syscmd(self, cmd, shell_encoding='utf-8'):
        """
        执行系统命令

        @param {string} cmd - 要执行的命令
        @param {string} shell_encoding='utf-8' - 界面编码

        @return {int} - 返回执行结果
        """
        _sp = subprocess.Popen(
            cmd, close_fds=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            shell=True
        )
        # 循环等待执行完成
        _exit_code = None
        try:
            while True:
                try:
                    # 打印内容
                    _show_str = _sp.stdout.readline().decode(shell_encoding).strip()
                    if _show_str != '':
                        print(_show_str)

                    _exit_code = _sp.poll()
                    if _exit_code is not None:
                        # 结束，打印异常日志
                        _show_str = _sp.stdout.read().decode(shell_encoding).strip()
                        if _show_str != '':
                            print(_show_str)
                        if _exit_code != 0:
                            _show_str = _sp.stderr.read().decode(shell_encoding).strip()
                            if _show_str != '':
                                print(_show_str)
                        break
                    # 释放一下CPU
                    time.sleep(0.01)
                except KeyboardInterrupt:
                    # 不允许取消
                    print(_("Command Executing, can't exit execute job!"))
        except KeyboardInterrupt:
            # 遇到 Ctrl + C 退出
            pass

        # 最后返回
        if _exit_code is not None:
            if _exit_code != 0:
                # 执行错误，显示异常
                print('%s : %d' % (_("Command done, exit code"), _exit_code))
            else:
                print('%s' % (_("Command execute done"), ))

        return _exit_code

    def _create_pic_dir(self):
        """
        新建或删除图片复制目录
        """
        if os.path.exists(self._para_dict['pic_dir']):
            FileTool.remove_files(path=os.path.join(
                self._para_dict['out'], self._para_dict['name'] + '_copy_pic'))
        else:
            # 创建目录
            FileTool.create_dir(self._para_dict['pic_dir'])

        print('%s %s' % (_('make pic path'), _('done')))


if __name__ == '__main__':
    # 当程序自己独立运行时执行的操作
    # 打印版本信息
    print(('模块名：%s  -  %s\n'
           '作者：%s\n'
           '发布日期：%s\n'
           '版本：%s' % (__MOUDLE__, __DESCRIPT__, __AUTHOR__, __PUBLISH__, __VERSION__)))
