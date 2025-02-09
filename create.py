import sqlite3



con = sqlite3.connect('807029.db')
cursor = con.cursor()


select_sql = f'''SELECT * FROM "{86}";'''

cursor.execute(select_sql)
rows = cursor.fetchall()


html_content = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users List</title>
</head>

<body>
    <table>
'''

for row in rows:
    
    html_content += f'''
        <tr>
            <td>{f"{row[0]:02} : {row[1]}"}</td>
        </tr>
    '''


html_content += '''
    </table>
    </body>
    </html>
'''

with open("test.html", "w", encoding="utf-8") as file:
    
    file.write(html_content)
    
con.close()