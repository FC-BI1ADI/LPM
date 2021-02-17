# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class AddNewSellerDlg
###########################################################################

class AddNewSellerDlg(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"添加新的人员信息", pos=wx.DefaultPosition,
                           size=wx.Size(800, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)

        bSizer_main = wx.BoxSizer(wx.VERTICAL)

        bSizerInfoInput = wx.BoxSizer(wx.VERTICAL)

        bSizerBaseInfo = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_seller_id = wx.StaticText(self, wx.ID_ANY, u"  人员ID  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_seller_id.Wrap(-1)

        bSizerBaseInfo.Add(self.m_staticText_seller_id, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_seller_id = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerBaseInfo.Add(self.m_textCtrl_seller_id, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_name = wx.StaticText(self, wx.ID_ANY, u"  姓名  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_name.Wrap(-1)

        bSizerBaseInfo.Add(self.m_staticText_name, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerBaseInfo.Add(self.m_textCtrl_name, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_gender = wx.StaticText(self, wx.ID_ANY, u"  性别  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_gender.Wrap(-1)

        bSizerBaseInfo.Add(self.m_staticText_gender, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_genderChoices = [u"男", u"女"]
        self.m_choice_gender = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_genderChoices, 0)
        self.m_choice_gender.SetSelection(0)
        bSizerBaseInfo.Add(self.m_choice_gender, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizerInfoInput.Add(bSizerBaseInfo, 0, wx.EXPAND, 5)

        bSizerIdEmail = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_id_number = wx.StaticText(self, wx.ID_ANY, u"  身份证号  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_id_number.Wrap(-1)

        bSizerIdEmail.Add(self.m_staticText_id_number, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_id_number = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerIdEmail.Add(self.m_textCtrl_id_number, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_email = wx.StaticText(self, wx.ID_ANY, u"  电子邮箱  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_email.Wrap(-1)

        bSizerIdEmail.Add(self.m_staticText_email, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_email = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerIdEmail.Add(self.m_textCtrl_email, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizerInfoInput.Add(bSizerIdEmail, 0, wx.EXPAND, 5)

        bSizerPhone = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_cell_phone = wx.StaticText(self, wx.ID_ANY, u"  移动电话  ", wx.DefaultPosition, wx.DefaultSize,
                                                     0)
        self.m_staticText_cell_phone.Wrap(-1)

        bSizerPhone.Add(self.m_staticText_cell_phone, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_cell_phone = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerPhone.Add(self.m_textCtrl_cell_phone, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_tel = wx.StaticText(self, wx.ID_ANY, u"  办公电话  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_tel.Wrap(-1)

        bSizerPhone.Add(self.m_staticText_tel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_tel = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerPhone.Add(self.m_textCtrl_tel, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizerInfoInput.Add(bSizerPhone, 0, wx.EXPAND, 5)

        bSizerDept = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_branch = wx.StaticText(self, wx.ID_ANY, u"  分支机构  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_branch.Wrap(-1)

        bSizerDept.Add(self.m_staticText_branch, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_branchChoices = []
        self.m_choice_branch = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_branchChoices, 0)
        self.m_choice_branch.SetSelection(0)
        bSizerDept.Add(self.m_choice_branch, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_dept = wx.StaticText(self, wx.ID_ANY, u"  部门  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_dept.Wrap(-1)

        bSizerDept.Add(self.m_staticText_dept, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_dept = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerDept.Add(self.m_textCtrl_dept, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizerInfoInput.Add(bSizerDept, 0, wx.EXPAND, 5)

        bSizerTitle = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_post = wx.StaticText(self, wx.ID_ANY, u"  职位  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_post.Wrap(-1)

        bSizerTitle.Add(self.m_staticText_post, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_post = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerTitle.Add(self.m_textCtrl_post, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_title = wx.StaticText(self, wx.ID_ANY, u"  任命职务  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_title.Wrap(-1)

        bSizerTitle.Add(self.m_staticText_title, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_title = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerTitle.Add(self.m_textCtrl_title, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText_type = wx.StaticText(self, wx.ID_ANY, u"  职能  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_type.Wrap(-1)

        bSizerTitle.Add(self.m_staticText_type, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_typeChoices = [u"销售", u"技术", u"综合"]
        self.m_choice_type = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_typeChoices, 0)
        self.m_choice_type.SetSelection(0)
        bSizerTitle.Add(self.m_choice_type, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizerInfoInput.Add(bSizerTitle, 0, wx.EXPAND, 5)

        bSizerRemarks = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_remarks = wx.StaticText(self, wx.ID_ANY, u"  备注  ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_remarks.Wrap(-1)

        bSizerRemarks.Add(self.m_staticText_remarks, 0, wx.ALL, 5)

        self.m_textCtrl_remarks = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerRemarks.Add(self.m_textCtrl_remarks, 1, wx.ALL | wx.EXPAND, 5)

        bSizerInfoInput.Add(bSizerRemarks, 1, wx.EXPAND, 5)

        bSizerLine = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizerLine.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizerInfoInput.Add(bSizerLine, 0, wx.EXPAND, 5)

        bSizer_main.Add(bSizerInfoInput, 1, wx.EXPAND, 5)

        bSizerButton = wx.BoxSizer(wx.HORIZONTAL)

        bSizerButton.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button_addseller = wx.Button(self, wx.ID_ANY, u"添加新人员", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerButton.Add(self.m_button_addseller, 0, wx.ALL, 5)

        self.m_button_cancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerButton.Add(self.m_button_cancel, 0, wx.ALL, 5)

        bSizer_main.Add(bSizerButton, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_addseller.Bind(wx.EVT_BUTTON, self.addSeller)
        self.m_button_cancel.Bind(wx.EVT_BUTTON, self.addSellerDlgCancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def addSeller(self, event):
        event.Skip()

    def addSellerDlgCancel(self, event):
        event.Skip()


###########################################################################
## Class GoOutRecodeCheckkDlg
###########################################################################

class GoOutRecodeCheckkDlg(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"外出记录单校验", pos=wx.DefaultPosition, size=wx.Size(800, -1),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer_main = wx.BoxSizer(wx.VERTICAL)

        bSizerFilePathSource = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_path_s = StaticText(self, wx.ID_ANY, u"  外出记录单 （原始） ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_path_s.Wrap(-1)

        bSizerFilePathSource.Add(self.m_staticText_path_s
                                 , 0, wx.ALL, 5)

        self.m_textCtrl_path_s = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerFilePathSource.Add(self.m_textCtrl_path_s, 1, wx.ALL, 5)

        self.m_button_select_path_s = wx.Button(self, wx.ID_ANY, u"  打开  ", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerFilePathSource.Add(self.m_button_select_path_s, 0, wx.ALL, 5)

        bSizer_main.Add(bSizerFilePathSource, 1, wx.EXPAND, 5)

        bSizerFilePathDest = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_path_d = wx.StaticText(self, wx.ID_ANY, u"  外出记录单（导出）   ", wx.DefaultPosition, wx.DefaultSize,
                                                 0)
        self.m_staticText_path_d.Wrap(-1)

        bSizerFilePathDest.Add(self.m_staticText_path_d, 0, wx.ALL, 5)

        self.m_textCtrl_path_d = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerFilePathDest.Add(self.m_textCtrl_path_d, 1, wx.ALL, 5)

        self.m_button_select_path_d = wx.Button(self, wx.ID_ANY, u"  打开  ", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerFilePathDest.Add(self.m_button_select_path_d, 0, wx.ALL, 5)

        bSizer_main.Add(bSizerFilePathDest, 1, wx.EXPAND, 5)

        bSizerLine1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizerLine1.Add(self.m_staticline1, 1, wx.ALL, 5)

        bSizer_main.Add(bSizerLine1, 1, wx.EXPAND, 5)

        bSizerProc = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_blank1 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_blank1.Wrap(-1)

        bSizerProc.Add(self.m_staticText_blank1, 0, wx.ALL, 5)

        self.m_gauge_proc = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge_proc.SetValue(0)
        bSizerProc.Add(self.m_gauge_proc, 1, wx.ALL, 5)

        self.m_staticText_proc = wx.StaticText(self, wx.ID_ANY, u"     %", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_proc.Wrap(-1)

        bSizerProc.Add(self.m_staticText_proc, 0, wx.ALL, 5)

        self.m_staticText_blank2 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_blank2.Wrap(-1)

        bSizerProc.Add(self.m_staticText_blank2, 0, wx.ALL, 5)

        bSizer_main.Add(bSizerProc, 1, wx.EXPAND, 5)

        bSizerLine2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizerLine2.Add(self.m_staticline2, 1, wx.ALL, 5)

        bSizer_main.Add(bSizerLine2, 1, wx.EXPAND, 5)

        bSizerButtons = wx.BoxSizer(wx.HORIZONTAL)

        bSizerButtons.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button_check = wx.Button(self, wx.ID_ANY, u"  较验  ", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerButtons.Add(self.m_button_check, 0, wx.ALL, 5)

        self.m_button_cancel = wx.Button(self, wx.ID_ANY, u"  取消  ", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerButtons.Add(self.m_button_cancel, 0, wx.ALL, 5)

        bSizer_main.Add(bSizerButtons, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_select_path_s.Bind(wx.EVT_BUTTON, self.get_source_path)
        self.m_button_select_path_d.Bind(wx.EVT_BUTTON, self.get_dest_path)
        self.m_button_check.Bind(wx.EVT_BUTTON, self.GoOutCheck)
        self.m_button_cancel.Bind(wx.EVT_BUTTON, self.GoOutRecodeCheckDlgCancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def get_source_path(self, event):
        event.Skip()

    def get_dest_path(self, event):
        event.Skip()

    def GoOutCheck(self, event):
        event.Skip()

    def GoOutRecodeCheckDlgCancel(self, event):
        event.Skip()


###########################################################################
## Class SelectStaffDlg
###########################################################################

class SelectStaffDlg(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(600, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizerMain = wx.BoxSizer(wx.VERTICAL)

        bSizerListArea = wx.BoxSizer(wx.HORIZONTAL)

        m_listBoxStaffChoices = []
        self.m_listBoxStaff = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxStaffChoices, 0)
        bSizerListArea.Add(self.m_listBoxStaff, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"选择 >>>", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerListArea.Add(self.m_button9, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        m_listBoxSelectChoices = []
        self.m_listBoxSelect = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxSelectChoices,
                                          0)
        bSizerListArea.Add(self.m_listBoxSelect, 1, wx.ALL | wx.EXPAND, 5)

        bSizerMain.Add(bSizerListArea, 1, wx.EXPAND, 5)

        bSizerBottomArea = wx.BoxSizer(wx.VERTICAL)

        bSizerButtonArea = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_submit = wx.Button(self, wx.ID_ANY, u"提交", wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizerButtonArea.Add(self.m_button_submit, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        bSizerButtonArea.Add(self.m_button_submit, 0, wx.ALL, 5)

        self.m_button_cancel = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizerButtonArea.Add(self.m_button_cancel, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        bSizerButtonArea.Add(self.m_button_cancel, 0, wx.ALL, 5)

        # bSizerBottomArea.Add(bSizerButtonArea, 1, wx.EXPAND | wx.ALIGN_RIGHT, 5)
        bSizerBottomArea.Add(bSizerButtonArea, 1, wx.EXPAND, 5)

        bSizerMain.Add(bSizerBottomArea, 1, wx.BOTTOM, 5)

        self.SetSizer(bSizerMain)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
