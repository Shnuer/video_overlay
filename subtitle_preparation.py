import datetime
import numpy
from tqdm import tqdm
from sys import stdout


def get_info_script():
    return ''

# Display Text Configuration
def get_config_ass_format():
    style_config = {
        'Name':'DefaultVCD',
        'Fontname':'Arial',
        'Fontsize':'10',
        'PrimaryColour':'&H0FFFFFF',
        'SecondaryColour':'&H0FFFFFF',
        'OutlineColour':'&H00000008',
        'BackColour':'&H00000008',
        'Bold':'-1',
        'Italic':'0',
        'Underline':'0',
        'StrikeOut':'0',
        'ScaleX':'100',
        'ScaleY':'100',
        'Spacing':'0.00',
        'Angle':'0.00',
        'BorderStyle':'1',
        'Outline':'1.00',
        'Shadow':'0.00',
        'Alignment':'2',
        'MarginL':'30',
        'MarginR':'30',
        'MarginV':'30',
        'Encoding':'0'  
    }

    base_str = 'Style: '
    second_part_str = ''

    for param in style_config:
        second_part_str = second_part_str + f'{style_config[param]},'

 
    second_part_str = second_part_str[:-1]
    style_setting = base_str + second_part_str

    return style_setting

# Converts ISO time format to ass file time format
def get_ass_format_time(time):
    time = float(time)
    ass_format_time = str(datetime.timedelta(seconds=time))

    if time.is_integer():
        ass_format_time = ass_format_time + '.00'

    else:
        ass_format_time = ass_format_time.replace('0000','')

    return ass_format_time


def get_display_string_time_format_ass(start_time, end_time):
    base_str = f'Dialogue: 0,{start_time},{end_time},DefaultVCD, NTP,0000,0000,0000,,{{\\an7}}{{\\pos(0,0)}}'
    return base_str

def get_display_string_data_format_ass(title, data):
    base_string = f'{title}: {data}\\N '
    return base_string

# Creates a basic subtitle file structure
def create_file_filing():
    info_str = '[Script Info]\n'
    info_str =  info_str + get_info_script() +'\n'

    style_str = '[V4+ Styles]\n'
    style_str = style_str + get_config_ass_format() + '\n'

    data_str = '[Events]\n'

    final_string = info_str + style_str + data_str

    return final_string


# Creating a subtitle file based on data with a given frequency
def create_subtitle_file(duration, title, data_gen, file_name_subtitle='subtitle.ass', start_time=0, step_size=0.02):

    with open(file_name_subtitle,'w',encoding='utf_8_sig') as f:

        buf_value_str = create_file_filing()

        f.write(buf_value_str)
        

        for second_of_time in tqdm(numpy.arange(start_time,  duration, step_size),file=stdout):
            
            if not data_gen:
                break

            data_string = next(data_gen)

            start_of_reference = get_ass_format_time(second_of_time) 
            end_of_reference = get_ass_format_time(second_of_time + step_size) 

            base_str = get_display_string_time_format_ass(start_of_reference, end_of_reference)


            for title_index, title_element in enumerate(title):
                base_str = base_str + get_display_string_data_format_ass(title_element, data_string[title_index])

            base_str = '\n' + base_str 
            f.write(base_str)

if __name__ == "__main__":
    print(get_config_ass_format())
    print(get_ass_format_time(0.00))
    print(get_ass_format_time(0))
    print(get_ass_format_time(0.02))

