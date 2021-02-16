import wx
import wx.html2
import UI
from LPMAddNewSellerDlg import LPMAddNewSellerDlg
from LPMGoOutRecodeCheckkDlg import LPMGoOutRecodeCheckkDlg
import sqlite3
import pandas as pd
import os
import openpyxl
import comm

# 程序规范写法统一设置：
mainFrameSize = (1024, 768)
defaultSubFrameSize = (800, 600)
# 报表显示格式控制统一设置
df_style = '''
<style type="text/css">
table.gridtable {
    font-size:14px;
    color:#333333;
    border-width: 1px;
    border-color: #666666;
    border-collapse: collapse;
}
table.gridtable th {
    border-width: 1px;
    padding: 4px;
    border-style: solid;
    border-color: #666666;
    background-color: #dedede;
}
table.gridtable td {
    border-width: 1px;
    padding: 4px;
    border-style: solid;
    border-color: #666666;
    background-color: #ffffff;
}
</style>
'''


# 主窗口类定义
class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        # 创建panel
        pnl = wx.Panel(self)

        # 创建布局器，并将panel设置为布局器
        sizer = wx.BoxSizer(wx.VERTICAL)

        # 设置工作区浏览器控件
        self.browser = wx.html2.WebView.New(pnl)
        # 在工作区浏览器控件显示main.html网页
        self.browser.LoadURL(os.path.realpath("main.html"))
        # self.browser.LoadURL("http://www.baidu.com")

        sizer.Add(self.browser, 1, wx.EXPAND, 10)

        pnl.SetSizer(sizer)

        # 创建菜单栏
        self.makeMenuBar()
        # 创建工具栏
        # self.makeToolBar()
        # 创建状态栏
        statusBar = self.CreateStatusBar()
        statusBar.SetStatusText("北京同有飞骥科技股份有限公司区域销售管理中心")

    def makeMenuBar(self):
        # 1.文件菜单
        fileMenu = wx.Menu()
        # 1.1 数据库备份菜单项
        dbBackupItem = fileMenu.Append(wx.ID_ANY, "数据库备份", "备份本地SQLite3数据库")
        # 菜单分隔线
        fileMenu.AppendSeparator()
        # 1.2 选项
        optionItem = fileMenu.Append((wx.ID_ANY), "选项", "系统选项设置")
        # 1.3 退出菜单项
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # 2.统计查询菜单
        queryMenu = wx.Menu()
        # 2.1 项目看板菜单项
        dashboardItem = queryMenu.Append(wx.ID_ANY, "项目看板", "显示项目统计信息")

        # 2.2 项目信息浏览菜单项
        projectListItem = queryMenu.Append(wx.ID_ANY, "项目信息浏览", "以列表形式显示人员库信息")
        # 2.3 人员信息浏览菜单项
        staffListItem = queryMenu.Append(wx.ID_ANY, "人员信息浏览", "以列表形式显示人员库信息")
        # 2.4 产品/服务信息浏览菜单项
        productListItem = queryMenu.Append(wx.ID_ANY, "产品/服务信息浏览", "以列表形式显示人员库信息")

        # 3.分发汇总菜单（splite切分、send发送、summary汇总)
        sssMenu = wx.Menu()
        # 3.1 提取信息菜单项
        spliteItem = sssMenu.Append(wx.ID_ANY, "Step 1: 提取信息", "从中心数据库中筛选提取信息并导出到EXCEL文件中")
        # 3.2 电邮发送菜单项
        sendItem = sssMenu.Append(wx.ID_ANY, "Step 2: 电邮发送", "将导出的EXCEL发送到指定人员的邮箱中")
        # 菜单分隔线
        sssMenu.AppendSeparator()
        # 3.3 汇集更新菜单项
        summaryItem = sssMenu.Append(wx.ID_ANY, "Step 3: 汇集更新", "汇集EXCEL文件并更新中心数据库中的信息")

        # 4.数据维护菜单
        dbMenu = wx.Menu()
        # 4.1 项目数据导出菜单项
        outputProjectItem = dbMenu.Append(wx.ID_ANY, "(O) 项目数据导出 >>>", "将中心数据库中的项目信息导出至EXCEL文件中")
        # 4.2 项目数据导入菜单项
        inputProjectItem = dbMenu.Append(wx.ID_ANY, "(I) 项目数据导入 <<<", "将EXCEL文件中项目信息导入至中心数据库")
        # 菜单分隔线
        dbMenu.AppendSeparator()
        # 4.3 人员数据导出菜单项
        outputStaffItem = dbMenu.Append(wx.ID_ANY, "(O) 人员数据导出 >>>", "将中心数据库中的人员信息导出至EXCEL文件中")
        # 4.4 项目数据导入菜单项
        inputStaffItem = dbMenu.Append(wx.ID_ANY, "(I) 人员数据导入 <<<", "将EXCEL文件中人员信息导入至中心数据库")
        # 菜单分隔线
        dbMenu.AppendSeparator()
        # 4.5 产品/服务数据导出菜单项
        outputProductItem = dbMenu.Append(wx.ID_ANY, "(O) 产品/服务数据导出 >>>", "将中心数据库中的产品/服务信息导出至EXCEL文件中")
        # 4.6 项目数据导入菜单项
        inputProductItem = dbMenu.Append(wx.ID_ANY, "(I) 产品/服务数据导入 <<<", "将EXCEL文件中产品/服务信息导入至中心数据库")

        # 5.工具菜单
        toolsMenu = wx.Menu()
        # 5.1 SQL语句执行菜单项
        sqlExecItem = toolsMenu.Append(wx.ID_ANY, "SQL执行", "对当前数据库直接执行SQL语句")
        # 5.2 外出记录单较验菜单项
        gooutRecChkItem = toolsMenu.Append(wx.ID_ANY, "外出记录单较验", "比对外出记录单中登记的拜访单位与登记地址")

        # 6.帮助菜单
        helpMenu = wx.Menu()
        # 6.1 操作说明菜单项
        helpDocItem = helpMenu.Append(wx.ID_ANY, "帮助文档", "显示操作说明的帮助文档")
        # 6.2 about菜单项
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # 菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "文件")
        menuBar.Append(queryMenu, "统计查询")
        menuBar.Append(sssMenu, "分发汇总")
        menuBar.Append(dbMenu, "数据维护")
        menuBar.Append(toolsMenu, "工具")
        menuBar.Append(helpMenu, "帮助")

        # 加载菜单栏至窗口
        self.SetMenuBar(menuBar)

        # 菜单栏事件消息绑定
        # 1.文件菜单
        self.Bind(wx.EVT_MENU, self.OnDbBackup, dbBackupItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        # 2.统计查询菜单
        self.Bind(wx.EVT_MENU, self.OnProjectList, projectListItem)
        self.Bind(wx.EVT_MENU, self.OnStaffList, staffListItem)

        # 3.分发汇总菜单

        # 4.数据维护菜单
        self.Bind(wx.EVT_MENU, self.OnProjectOutput, outputProjectItem)
        self.Bind(wx.EVT_MENU, self.OnProjectInput, inputProjectItem)
        self.Bind(wx.EVT_MENU, self.OnStaffOutput, outputStaffItem)
        self.Bind(wx.EVT_MENU, self.OnStaffInput, inputStaffItem)

        # 5.工具菜单
        self.Bind(wx.EVT_MENU, self.OnGoOutCheck, gooutRecChkItem)

        # 6.帮助菜单
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    ############################## EVENT DEFINE ##############################
    def OnExit(self, event):
        self.Close(True)

    def OnDbBackup(self, event):
        pass
        # with open("test.mht", 'r') as f:
        #     html_cont = f.read()
        # self.browser.SetPage(html_cont, "")

    def OnProjectList(self, event):
        # 连接LPM数据库
        conn = sqlite3.connect('./data/lpm_c.db')
        query_sql = "SELECT * FROM T_Projects"
        # print(query_sql)
        project_df = pd.read_sql_query(query_sql, conn)
        conn.close()
        # 调整DF显示表头
        project_df.rename(inplace=True, columns={
            'pid': '项目ID',
            'name': '项目名称',
            'p_no': '项目编码',
            'p_type': '项目类型',
            'final_client': '最终用户',
            'partner': '合作伙伴',
            'amount': '项目金额',
            'phase': '项目阶段',
            'plan_sign_time': '预计签约时间',
            'sno': '员工编号',
            'remarks': '备注',
        })
        # 调整DF显示顺序
        project_df = project_df[
            ['项目ID', '项目名称', '项目编码', '项目类型', '最终用户', '合作伙伴', '项目金额', '项目阶段', '预计签约时间', '员工编号', '备注']]
        # 在浏览器区域显示staff_df
        self.browser.SetPage(project_df.to_html(index=False, classes='gridtable') + df_style, '')

    def OnStaffList(self, event):
        # 连接LPM数据库
        conn = sqlite3.connect('./data/lpm_c.db')
        query_sql = "SELECT * FROM T_Staffs"
        # print(query_sql)
        staff_df = pd.read_sql_query(query_sql, conn)
        conn.close()
        # 调整DF显示表头
        staff_df.rename(inplace=True, columns={
            'sno': '员工编号',
            'name': '姓名',
            'gender': '性别',
            'id_number': '身份信息',
            'email': '邮箱',
            'cell_phone': '手机',
            'office_tel': '办公电话',
            'branch': '分支机构',
            'dept': '部门',
            'post': '职位',
            'title': '任命职务',
            's_type': '人员类别',
            'remarks': '备注',
        })
        # 调整DF显示顺序
        staff_df = staff_df[['员工编号', '姓名', '性别', '身份信息', '邮箱', '手机', '办公电话', '分支机构', '部门', '职位', '任命职务', '人员类别', '备注']]
        # 在浏览器区域显示staff_df
        self.browser.SetPage(staff_df.to_html(index=False, classes='gridtable') + df_style, '')

    def OnProjectOutput(self, event):
        # 从中心数据库中读取T_Projects表，并将所有数据导出指定excel文件中
        # step1：获取保存文件对话框并获取存取路径
        with wx.FileDialog(self, "导出至EXCEL文件", wildcard="EXCEL files (*.xlsx)|*.xlsx",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            else:
                pathname = fileDialog.GetPath()
                print(pathname)
        # step2：从数据库中T_Projects表中读取数据至pandas DataFrame中
        conn = sqlite3.connect('./data/lpm_c.db')
        query_sql = "SELECT * FROM T_Projects"
        cursor = conn.execute(query_sql)
        df_project = pd.DataFrame(cursor.fetchall())
        df_project.columns = ["PID", "项目名称", "项目编号", "项目类型", "最终客户", "合作伙伴", "项目金额", "项目阶段", "预计签约时间", "SNO", "备注"]
        print(df_project)
        # 将人员编号换成编号加人名的格式，便于查阅和修改
        query_sql = "SELECT sno,name FROM T_Staffs"
        cursor = conn.execute(query_sql)
        df_staff = pd.DataFrame(cursor.fetchall())
        df_staff.columns = ["SNO", "姓名"]
        print(df_staff)
        # 使用合并联合查询人员姓名
        df_output = df_project.merge(df_staff, how="left", on="SNO")
        # 调整output输出顺序
        df_output = df_output[["PID", "项目名称", "项目编号", "项目类型", "最终客户", "合作伙伴", "项目金额", "项目阶段", "预计签约时间", "SNO", "姓名", "备注"]]
        print(df_output)
        # step3：导出df中的数据至EXCEL文件中
        df_output.to_excel(pathname, index=False)
        # step4: 提示导出成功
        wx.MessageBox("项目信息已导出至【%s】文件中！" % (pathname), "数据导出", wx.OK | wx.ICON_INFORMATION)

    def OnProjectInput(self, event):
        # 扫描指定的EXCEL数据表，并修改中心数据库中的T_Projects表
        # step1：获取需导入的EXCEL数据表文件路径
        with wx.FileDialog(self, "选择导入EXCEL文件", wildcard="EXCEL files (*.xlsx)|*.xlsx", style=wx.FD_OPEN) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            else:
                pathname = fileDialog.GetPath()
                print(pathname)
        # step2：读入EXCEL文件至pandas中，依次扫描每行数据并根据情况写入中心数据库
        # 若找到对应的项目则用EXCEL文件中的数据整行覆盖中心数据库对应条目
        # 若发现NEW标识或PID为空，则将EXCEL文件中的数据整行添加到中心数据库中
        df = pd.read_excel(pathname)
        # step3：对dataframe中的数据进行预处理，主要是去除重复的数据行、日期型数据进行字符串转化（YYYY-MM-DD)
        # 删除姓名列
        print(df)
        df.drop("姓名",inplace=True,axis=1)
        print(df)
        # step4: 扫描预处理后的df,若标志为NEW，则添加本行记录至中心数据库中，否则更新中心数据库中的信息

        for idx_df in range(df.shape[0]):
            # T_Projects表的结构：pid,name,p_no,p_type,final_client,partner,amount,phase,plan_sign_time,sno,remarks
            pid = df.iloc[idx_df, 0]
            name = df.iloc[idx_df, 1]
            p_no = df.iloc[idx_df, 2]
            p_type = df.iloc[idx_df, 3]
            final_client = df.iloc[idx_df, 4]
            partner = df.iloc[idx_df, 5]
            amount = df.iloc[idx_df, 6]
            phase = df.iloc[idx_df, 7]
            plan_sign_time = df.iloc[idx_df, 8]
            sno = df.iloc[idx_df, 9]
            remarks = df.iloc[idx_df, 10]

            if pid == "NEW":
                # 获取项目库中的PID：8位日期+4位流水码
                pid = comm.get_pid()
                # 构建SQL语句：INSERT
                query_sql = "INSERT INTO T_Projects (pid,name,p_no,p_type,final_client,partner,amount,phase,plan_sign_time,sno,remarks) values ('%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s')" % (
                    pid, name, p_no, p_type, final_client, partner, amount, phase, plan_sign_time, sno, remarks)
            else:
                # 构建SQL语句：UPDATE
                query_sql = "UPDATE T_Projects SET name='%s',p_no='%s',p_type='%s',final_client='%s',partner='%s',amount=%s,phase='%s',plan_sign_time='%s',sno='%s',remarks='%s' WHERE pid='%s'" % (
                    name, p_no, p_type, final_client, partner, amount, phase, plan_sign_time, sno, remarks, pid)
            # 显示SQL语句
            print(query_sql)
            conn = sqlite3.connect('./data/lpm_c.db')
            conn.execute(query_sql)
            conn.commit()
        # step5: 显示提示信息
        wx.MessageBox("项目信息已导入中心数据库！", "数据导入", wx.OK | wx.ICON_INFORMATION)

    def OnStaffOutput(self, event):
        # 从中心数据库中读取T_Staffs表，并将所有数据导出指定excel文件中
        # step1：获取保存文件对话框并获取存取路径
        with wx.FileDialog(self, "导出至EXCEL文件", wildcard="EXCEL files (*.xlsx)|*.xlsx",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            else:
                pathname = fileDialog.GetPath()
                print(pathname)
        # step2：从数据库中T_Staffs表中读取数据至pandas DataFrame中
        conn = sqlite3.connect('./data/lpm_c.db')
        query_sql = "SELECT * FROM T_Staffs"
        cursor = conn.execute(query_sql)
        df_staff = pd.DataFrame(cursor.fetchall())
        df_staff.columns = ["SNO", "姓名", "性别", "身份证号", "电子邮件", "移动电话", "办公电话", "分支机构", "部门", "职位", "任命职务","备注","人员类别"]
        print(df_staff)
        df_output = df_staff[["SNO", "姓名", "性别", "身份证号", "电子邮件", "移动电话", "办公电话", "分支机构", "部门", "职位", "任命职务","人员类别","备注"]]
        # step3：导出df中的数据至EXCEL文件中
        df_output.to_excel(pathname, index=False)
        # step4: 提示导出成功
        wx.MessageBox("人员信息已导出至【%s】文件中！" % (pathname), "数据导出", wx.OK | wx.ICON_INFORMATION)

    def OnStaffInput(self, event):
        # 扫描指定的EXCEL数据表，并修改中心数据库中的T_Staffs表
        # step1：获取需导入的EXCEL数据表文件路径
        with wx.FileDialog(self, "选择导入EXCEL文件", wildcard="EXCEL files (*.xlsx)|*.xlsx", style=wx.FD_OPEN) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            else:
                pathname = fileDialog.GetPath()
                print(pathname)
        # step2：读入EXCEL文件至pandas中，依次扫描每行数据并根据情况写入中心数据库
        # 若找到对应的项目则用EXCEL文件中的数据整行覆盖中心数据库对应条目
        # 若发现NEW标识或PID为空，则将EXCEL文件中的数据整行添加到中心数据库中
        df = pd.read_excel(pathname)
        # step3：对dataframe中的数据进行预处理，主要是去除重复的数据行、日期型数据进行字符串转化（YYYY-MM-DD)

        # print(df)
        # step4: 扫描预处理后的df,若标志为NEW，则添加本行记录至中心数据库中，否则更新中心数据库中的信息

        for idx_df in range(df.shape[0]):
            # T_Projects表的结构：pid,name,p_no,p_type,final_client,partner,amount,phase,plan_sign_time,sno,remarks
            sno = df.iloc[idx_df, 0]
            name = df.iloc[idx_df, 1]
            gender = df.iloc[idx_df, 2]
            id_number = df.iloc[idx_df, 3]
            email = df.iloc[idx_df, 4]
            cell_phone = df.iloc[idx_df, 5]
            office_tel = df.iloc[idx_df, 6]
            branch = df.iloc[idx_df, 7]
            dept = df.iloc[idx_df, 8]
            post = df.iloc[idx_df, 9]
            title = df.iloc[idx_df,10]
            s_type = df.iloc[idx_df,11]
            remarks = df.iloc[idx_df, 12]
            print(s_type,remarks)
            if sno == "NEW":
                # 用户备注中提取新的人员编号
                sno = remarks
                # 构建SQL语句：INSERT
                query_sql = "INSERT INTO T_Staffs (sno,name,gender,id_number,email,cell_phone,office_tel,branch,dept,post,title,s_type,remarks) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (sno,name,gender,id_number,email,cell_phone,office_tel,branch,dept,post,title,s_type,remarks)
            else:
                # 构建SQL语句：UPDATE
                query_sql = "UPDATE T_Staffs SET name='%s',gender='%s',id_number='%s',email='%s',cell_phone='%s',office_tel='%s',branch='%s',dept='%s',post='%s',title='%s',s_type='%s',remarks='%s' WHERE sno='%s'" % (name,gender,id_number,email,cell_phone,office_tel,branch,dept,post,title,s_type,remarks, sno)
            # 显示SQL语句
            print(query_sql)
            conn = sqlite3.connect('./data/lpm_c.db')
            conn.execute(query_sql)
            conn.commit()
        # step5: 显示提示信息
        wx.MessageBox("项目信息已导入中心数据库！", "数据导入", wx.OK | wx.ICON_INFORMATION)

    def OnAbout(self, event):
        wx.MessageBox("区域项目管理系统主要用于区域管理中心项目集中式管理。",
                      "区域项目管理系统 Version 1.0",
                      wx.OK | wx.ICON_INFORMATION)

    # def OnNewProject(self, event):
    #     pass
    #
    # def OnNewSeller(self, event):
    #     # 建立新增用户对话框类
    #     newSellerDlg = LPMAddNewSellerDlg(self)
    #     # 显示对话框
    #     newSellerDlg.ShowModal()

    def OnGoOutCheck(self, event):
        # 创建外出记录单较验对话框类
        gooutRecChkDlg = LPMGoOutRecodeCheckkDlg(self)
        # 显示对话框
        gooutRecChkDlg.ShowModal()


# LPM_App 类定义
class LPM_App(wx.App):
    def __init__(self):
        super(self.__class__, self).__init__()


###############################################################
#                       MAIN PROGRAM                          #
###############################################################
if __name__ == '__main__':
    # 构建应用程序
    app = LPM_App()
    # 构建主窗体
    frm = MainFrame(None, title="Local Project Manage - LPM")
    # 设置窗体的默认大小
    frm.SetSize(mainFrameSize)
    frm.Show()

    # 启动消息循环
    app.MainLoop()
