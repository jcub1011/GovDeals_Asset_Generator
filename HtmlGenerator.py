form Directories import Directories


class HtmlGenerator:
    def __init__():
        pass
    
    @classmethod
    def generateSpecHTML(cls, dictionary, dict_name):
        seperator = ": "
        dict_html = "<UL><B>" + dict_name + seperator + "</B>\n"
        for key, value in dictionary.items():
            if type(value) == dict:
                dict_html += generateSpecHTML(dictionary, key)
            else:
                dict_html += "<LI><B>" + key + seperator + "</B> " + value
            dict_html += "</LI>\n"
            
        dict_html += "</UL>\n"
    
    @classmethod
    def generateHTML(cls, asset):
        direc = Directories()
        seperator = ": "
        head_string = ""
        with open(direc.disclaimer + "\\long_desc_pickup_disclaimer.txt") as pickup_disc:
            head_string += pickup_disc + "<BR><BR>\n"
        
        for key, value in asset.header.items():
            head_string += "<P>" + key + seperator + value + "<\P><BR><BR>\n"
        
        spec_string = cls.generateSpecHTML(asset.specs)
        
        foot_string = ""
        for key, value in asset.footer.items():
            foot_string += "<P>" + key + seperator + value + "<\P><BR><BR>\n"
            
        with open(direc.disclaimer + "\\long_desc_retire_disclaimer.txt") as retire_disc:
            foot_string += retire_disc
        
        return head_string + spec_string + foot_string
            
            