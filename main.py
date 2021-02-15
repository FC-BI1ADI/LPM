import wx
import wx.html2
import UI
from LPMAddNewSellerDlg import LPMAddNewSellerDlg
from LPMGoOutRecodeCheckkDlg import LPMGoOutRecodeCheckkDlg
import sqlite3
import pandas as pd
import os


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
        self.makeToolBar()
        # 创建状态栏
        statusBar = self.CreateStatusBar()
        statusBar.SetStatusText("北京同有飞骥科技股份有限公司区域销售管理中心")

    def makeMenuBar(self):
        # 1.文件菜单
        fileMenu = wx.Menu()
        # 1.1 用户管理菜单项
        userManageItem = fileMenu.Append(wx.ID_ANY,"用户管理", "LPM系统用户管理")
        # 1.2 数据库备份菜单项
        dbBackupItem = fileMenu.Append(wx.ID_ANY, "数据库备份", "备份本地SQLite3数据库")
        # 1.3 菜单分隔线
        fileMenu.AppendSeparator()
        # 1.4 选项
        optionItem = fileMenu.Append((wx.ID_ANY),"选项", "系统选项设置")
        # 1.5 退出菜单项
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # 2.汇总报表菜单
        reportMenu = wx.Menu()
        # 2.1 仪表盘dashboard菜单项
        dashboardItem = reportMenu.Append(wx.ID_ANY, "项目仪表盘", "显示项目统计信息")

        # 3.项目管理菜单
        projectMenu = wx.Menu()
        # 3.1 新项目登录菜单项
        newProjectItem = projectMenu.Append(wx.ID_ANY, "新项目登录" ,"手动创建新项目")
        # 3.2 项目信息维护菜单项
        projectInfoItem = projectMenu.Append(wx.ID_ANY, "项目信息维护", "对项目库中信息进行CRUD操作")
        # 3.3 菜单分隔符
        projectMenu.AppendSeparator()
        # 3.4 项目信息浏览菜单项
        projectListItem = projectMenu.Append(wx.ID_ANY, "项目信息浏览", "以列表形式显示项目库信息")

        # 4.人员管理菜单
        staffMenu = wx.Menu()
        # 4.1 新人员菜单项
        newStaffItem = staffMenu.Append(wx.ID_ANY, "新人员登录", "将新的销售人员登录进人员信息库中")
        # 4.2 人员信息修改菜单项
        staffInfoItem = staffMenu.Append(wx.ID_ANY, "人员信息修改", "修改人员信息库中的销售人员信息")
        # 4.3 人员注销菜单项
        staffDelItem = staffMenu.Append(wx.ID_ANY, "人员注销", "在人员信息库中标注已离职人员")
        # 4.4 菜单分隔线
        staffMenu.AppendSeparator()
        # 4.5 人员信息浏览菜单项
        staffListItem = staffMenu.Append(wx.ID_ANY, "人员信息浏览", "以列表形式显示人员库信息")


        # 5.产品管理菜单
        productMenu = wx.Menu()
        # 5.1 新产品登录菜单项
        newProductItem = productMenu.Append(wx.ID_ANY, "新产品/服务登录", "将新的产品或服务信息登录进产品信息库中")
        # 5.2 产品信息修改菜单项
        productInfoItem = productMenu.Append(wx.ID_ANY, "产品/服务信息修改", "修改产品信息库中的产品或服务信息")
        # 5.3 停产产品标注菜单项
        productDelItem = productMenu.Append(wx.ID_ANY, "产品停产/服务中止", "在产品信息库中标注已停产产品或中止服务")
        # 5.4 菜单分隔线
        productMenu.AppendSeparator()
        # 5.5 产品/服务信息浏览
        productListItem = productMenu.Append(wx.ID_ANY, "产品/服务信息浏览", "以列表形式显示产品或服务信息")

        # 6.工具菜单
        toolsMenu = wx.Menu()

        # 6.1 SQL语句执行菜单项
        sqlExecItem = toolsMenu.Append(wx.ID_ANY, "SQL执行", "对当前数据库直接执行SQL语句")
        # 6.2 外出记录单较验菜单项
        gooutRecChkItem = toolsMenu.Append(wx.ID_ANY, "外出记录单较验", "比对外出记录单中登记的拜访单位与登记地址")


        # 7.帮助菜单
        helpMenu = wx.Menu()
        # 7.1 操作说明菜单项
        helpDocItem = helpMenu.Append(wx.ID_ANY, "帮助文档", "显示操作说明的帮助文档")
        # 7.2 about菜单项
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # 菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "文件")
        menuBar.Append(reportMenu, "汇总报表")
        menuBar.Append(projectMenu, "项目管理")
        menuBar.Append(staffMenu, "人员管理")
        menuBar.Append(productMenu, "产品/服务管理")
        menuBar.Append(toolsMenu, "工具")
        menuBar.Append(helpMenu, "帮助")

        # 加载菜单栏至窗口
        self.SetMenuBar(menuBar)

        # 菜单栏事件消息绑定
        # 1.文件菜单
        self.Bind(wx.EVT_MENU, self.OnDbBackup, dbBackupItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        # 2.汇总报表菜单

        # 3.项目管理菜单
        self.Bind(wx.EVT_MENU, self.OnProjectList, projectListItem)

        # 4.人员管理菜单
        self.Bind(wx.EVT_MENU, self.OnNewSeller, newStaffItem)
        self.Bind(wx.EVT_MENU, self.OnStaffList, staffListItem)

        # 5.产品/服务管理菜单

        # 6.工具菜单
        self.Bind(wx.EVT_MENU,self.OnGoOutCheck, gooutRecChkItem)

        # 7.帮助菜单
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def makeToolBar(self):
        toolBar = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        # 添加新项目工具项
        newProjectTool = toolBar.AddTool(wx.ID_ANY, "添加新项目信息", wx.Bitmap(r".\icons\newProject.png"),
                                         shortHelp="添加新项目信息", kind=wx.ITEM_NORMAL)
        # 显示人员信息工具项
        sellerInfoTool = toolBar.AddTool(wx.ID_ANY, "显示人员信息", wx.Bitmap(r".\icons\users.png"),
                                         shortHelp="显示销售人员信息", kind=wx.ITEM_NORMAL)
        # 工具栏分隔符
        toolBar.AddSeparator()
        # 数据库备份工具项
        dbBackupTool = toolBar.AddTool(wx.ID_ANY, "数据库备份", wx.Bitmap(r".\icons\dbBackup.png"), shortHelp="数据库备份",
                                       kind=wx.ITEM_NORMAL)
        toolBar.Realize()

        # 工具栏事件消息绑定
        self.Bind(wx.EVT_TOOL, self.OnNewSeller, newProjectTool)
        self.Bind(wx.EVT_TOOL, self.OnAbout, sellerInfoTool)
        self.Bind(wx.EVT_TOOL, self.OnAbout, dbBackupTool)

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
        project_df =  pd.read_sql_query(query_sql, conn)
        conn.close()
        # 调整DF显示表头
        project_df.rename(inplace=True, columns = {
            'pid':'项目ID',
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
        project_df = project_df[['项目ID','项目名称','项目编码','项目类型','最终用户','合作伙伴','项目金额','项目阶段','预计签约时间','员工编号','备注']]
        # 在浏览器区域显示staff_df
        self.browser.SetPage(project_df.to_html(index=False,classes='gridtable') + df_style,'')

    def OnStaffList(self, event):
        # 连接LPM数据库
        conn = sqlite3.connect('./data/lpm_c.db')
        query_sql = "SELECT * FROM T_Staffs"
        # print(query_sql)
        staff_df =  pd.read_sql_query(query_sql, conn)
        conn.close()
        # 调整DF显示表头
        staff_df.rename(inplace=True, columns = {
            'sno':'员工编号',
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
        staff_df = staff_df[['员工编号','姓名','性别','身份信息','邮箱','手机','办公电话','分支机构','部门','职位','任命职务','人员类别','备注']]
        # 在浏览器区域显示staff_df
        self.browser.SetPage(staff_df.to_html(index=False,classes='gridtable') + df_style,'')

    def OnAbout(self, event):
        wx.MessageBox("区域项目管理系统主要用于区域管理中心项目集中式管理。\nVersion 1.0",
                      "区域项目管理系统",
                      wx.OK | wx.ICON_INFORMATION)

    def OnNewProject(self, event):
        pass

    def OnNewSeller(self, event):
        # 建立新增用户对话框类
        newSellerDlg = LPMAddNewSellerDlg(self)
        # 显示对话框
        newSellerDlg.ShowModal()

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
