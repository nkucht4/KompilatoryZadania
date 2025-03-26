class ToHtml:
    def __init__(self):
        self.colours = {'DARK_GREEN': '#32a800',
                        'BLUE': '#00bfff',
                        'PINK': '#ff52bf',
                        'PURPLE': '#ae6bff',
                        'GREY': '#a8a8a8',
                        'YELLOW': '#ffea00',
                        'ORANGE': '#ff8800',
                        'LIGHT_GREEN': '#4dff00',
                        'RED': '#ff0000',
                        'DEFAULT': '#000000',
                        'WHITE': '#ffffff'}
        self.file = ""

    def start(self, filename, dark_mode=False):
        if dark_mode:
            background_colour = '#424242'
            self.colours['#ffffff'] = background_colour
        else:
            background_colour = '#ffffff'
        self.file = open(filename, 'a')
        self.file.truncate(0)
        self.file.write('<!DOCTYPE html>\n')
        self.file.write('<html lang="en">\n')
        self.file.write('<head>\n')
        self.file.write('<title>Kolorowy kod</title>')
        self.file.write('<meta charset="utf-8"/>\n')
        self.file.write('</head>\n')
        self.file.write(f'<body style="background-color:{background_colour}; '
                   f'font-family: \'Cascadia Mono\'; font-size: 16px;">\n')
        return self.file

    def adding_token(self, token):
        colour, t = token
        if colour == "WHITE":
            t = t.replace('\t', '&nbsp;')
            t = t.replace('\n', '<br>')
        else:
            t = t.replace('\n', '\\n')
            t = t.replace('\t', '\\t')
        if colour in self.colours:
            colour = self.colours[colour]
        else:
            colour = self.colours['DEFAULT']
        self.file.write(f'<span style="color:{colour}">{t}</span>\n')

    def close(self):
        self.file.write('</body>\n')
        self.file.write('</html>\n')
        self.file.close()
