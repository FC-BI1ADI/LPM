"""Subclass of AddNewSellerDlg, which is generated by wxFormBuilder."""

import UI
import sqlite3


# Implementing AddNewSellerDlg
class LPMAddNewSellerDlg(UI.AddNewSellerDlg):
    # 类初始化函数
    def __init__(self, parent):
        UI.AddNewSellerDlg.__init__(self, parent)
        # 初始化对话框数据项值
        conn = sqlite3.connect('.\DATA\lpm.db')
        # SQL = "select distinct branch from seller_info"
        SQL = "select distinct dept from seller_info"
        cursor = conn.execute(SQL)
        branch_options = []
        for row in cursor:
            # 剔除数据库中空值
            if row[0] != None and row[0] != '':
                branch_options.append(row[0])
        self.m_choice_branch.SetItems(branch_options)
        conn.close()

    # 点击添加新人员按钮的处理函数
    def addSeller(self, event):
        seller_id = self.m_textCtrl_seller_id.GetValue()
        name = self.m_textCtrl_name.GetValue()
        gender = self.m_choice_gender.GetString(self.m_choice_gender.GetCurrentSelection())
        id_number = self.m_textCtrl_id_number.GetValue()
        email = self.m_textCtrl_email.GetValue()
        cell_phone = self.m_textCtrl_cell_phone.GetValue()
        tel = self.m_textCtrl_tel.GetValue()
        branch = self.m_choice_branch.GetString(self.m_choice_branch.GetCurrentSelection())
        dept = self.m_textCtrl_dept.GetValue()
        post = self.m_textCtrl_dept.GetValue()
        title = self.m_textCtrl_title.GetValue()
        seller_type = self.m_choice_type.GetString(self.m_choice_type.GetCurrentSelection())
        remarks = self.m_textCtrl_remarks.GetValue()
        # 拼接SQL语句
        SQL = "INSERT INTO seller_info " + \
              "(seller_id,name,gender,id_number,email,cell_phone,tel,branch,dept,post,title,seller_type,remarks) " + \
              "valuses (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % \
              (seller_id,name,gender,id_number,email,cell_phone,tel,branch,dept,post,title,seller_type,remarks)
        print(SQL)

    # 点击Cancel按钮的处理函数
    def addSellerDlgCancel(self, event):
        self.Close(True)
