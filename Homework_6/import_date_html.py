import user_interface as u

def file_html():
    date = u.Date_input()
    name, surname, tel_number, description = date
    style = 'style = "font-size:30px;"'
    html = '<html>\n  <head>/<head>\n <body> \n'
    html += '     <p {}>Имя: {} c</p>\n'.format(style, name)
    html += '     <p {}>Фамилия: {} </p>\n'.format(style, surname)
    html += '     <p {}>Телефон: {} </p>\n'.format(style, tel_number)
    html += '     <p {}>Описание: {}</p>\n'.format(style, description) 
    html += ' </body>\n</html>'
    with open('bd.html', 'a+', encoding='utf-8') as page:
        page.write(html)
    