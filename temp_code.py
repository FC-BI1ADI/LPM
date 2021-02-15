df = pd.DataFrame({'c1': [1.005, 2], 'c2': [2, 3.5], 'c3': [3, 4]})

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

# self.browser.SetPage(df.to_html(index=False,classes='gridtable') + df_style,'')